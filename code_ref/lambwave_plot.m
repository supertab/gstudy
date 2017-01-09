function Fedisper
%绘制平板频散曲线
%tic
clc;clear;
cl=5940;%材料 纵波波速（钢板）
cs=3240;%材料横波波速（钢板）
dfd=0.01*1e3;
fd0=(0.01:dfd/1e3:20)*1e3;%频厚积（MHz*mm）
d_Q235=1;

cps_min=2700;
cpa_min=100;
cp_max=10000;% cp极值决定A1
mode=2;%绘制的模式数
precision=1e-8;
cpa=zeros(length(fd0),mode);
cps=zeros(length(fd0),mode);
for i=1:length(fd0)
    fd=fd0(i);
    [cp12 n]=ss(cps_min,cp_max,fd,cl,cs,mode); %得到零点区间，有几个模式得到几个零点区间
    for j=1:n
        cp1=cp12(j,1);
        cp2=cp12(j,2);
        cps(i,j)=serfen(cp1,cp2,fd,cl,cs,precision); %二分法在区间求得相速度
    end
    
    [cp12 n]=aa(cpa_min,cp_max,fd,cl,cs,mode);
    for j=1:n
        cp1=cp12(j,1);
        cp2=cp12(j,2);
        cpa(i,j)=aerfen(cp1,cp2,fd,cl,cs,precision);
    end
end

h=zeros(mode,2);
%相速度
figure(1)
for j=1:2
    if j==1
        cp=cps;
        color='k';
    else
        cp=cpa;
        color='k';
    end
    for i=1:mode
        cpp=cp(:,i);
        ind=find(cpp==0);
%         drawnow;%强制刷新
        if ~isempty(ind)
            h(i,j)=plot((fd0(ind(end)+1:end))/d_Q235,cpp(ind(end)+1:end),color','LineWidth',2.5);
        else
            h(i,j)=plot(fd0/d_Q235,cpp,color,'LineWidth',2.5);
        end
        hold on
    end
    if j==2
        xlabel('f/(MHz)')
        ylabel('C_{p}/(km/s)')
        title('Q235 相速度频散曲线')
        set(gca,'xtick',(0:1:20)*1e3/d_Q235,'xticklabel',(0:1:20)*1e3*(1e-3)/d_Q235)
        xlim([0, 10000]);%
        set(gca,'ylim',[0 cp_max],'ytick',(0:cp_max/1e3)*1e3,...
            'yticklabel',0:cp_max/1e3)
        grid on
        hSGroup = hggroup;%要在子对象构建之后构建，构建后立即使用，否则将失效
        hAGroup = hggroup;
        set(h(:,1),'parent',hSGroup)
        set(h(:,2),'parent',hAGroup,'LineStyle','--')
        set(get(get(hSGroup,'Annotation'),'LegendInformation'),...
            'IconDisplayStyle','on');
        set(get(get(hAGroup,'Annotation'),'LegendInformation'),...
            'IconDisplayStyle','on');
%         legend('对称模式','反对称模式')
    end
end

%群速度
figure(2)
for j=1:2
    if j==1
        cp=cps;
        color='k';
    else
        cp=cpa;
        color='k';
    end
    for i=1:mode
        cpp=cp(:,i);
        ind=find(cpp==0);
        if ~isempty(ind)
            fd=fd0(ind(end)+1:end)';
            cpp=cpp(ind(end)+1:end);
        else
            fd=fd0';
        end
        dcdf=diff(cpp)/dfd;
        cg=cpp(1:end-1).^2./(cpp(1:end-1)-fd(1:end-1).*dcdf);
        h(i,j)=plot(fd(1:end-1)/d_Q235,cg,color,'LineWidth',2.5);
        hold on
    end
    if j==2
        xlabel('f/(MHz)')
        ylabel('C_{g}/(km/s)')
%         title('Q235 群速度频散曲线')
%         set(gca,'linewidth',1.5);
        set(gca,'xtick',(0:1:20)*1e3/d_Q235,'xticklabel',(0:1:20)*1e3*(1e-3)/d_Q235)
        xlim([0, 10000]);%
        set(gca,'ylim',[0 5.5]*1e3,'ytick',(0:0.5:5.5)*1e3,'yticklabel',0:0.5:5.5)
        grid on
        hSGroup = hggroup;%要在子对象构建之后构建，构建后立即使用，否则将失效
        hAGroup = hggroup;
        set(h(:,1),'parent',hSGroup)
        set(h(:,2),'parent',hAGroup,'LineStyle','--')
        set(get(get(hSGroup,'Annotation'),'LegendInformation'),...
            'IconDisplayStyle','on');
        set(get(get(hAGroup,'Annotation'),'LegendInformation'),...
            'IconDisplayStyle','on');
%         legend('对称模式','反对称模式')
    end
end

end


%对称模式
function [cp0 n]=ss(cp_min,cp_max,fd,cl,cs,mode)
cp2=cp_min;
deter=33;
cp0=zeros(mode,2);
n=0;
while cp2<cp_max&&n<mode
    cp1=cp2;
    cp2=cp1+deter;
    % 试值法，无法直接求cp，通过带入cp测试
    y1=smode(cp1,fd,cl,cs);
    y2=smode(cp2,fd,cl,cs);
    % 寻找异号的y1,y2保存对应的cp1,cp2
    while y1*y2>0&&cp2<cp_max
        cp1=cp2;
        cp2=cp1+deter;
        y1=smode(cp1,fd,cl,cs);
        y2=smode(cp2,fd,cl,cs);
    end
    if y1*y2<0
        n=n+1;
        cp0(n,:)=[cp1 cp2];
    else
        if y1==0&&y2~=0
            n=n+1;
            cp0(n,:)=[cp1 cp1];
        elseif y2==0&&y1~=0
            n=n+1;
            cp0(n,:)=[cp2 cp2];
            cp2=cp2+1;
        elseif y1==0&&y2==0
            n=n+1;
            cp0(n,:)=[cp1 cp1];
            n=n+1;
            cp0(n,:)=[cp2 cp2];
            cp2=cp2+1;
        end
    end
end
end

function fs=smode(cp,fd,cl,cs)
p=abs(sqrt((cp/cs)^2-1));
q=abs(sqrt((cp/cl)^2-1));
if cp<=cs%p和q都是复数
    fs=-4*p*q*sinh(pi*fd/cp*q)*cosh(pi*fd/cp*p)+(-p^2-1)^2*sinh(pi*fd/cp*p)*cosh(pi*fd/cp*q);
elseif cp>cs&&cp<=cl%p是实数，q是复数
    fs=-4*p*q*sinh(pi*fd/cp*q)*cos(pi*fd/cp*p)+(p^2-1)^2*sin(pi*fd/cp*p)*cosh(pi*fd/cp*q);
else
    fs=4*p*q*sin(pi*fd/cp*q)*cos(pi*fd/cp*p)+(p^2-1)^2*sin(pi*fd/cp*p)*cos(pi*fd/cp*q);
end
end

function cp=serfen(cp1,cp2,fd,cl,cs,precision)
while cp2-cp1>precision
    y1=smode(cp1,fd,cl,cs);
    y2=smode(cp2,fd,cl,cs);
    cp0=(cp1+cp2)/2;
    y0=smode(cp0,fd,cl,cs);
    if y1*y0<0
        cp2=cp0;
    elseif y2*y0<0
        cp1=cp0;
    elseif y0==0
        break
    elseif y1==0
        cp2=cp1;
        break
    elseif y2==0
        cp1=cp2;
        break
    end
end
cp=(cp2+cp1)/2;
end

%反对称模式
function [cp0 n]=aa(cp_min,cp_max,fd,cl,cs,mode)
cp2=cp_min;
deter=33;
cp0=zeros(mode,2);
n=0;
while cp2<cp_max&&n<mode
    cp1=cp2;
    cp2=cp1+deter;
    y1=amode(cp1,fd,cl,cs);
    y2=amode(cp2,fd,cl,cs);
    while y1*y2>0&&cp2<cp_max
        cp1=cp2;
        cp2=cp1+deter;
        y1=amode(cp1,fd,cl,cs);
        y2=amode(cp2,fd,cl,cs);
    end
    if y1*y2<0
        n=n+1;
        cp0(n,:)=[cp1 cp2];
    else
        if y1==0&&y2~=0
            n=n+1;
            cp0(n,:)=[cp1 cp1];
        elseif y2==0&&y1~=0
            n=n+1;
            cp0(n,:)=[cp2 cp2];
            cp2=cp2+1;
        elseif y1==0&&y2==0
            n=n+1;
            cp0(n,:)=[cp1 cp1];
            n=n+1;
            cp0(n,:)=[cp2 cp2];
            cp2=cp2+1;
        end
    end
end
end

function fs=amode(cp,fd,cl,cs)
p=abs(sqrt((cp/cs)^2-1));
q=abs(sqrt((cp/cl)^2-1));
if cp<=cs%p和q都是复数
    fs=-4*p*q*sinh(pi*fd/cp*p)*cosh(pi*fd/cp*q)+(-p^2-1)^2*sinh(pi*fd/cp*q)*cosh(pi*fd/cp*p);
elseif cp>cs&&cp<=cl%p是实数，q是复数
    fs=4*p*q*sin(pi*fd/cp*p)*cosh(pi*fd/cp*q)+(p^2-1)^2*sinh(pi*fd/cp*q)*cos(pi*fd/cp*p);
else
    fs=4*p*q*sin(pi*fd/cp*p)*cos(pi*fd/cp*q)+(p^2-1)^2*sin(pi*fd/cp*q)*cos(pi*fd/cp*p);
end
end

function cp=aerfen(cp1,cp2,fd,cl,cs,precision)
while cp2-cp1>precision
    y1=amode(cp1,fd,cl,cs);
    y2=amode(cp2,fd,cl,cs);
    cp0=(cp1+cp2)/2;
    y0=amode(cp0,fd,cl,cs);
    if y1*y0<0
        cp2=cp0;
    elseif y2*y0<0
        cp1=cp0;
    elseif y0==0
        break
    elseif y1==0
        cp2=cp1;
        break
    elseif y2==0
        cp1=cp2;
        break
    end
end
cp=(cp2+cp1)/2;
end

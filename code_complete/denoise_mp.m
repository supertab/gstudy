clear;clc;
f=0.9251;
fai=0.512*pi;
snr=-20;
t=0:0.01:32;
s=cos(2*pi*f*t+fai);
plot(t, s)
% noise generation
tr=randn(size(s));
amplifytr=max(abs(tr));
ampsig=amplifytr*10^(snr/20); % why?
s=ampsig*s;

% signal with noise generation
s_o=s+tr;
error=zeros(101,201);
for f_atom=0:1000
    for fai_atom1=0:1:200;
        fai_atom=fai_atom1*0.01*pi;
        f_atom1=f_atom*0.01;
        s1=cos(2*pi*f_atom1*t+fai_atom);
        s_s1=sqrt(sum(s1.*s1));
        s1=s1/s_s1;
        error(f_atom+1, fai_atom1+1)=sum(s_o.*s1);
    end
end

yabs=abs(error)
[m,n]=max(yabs)
[k,l]=max(m)
result_f=(n(l)-1)/100;
result_fai=(l-1)*0.01;
result_a=error(n(1),1);

if result_a<0
    result_a=-result_a;
    result_fai=result_fai-l;
end
result_a=result_a/s_s1;
result_fai;
% renow the cosinoidal signal
sr=result_a*cos(2*pi*result_f*t+result_fai*pi);

% plot
tt=0:1:1000;
subplot(2,2,1);
plot(tt,s(1:1001));
subplot(2,2,2);
plot(tt,s_o(1:1001));
subplot(2,2,3);
plot(tt, sr(1:1001));
subplot(2,2,4);
plot(yabs(:,l-1));

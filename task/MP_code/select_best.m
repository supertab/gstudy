Function [proj, scale, translation, freq, phase]=select_best(signal_r, N, a_base, j_min, j_max, u_base, p_min, v_base, k_min, w_base, i_min,i_max);

% this subroutine is to select in the dictionary the best aton suited the signal or the %residual of the signed
% INPUT
% signal_r: the signal or the residual of the signal to be decomposed
% N: the length of the signal or of the residual of the signal or the length of the atoms
% parameters: the parameter to construct the dictionary, it has much influence on the speed of the decomposition
% a_base=2
%j_min=0;
%j_max=log2(N);

%OUTPUT
% proj: the projetion of the signal or the residual of the signal on the best atom 
% the scale: the scale of the best atom(s in  the formula)
% translaton: the translation of the best atom(u in the formula)
% freq: the frequency of the best atom(v in the formula)
% phase: the phase of the best aton (w in the formual)
% proj_trans:to determine which projection is biggest

proj_trans=0;
proj=0;

% size_dic is one parameter to show the size of the over-complete dictionary used 
size_dic=0;
for j=j_min:j_max
    for p=p_min:N*2^(-j+1)
        for k=k_min:2^(j+1)
	    for i=i_min:i_max
	        
		size_dic=size_dic+1;
		s=a_base^j;
		u=p*s*u_base;
		v=k*(1/s)*v_base;
		w=i*w_base;
		t=0:N-1;
		t=(t-u)/s;

		g=(1/sqrt(s))*exp(-pi*t.*t).*cos(v*t+w);
		g=g/sqrt(sum(g.*g));
		proj_trans=sum(signal_r.*g);

		if abs(proj_trans)>abs(proj)
		    proj=proj_trans;
		    scale=s;
		    translation=u;
		    freq=v;
		    phase=w;
		end
            end
	end
    end
end

%size_dic: display the size of the dictionary
size_dic

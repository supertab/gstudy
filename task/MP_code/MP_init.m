% function: MP algotithm applied to decomposition of one signal named bat
% the over-complete dictionary used in the program id the Fabor atom ditionary

% part one: read signal data, which is asved in the format: save bat.dat bat --ascii
load bat.dat -ascii;


%part 2:
%part 2.1
%determine the decomposition parameters
%the matching pursuit processing iterative number
iteratiove_number=10;

% the length of signal and the length of atoms;N
[a, N]=size(bat);

% signal_reconstruct is the signal reconstructed by the sparse parameters
% signal_r is the residual signal, that is the left signal of the original
% signal reduced by the signal_reconstruct

signal_reconstruct=zeros(1,N);
signal_r=bat;

% the follwing is the Gabor atom parameters which are closely relate to the size of the % over-complete atom dictionary
% scale: the scale is determined by a and j;
% i think that the j should include the 0

a_base=2;
j_min=0;
j_max=log2(N);

% the transmission or displacement u should determined as following
u_base=1/2;
p_min=0;

% p_max can be determined by its relationship with j
% the frequency v
v_base=pi;
k_min=0;

%k_max can be determined by it relationship with j
% the phase w
w_base=pi/6;
i_min=0;
i_max=12;

%part 2.2
% the matching pursuit process
for n=1:iterative_number

% the following program uses one subroutine to select the best atom

[proj,scale,translation,freq,phase]=select_best(signal_r, N, a_base, j_min, j_max, u_base, p_min, v_base, k_min, w_base, i_min, i_max);

% reconstruct the best atom from the parameters gotted by the above subroutine
t=0:N-1;
t=(t-translation)/scale;
g=(1/sqrt(scale))*exp(-pi*t.*t).*cos(freq*t+phase);
g=g/sqrt(sum(g.*g));

% reducing the best atom part from the residual signal and adding it to the reconstructed signal
signal_reconstruct=signal_reconstruct+proj*g;
signal_r=signal_r-proj*g;

% at each step of MP, we display the figures of the orignal signal, the best atom selected, the residual signal and hte reconstruced signal at window 1,2,3,4 respectively
subplot(221);
plot(bat);
subplot(222);
plot(g);
subplot(223);
plot(signal_r);
subplot(224);
plot(signal_reconstruct);
drawnow;
% n is the MP process number, or the number,or the number of atom selected
n
end



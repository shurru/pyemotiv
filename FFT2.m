Data=dlmread('onhead.dat'); 

fs= 128;
nf=128;
Y=fft(Data, nf);
f=fs/2*linspace(0,1,nf/2+1);
Z=abs(Y(1:nf/2+1));
plot(f, abs(Y(1:nf/2+1)));

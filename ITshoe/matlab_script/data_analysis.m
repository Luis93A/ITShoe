%% Clean
clc, clear all, close all;

%% Global var
global qploL;
global qploR;
global WL;
global WR;

%% Foot selection
%%WL- LEFT SHOE 1/0 (ON.OFF) 
WL= 1;
%%WR- RIGHT SHOE 1/0 (ON.OFF) 
WR= 0;

%% info 

%% Read file 
if WL
M= csvread('shoe_Left'); 
end
if WR
M1= csvread('shoe_Right');
end

%% input parameters
%%stp: number of steps
%%on_off: 0 = all steps; 
%%on_off: 1 = 1 step; 
%%on_off: 2= step range;

stp=6; on_off=0; whs=8; s_1 = 4; s_2 = 6; 

%% Data size
if WL
n= size(M,1);
end
if WR
n1= size(M1,1);
end

%% Calibration info
if WL
%%Calibration Var left shoe
a0 = 0.0005; a1 = 0.0003731; a2 = 0.0005; a3= 0.0005;
a4 = 1.0963; a5 = 1.0958; a6 = 1.0845; a7 = 1.0809;
b0 = -0.00004; b1 = 0.000049; b2 = 0.0001; b3 = 0.00001;
b4 = 65.881; b5 = 69.702; b6 = 66.179; b7 = 63.568;
end

if WR
%%Calibration Var right shoe
 a0r = 0.83; a1r = 0.83; a2r = 0.83 ; a3r= 0.83;
 a4r = 1.1869 ; a5r = 1.4093; a6r = 1.1358; a7r = 1.1358 ;
 b0r = 33 ; b1r =33 ; b2r = 33; b3r =33 ;
 b4r = 12.377; b5r = 8.8946 ; b6r = 33.055 ; b7r = 33.055 ;
end

%% Data extraction
if WL
%%Data extraction LEFT
for i=1:n
    F2(i)=M(i,5);
    F4(i)=M(i,8);
    F6(i)=M(i,2);%-M(1,2);
    F7(i)=M(i,6);%-M(1,6);
    F3(i)=M(i,7);
    F1(i)=M(i,3);
    F5(i)=M(i,4);%-M(1,4);
    F8(i)=M(i,9);%-M(1,9);
   
    r = M(end,10)-M(1,10);
    az(i) = M(i,1);
end
end

if WR
%%Data extraction RIGHT
for i=1:n1
    F2r(i)=M1(i,5);
    F4r(i)=M1(i,8);
    F6r(i)=M1(i,2);%-M1(1,2);
    F7r(i)=M1(i,6);%-M1(1,6);
    F3r(i)=M1(i,7);
    F1r(i)=M1(i,3);
    F5r(i)=M1(i,4);%-M1(1,4);
    F8r(i)=M1(i,9);%-M1(1,9);
   
    r1 = M1(end,10)-M1(1,10);
    az1(i) = M1(i,1);
    
end
end

%%

%% rate
if WL
%rate left
rate = (n)/r;
imp_aux= ['Rate_leftshoe:  ' ,num2str(rate), ' Hz'];
disp(imp_aux); 
end

if WR
%rate right
rate1 = (n1)/r1;
imp_aux1= ['Rate_rightshoe:  ' ,num2str(rate1), ' Hz'];
disp(imp_aux1); 
end

%% Data loss
if WL
%lost data left
dados_perdidos = ((az(n)-n)/n)*100;
dados_per_aux = [ 'Erro[%]: ', num2str(dados_perdidos)];
disp(dados_per_aux);
end

if WR
%dados perdidos right
dados_perdidos1 = ((az1(n1)-n1)/n1)*100;
dados_per_aux1 = [ 'Erro[%]: ', num2str(dados_perdidos1)];
disp(dados_per_aux1);
end

%% Time
if WL
%%Time shoe left
nn=size(F1,2);
Time_send1 = 0:(1/100):(nn/100);
Time_send = Time_send1(1,1:end-1);
end

if WR
%%Time shoe right
nn1=size(F1r,2);
Time_send1r = 0:(1/100):(nn1/100);
Time_sendr = Time_send1r(1,1:end-1);
end

%% PLOT1 raw data
plot(Time_send, F1+F2+F3+F4,'r');

%plot(Time_sendr, F5r+F6r+F7r+F8r); hold on; plot(Time_send, F5+F6+F7+F8, 'r');
%% Force calculation
if WL
%%Force calculation shoe left 
Vout0 = (F1+100) * (5.0 / 1023.0); Vout1 = F2 * (5.0 / 1023.0); Vout2 = F3 * (5.0 / 1023.0); Vout3 = F4 * (5.0 / 1023.0);
for k=1:nn
 Rfsr0(k) = (6000/Vout0(k))-1200;
 Rfsr1(k) = (6000/Vout1(k))- 1200;
Rfsr2(k) = (6000/Vout2(k))- 1200;
  Rfsr3(k)= (6000/Vout3(k))- 1200;
end
for h=1:nn
 F0a(h) = ((1/Rfsr0(h)) - b0) *(4.44822162825/a0);
 F1a(h) = ((1/Rfsr1(h)) - b1) *(4.44822162825/a1);
F2a(h) = ((1/Rfsr2(h)) - b2) *(4.44822162825/a2);
 F3a(h) = ((1/Rfsr3(h)) - b3) *(4.44822162825/a3); 
end
F4a = ((F5-b4)/a4)/100; F5a = ((F6-b5)/a5)/100; F6a = ((F7-b6)/a6)/100; F7a = ((F8-b7)/a7)/100;
end

if WR
%Force calculation right foot

F0ar = ((F1r-b0r)/a0r)/100; F1ar = ((F2r-b1r)/a1r)/100; F2ar = ((F3r-b2r)/a2r)/100; F3ar = ((F4r-b3r)/a3r)/100;
F4ar = ((F5r-b4r)/a4r)/100; F5ar = ((F6r-b5r)/a5r)/100; F6ar = ((F7r-b6r)/a6r)/100; F7ar = ((F8r-b7r)/a7r)/100;
end

if WL
%%fn, fhmov shoe left
fn=(F0a+F1a+F2a+F3a);
fhmov=-F4a*0.7071+F5a*0.7071-F6a*0.7071+F7a*0.7071;
end

if WR
%%fn, fhmov shoe right
fnr=(F0ar+F1ar+F2ar+F3ar);
fhmovr=-F4ar*0.7071+F5ar*0.7071-F6ar*0.7071+F7ar*0.7071;
end

%% plot selection 

%%plot qploL/R = fn or fhmov
if WL
qploL =fn;
end

if WR
qploR =fnr;
end

%% plots


%% Step extraction
if WL
%%Extract steps left
a=1; x=-1; j=1; z=0; b=0; indzero=find(fn(a:end)<1.5 & fn(a:end)>-5); a1=indzero(1);
for g=1:1:stp
    while x==-1
        x=indzero(1,j)-indzero(1,j+1); j=j+1; z=z+1; %n de zeros (pontos - pé no ar)
    end
    y=indzero(1,j-1)-indzero(1,j); a=a1+b+z; c=a-y-1;
    if g ~=1 %step index
        I(1,g)=a+1; %start step
        F(1,g)=c; %end step
    end
    b=c; z=0; x=-1; a1=0;
end
end

%%%

%%%

if WR
%%Extract steps right
ar=1; xr=-1; jr=1; zr=0; br=0; indzeror=find(fnr(ar:end)<1.5 & fnr(ar:end)>-5); a1r=indzeror(1);
for gr=1:1:stp
    while xr==-1
        xr=indzeror(1,jr)-indzeror(1,jr+1); jr=jr+1; zr=zr+1; %n de zeros (pontos - pé no ar)
    end
    yr=indzeror(1,jr-1)-indzeror(1,jr); ar=a1r+br+zr; cr=ar-yr-1;
    if gr ~=1 %step index
        Ir(1,gr)=ar+1; %start step
        Fr(1,gr)=cr; %end step
    end
    br=cr; zr=0; xr=-1; a1r=0;
end
end

%% Zeros remove
if WL
%%Remove ZEROS left
bb=1;
for hhh=1:1:size(I,2)
    if F(1,hhh)-I(1,hhh) > 0 
        II(1,bb) = I(1,hhh); FF(1,bb) = F(1,hhh); bb=bb+1;    
    end
end
end

if WR
%%Remove ZEROS right
bbr=1;
for hhhr=1:1:size(Ir,2)
    if Fr(1,hhhr)-Ir(1,hhhr) > 0 
        IIr(1,bbr) = Ir(1,hhhr); FFr(1,bbr) = Fr(1,hhhr); bbr=bbr+1;    
    end
end
end

%% Check step lenght
if WL
%%check 'steps' length left
jg=size(FF,2);
for kh=1:1:jg;
gj(kh)=FF(kh)-II(kh);
end
end

if WR
%%check 'steps' length right
jgr=size(FF,2);
for kh=1:1:jgr;
gjr(kh)=FFr(kh)-IIr(kh);
end
end
%% 
if WL
%%Look for steps with length between xx-xx %%% LEFT
baba=1;
for jl=1:1:jg
    if ( gj(jl) < 100 && gj(jl) >70  )
        III(1,baba) = II(1,jl); FFF(1,baba) = FF(1,jl); baba=baba+1;
    end
end
end

if WR
%%Look for steps with length between xx-xx %%% Right
baba=1;
for jl=1:1:jgr
    if ( gjr(jl) < 100 && gjr(jl) >70  )
        IIIr(1,baba) = IIr(1,jl); FFFr(1,baba) = FFr(1,jl); baba=baba+1;
    end
end
end

%%

if WL
if(on_off == 1) ws= whs; end
if(on_off == 0) ws=1:1:size(III,2); end
if(on_off == 2) ws= s_1:1:s_2; end
end

if WR
if(on_off == 1) wsr= whs; end
if(on_off == 0) wsr=1:1:size(IIIr,2); end
if(on_off == 2) wsr= s_1:1:s_2; end
end

%% interp , store data
if WL
for mpl=ws  
xol=1:numel(fhmov(III(mpl):FFF(mpl)));
xil= linspace(1,numel(fhmov(III(mpl):FFF(mpl))),100);
UU(:,:,1,mpl)= interp1(xol,fhmov(III(mpl):FFF(mpl)),xil);
end
end


%% Step indexs 
%all steps xx=1:1:size(III,2)
%which step -> ws=N;

% if WL
% if(on_off == 1) ws= whs; end
% if(on_off == 0) ws=1:1:size(III,2); end
% if(on_off == 2) ws= s_1:1:s_2; end
% end

% if WR
% if(on_off == 1) wsr= whs; end
% if(on_off == 0) wsr=1:1:size(IIIr,2); end
% if(on_off == 2) wsr= s_1:1:s_2; end
% end

% if WL
% %LEFT
% for xx=ws;
%     Y=qploL(III(1,xx):FFF(1,xx));
%     an(:,:,1)=Y;
% end
% end
% 
% if WR
% %RIGHT
% for xxr=wsr;
%     Yr=qploR(IIIr(1,xxr):FFFr(1,xxr));
%     anr(:,:,xxr)=Yr;
% end
% end

%% Steps Assembly
% if WL
% %%assembly steps vari: assem LEFT
% cll=size(an,2);%;*size(an,3);
% assem(1:cll)=an(1,:,:);
% end
% 
% if WR
% %%assembly steps vari: assem LEFT
% cllr=size(anr,2)*size(anr,3); assemr(1:cllr)=anr(1,:,:);
% end

%%plot all steps mpl=1:1:size(III,2)
%%plot 1 step ws=N

%% extra corr

%%
%% COP calculation
% distx= 38.4;
% disty=96;
% if WL
% for mm=1:1:n
% Copx(mm)= (F0a(mm)*(-distx/2)+ F1a(mm)*(distx/2)+ F2a(mm)*(-distx/2) +F3a(mm)*(distx/2))/(F0a(mm)+F1a(mm)+F2a(mm)+F3a(mm));
% Copy(mm)= (F0a(mm)*(disty/2)+ F1a(mm)*(disty/2)+ F2a(mm)*(-disty/2) +F3a(mm)*(-disty/2))/(F0a(mm)+F1a(mm)+F2a(mm)+F3a(mm));
% end
% end
% 
% if WR
% for mm=1:1:n1
% Copx(mm)= (F0ar(mm)*(-distx/2)+ F1ar(mm)*(distx/2)+ F2ar(mm)*(-distx/2) +F3ar(mm)*(distx/2))/(F0ar(mm)+F1ar(mm)+F2ar(mm)+F3ar(mm));
% Copy(mm)= (F0ar(mm)*(disty/2)+ F1ar(mm)*(disty/2)+ F2ar(mm)*(-disty/2) +F3ar(mm)*(-disty/2))/(F0ar(mm)+F1ar(mm)+F2ar(mm)+F3ar(mm));
% end
% end 

%%% FFT analysis
%if WL
%%%fft LEFT
%L=(mini+1);%*size(an,3); %Signal lenght
%Fs=mini+1; %sampling frequency
%bbb = detrend(assem); %remove 1st peak
%res = fft(bbb); %fft
%P1=abs(res/L); 
%f=Fs*(0:(L-1))/L;
%figure(1);
%subplot(2,2,3); 
%plot(f(1:end/2),P1(1:end/2)); hold on;% plot(f(1:end/2),P1(1:end/2),'.');
%inpaux=P1(1:end/2);
%end

%if WR
%%%fft RIGHT
%Lr=(minir+1)*size(anr,3); %Signal lenght
%Fsr=minir+1; %sampling frequency
%bbbr= detrend(assemr); %remove 1st peak
%resr = fft(bbbr); %fft
%P1r=abs(resr/Lr); 
%fr=Fsr*(0:(Lr-1))/Lr;
%figure(2);
%subplot(2,2,3);
%plot(fr(1:end/2),P1r(1:end/2));  hold on; plot(fr(1:end/2),P1r(1:end/2),'.');
%end

%%% FFT maxs
%if WL
%%%step fftmax LEFT
%[maxmax, Indd]=max(P1); %MAX
%[ndmax, inddnd] = max(P1(P1<max(P1))); %2ND MAX
%[ndmax1, inddnd1] = max(P1(P1<ndmax));%3rd max
%[ndmax2, inddnd2] = max(P1(P1<ndmax1)); %4th max
%end

%if WR
%%%step fftmax right
%[maxmaxr, Inddr]=max(P1r); %MAX
%[ndmaxr, inddndr] = max(P1r(P1r<max(P1r))); %2ND MAX
%[ndmax1r, inddnd1r] = max(P1r(P1r<ndmaxr));%3rd max
%[ndmax2r, inddnd2r] = max(P1r(P1r<ndmax1r)); %4th max
%end

%%% correlation coefs
%if WL
%%%correlation coef between steps, FFT each step- LEFT
%for xx=1:1:size(III,2)
%    %%subplot(2,2,4);  plot(Time_send(II(1,xx):FF(1,xx)),fn(II(1,xx):FF(1,xx)));hold on;; hold on; 
%    Y=fft(qploL(III(1,xx):FFF(1,xx)));
%    en(:,:,xx)=Y;
%end
%end

%if WR
%%%correlation coef between steps, FFT each step- right
%for xxr=1:1:size(IIIr,2)
%    %%subplot(2,2,4);  plot(Time_send(II(1,xx):FF(1,xx)),fn(II(1,xx):FF(1,xx)));hold on;; hold on; 
%    Yr=fft(qploR(IIIr(1,xxr):FFFr(1,xxr)));
%    enr(:,:,xxr)=Yr;
%end
%end

%if WL
%%left
%for cc0=1:1:size(III,2)-1;
%    for cc1=1:1:size(III,2)-1;
%    relat(cc0,cc1)=corr2(abs(en(:,:,cc0)),abs(en(:,:,cc1)));
%    end
%end
%end

%if WR
%%right 
%for cc0r=1:1:size(IIIr,2)-1;
%    for cc1r=1:1:size(IIIr,2)-1;
%    relatr(cc0r,cc1r)=corr2(abs(enr(:,:,cc0r)),abs(enr(:,:,cc1r)));
%    end
%end
%end

%%% fft phase angle
%if WL
%%%phase angle LEFT
%X_phase = angle(res);
%X_phase(inddnd+1);
%figure(1);
%subplot(2,2,4); plot(f(1:end/2),X_phase(1:end/2)); hold on; 
%end

%if WR
%%%phase angle RIGHT
%X_phaser = angle(resr);
%X_phaser(inddndr+1);
%figure(2);
%subplot(2,2,4); plot(fr(1:end/2),X_phaser(1:end/2)); hold on; 
%end

%%% Displays
%if WL
%%%Disp ans LEFT
%disp('MaxL: '); disp(maxmax);
%disp('2nd_MaxL: '); disp(ndmax);
%disp('3rd_MaxL: '); disp(ndmax1);
%disp('4th_MaxL: '); disp(ndmax2);
%disp('angle_MaxL: '); disp(X_phase(Indd));
%end

%if WR
%%%Disp ans RIGHT
%disp('MaxR: '); disp(maxmaxr);
%disp('2nd_MaxR: '); disp(ndmaxr);
%disp('3rd_MaxR: '); disp(ndmax1r);
%disp('4th_MaxR: '); disp(ndmax2r);
%disp('angle_MaxR: '); disp(X_phaser(Inddr));
%end

%%% RMS

%%ys= rms(F1+F2+F3+F4)

%%% Peak

%%[pks,locs] = findpeaks(F1+F2+F3+F4) 

%%% Crest factor

%%CF= pks/ys;

%%% kurtosis

%%wakur = kurtosis(F1+F2+F3+F4);

%%% Spectrogram

%%s = spectrogram(F1+F2+F3+F4);
%%spectrogram(F1+F2+F3+F4,'yaxis')

%%% future attempts: 
%%wavelet toolbox
%%stft
%%http://www.acoustics.asn.au/conference_proceedings/ICSVS-1997/pdf/scan/sv970356.pdf
%%http://cdn.intechopen.com/pdfs-wm/10675.pdf
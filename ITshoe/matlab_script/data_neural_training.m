
clc, clear all,close all;

z=1; %lixo
HL =70; %HL neurons
perf=1; % goal 
%rng(0)
while(perf > 0.003)

%if(z==100)
%HL=HL+1;
%end
%z=z+1;
    
%% Load data:
%Teflon FREQ 0.6 step 0.06

load('T66.mat');

T_aux=diff(UU);
T66= T_aux(:,:,1,:);
T66=reshape(T66,[99,231]);

load('T661.mat');

T_aux1=diff(UU1);
T661= T_aux1(:,:,1,:);
T661=reshape(T661,[99,43]);

T66=[T66 T661]; 

%Teflon FREQ 0.6 step 0.04
load('T64.mat');

T_aux2=diff(UU2);
T64= T_aux2(:,:,1,:);
T64=reshape(T64,[99,460]); 

%Teflon FREQ 0.6 step 0.02
load('T62.mat');

T_aux3=diff(UU3);
T62= T_aux3(:,:,1,:);
T62=reshape(T62,[99,155]);

load('T621.mat');

T_aux4=diff(UU4);
T621= T_aux4(:,:,1,:);
T621=reshape(T621,[99,312]);

T62=[ T62 T621] ; 

%Teflon FREQ 0.4 step 0.06
load('T46.mat');

T_aux5=diff(UU5);
T46= T_aux5(:,:,1,:);
T46=reshape(T46,[99,266]); 

%Teflon FREQ 0.4 step 0.04

load('T44.mat');

T_aux5=diff(UU6);
T44= T_aux5(:,:,1,:);
T44=reshape(T44,[99,382]); 

%Teflon FREQ 0.4 step 0.02

load('T42.mat');

T_aux5=diff(UU7);
T42= T_aux5(:,:,1,:);
T42=reshape(T42,[99,379]); 

%Teflon FREQ 0.2 step 0.06

load('T26.mat');

T_aux5=diff(UU8);
T26= T_aux5(:,:,1,:);
T26=reshape(T26,[99,223]); 

%Teflon FREQ 0.2 step 0.04

load('T24.mat');

T_aux5=diff(UU9);
T24= T_aux5(:,:,1,:);
T24=reshape(T24,[99,83]);

load('T241.mat');

T_aux5=diff(UU10);
T241= T_aux5(:,:,1,:);
T241=reshape(T241,[99,154]);

T24 = [ T24 T241]; 

%Teflon FREQ 0.2 step 0.02

load('T22.mat');

T_aux5=diff(UU11);
T22= T_aux5(:,:,1,:);
T22=reshape(T22,[99,288]); 

%ALUM FREQ 0.6 step 0.06

load('A66.mat');

T_aux5=diff(UU12);
A66= T_aux5(:,:,1,:);
A66=reshape(A66,[99,123]); 

%ALUM FREQ 0.6 step 0.04

load('A64.mat');

T_aux5=diff(UU14);
A64= T_aux5(:,:,1,:);
A64=reshape(A64,[99,108]); 


%ALUM FREQ 0.6 step 0.02

load('A62.mat');

T_aux5=diff(UU15);
A62= T_aux5(:,:,1,:);
A62=reshape(A62,[99,154]); 

%ALUM FREQ 0.4 step 0.06

load('A46.mat');

T_aux5=diff(UU16);
A46= T_aux5(:,:,1,:);
A46=reshape(A46,[99,41]);

load('A461.mat');

T_aux5=diff(UU17);
A461= T_aux5(:,:,1,:);
A461=reshape(A461,[99,68]);

A46 = [ A46 A461]; 

%ALUM FREQ 0.4 step 0.04

load('A44.mat');

T_aux5=diff(UU18);
A44= T_aux5(:,:,1,:);
A44=reshape(A44,[99,141]); 

%ALUM FREQ 0.4 step 0.02

load('A42.mat');

T_aux5=diff(UU19);
A42= T_aux5(:,:,1,:);
A42=reshape(A42,[99,139]); 

%ALUM FREQ 0.2 step 0.06

load('A26.mat');

T_aux5=diff(UU20);
A26= T_aux5(:,:,1,:);
A26=reshape(A26,[99,23]);

load('A261.mat');

T_aux5=diff(UU21);
A261= T_aux5(:,:,1,:);
A261=reshape(A261,[99,76]);

A26= [A26 A261]; 

%ALUM FREQ 0.2 step 0.04

load('A24.mat');

T_aux5=diff(UU22);
A24= T_aux5(:,:,1,:);
A24=reshape(A24,[99,129]); 

%ALUM FREQ 0.2 step 0.02

load('A22.mat');

T_aux5=diff(UU24);
A22= T_aux5(:,:,1,:);
A22=reshape(A22,[99,156]); 

%Acryl FREQ 0.6 step 0.06

load('AC66.mat');

T_aux5=diff(UU25);
AC66= T_aux5(:,:,1,:);
AC66=reshape(AC66,[99,223]); 

%Acryl FREQ 0.6 step 0.04

load('AC64.mat');

T_aux5=diff(UU26);
AC64= T_aux5(:,:,1,:);
AC64=reshape(AC64,[99,131]); 


%Acryl FREQ 0.6 step 0.02

load('AC62.mat');

T_aux5=diff(UU27);
AC62= T_aux5(:,:,1,:);
AC62=reshape(AC62,[99,149]); 

%Acryl FREQ 0.4 step 0.06

load('AC46.mat');

T_aux5=diff(UU28);
AC46= T_aux5(:,:,1,:);
AC46=reshape(AC46,[99,73]);

load('AC461.mat');

T_aux5=diff(UU29);
AC461= T_aux5(:,:,1,:);
AC461=reshape(AC461,[99,53]);

AC46= [AC46 AC461]; 


%Acryl FREQ 0.4 step 0.04

load('AC44.mat');

T_aux5=diff(UU30);
AC44= T_aux5(:,:,1,:);
AC44=reshape(AC44,[99,60]);

load('AC441.mat');

T_aux5=diff(UU31);
AC441= T_aux5(:,:,1,:);
AC441=reshape(AC441,[99,93]);

AC44 = [AC44 AC441]; 

%Acryl FREQ 0.4 step 0.02

load('AC42.mat');

T_aux5=diff(UU32);
AC42= T_aux5(:,:,1,:);
AC42=reshape(AC42,[99,175]); 

%Acryl FREQ 0.2 step 0.06

load('AC26.mat');

T_aux5=diff(UU33);
AC26= T_aux5(:,:,1,:);
AC26=reshape(AC26,[99,130]); 

%Acryl FREQ 0.2 step 0.04

load('AC24.mat');

T_aux5=diff(UU34);
AC24= T_aux5(:,:,1,:);
AC24=reshape(AC24,[99,148]); 

%Acryl FREQ 0.2 step 0.02

load('AC22.mat');

T_aux5=diff(UU35);
AC22= T_aux5(:,:,1,:);
AC22=reshape(AC22,[99,156]); 


%GREEN FREQ 0.6 step 0.06

load('G66.mat');

T_aux5=diff(UU36);
G66= T_aux5(:,:,1,:);
G66=reshape(G66,[99,115]); 

%GREEN FREQ 0.6 step 0.04

load('G64.mat');

T_aux5=diff(UU37);
G64= T_aux5(:,:,1,:);
G64=reshape(G64,[99,128]); 

%GREEN FREQ 0.6 step 0.02

load('G62.mat');

T_aux5=diff(UU38);
G62= T_aux5(:,:,1,:);
G62=reshape(G62,[99,133]); 

%GREEN FREQ 0.4 step 0.06

load('G46.mat');

T_aux5=diff(UU39);
G46= T_aux5(:,:,1,:);
G46=reshape(G46,[99,125]); 

%GREEN FREQ 0.4 step 0.04

load('G44.mat');

T_aux5=diff(UU40);
G44= T_aux5(:,:,1,:);
G44=reshape(G44,[99,121]); 


%GREEN FREQ 0.4 step 0.02

load('G42.mat');

T_aux5=diff(UU41);
G42= T_aux5(:,:,1,:);
G42=reshape(G42,[99,156]); 


%GREEN FREQ 0.2 step 0.06

load('G26.mat');

T_aux5=diff(UU42);
G26= T_aux5(:,:,1,:);
G26=reshape(G26,[99,133]); 

%GREEN FREQ 0.2 step 0.04

load('G24.mat');

T_aux5=diff(UU43);
G24= T_aux5(:,:,1,:);
G24=reshape(G24,[99,52]);

load('G241.mat');

T_aux5=diff(UU44);
G241= T_aux5(:,:,1,:);
G241=reshape(G241,[99,53]);

G24 = [G24 G241]; 


%GREEN FREQ 0.2 step 0.02

load('G22.mat');

T_aux5=diff(UU45);
G22= T_aux5(:,:,1,:);
G22=reshape(G22,[99,155]); 

%% ASSEMBLY 

%% TEFLON
aux1=randperm(274,99);
aux2=randperm(460,99);
aux3=randperm(467,99);
aux4=randperm(266,99);
aux5=randperm(382,99);
aux6=randperm(379,99);
aux7=randperm(223,99);
aux8=randperm(237,99);
aux9=randperm(288,99);

i=1;
for i=1:1:99
    T1(:,i)=T66(:,aux1(i));   
    T2(:,i)=T64(:,aux2(i)); 
    T3(:,i)=T62(:,aux3(i)); 
    T4(:,i)=T46(:,aux4(i)); 
    T5(:,i)=T44(:,aux5(i)); 
    T6(:,i)=T42(:,aux6(i)); 
    T7(:,i)=T26(:,aux7(i)); 
    T8(:,i)=T24(:,aux8(i)); 
    T9(:,i)=T22(:,aux9(i)); 
end

T= [T1 T2 T3 T4 T5 T6 T7 T8 T9];

%% ALUM
aux1=randperm(123,99);
aux2=randperm(108,99);
aux3=randperm(154,99);
aux4=randperm(109,99);
aux5=randperm(141,99);
aux6=randperm(139,99);
aux7=randperm(99,99);
aux8=randperm(129,99);
aux9=randperm(156,99);

i=1;
for i=1:1:99
    A1(:,i)=A66(:,aux1(i));   
    A2(:,i)=A64(:,aux2(i)); 
    A3(:,i)=A62(:,aux3(i)); 
    A4(:,i)=A46(:,aux4(i)); 
    A5(:,i)=A44(:,aux5(i)); 
    A6(:,i)=A42(:,aux6(i)); 
    A7(:,i)=A26(:,aux7(i)); 
    A8(:,i)=A24(:,aux8(i)); 
    A9(:,i)=A22(:,aux9(i)); 
end

A= [A1 A2 A3 A4 A5 A6 A7 A8 A9];

%% Acryl
aux1=randperm(223,99);
aux2=randperm(131,99);
aux3=randperm(149,99);
aux4=randperm(126,99);
aux5=randperm(153,99);
aux6=randperm(175,99);
aux7=randperm(130,99);
aux8=randperm(148,99);
aux9=randperm(156,99);

i=1;
for i=1:1:99
    AC1(:,i)=AC66(:,aux1(i));   
    AC2(:,i)=AC64(:,aux2(i)); 
    AC3(:,i)=AC62(:,aux3(i)); 
    AC4(:,i)=AC46(:,aux4(i)); 
    AC5(:,i)=AC44(:,aux5(i)); 
    AC6(:,i)=AC42(:,aux6(i)); 
    AC7(:,i)=AC26(:,aux7(i)); 
    AC8(:,i)=AC24(:,aux8(i)); 
    AC9(:,i)=AC22(:,aux9(i)); 
end

AC= [AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC9];


%% GREEN
aux1=randperm(115,99);
aux2=randperm(128,99);
aux3=randperm(133,99);
aux4=randperm(125,99);
aux5=randperm(121,99);
aux6=randperm(156,99);
aux7=randperm(133,99);
aux8=randperm(105,99);
aux9=randperm(155,99);

i=1;
for i=1:1:99
    G1(:,i)=G66(:,aux1(i));   
    G2(:,i)=G64(:,aux2(i)); 
    G3(:,i)=G62(:,aux3(i)); 
    G4(:,i)=G46(:,aux4(i)); 
    G5(:,i)=G44(:,aux5(i)); 
    G6(:,i)=G42(:,aux6(i)); 
    G7(:,i)=G26(:,aux7(i)); 
    G8(:,i)=G24(:,aux8(i)); 
    G9(:,i)=G22(:,aux9(i)); 
end

G= [G1 G2 G3 G4 G5 G6 G7 G8 G9];

%% Inputs
Input= [ T AC A G];

%% Targets
Targets= [ones(1,891) zeros(1,2673)
        zeros(1,891) ones(1,891) zeros(1,1782)
        zeros(1,1782) ones(1,891) zeros(1,891)
        zeros(1,2673) ones(1,891)];
   
     
%% Create a Pattern Recognition Network
net = patternnet([HL], 'trainlm'); % layers
net.divideParam.trainRatio = 0.5;
net.divideParam.valRatio = 0.25;
net.divideParam.testRatio = 0.25;
net.trainParam.min_grad = 1e-15;
net.trainParam.max_fail = 10;
net.trainparam.epochs=1000;
net.trainparam.goal=1e-15;
%net.trainparam.lr=0.1;

%% Train the Network
% Train the Network
[net,tr] = train(net,Input,Targets);

%% Test the network
Output=net(Input);
errors = gsubtract(Targets,Output);
perf= perform(net,Targets,Output);


%% Recalculate Training, Validation and Test Performance
trainTargets = Targets .* tr.trainMask{1};
valTargets = Targets  .* tr.valMask{1};
testTargets = Targets  .* tr.testMask{1};
trainPerformance = perform(net,trainTargets,Output)
valPerformance = perform(net,valTargets,Output)
testPerformance = perform(net,testTargets,Output)
%%TOTAL DATA ASSEMBLY%%%


%% Other test

%Input_test= [ T66 T64 T62 T46 T44 T42 T26 T24 T22 AC66 AC64 AC62 AC46 AC44 AC42 AC26 AC24 AC22 A66 A64 A62 A46 A44 A42 A26 A24 A22 G66 G64 G62 G46 G44 G42 G26 G24 G22];

%Output_test= [ones(1,2976) zeros(1,3720)
  %  zeros(1,2976) ones(1,1391) zeros(1,2329)
  %  zeros(1,2976+1391) ones(1,1158) zeros(1,1171)
  %  zeros(1,2976+1391+1158) ones(1,1171)];

%Outp=net(Input_test);
%Outp=round(Outp);
%nn=sum(Outp==Output_test);
%nn=sum(nn==4)
%new_perf=(nn/(6696))*100
 
end



%Calculo para la EDO en la parte espacial de la ecuación de K-G.
%Variamos las ctes Eo y w
syms Eo
syms w
syms m
%ctes xspan y CI 
xspan=[0,10];
yazero=[1;1];
options=odeset('AbsTol',1e-7,'RelTol',1e-4);
%Caso A
Eo=1; m=1; w=1;
[xA,yA]=ode45(@yprime,xspan,yazero,options,Eo,m,w);
subplot(2,2,1)
plot(xA,yA(:,1))
xlabel('x')
ylabel('g(x)')
title(' E_{0}=1 m=1 \omega=1')
axis([0 10 -2 2]);
%Caso B
Eo=1; m=1; w=3;
[xA,yA]=ode45(@yprime,xspan,yazero,options,Eo,m,w);
subplot(2,2,2)
plot(xA,yA(:,1))
xlabel('x')
ylabel('g(x)')
title(' E_{0}=1 \omega=3 m=1')
axis([0 10 -2 2]);
%Caso c
Eo=3; m=1; w=1;
[xA,yA]=ode45(@yprime,xspan,yazero,options,Eo,m,w);
subplot(2,2,3)
plot(xA,yA(:,1))
xlabel('x')
ylabel('g(x)')
title(' E_{0}=3 \omega=1 m=1')
axis([0 10 -2 2]);
%Caso D
Eo=6; m=1; w=6;
[xA,yA]=ode45(@yprime,xspan,yazero,options,Eo,m,w);
subplot(2,2,4) 
plot(xA,yA(:,1))
xlabel('x')
ylabel('g(x)')
title(' E_{0}=6 \omega=6,m=1')
axis([0 10 -2 2]);

function yprime=klg(x,y,Eo,m,w)
%ctes Eo,m y w
yprime=[y(2);-(w^2+Eo^2*x^2+w*Eo*x-m^2)*y(1)];
options=odeset('AbsTol',1e-7,'RelTol',1e-4);

end



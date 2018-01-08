% 计算单个神经元的元误差曲面

clear all;clc;

p = [-6.0 -6.1 -4.1 -4.0 4.0 4.1 6.0 6.1];
t = [0.0 0.0 0.97 0.99 0.01 0.03 1.0 1.0];

wv = -1 : 0.1 : 1;
bv = -2.5:0.25:2.5;

es = errsurf(p,t,wv,bv,'logsig');
plotes(wv,bv,es,[60 30])
set(gcf,'color','w')
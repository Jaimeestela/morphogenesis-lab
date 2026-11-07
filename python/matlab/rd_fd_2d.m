%% rd_fd_2d.m - 2D reaction-diffusion finite difference (minimal)
% Laplacian 5-point, explicit Euler. Gray-Scott parameters.
% Usage: run in MATLAB; u,v are (ny,nx); optionally save/plot.

function [u, v] = rd_fd_2d(nx, ny, n_steps, dt, dx, F, k, Du, Dv, seed)
if nargin < 10, seed = 42; end
if nargin < 9, Dv = 0.0001; end
if nargin < 8, Du = 0.0002; end
if nargin < 7, k = 0.062; end
if nargin < 6, F = 0.03; end
if nargin < 5, dx = 1; end
if nargin < 4, dt = 0.5; end
if nargin < 3, n_steps = 500; end
if nargin < 2, ny = 64; end
if nargin < 1, nx = 64; end

rng(seed);
u0 = 1; v0 = 0;
u = u0 + 0.01*(rand(ny,nx)-0.5);
v = v0 + 0.01*(rand(ny,nx)-0.5);

for step = 1:n_steps
    % Laplacian 5-point (Neumann: extend at boundary)
    Lu = (u([2:end end],:) + u([1 1:end-1],:) + u(:,[2:end end]) + u(:,[1 1:end-1]) - 4*u) / (dx^2);
    Lv = (v([2:end end],:) + v([1 1:end-1],:) + v(:,[2:end end]) + v(:,[1 1:end-1]) - 4*v) / (dx^2);
    f = -u.*v.^2 + F*(1-u);
    g = u.*v.^2 - (F+k)*v;
    u = u + dt*(Du*Lu + f);
    v = v + dt*(Dv*Lv + g);
end
end

%% rd_stability_linear.m - Linear stability: eigenvalues of (J - k^2*D), find dominant k
% Gray-Scott at equilibrium (1,0): J = [-F -0; 0 -(F+k)], then J - k^2*diag(Du,Dv).
% Returns k_dominant and Re(lambda) at that k.

function [k_dominant, lambda_max, k_arr, re_lambda] = rd_stability_linear(Du, Dv, F, k, k_min, k_max, n_k)
if nargin < 7, n_k = 200; end
if nargin < 6, k_max = 20; end
if nargin < 5, k_min = 0; end
if nargin < 4, k = 0.062; end
if nargin < 3, F = 0.03; end
if nargin < 2, Dv = 0.0001; end
if nargin < 1, Du = 0.0002; end

u0 = 1; v0 = 0;
% Jacobian Gray-Scott at (1,0): df/du=-F, df/dv=0, dg/du=0, dg/dv=-(F+k)
J = [-F 0; 0 -(F+k)];
D = diag([Du, Dv]);

k_arr = linspace(k_min, k_max, n_k);
re_lambda = zeros(size(k_arr));
for i = 1:length(k_arr)
    M = J - k_arr(i)^2 * D;
    w = eig(M);
    re_lambda(i) = max(real(w));
end
[lambda_max, idx] = max(re_lambda);
k_dominant = k_arr(idx);
end

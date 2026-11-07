%% rd_demo_patterns.m - Demo: stability barrido + FD 2D run
% Run rd_stability_linear and rd_fd_2d; plot results.

% 1) Stability
[k_dom, lam_max, k_arr, re_lam] = rd_stability_linear(0.0002, 0.0001, 0.03, 0.062, 0, 20, 200);
figure(1); plot(k_arr, re_lam); xlabel('k'); ylabel('Re(\lambda)'); title('Gray-Scott linear stability');
hold on; plot(k_dom, lam_max, 'ro'); hold off;
saveas(gcf, 'stability_demo.png');

% 2) FD 2D
[u, v] = rd_fd_2d(128, 128, 2000, 0.5, 1, 0.03, 0.062, 0.0002, 0.0001, 42);
figure(2); subplot(1,2,1); imagesc(u); colorbar; title('u');
subplot(1,2,2); imagesc(v); colorbar; title('v');
saveas(gcf, 'pattern_demo.png');

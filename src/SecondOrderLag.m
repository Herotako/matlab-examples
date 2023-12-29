%% 初期化
clc         % コマンドウィンドウの初期化
clear       % ワークスペースの初期化
close all   % グラフを全部閉じる

%% 変数宣言
% ===== 制御対象 =====
zeta = 0.2;       % 減衰係数
omega_n = 1;      % 固有角周波数
K = 2;            % システムゲイン

%% 伝達関数
s = tf('s');                    % ラプラス演算子
Gs = K*omega_n^2 / (s^2 + 2*zeta*omega_n*s + omega_n^2); % 制御対象G(s)

%% ボード線図描画
figure;
nyquist(Gs)
grid on;

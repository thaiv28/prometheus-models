# Elo variants benchmark

## Combined summary (validation, all sections)

| Model | Series Δ log loss | Series flat ROI | Series Kelly (LoL caps) $ | Series flat ROI depth-capped | Series Kelly depth-capped $ | Game Δ log loss | Game flat ROI | Game Kelly (LoL caps) $ | Game flat ROI depth-capped | Game Kelly depth-capped $ | Series blended Δ log loss | Series blended flat ROI | Series blended Kelly (LoL caps) $ | Series blended flat ROI depth-capped | Series blended Kelly depth-capped $ | Game blended Δ log loss | Game blended flat ROI | Game blended Kelly (LoL caps) $ | Game blended flat ROI depth-capped | Game blended Kelly depth-capped $ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| player_glicko | -0.000787 | 2.51% | $61.17 | 0.49% | $48.14 | 0.010214 | -6.61% | $15.58 | -21.16% | $41.30 | -0.004193 | 11.82% | $88.24 | 12.31% | $74.91 | 0.005517 | -2.68% | $34.20 | 38.11% | $50.56 |
| player_glicko_rookie_weights | -0.004780 | 4.14% | $101.33 | -2.18% | $73.47 | 0.011380 | -13.97% | $12.88 | -15.41% | $37.23 | -0.007002 | 4.55% | $76.17 | 0.98% | $52.11 | 0.008170 | -14.18% | $16.35 | 3.69% | $48.48 |
| player_glicko_rw_tier_revert | -0.004179 | 5.16% | $84.26 | -2.15% | $49.50 | 0.011705 | -11.88% | $11.91 | -28.38% | $37.98 | -0.006625 | 9.11% | $61.82 | 2.73% | $52.09 | 0.008881 | -12.55% | $17.09 | 33.50% | $52.31 |
| player_glicko+none | -0.000787 | 2.51% | $61.17 | 0.49% | $48.14 | 0.010214 | -6.61% | $15.58 | -21.16% | $41.30 | -0.004193 | 11.82% | $88.24 | 12.31% | $74.91 | 0.005517 | -2.68% | $34.20 | 38.11% | $50.56 |
| player_glicko+regional | -0.002240 | -1.33% | $60.49 | -4.79% | $49.29 | 0.007743 | -2.50% | $25.31 | -26.22% | $38.04 | -0.004924 | 24.19% | $84.37 | 25.41% | $77.34 | 0.006827 | -8.00% | $31.78 | 33.34% | $51.68 |
| player_glicko+calibration | -0.003952 | 6.60% | $249.38 | 2.89% | $78.83 | 0.008021 | -8.68% | $14.98 | -6.20% | $42.80 | -0.006728 | 27.95% | $89.04 | 26.91% | $83.05 | 0.004171 | -16.07% | $35.27 | 96.23% | $50.28 |
| player_glicko+form | 0.001004 | 0.88% | $30.31 | -0.76% | $29.96 | 0.012749 | -10.34% | $15.59 | -15.93% | $40.05 | -0.003305 | 9.77% | $81.33 | 14.99% | $77.52 | 0.003774 | -23.34% | $43.24 | 4.46% | $49.82 |
| player_glicko_rookie_weights+none | -0.004780 | 4.14% | $101.33 | -2.18% | $73.47 | 0.011380 | -13.97% | $12.88 | -15.41% | $37.23 | -0.007002 | 4.55% | $76.17 | 0.98% | $52.11 | 0.008170 | -14.18% | $16.35 | 3.69% | $48.48 |
| player_glicko_rookie_weights+regional | -0.005906 | 6.84% | $131.65 | -0.59% | $76.57 | 0.009147 | -7.19% | $15.92 | -23.15% | $33.37 | -0.007831 | 9.24% | $83.95 | 3.05% | $59.88 | 0.010325 | -14.06% | $18.08 | -1.81% | $51.73 |
| player_glicko_rookie_weights+calibration | -0.006768 | 8.60% | $234.70 | 2.09% | $84.35 | 0.009509 | -10.31% | $16.51 | -1.07% | $41.17 | -0.008883 | 11.53% | $87.23 | 4.41% | $57.32 | 0.007197 | -15.68% | $25.87 | 21.48% | $55.12 |
| player_glicko_rookie_weights+form | -0.006079 | 6.80% | $217.72 | 5.77% | $98.29 | 0.011561 | -11.05% | $11.67 | -19.77% | $39.66 | -0.008193 | 8.43% | $65.73 | 12.19% | $79.72 | 0.002252 | 0.18% | $49.55 | — | $50.00 |
| player_glicko_rw_tier_revert+none | -0.004179 | 5.16% | $84.26 | -2.15% | $49.50 | 0.011705 | -11.88% | $11.91 | -28.38% | $37.98 | -0.006625 | 9.11% | $61.82 | 2.73% | $52.09 | 0.008881 | -12.55% | $17.09 | 33.50% | $52.31 |
| player_glicko_rw_tier_revert+regional | -0.004771 | 4.80% | $73.03 | -2.86% | $43.24 | 0.010927 | -7.93% | $13.08 | -36.25% | $34.95 | -0.006817 | 16.89% | $55.80 | 8.32% | $57.21 | 0.013925 | -17.49% | $12.39 | 18.89% | $52.92 |
| player_glicko_rw_tier_revert+calibration | -0.005901 | 8.88% | $172.54 | 2.20% | $62.53 | 0.010378 | -11.22% | $15.39 | -13.91% | $44.07 | -0.008260 | 18.30% | $58.96 | 13.53% | $55.07 | 0.008492 | -11.76% | $25.13 | 35.15% | $59.53 |
| player_glicko_rw_tier_revert+form | -0.005413 | 5.54% | $178.74 | 4.36% | $71.92 | 0.011907 | -12.20% | $11.75 | -23.84% | $41.72 | -0.007980 | 12.13% | $60.09 | 15.97% | $70.77 | 0.002141 | -40.84% | $49.92 | — | $50.00 |

Series temperatures (stage 1; p′ = σ(T·logit p), T < 1 pulls odds toward 50%): player_glicko Bo3 0.69, Bo5 0.82; player_glicko_rookie_weights Bo3 0.74, Bo5 0.89; player_glicko_rw_tier_revert Bo3 0.80, Bo5 0.97; player_glicko+none Bo3 0.69, Bo5 0.82; player_glicko+regional Bo3 0.70, Bo5 0.84; player_glicko+calibration Bo3 0.72, Bo5 0.83; player_glicko+form Bo3 0.66, Bo5 0.80; player_glicko_rookie_weights+none Bo3 0.74, Bo5 0.89; player_glicko_rookie_weights+regional Bo3 0.76, Bo5 0.90; player_glicko_rookie_weights+calibration Bo3 0.78, Bo5 0.92; player_glicko_rookie_weights+form Bo3 0.71, Bo5 0.85; player_glicko_rw_tier_revert+none Bo3 0.80, Bo5 0.97; player_glicko_rw_tier_revert+regional Bo3 0.81, Bo5 0.97; player_glicko_rw_tier_revert+calibration Bo3 0.78, Bo5 0.93; player_glicko_rw_tier_revert+form Bo3 0.76, Bo5 0.92

Parameters minimize tuning game log loss across all sections. Replay predicts before update; Replay starts at the first game. Tuning: [2023-01-01, 2025-11-01); validation: [2025-11-01, 2026-07-01). Holdout is scored only with --holdout and never selects parameters. Series use the first game prediction and independent games in Bo1/Bo3/Bo5; Bo2, unknown/unsupported lengths and unknown results are skipped. Accuracy gives 0.5 predictions half credit; ECE uses 10 equal-width bins. Log loss clips probabilities at 1e-6. Paired bootstrap uses 2,000 resamples, seed 0, clustered by match_id. Differences are the named model minus its comparator; negative favors the model. Significance requires a 95% percentile interval excluding zero. Tuning scores are selection diagnostics, not independent evidence of improvement.

Fit through 2025-10-31. Unknown host-region game rows: 2576 (including missing/un).

## Stage 1 — tuning (outcomes)

### Leaderboard

| Model | Best params | Game log loss | Series log loss | Rows |
|---|---|---:|---:|---:|
| player_glicko_rw_tier_revert | {"inactive_half_life": 0, "k": 24, "new_player": "fixed", "online_k": 0.75, "rd_info": 0.0625, "rd_new": 280, "revert_target": "tier", "rookie_maps": 800, "rookie_penalty": 600, "season_month": 10, "season_revert": 0.1, "tier3_k": 0.75} | 0.608853 | 0.570665 | 38138 |
| player_glicko_rookie_weights | {"k": 24, "new_player": "fixed", "online_k": 0.75, "rd_info": 0.0625, "rd_new": 280, "rookie_maps": 800, "rookie_penalty": 600, "tier3_k": 0.75} | 0.609371 | 0.570966 | 38138 |
| player_glicko | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 280} | 0.621611 | 0.599064 | 38138 |
| team_elo | {"k": 32} | 0.650054 | 0.638841 | 38138 |

Kalshi uses the first hourly bid/ask (midpoint for log loss, ask/bid for bets) ending ≥30 min after the market opened and ≥2 h before the scheduled start, with a spread ≤ 0.06: a price a bot could trade before the series. Markets without such a quote are skipped. oriented to team1 using aliases. One contract per event, preferring team1. Compare identical rows; game predictions use the first game's pre-match chance. Missing links, aliases or candles are skipped; unplayed games are not in the rows. Returns use frozen stage-1 parameters. Each bet buys $1 of contracts, fees extra; order fees ceil to a cent (0.07 × contracts × price × (1−price)). Edge selection uses unrounded per-contract fees. ROI divides profit by stake plus fees; intervals resample matches 2,000 times. Unlimited depth and depth-capped returns are shown together. Depth uses 0.5 of acceptable-price tape volume in the 6 hours after the quote, missing tapes give zero fills. Partial Kelly fills are allowed; flat bets require the full $1 stake. Kelly uses LoL caps and rounded-fee affordability, from a $50 seed. Each slice runs independently. Tape volume is a fill proxy; no slippage is modeled.

### Games

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| coin | all | 38138 | 0.693147 | 0.250000 | 0.500000 | 0.045309 |
| coin | tier1 | 14067 | 0.693147 | 0.250000 | 0.500000 | 0.064655 |
| coin | tier2 | 4028 | 0.693147 | 0.250000 | 0.500000 | 0.067527 |
| coin | tier3 | 20036 | 0.693147 | 0.250000 | 0.500000 | 0.027301 |
| coin | unknown | 7 | 0.693147 | 0.250000 | 0.500000 | 0.071429 |
| coin | international=1 | 14341 | 0.693147 | 0.250000 | 0.500000 | 0.063838 |
| coin | international=0 | 23797 | 0.693147 | 0.250000 | 0.500000 | 0.034143 |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko | all | 38138 | 0.621611 | 0.216843 | 0.647884 | 0.015926 |
| player_glicko | tier1 | 14067 | 0.602339 | 0.208555 | 0.670399 | 0.017557 |
| player_glicko | tier2 | 4028 | 0.615472 | 0.214144 | 0.649950 | 0.026351 |
| player_glicko | tier3 | 20036 | 0.636334 | 0.223185 | 0.631738 | 0.016229 |
| player_glicko | unknown | 7 | 0.740453 | 0.273159 | 0.428571 | 0.144047 |
| player_glicko | international=1 | 14341 | 0.602825 | 0.208746 | 0.669967 | 0.016413 |
| player_glicko | international=0 | 23797 | 0.632932 | 0.221723 | 0.634576 | 0.016432 |

player_glicko − coin (paired log loss):

| Section | Rows | player_glicko log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 38138 | 0.621611 | 0.693147 | -0.071536 | [-0.075521, -0.067687] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko_rookie_weights | all | 38138 | 0.609371 | 0.211474 | 0.661584 | 0.011006 |
| player_glicko_rookie_weights | tier1 | 14067 | 0.588778 | 0.203017 | 0.680493 | 0.010313 |
| player_glicko_rookie_weights | tier2 | 4028 | 0.604510 | 0.209178 | 0.660626 | 0.021812 |
| player_glicko_rookie_weights | tier3 | 20036 | 0.624802 | 0.217872 | 0.648483 | 0.014337 |
| player_glicko_rookie_weights | unknown | 7 | 0.619052 | 0.213743 | 0.714286 | 0.128246 |
| player_glicko_rookie_weights | international=1 | 14341 | 0.589231 | 0.203175 | 0.680148 | 0.009629 |
| player_glicko_rookie_weights | international=0 | 23797 | 0.621507 | 0.216475 | 0.650397 | 0.012553 |

player_glicko_rookie_weights − coin (paired log loss):

| Section | Rows | player_glicko_rookie_weights log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 38138 | 0.609371 | 0.693147 | -0.083777 | [-0.088172, -0.079637] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko_rw_tier_revert | all | 38138 | 0.608853 | 0.211262 | 0.662187 | 0.011245 |
| player_glicko_rw_tier_revert | tier1 | 14067 | 0.588677 | 0.202932 | 0.681702 | 0.012028 |
| player_glicko_rw_tier_revert | tier2 | 4028 | 0.604114 | 0.209035 | 0.663357 | 0.024732 |
| player_glicko_rw_tier_revert | tier3 | 20036 | 0.623967 | 0.217558 | 0.648233 | 0.010188 |
| player_glicko_rw_tier_revert | unknown | 7 | 0.621019 | 0.214689 | 0.714286 | 0.298605 |
| player_glicko_rw_tier_revert | international=1 | 14341 | 0.589208 | 0.203125 | 0.681264 | 0.012184 |
| player_glicko_rw_tier_revert | international=0 | 23797 | 0.620692 | 0.216166 | 0.650691 | 0.011300 |

player_glicko_rw_tier_revert − coin (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 38138 | 0.608853 | 0.693147 | -0.084294 | [-0.088454, -0.080423] | yes |

player_glicko − team_elo (paired log loss):

| Section | Rows | player_glicko log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 38138 | 0.621611 | 0.650054 | -0.028443 | [-0.030994, -0.025778] | yes |

player_glicko_rookie_weights − team_elo (paired log loss):

| Section | Rows | player_glicko_rookie_weights log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 38138 | 0.609371 | 0.650054 | -0.040683 | [-0.043688, -0.037453] | yes |

player_glicko_rw_tier_revert − team_elo (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 38138 | 0.608853 | 0.650054 | -0.041201 | [-0.044095, -0.038163] | yes |

player_glicko_rookie_weights − player_glicko (paired log loss):

| Section | Rows | player_glicko_rookie_weights log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 38138 | 0.609371 | 0.621611 | -0.012240 | [-0.013947, -0.010575] | yes |
| tier1 | 14067 | 0.588778 | 0.602339 | -0.013561 | [-0.016103, -0.010897] | yes |
| tier2 | 4028 | 0.604510 | 0.615472 | -0.010962 | [-0.015108, -0.006612] | yes |
| tier3 | 20036 | 0.624802 | 0.636334 | -0.011532 | [-0.014097, -0.009020] | yes |
| unknown | 7 | 0.619052 | 0.740453 | -0.121400 | [-0.245811, 0.002198] | no |
| international=1 | 14341 | 0.589231 | 0.602825 | -0.013594 | [-0.016158, -0.010850] | yes |
| international=0 | 23797 | 0.621507 | 0.632932 | -0.011425 | [-0.013571, -0.009213] | yes |

player_glicko_rw_tier_revert − player_glicko (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 38138 | 0.608853 | 0.621611 | -0.012758 | [-0.014367, -0.011159] | yes |
| tier1 | 14067 | 0.588677 | 0.602339 | -0.013662 | [-0.016084, -0.011216] | yes |
| tier2 | 4028 | 0.604114 | 0.615472 | -0.011357 | [-0.015372, -0.007033] | yes |
| tier3 | 20036 | 0.623967 | 0.636334 | -0.012367 | [-0.014862, -0.009943] | yes |
| unknown | 7 | 0.621019 | 0.740453 | -0.119433 | [-0.245580, 0.006019] | no |
| international=1 | 14341 | 0.589208 | 0.602825 | -0.013617 | [-0.016035, -0.011148] | yes |
| international=0 | 23797 | 0.620692 | 0.632932 | -0.012240 | [-0.014310, -0.010112] | yes |

### Series

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| coin | all | 12117 | 0.693147 | 0.250000 | 0.500000 | 0.066724 |
| coin | tier1 | 4843 | 0.693147 | 0.250000 | 0.500000 | 0.086413 |
| coin | tier2 | 1352 | 0.693147 | 0.250000 | 0.500000 | 0.079882 |
| coin | tier3 | 5921 | 0.693147 | 0.250000 | 0.500000 | 0.047712 |
| coin | unknown | 1 | 0.693147 | 0.250000 | 0.500000 | 0.500000 |
| coin | international=1 | 4917 | 0.693147 | 0.250000 | 0.500000 | 0.085520 |
| coin | international=0 | 7200 | 0.693147 | 0.250000 | 0.500000 | 0.053889 |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko | all | 12117 | 0.599064 | 0.207265 | 0.666502 | 0.027834 |
| player_glicko | tier1 | 4843 | 0.565549 | 0.192839 | 0.707206 | 0.036232 |
| player_glicko | tier2 | 1352 | 0.576021 | 0.197879 | 0.680473 | 0.038100 |
| player_glicko | tier3 | 5921 | 0.631703 | 0.221191 | 0.630130 | 0.028471 |
| player_glicko | unknown | 1 | 0.816057 | 0.311173 | 0.000000 | 0.557828 |
| player_glicko | international=1 | 4917 | 0.566819 | 0.193401 | 0.706223 | 0.035963 |
| player_glicko | international=0 | 7200 | 0.621085 | 0.216734 | 0.639375 | 0.028234 |

player_glicko − coin (paired log loss):

| Section | Rows | player_glicko log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 12117 | 0.599064 | 0.693147 | -0.094083 | [-0.100287, -0.087640] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko_rookie_weights | all | 12117 | 0.570966 | 0.195001 | 0.700215 | 0.019481 |
| player_glicko_rookie_weights | tier1 | 4843 | 0.538846 | 0.181794 | 0.729094 | 0.019704 |
| player_glicko_rookie_weights | tier2 | 1352 | 0.549990 | 0.187627 | 0.696746 | 0.034638 |
| player_glicko_rookie_weights | tier3 | 5921 | 0.601985 | 0.207467 | 0.677504 | 0.023512 |
| player_glicko_rookie_weights | unknown | 1 | 0.830546 | 0.318309 | 0.000000 | 0.564189 |
| player_glicko_rookie_weights | international=1 | 4917 | 0.541077 | 0.182655 | 0.727578 | 0.019187 |
| player_glicko_rookie_weights | international=0 | 7200 | 0.591378 | 0.203433 | 0.681528 | 0.021249 |

player_glicko_rookie_weights − coin (paired log loss):

| Section | Rows | player_glicko_rookie_weights log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 12117 | 0.570966 | 0.693147 | -0.122181 | [-0.129668, -0.114469] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko_rw_tier_revert | all | 12117 | 0.570665 | 0.194935 | 0.699472 | 0.020111 |
| player_glicko_rw_tier_revert | tier1 | 4843 | 0.537923 | 0.181527 | 0.726203 | 0.017243 |
| player_glicko_rw_tier_revert | tier2 | 1352 | 0.551047 | 0.188068 | 0.700444 | 0.036818 |
| player_glicko_rw_tier_revert | tier3 | 5921 | 0.601878 | 0.207447 | 0.677504 | 0.022453 |
| player_glicko_rw_tier_revert | unknown | 1 | 0.857032 | 0.331293 | 0.000000 | 0.575580 |
| player_glicko_rw_tier_revert | international=1 | 4917 | 0.540281 | 0.182455 | 0.724527 | 0.016488 |
| player_glicko_rw_tier_revert | international=0 | 7200 | 0.591415 | 0.203458 | 0.682361 | 0.022586 |

player_glicko_rw_tier_revert − coin (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 12117 | 0.570665 | 0.693147 | -0.122482 | [-0.129703, -0.115106] | yes |

player_glicko − team_elo (paired log loss):

| Section | Rows | player_glicko log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 12117 | 0.599064 | 0.638841 | -0.039777 | [-0.044407, -0.034826] | yes |

player_glicko_rookie_weights − team_elo (paired log loss):

| Section | Rows | player_glicko_rookie_weights log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 12117 | 0.570966 | 0.638841 | -0.067875 | [-0.074115, -0.061283] | yes |

player_glicko_rw_tier_revert − team_elo (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 12117 | 0.570665 | 0.638841 | -0.068176 | [-0.074181, -0.061804] | yes |

player_glicko_rookie_weights − player_glicko (paired log loss):

| Section | Rows | player_glicko_rookie_weights log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 12117 | 0.570966 | 0.599064 | -0.028098 | [-0.031881, -0.024272] | yes |
| tier1 | 4843 | 0.538846 | 0.565549 | -0.026703 | [-0.033324, -0.020011] | yes |
| tier2 | 1352 | 0.549990 | 0.576021 | -0.026031 | [-0.033980, -0.018056] | yes |
| tier3 | 5921 | 0.601985 | 0.631703 | -0.029718 | [-0.035281, -0.024122] | yes |
| unknown | 1 | 0.830546 | 0.816057 | 0.014489 | [0.014489, 0.014489] | yes |
| international=1 | 4917 | 0.541077 | 0.566819 | -0.025743 | [-0.032364, -0.019207] | yes |
| international=0 | 7200 | 0.591378 | 0.621085 | -0.029707 | [-0.034383, -0.024974] | yes |

player_glicko_rw_tier_revert − player_glicko (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 12117 | 0.570665 | 0.599064 | -0.028399 | [-0.032099, -0.024690] | yes |
| tier1 | 4843 | 0.537923 | 0.565549 | -0.027626 | [-0.033845, -0.021294] | yes |
| tier2 | 1352 | 0.551047 | 0.576021 | -0.024974 | [-0.032562, -0.016953] | yes |
| tier3 | 5921 | 0.601878 | 0.631703 | -0.029825 | [-0.035373, -0.024240] | yes |
| unknown | 1 | 0.857032 | 0.816057 | 0.040975 | [0.040975, 0.040975] | yes |
| international=1 | 4917 | 0.540281 | 0.566819 | -0.026538 | [-0.032898, -0.020373] | yes |
| international=0 | 7200 | 0.591415 | 0.621085 | -0.029670 | [-0.034166, -0.024936] | yes |

## Stage 2 — validation (outcomes)

### Leaderboard (frozen stage-1 parameters)

| Model | Best params | Game log loss | Series log loss | Rows |
|---|---|---:|---:|---:|
| player_glicko_rookie_weights+form | {"k": 24, "new_player": "fixed", "online_k": 0.75, "rd_info": 0.0625, "rd_new": 280, "rookie_maps": 800, "rookie_penalty": 600, "tier3_k": 0.75} | 0.597809 | 0.562929 | 9328 |
| player_glicko_rw_tier_revert+form | {"inactive_half_life": 0, "k": 24, "new_player": "fixed", "online_k": 0.75, "rd_info": 0.0625, "rd_new": 280, "revert_target": "tier", "rookie_maps": 800, "rookie_penalty": 600, "season_month": 10, "season_revert": 0.1, "tier3_k": 0.75} | 0.597944 | 0.563975 | 9328 |
| player_glicko_rookie_weights+regional | {"k": 24, "new_player": "fixed", "online_k": 0.75, "rd_info": 0.0625, "rd_new": 280, "rookie_maps": 800, "rookie_penalty": 600, "tier3_k": 0.75} | 0.599045 | 0.563269 | 9328 |
| player_glicko_rw_tier_revert+regional | {"inactive_half_life": 0, "k": 24, "new_player": "fixed", "online_k": 0.75, "rd_info": 0.0625, "rd_new": 280, "revert_target": "tier", "rookie_maps": 800, "rookie_penalty": 600, "season_month": 10, "season_revert": 0.1, "tier3_k": 0.75} | 0.599424 | 0.564043 | 9328 |
| player_glicko_rookie_weights+calibration | {"k": 24, "new_player": "fixed", "online_k": 0.75, "rd_info": 0.0625, "rd_new": 280, "rookie_maps": 800, "rookie_penalty": 600, "tier3_k": 0.75} | 0.599657 | 0.564054 | 9328 |
| player_glicko_rw_tier_revert+calibration | {"inactive_half_life": 0, "k": 24, "new_player": "fixed", "online_k": 0.75, "rd_info": 0.0625, "rd_new": 280, "revert_target": "tier", "rookie_maps": 800, "rookie_penalty": 600, "season_month": 10, "season_revert": 0.1, "tier3_k": 0.75} | 0.599751 | 0.564667 | 9328 |
| player_glicko_rookie_weights | {"k": 24, "new_player": "fixed", "online_k": 0.75, "rd_info": 0.0625, "rd_new": 280, "rookie_maps": 800, "rookie_penalty": 600, "tier3_k": 0.75} | 0.599786 | 0.564266 | 9328 |
| player_glicko_rookie_weights+none | {"k": 24, "new_player": "fixed", "online_k": 0.75, "rd_info": 0.0625, "rd_new": 280, "rookie_maps": 800, "rookie_penalty": 600, "tier3_k": 0.75} | 0.599786 | 0.564266 | 9328 |
| player_glicko_rw_tier_revert | {"inactive_half_life": 0, "k": 24, "new_player": "fixed", "online_k": 0.75, "rd_info": 0.0625, "rd_new": 280, "revert_target": "tier", "rookie_maps": 800, "rookie_penalty": 600, "season_month": 10, "season_revert": 0.1, "tier3_k": 0.75} | 0.600167 | 0.565121 | 9328 |
| player_glicko_rw_tier_revert+none | {"inactive_half_life": 0, "k": 24, "new_player": "fixed", "online_k": 0.75, "rd_info": 0.0625, "rd_new": 280, "revert_target": "tier", "rookie_maps": 800, "rookie_penalty": 600, "season_month": 10, "season_revert": 0.1, "tier3_k": 0.75} | 0.600167 | 0.565121 | 9328 |
| player_glicko+form | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 280} | 0.609787 | 0.584302 | 9328 |
| player_glicko+regional | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 280} | 0.609909 | 0.583839 | 9328 |
| player_glicko+calibration | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 280} | 0.610394 | 0.583996 | 9328 |
| player_glicko | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 280} | 0.610785 | 0.584862 | 9328 |
| player_glicko+none | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 280} | 0.610785 | 0.584862 | 9328 |

### Games

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| coin | all | 9328 | 0.693147 | 0.250000 | 0.500000 | 0.051565 |
| coin | tier1 | 3827 | 0.693147 | 0.250000 | 0.500000 | 0.079828 |
| coin | tier2 | 571 | 0.693147 | 0.250000 | 0.500000 | 0.067426 |
| coin | tier3 | 4930 | 0.693147 | 0.250000 | 0.500000 | 0.027789 |
| coin | unknown | 0 | — | — | — | — |
| coin | international=1 | 3843 | 0.693147 | 0.250000 | 0.500000 | 0.080276 |
| coin | international=0 | 5485 | 0.693147 | 0.250000 | 0.500000 | 0.031449 |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko | all | 9328 | 0.610785 | 0.212214 | 0.651801 | 0.015998 |
| player_glicko | tier1 | 3827 | 0.589637 | 0.203331 | 0.668801 | 0.021120 |
| player_glicko | tier2 | 571 | 0.629961 | 0.220270 | 0.640981 | 0.037178 |
| player_glicko | tier3 | 4930 | 0.624981 | 0.218176 | 0.639858 | 0.017594 |
| player_glicko | unknown | 0 | — | — | — | — |
| player_glicko | international=1 | 3843 | 0.589611 | 0.203320 | 0.668618 | 0.021268 |
| player_glicko | international=0 | 5485 | 0.625620 | 0.218445 | 0.640018 | 0.017840 |

player_glicko − coin (paired log loss):

| Section | Rows | player_glicko log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.610785 | 0.693147 | -0.082362 | [-0.090678, -0.074629] | yes |
| tier1 | 3827 | 0.589637 | 0.693147 | -0.103511 | [-0.117210, -0.090559] | yes |
| tier2 | 571 | 0.629961 | 0.693147 | -0.063186 | [-0.096632, -0.028646] | yes |
| tier3 | 4930 | 0.624981 | 0.693147 | -0.068166 | [-0.079164, -0.057944] | yes |
| international=1 | 3843 | 0.589611 | 0.693147 | -0.103536 | [-0.116688, -0.091034] | yes |
| international=0 | 5485 | 0.625620 | 0.693147 | -0.067527 | [-0.076942, -0.057721] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko_rookie_weights | all | 9328 | 0.599786 | 0.207608 | 0.660806 | 0.014649 |
| player_glicko_rookie_weights | tier1 | 3827 | 0.573847 | 0.197368 | 0.683433 | 0.016234 |
| player_glicko_rookie_weights | tier2 | 571 | 0.622693 | 0.217160 | 0.639229 | 0.034341 |
| player_glicko_rookie_weights | tier3 | 4930 | 0.617269 | 0.214450 | 0.645740 | 0.017240 |
| player_glicko_rookie_weights | unknown | 0 | — | — | — | — |
| player_glicko_rookie_weights | international=1 | 3843 | 0.573518 | 0.197228 | 0.683711 | 0.016181 |
| player_glicko_rookie_weights | international=0 | 5485 | 0.618191 | 0.214880 | 0.644758 | 0.015439 |

player_glicko_rookie_weights − coin (paired log loss):

| Section | Rows | player_glicko_rookie_weights log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.599786 | 0.693147 | -0.093361 | [-0.101807, -0.085331] | yes |
| tier1 | 3827 | 0.573847 | 0.693147 | -0.119300 | [-0.133802, -0.105339] | yes |
| tier2 | 571 | 0.622693 | 0.693147 | -0.070455 | [-0.104241, -0.036175] | yes |
| tier3 | 4930 | 0.617269 | 0.693147 | -0.075879 | [-0.087053, -0.065049] | yes |
| international=1 | 3843 | 0.573518 | 0.693147 | -0.119629 | [-0.133757, -0.105956] | yes |
| international=0 | 5485 | 0.618191 | 0.693147 | -0.074956 | [-0.085101, -0.064523] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko_rw_tier_revert | all | 9328 | 0.600167 | 0.207708 | 0.661664 | 0.015305 |
| player_glicko_rw_tier_revert | tier1 | 3827 | 0.575048 | 0.197725 | 0.681866 | 0.021648 |
| player_glicko_rw_tier_revert | tier2 | 571 | 0.622421 | 0.217062 | 0.637478 | 0.040632 |
| player_glicko_rw_tier_revert | tier3 | 4930 | 0.617088 | 0.214374 | 0.648783 | 0.019403 |
| player_glicko_rw_tier_revert | unknown | 0 | — | — | — | — |
| player_glicko_rw_tier_revert | international=1 | 3843 | 0.574763 | 0.197604 | 0.682149 | 0.021391 |
| player_glicko_rw_tier_revert | international=0 | 5485 | 0.617965 | 0.214787 | 0.647311 | 0.017770 |

player_glicko_rw_tier_revert − coin (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.600167 | 0.693147 | -0.092981 | [-0.100867, -0.085338] | yes |
| tier1 | 3827 | 0.575048 | 0.693147 | -0.118099 | [-0.131399, -0.105061] | yes |
| tier2 | 571 | 0.622421 | 0.693147 | -0.070726 | [-0.101996, -0.039276] | yes |
| tier3 | 4930 | 0.617088 | 0.693147 | -0.076060 | [-0.086637, -0.066072] | yes |
| international=1 | 3843 | 0.574763 | 0.693147 | -0.118384 | [-0.131689, -0.105571] | yes |
| international=0 | 5485 | 0.617965 | 0.693147 | -0.075182 | [-0.084642, -0.065366] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko+none | all | 9328 | 0.610785 | 0.212214 | 0.651801 | 0.015998 |
| player_glicko+none | tier1 | 3827 | 0.589637 | 0.203331 | 0.668801 | 0.021120 |
| player_glicko+none | tier2 | 571 | 0.629961 | 0.220270 | 0.640981 | 0.037178 |
| player_glicko+none | tier3 | 4930 | 0.624981 | 0.218176 | 0.639858 | 0.017594 |
| player_glicko+none | unknown | 0 | — | — | — | — |
| player_glicko+none | international=1 | 3843 | 0.589611 | 0.203320 | 0.668618 | 0.021268 |
| player_glicko+none | international=0 | 5485 | 0.625620 | 0.218445 | 0.640018 | 0.017840 |

player_glicko+none − coin (paired log loss):

| Section | Rows | player_glicko+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.610785 | 0.693147 | -0.082362 | [-0.090678, -0.074629] | yes |
| tier1 | 3827 | 0.589637 | 0.693147 | -0.103511 | [-0.117210, -0.090559] | yes |
| tier2 | 571 | 0.629961 | 0.693147 | -0.063186 | [-0.096632, -0.028646] | yes |
| tier3 | 4930 | 0.624981 | 0.693147 | -0.068166 | [-0.079164, -0.057944] | yes |
| international=1 | 3843 | 0.589611 | 0.693147 | -0.103536 | [-0.116688, -0.091034] | yes |
| international=0 | 5485 | 0.625620 | 0.693147 | -0.067527 | [-0.076942, -0.057721] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko+regional | all | 9328 | 0.609909 | 0.211867 | 0.651265 | 0.017298 |
| player_glicko+regional | tier1 | 3827 | 0.589075 | 0.203099 | 0.670107 | 0.018363 |
| player_glicko+regional | tier2 | 571 | 0.628180 | 0.219419 | 0.635727 | 0.042781 |
| player_glicko+regional | tier3 | 4930 | 0.623966 | 0.217798 | 0.638438 | 0.018881 |
| player_glicko+regional | unknown | 0 | — | — | — | — |
| player_glicko+regional | international=1 | 3843 | 0.588996 | 0.203064 | 0.669919 | 0.018836 |
| player_glicko+regional | international=0 | 5485 | 0.624562 | 0.218034 | 0.638195 | 0.019571 |

player_glicko+regional − coin (paired log loss):

| Section | Rows | player_glicko+regional log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.609909 | 0.693147 | -0.083238 | [-0.091361, -0.075710] | yes |
| tier1 | 3827 | 0.589075 | 0.693147 | -0.104072 | [-0.117878, -0.091386] | yes |
| tier2 | 571 | 0.628180 | 0.693147 | -0.064967 | [-0.097808, -0.030359] | yes |
| tier3 | 4930 | 0.623966 | 0.693147 | -0.069181 | [-0.080060, -0.059265] | yes |
| international=1 | 3843 | 0.588996 | 0.693147 | -0.104151 | [-0.117137, -0.091827] | yes |
| international=0 | 5485 | 0.624562 | 0.693147 | -0.068585 | [-0.077921, -0.058852] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko+calibration | all | 9328 | 0.610394 | 0.212083 | 0.651801 | 0.016938 |
| player_glicko+calibration | tier1 | 3827 | 0.588886 | 0.203148 | 0.668801 | 0.017361 |
| player_glicko+calibration | tier2 | 571 | 0.628291 | 0.219496 | 0.640981 | 0.044378 |
| player_glicko+calibration | tier3 | 4930 | 0.625016 | 0.218161 | 0.639858 | 0.020198 |
| player_glicko+calibration | unknown | 0 | — | — | — | — |
| player_glicko+calibration | international=1 | 3843 | 0.588863 | 0.203137 | 0.668618 | 0.017201 |
| player_glicko+calibration | international=0 | 5485 | 0.625479 | 0.218352 | 0.640018 | 0.019773 |

player_glicko+calibration − coin (paired log loss):

| Section | Rows | player_glicko+calibration log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.610394 | 0.693147 | -0.082754 | [-0.090665, -0.075119] | yes |
| tier1 | 3827 | 0.588886 | 0.693147 | -0.104261 | [-0.118612, -0.091034] | yes |
| tier2 | 571 | 0.628291 | 0.693147 | -0.064856 | [-0.097195, -0.031232] | yes |
| tier3 | 4930 | 0.625016 | 0.693147 | -0.068131 | [-0.078302, -0.058923] | yes |
| international=1 | 3843 | 0.588863 | 0.693147 | -0.104285 | [-0.117779, -0.091117] | yes |
| international=0 | 5485 | 0.625479 | 0.693147 | -0.067668 | [-0.076488, -0.058579] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko+form | all | 9328 | 0.609787 | 0.211840 | 0.654267 | 0.015182 |
| player_glicko+form | tier1 | 3827 | 0.588370 | 0.202937 | 0.672981 | 0.018022 |
| player_glicko+form | tier2 | 571 | 0.630918 | 0.220683 | 0.635727 | 0.033781 |
| player_glicko+form | tier3 | 4930 | 0.623964 | 0.217728 | 0.641886 | 0.020177 |
| player_glicko+form | unknown | 0 | — | — | — | — |
| player_glicko+form | international=1 | 3843 | 0.588344 | 0.202931 | 0.672782 | 0.018228 |
| player_glicko+form | international=0 | 5485 | 0.624810 | 0.218083 | 0.641294 | 0.020536 |

player_glicko+form − coin (paired log loss):

| Section | Rows | player_glicko+form log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.609787 | 0.693147 | -0.083360 | [-0.091989, -0.075294] | yes |
| tier1 | 3827 | 0.588370 | 0.693147 | -0.104777 | [-0.118905, -0.091621] | yes |
| tier2 | 571 | 0.630918 | 0.693147 | -0.062229 | [-0.096305, -0.026760] | yes |
| tier3 | 4930 | 0.623964 | 0.693147 | -0.069183 | [-0.080905, -0.058156] | yes |
| international=1 | 3843 | 0.588344 | 0.693147 | -0.104803 | [-0.118426, -0.092083] | yes |
| international=0 | 5485 | 0.624810 | 0.693147 | -0.068337 | [-0.078468, -0.057946] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko_rookie_weights+none | all | 9328 | 0.599786 | 0.207608 | 0.660806 | 0.014649 |
| player_glicko_rookie_weights+none | tier1 | 3827 | 0.573847 | 0.197368 | 0.683433 | 0.016234 |
| player_glicko_rookie_weights+none | tier2 | 571 | 0.622693 | 0.217160 | 0.639229 | 0.034341 |
| player_glicko_rookie_weights+none | tier3 | 4930 | 0.617269 | 0.214450 | 0.645740 | 0.017240 |
| player_glicko_rookie_weights+none | unknown | 0 | — | — | — | — |
| player_glicko_rookie_weights+none | international=1 | 3843 | 0.573518 | 0.197228 | 0.683711 | 0.016181 |
| player_glicko_rookie_weights+none | international=0 | 5485 | 0.618191 | 0.214880 | 0.644758 | 0.015439 |

player_glicko_rookie_weights+none − coin (paired log loss):

| Section | Rows | player_glicko_rookie_weights+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.599786 | 0.693147 | -0.093361 | [-0.101807, -0.085331] | yes |
| tier1 | 3827 | 0.573847 | 0.693147 | -0.119300 | [-0.133802, -0.105339] | yes |
| tier2 | 571 | 0.622693 | 0.693147 | -0.070455 | [-0.104241, -0.036175] | yes |
| tier3 | 4930 | 0.617269 | 0.693147 | -0.075879 | [-0.087053, -0.065049] | yes |
| international=1 | 3843 | 0.573518 | 0.693147 | -0.119629 | [-0.133757, -0.105956] | yes |
| international=0 | 5485 | 0.618191 | 0.693147 | -0.074956 | [-0.085101, -0.064523] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko_rookie_weights+regional | all | 9328 | 0.599045 | 0.207320 | 0.662629 | 0.012209 |
| player_glicko_rookie_weights+regional | tier1 | 3827 | 0.573399 | 0.197174 | 0.683956 | 0.013421 |
| player_glicko_rookie_weights+regional | tier2 | 571 | 0.621881 | 0.216763 | 0.642732 | 0.036898 |
| player_glicko_rookie_weights+regional | tier3 | 4930 | 0.616308 | 0.214103 | 0.648377 | 0.017243 |
| player_glicko_rookie_weights+regional | unknown | 0 | — | — | — | — |
| player_glicko_rookie_weights+regional | international=1 | 3843 | 0.573016 | 0.197010 | 0.684491 | 0.013451 |
| player_glicko_rookie_weights+regional | international=0 | 5485 | 0.617281 | 0.214544 | 0.647311 | 0.015704 |

player_glicko_rookie_weights+regional − coin (paired log loss):

| Section | Rows | player_glicko_rookie_weights+regional log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.599045 | 0.693147 | -0.094102 | [-0.102475, -0.086057] | yes |
| tier1 | 3827 | 0.573399 | 0.693147 | -0.119748 | [-0.134119, -0.105969] | yes |
| tier2 | 571 | 0.621881 | 0.693147 | -0.071266 | [-0.104635, -0.037351] | yes |
| tier3 | 4930 | 0.616308 | 0.693147 | -0.076839 | [-0.087710, -0.066334] | yes |
| international=1 | 3843 | 0.573016 | 0.693147 | -0.120131 | [-0.134329, -0.106739] | yes |
| international=0 | 5485 | 0.617281 | 0.693147 | -0.075866 | [-0.085710, -0.065608] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko_rookie_weights+calibration | all | 9328 | 0.599657 | 0.207558 | 0.660806 | 0.014766 |
| player_glicko_rookie_weights+calibration | tier1 | 3827 | 0.573592 | 0.197279 | 0.683433 | 0.015029 |
| player_glicko_rookie_weights+calibration | tier2 | 571 | 0.621615 | 0.216621 | 0.639229 | 0.033129 |
| player_glicko_rookie_weights+calibration | tier3 | 4930 | 0.617346 | 0.214487 | 0.645740 | 0.018778 |
| player_glicko_rookie_weights+calibration | unknown | 0 | — | — | — | — |
| player_glicko_rookie_weights+calibration | international=1 | 3843 | 0.573263 | 0.197140 | 0.683711 | 0.015217 |
| player_glicko_rookie_weights+calibration | international=0 | 5485 | 0.618149 | 0.214857 | 0.644758 | 0.016939 |

player_glicko_rookie_weights+calibration − coin (paired log loss):

| Section | Rows | player_glicko_rookie_weights+calibration log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.599657 | 0.693147 | -0.093490 | [-0.101631, -0.085564] | yes |
| tier1 | 3827 | 0.573592 | 0.693147 | -0.119555 | [-0.133637, -0.105872] | yes |
| tier2 | 571 | 0.621615 | 0.693147 | -0.071532 | [-0.104469, -0.037917] | yes |
| tier3 | 4930 | 0.617346 | 0.693147 | -0.075801 | [-0.086360, -0.065536] | yes |
| international=1 | 3843 | 0.573263 | 0.693147 | -0.119884 | [-0.133843, -0.106515] | yes |
| international=0 | 5485 | 0.618149 | 0.693147 | -0.074998 | [-0.084669, -0.065082] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko_rookie_weights+form | all | 9328 | 0.597809 | 0.206861 | 0.664237 | 0.013279 |
| player_glicko_rookie_weights+form | tier1 | 3827 | 0.572764 | 0.197055 | 0.685263 | 0.016012 |
| player_glicko_rookie_weights+form | tier2 | 571 | 0.621263 | 0.216592 | 0.646235 | 0.051130 |
| player_glicko_rookie_weights+form | tier3 | 4930 | 0.614535 | 0.213345 | 0.650000 | 0.015856 |
| player_glicko_rookie_weights+form | unknown | 0 | — | — | — | — |
| player_glicko_rookie_weights+form | international=1 | 3843 | 0.572490 | 0.196943 | 0.685272 | 0.015704 |
| player_glicko_rookie_weights+form | international=0 | 5485 | 0.615550 | 0.213809 | 0.649499 | 0.015644 |

player_glicko_rookie_weights+form − coin (paired log loss):

| Section | Rows | player_glicko_rookie_weights+form log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.597809 | 0.693147 | -0.095338 | [-0.104023, -0.086854] | yes |
| tier1 | 3827 | 0.572764 | 0.693147 | -0.120383 | [-0.135246, -0.105953] | yes |
| tier2 | 571 | 0.621263 | 0.693147 | -0.071884 | [-0.106402, -0.037156] | yes |
| tier3 | 4930 | 0.614535 | 0.693147 | -0.078612 | [-0.090607, -0.067599] | yes |
| international=1 | 3843 | 0.572490 | 0.693147 | -0.120658 | [-0.135313, -0.106593] | yes |
| international=0 | 5485 | 0.615550 | 0.693147 | -0.077598 | [-0.087999, -0.066712] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko_rw_tier_revert+none | all | 9328 | 0.600167 | 0.207708 | 0.661664 | 0.015305 |
| player_glicko_rw_tier_revert+none | tier1 | 3827 | 0.575048 | 0.197725 | 0.681866 | 0.021648 |
| player_glicko_rw_tier_revert+none | tier2 | 571 | 0.622421 | 0.217062 | 0.637478 | 0.040632 |
| player_glicko_rw_tier_revert+none | tier3 | 4930 | 0.617088 | 0.214374 | 0.648783 | 0.019403 |
| player_glicko_rw_tier_revert+none | unknown | 0 | — | — | — | — |
| player_glicko_rw_tier_revert+none | international=1 | 3843 | 0.574763 | 0.197604 | 0.682149 | 0.021391 |
| player_glicko_rw_tier_revert+none | international=0 | 5485 | 0.617965 | 0.214787 | 0.647311 | 0.017770 |

player_glicko_rw_tier_revert+none − coin (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.600167 | 0.693147 | -0.092981 | [-0.100867, -0.085338] | yes |
| tier1 | 3827 | 0.575048 | 0.693147 | -0.118099 | [-0.131399, -0.105061] | yes |
| tier2 | 571 | 0.622421 | 0.693147 | -0.070726 | [-0.101996, -0.039276] | yes |
| tier3 | 4930 | 0.617088 | 0.693147 | -0.076060 | [-0.086637, -0.066072] | yes |
| international=1 | 3843 | 0.574763 | 0.693147 | -0.118384 | [-0.131689, -0.105571] | yes |
| international=0 | 5485 | 0.617965 | 0.693147 | -0.075182 | [-0.084642, -0.065366] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko_rw_tier_revert+regional | all | 9328 | 0.599424 | 0.207419 | 0.663379 | 0.015470 |
| player_glicko_rw_tier_revert+regional | tier1 | 3827 | 0.574595 | 0.197553 | 0.682650 | 0.019362 |
| player_glicko_rw_tier_revert+regional | tier2 | 571 | 0.621240 | 0.216590 | 0.639229 | 0.039914 |
| player_glicko_rw_tier_revert+regional | tier3 | 4930 | 0.616171 | 0.214015 | 0.651217 | 0.019916 |
| player_glicko_rw_tier_revert+regional | unknown | 0 | — | — | — | — |
| player_glicko_rw_tier_revert+regional | international=1 | 3843 | 0.574258 | 0.197408 | 0.682930 | 0.019535 |
| player_glicko_rw_tier_revert+regional | international=0 | 5485 | 0.617056 | 0.214432 | 0.649681 | 0.018407 |

player_glicko_rw_tier_revert+regional − coin (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+regional log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.599424 | 0.693147 | -0.093723 | [-0.101630, -0.086234] | yes |
| tier1 | 3827 | 0.574595 | 0.693147 | -0.118552 | [-0.132120, -0.105583] | yes |
| tier2 | 571 | 0.621240 | 0.693147 | -0.071907 | [-0.103162, -0.040232] | yes |
| tier3 | 4930 | 0.616171 | 0.693147 | -0.076976 | [-0.087305, -0.067120] | yes |
| international=1 | 3843 | 0.574258 | 0.693147 | -0.118890 | [-0.132421, -0.106026] | yes |
| international=0 | 5485 | 0.617056 | 0.693147 | -0.076091 | [-0.085460, -0.066322] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko_rw_tier_revert+calibration | all | 9328 | 0.599751 | 0.207555 | 0.661664 | 0.013267 |
| player_glicko_rw_tier_revert+calibration | tier1 | 3827 | 0.574177 | 0.197470 | 0.681866 | 0.014153 |
| player_glicko_rw_tier_revert+calibration | tier2 | 571 | 0.621918 | 0.216759 | 0.637478 | 0.039431 |
| player_glicko_rw_tier_revert+calibration | tier3 | 4930 | 0.617035 | 0.214317 | 0.648783 | 0.020226 |
| player_glicko_rw_tier_revert+calibration | unknown | 0 | — | — | — | — |
| player_glicko_rw_tier_revert+calibration | international=1 | 3843 | 0.573873 | 0.197343 | 0.682149 | 0.014153 |
| player_glicko_rw_tier_revert+calibration | international=0 | 5485 | 0.617881 | 0.214709 | 0.647311 | 0.017832 |

player_glicko_rw_tier_revert+calibration − coin (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+calibration log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.599751 | 0.693147 | -0.093397 | [-0.101402, -0.085506] | yes |
| tier1 | 3827 | 0.574177 | 0.693147 | -0.118970 | [-0.132872, -0.105294] | yes |
| tier2 | 571 | 0.621918 | 0.693147 | -0.071229 | [-0.103878, -0.038191] | yes |
| tier3 | 4930 | 0.617035 | 0.693147 | -0.076112 | [-0.086757, -0.065975] | yes |
| international=1 | 3843 | 0.573873 | 0.693147 | -0.119274 | [-0.133289, -0.105734] | yes |
| international=0 | 5485 | 0.617881 | 0.693147 | -0.075266 | [-0.084833, -0.065376] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko_rw_tier_revert+form | all | 9328 | 0.597944 | 0.206889 | 0.665845 | 0.013361 |
| player_glicko_rw_tier_revert+form | tier1 | 3827 | 0.573809 | 0.197381 | 0.683695 | 0.013786 |
| player_glicko_rw_tier_revert+form | tier2 | 571 | 0.620820 | 0.216425 | 0.644483 | 0.040784 |
| player_glicko_rw_tier_revert+form | tier3 | 4930 | 0.614030 | 0.213165 | 0.654462 | 0.016628 |
| player_glicko_rw_tier_revert+form | unknown | 0 | — | — | — | — |
| player_glicko_rw_tier_revert+form | international=1 | 3843 | 0.573584 | 0.197289 | 0.683711 | 0.014052 |
| player_glicko_rw_tier_revert+form | international=0 | 5485 | 0.615012 | 0.213615 | 0.653327 | 0.017062 |

player_glicko_rw_tier_revert+form − coin (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+form log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.597944 | 0.693147 | -0.095203 | [-0.103589, -0.087256] | yes |
| tier1 | 3827 | 0.573809 | 0.693147 | -0.119338 | [-0.133250, -0.105584] | yes |
| tier2 | 571 | 0.620820 | 0.693147 | -0.072327 | [-0.104304, -0.039730] | yes |
| tier3 | 4930 | 0.614030 | 0.693147 | -0.079118 | [-0.090306, -0.068527] | yes |
| international=1 | 3843 | 0.573584 | 0.693147 | -0.119564 | [-0.133452, -0.106298] | yes |
| international=0 | 5485 | 0.615012 | 0.693147 | -0.078136 | [-0.088167, -0.067819] | yes |

player_glicko − team_elo (paired log loss):

| Section | Rows | player_glicko log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.610785 | 0.646281 | -0.035496 | [-0.040569, -0.030402] | yes |

player_glicko_rookie_weights − team_elo (paired log loss):

| Section | Rows | player_glicko_rookie_weights log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.599786 | 0.646281 | -0.046495 | [-0.052660, -0.040411] | yes |

player_glicko_rw_tier_revert − team_elo (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.600167 | 0.646281 | -0.046114 | [-0.052027, -0.040414] | yes |

player_glicko+none − team_elo (paired log loss):

| Section | Rows | player_glicko+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.610785 | 0.646281 | -0.035496 | [-0.040569, -0.030402] | yes |

player_glicko+regional − team_elo (paired log loss):

| Section | Rows | player_glicko+regional log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.609909 | 0.646281 | -0.036372 | [-0.041407, -0.031406] | yes |

player_glicko+calibration − team_elo (paired log loss):

| Section | Rows | player_glicko+calibration log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.610394 | 0.646281 | -0.035887 | [-0.041024, -0.030609] | yes |

player_glicko+form − team_elo (paired log loss):

| Section | Rows | player_glicko+form log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.609787 | 0.646281 | -0.036494 | [-0.041798, -0.031062] | yes |

player_glicko_rookie_weights+none − team_elo (paired log loss):

| Section | Rows | player_glicko_rookie_weights+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.599786 | 0.646281 | -0.046495 | [-0.052660, -0.040411] | yes |

player_glicko_rookie_weights+regional − team_elo (paired log loss):

| Section | Rows | player_glicko_rookie_weights+regional log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.599045 | 0.646281 | -0.047236 | [-0.053211, -0.041277] | yes |

player_glicko_rookie_weights+calibration − team_elo (paired log loss):

| Section | Rows | player_glicko_rookie_weights+calibration log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.599657 | 0.646281 | -0.046624 | [-0.052805, -0.040701] | yes |

player_glicko_rookie_weights+form − team_elo (paired log loss):

| Section | Rows | player_glicko_rookie_weights+form log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.597809 | 0.646281 | -0.048471 | [-0.054706, -0.042223] | yes |

player_glicko_rw_tier_revert+none − team_elo (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.600167 | 0.646281 | -0.046114 | [-0.052027, -0.040414] | yes |

player_glicko_rw_tier_revert+regional − team_elo (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+regional log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.599424 | 0.646281 | -0.046857 | [-0.052691, -0.041188] | yes |

player_glicko_rw_tier_revert+calibration − team_elo (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+calibration log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.599751 | 0.646281 | -0.046530 | [-0.052631, -0.040661] | yes |

player_glicko_rw_tier_revert+form − team_elo (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+form log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.597944 | 0.646281 | -0.048337 | [-0.054231, -0.042407] | yes |

player_glicko_rookie_weights − player_glicko (paired log loss):

| Section | Rows | player_glicko_rookie_weights log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.599786 | 0.610785 | -0.010999 | [-0.014128, -0.008065] | yes |
| tier1 | 3827 | 0.573847 | 0.589637 | -0.015789 | [-0.020063, -0.011473] | yes |
| tier2 | 571 | 0.622693 | 0.629961 | -0.007269 | [-0.013643, 0.000115] | no |
| tier3 | 4930 | 0.617269 | 0.624981 | -0.007712 | [-0.012490, -0.002875] | yes |
| international=1 | 3843 | 0.573518 | 0.589611 | -0.016094 | [-0.020475, -0.011949] | yes |
| international=0 | 5485 | 0.618191 | 0.625620 | -0.007429 | [-0.011348, -0.003313] | yes |

player_glicko_rw_tier_revert − player_glicko (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.600167 | 0.610785 | -0.010618 | [-0.013610, -0.007786] | yes |
| tier1 | 3827 | 0.575048 | 0.589637 | -0.014588 | [-0.018750, -0.010584] | yes |
| tier2 | 571 | 0.622421 | 0.629961 | -0.007540 | [-0.014268, -0.000397] | yes |
| tier3 | 4930 | 0.617088 | 0.624981 | -0.007893 | [-0.012439, -0.003221] | yes |
| international=1 | 3843 | 0.574763 | 0.589611 | -0.014848 | [-0.019007, -0.010735] | yes |
| international=0 | 5485 | 0.617965 | 0.625620 | -0.007655 | [-0.011382, -0.003682] | yes |

player_glicko+none − player_glicko (paired log loss):

| Section | Rows | player_glicko+none log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.610785 | 0.610785 | 0.000000 | [0.000000, 0.000000] | no |
| tier1 | 3827 | 0.589637 | 0.589637 | 0.000000 | [0.000000, 0.000000] | no |
| tier2 | 571 | 0.629961 | 0.629961 | 0.000000 | [0.000000, 0.000000] | no |
| tier3 | 4930 | 0.624981 | 0.624981 | 0.000000 | [0.000000, 0.000000] | no |
| international=1 | 3843 | 0.589611 | 0.589611 | 0.000000 | [0.000000, 0.000000] | no |
| international=0 | 5485 | 0.625620 | 0.625620 | 0.000000 | [0.000000, 0.000000] | no |

player_glicko+regional − player_glicko (paired log loss):

| Section | Rows | player_glicko+regional log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.609909 | 0.610785 | -0.000876 | [-0.001644, -0.000125] | yes |
| tier1 | 3827 | 0.589075 | 0.589637 | -0.000562 | [-0.001705, 0.000531] | no |
| tier2 | 571 | 0.628180 | 0.629961 | -0.001781 | [-0.004014, 0.000175] | no |
| tier3 | 4930 | 0.623966 | 0.624981 | -0.001015 | [-0.002150, 0.000059] | no |
| international=1 | 3843 | 0.588996 | 0.589611 | -0.000615 | [-0.001779, 0.000467] | no |
| international=0 | 5485 | 0.624562 | 0.625620 | -0.001058 | [-0.002048, -0.000070] | yes |

player_glicko+calibration − player_glicko (paired log loss):

| Section | Rows | player_glicko+calibration log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.610394 | 0.610785 | -0.000391 | [-0.001238, 0.000503] | no |
| tier1 | 3827 | 0.588886 | 0.589637 | -0.000751 | [-0.002338, 0.000727] | no |
| tier2 | 571 | 0.628291 | 0.629961 | -0.001670 | [-0.004225, 0.000545] | no |
| tier3 | 4930 | 0.625016 | 0.624981 | 0.000036 | [-0.001010, 0.001117] | no |
| international=1 | 3843 | 0.588863 | 0.589611 | -0.000749 | [-0.002283, 0.000799] | no |
| international=0 | 5485 | 0.625479 | 0.625620 | -0.000141 | [-0.001106, 0.000818] | no |

player_glicko+form − player_glicko (paired log loss):

| Section | Rows | player_glicko+form log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.609787 | 0.610785 | -0.000998 | [-0.002020, 0.000003] | no |
| tier1 | 3827 | 0.588370 | 0.589637 | -0.001266 | [-0.002435, -0.000091] | yes |
| tier2 | 571 | 0.630918 | 0.629961 | 0.000957 | [-0.001116, 0.003098] | no |
| tier3 | 4930 | 0.623964 | 0.624981 | -0.001017 | [-0.002606, 0.000537] | no |
| international=1 | 3843 | 0.588344 | 0.589611 | -0.001267 | [-0.002471, -0.000112] | yes |
| international=0 | 5485 | 0.624810 | 0.625620 | -0.000810 | [-0.002242, 0.000759] | no |

player_glicko_rookie_weights+none − player_glicko (paired log loss):

| Section | Rows | player_glicko_rookie_weights+none log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.599786 | 0.610785 | -0.010999 | [-0.014128, -0.008065] | yes |
| tier1 | 3827 | 0.573847 | 0.589637 | -0.015789 | [-0.020063, -0.011473] | yes |
| tier2 | 571 | 0.622693 | 0.629961 | -0.007269 | [-0.013643, 0.000115] | no |
| tier3 | 4930 | 0.617269 | 0.624981 | -0.007712 | [-0.012490, -0.002875] | yes |
| international=1 | 3843 | 0.573518 | 0.589611 | -0.016094 | [-0.020475, -0.011949] | yes |
| international=0 | 5485 | 0.618191 | 0.625620 | -0.007429 | [-0.011348, -0.003313] | yes |

player_glicko_rookie_weights+regional − player_glicko (paired log loss):

| Section | Rows | player_glicko_rookie_weights+regional log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.599045 | 0.610785 | -0.011740 | [-0.014874, -0.008766] | yes |
| tier1 | 3827 | 0.573399 | 0.589637 | -0.016238 | [-0.020511, -0.011842] | yes |
| tier2 | 571 | 0.621881 | 0.629961 | -0.008080 | [-0.014964, -0.000493] | yes |
| tier3 | 4930 | 0.616308 | 0.624981 | -0.008673 | [-0.013563, -0.003887] | yes |
| international=1 | 3843 | 0.573016 | 0.589611 | -0.016595 | [-0.021140, -0.012202] | yes |
| international=0 | 5485 | 0.617281 | 0.625620 | -0.008339 | [-0.012282, -0.004260] | yes |

player_glicko_rookie_weights+calibration − player_glicko (paired log loss):

| Section | Rows | player_glicko_rookie_weights+calibration log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.599657 | 0.610785 | -0.011128 | [-0.014248, -0.008170] | yes |
| tier1 | 3827 | 0.573592 | 0.589637 | -0.016044 | [-0.020550, -0.011632] | yes |
| tier2 | 571 | 0.621615 | 0.629961 | -0.008346 | [-0.015241, -0.000863] | yes |
| tier3 | 4930 | 0.617346 | 0.624981 | -0.007634 | [-0.012309, -0.002913] | yes |
| international=1 | 3843 | 0.573263 | 0.589611 | -0.016348 | [-0.020890, -0.011987] | yes |
| international=0 | 5485 | 0.618149 | 0.625620 | -0.007471 | [-0.011342, -0.003436] | yes |

player_glicko_rookie_weights+form − player_glicko (paired log loss):

| Section | Rows | player_glicko_rookie_weights+form log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.597809 | 0.610785 | -0.012976 | [-0.015984, -0.009961] | yes |
| tier1 | 3827 | 0.572764 | 0.589637 | -0.016873 | [-0.021404, -0.012234] | yes |
| tier2 | 571 | 0.621263 | 0.629961 | -0.008698 | [-0.015308, -0.001234] | yes |
| tier3 | 4930 | 0.614535 | 0.624981 | -0.010446 | [-0.015310, -0.005837] | yes |
| international=1 | 3843 | 0.572490 | 0.589611 | -0.017122 | [-0.021725, -0.012474] | yes |
| international=0 | 5485 | 0.615550 | 0.625620 | -0.010070 | [-0.013929, -0.005960] | yes |

player_glicko_rw_tier_revert+none − player_glicko (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+none log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.600167 | 0.610785 | -0.010618 | [-0.013610, -0.007786] | yes |
| tier1 | 3827 | 0.575048 | 0.589637 | -0.014588 | [-0.018750, -0.010584] | yes |
| tier2 | 571 | 0.622421 | 0.629961 | -0.007540 | [-0.014268, -0.000397] | yes |
| tier3 | 4930 | 0.617088 | 0.624981 | -0.007893 | [-0.012439, -0.003221] | yes |
| international=1 | 3843 | 0.574763 | 0.589611 | -0.014848 | [-0.019007, -0.010735] | yes |
| international=0 | 5485 | 0.617965 | 0.625620 | -0.007655 | [-0.011382, -0.003682] | yes |

player_glicko_rw_tier_revert+regional − player_glicko (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+regional log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.599424 | 0.610785 | -0.011361 | [-0.014397, -0.008514] | yes |
| tier1 | 3827 | 0.574595 | 0.589637 | -0.015042 | [-0.019225, -0.010705] | yes |
| tier2 | 571 | 0.621240 | 0.629961 | -0.008721 | [-0.015663, -0.001119] | yes |
| tier3 | 4930 | 0.616171 | 0.624981 | -0.008810 | [-0.013483, -0.004212] | yes |
| international=1 | 3843 | 0.574258 | 0.589611 | -0.015354 | [-0.019553, -0.011200] | yes |
| international=0 | 5485 | 0.617056 | 0.625620 | -0.008564 | [-0.012430, -0.004622] | yes |

player_glicko_rw_tier_revert+calibration − player_glicko (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+calibration log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.599751 | 0.610785 | -0.011034 | [-0.014136, -0.007998] | yes |
| tier1 | 3827 | 0.574177 | 0.589637 | -0.015460 | [-0.020111, -0.010947] | yes |
| tier2 | 571 | 0.621918 | 0.629961 | -0.008044 | [-0.014897, -0.000788] | yes |
| tier3 | 4930 | 0.617035 | 0.624981 | -0.007945 | [-0.012609, -0.003181] | yes |
| international=1 | 3843 | 0.573873 | 0.589611 | -0.015738 | [-0.020269, -0.011246] | yes |
| international=0 | 5485 | 0.617881 | 0.625620 | -0.007739 | [-0.011536, -0.003644] | yes |

player_glicko_rw_tier_revert+form − player_glicko (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+form log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.597944 | 0.610785 | -0.012841 | [-0.015751, -0.009987] | yes |
| tier1 | 3827 | 0.573809 | 0.589637 | -0.015828 | [-0.020113, -0.011523] | yes |
| tier2 | 571 | 0.620820 | 0.629961 | -0.009141 | [-0.016407, -0.001787] | yes |
| tier3 | 4930 | 0.614030 | 0.624981 | -0.010951 | [-0.015453, -0.006469] | yes |
| international=1 | 3843 | 0.573584 | 0.589611 | -0.016028 | [-0.020506, -0.011509] | yes |
| international=0 | 5485 | 0.615012 | 0.625620 | -0.010608 | [-0.014351, -0.006649] | yes |

### Series

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| coin | all | 4366 | 0.693147 | 0.250000 | 0.500000 | 0.075126 |
| coin | tier1 | 1960 | 0.693147 | 0.250000 | 0.500000 | 0.105102 |
| coin | tier2 | 268 | 0.693147 | 0.250000 | 0.500000 | 0.082090 |
| coin | tier3 | 2138 | 0.693147 | 0.250000 | 0.500000 | 0.046773 |
| coin | unknown | 0 | — | — | — | — |
| coin | international=1 | 1974 | 0.693147 | 0.250000 | 0.500000 | 0.105876 |
| coin | international=0 | 2392 | 0.693147 | 0.250000 | 0.500000 | 0.049749 |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko | all | 4366 | 0.584862 | 0.201406 | 0.675332 | 0.031301 |
| player_glicko | tier1 | 1960 | 0.550511 | 0.186772 | 0.708418 | 0.026638 |
| player_glicko | tier2 | 268 | 0.590452 | 0.203388 | 0.660448 | 0.067307 |
| player_glicko | tier3 | 2138 | 0.615654 | 0.214573 | 0.646866 | 0.037057 |
| player_glicko | unknown | 0 | — | — | — | — |
| player_glicko | international=1 | 1974 | 0.550617 | 0.186811 | 0.707953 | 0.027032 |
| player_glicko | international=0 | 2392 | 0.613123 | 0.213450 | 0.648411 | 0.036354 |

player_glicko − coin (paired log loss):

| Section | Rows | player_glicko log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.584862 | 0.693147 | -0.108285 | [-0.119287, -0.097423] | yes |
| tier1 | 1960 | 0.550511 | 0.693147 | -0.142637 | [-0.159748, -0.125033] | yes |
| tier2 | 268 | 0.590452 | 0.693147 | -0.102695 | [-0.148419, -0.054213] | yes |
| tier3 | 2138 | 0.615654 | 0.693147 | -0.077494 | [-0.091999, -0.063213] | yes |
| international=1 | 1974 | 0.550617 | 0.693147 | -0.142530 | [-0.159866, -0.124664] | yes |
| international=0 | 2392 | 0.613123 | 0.693147 | -0.080024 | [-0.093468, -0.066049] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko_rookie_weights | all | 4366 | 0.564266 | 0.192491 | 0.695946 | 0.020688 |
| player_glicko_rookie_weights | tier1 | 1960 | 0.524798 | 0.176845 | 0.729847 | 0.025151 |
| player_glicko_rookie_weights | tier2 | 268 | 0.582787 | 0.199619 | 0.671642 | 0.049640 |
| player_glicko_rookie_weights | tier3 | 2138 | 0.598126 | 0.205940 | 0.667914 | 0.034140 |
| player_glicko_rookie_weights | unknown | 0 | — | — | — | — |
| player_glicko_rookie_weights | international=1 | 1974 | 0.524395 | 0.176669 | 0.730243 | 0.025073 |
| player_glicko_rookie_weights | international=0 | 2392 | 0.597169 | 0.205548 | 0.667642 | 0.030007 |

player_glicko_rookie_weights − coin (paired log loss):

| Section | Rows | player_glicko_rookie_weights log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.564266 | 0.693147 | -0.128881 | [-0.141700, -0.115658] | yes |
| tier1 | 1960 | 0.524798 | 0.693147 | -0.168349 | [-0.187822, -0.148410] | yes |
| tier2 | 268 | 0.582787 | 0.693147 | -0.110360 | [-0.159403, -0.058464] | yes |
| tier3 | 2138 | 0.598126 | 0.693147 | -0.095021 | [-0.111816, -0.078673] | yes |
| international=1 | 1974 | 0.524395 | 0.693147 | -0.168752 | [-0.188500, -0.148181] | yes |
| international=0 | 2392 | 0.597169 | 0.693147 | -0.095978 | [-0.112058, -0.079411] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko_rw_tier_revert | all | 4366 | 0.565121 | 0.192751 | 0.698465 | 0.019997 |
| player_glicko_rw_tier_revert | tier1 | 1960 | 0.525977 | 0.177252 | 0.730867 | 0.031903 |
| player_glicko_rw_tier_revert | tier2 | 268 | 0.584509 | 0.200283 | 0.675373 | 0.052574 |
| player_glicko_rw_tier_revert | tier3 | 2138 | 0.598576 | 0.206016 | 0.671656 | 0.036068 |
| player_glicko_rw_tier_revert | unknown | 0 | — | — | — | — |
| player_glicko_rw_tier_revert | international=1 | 1974 | 0.525688 | 0.177122 | 0.731256 | 0.031721 |
| player_glicko_rw_tier_revert | international=0 | 2392 | 0.597664 | 0.205649 | 0.671405 | 0.032590 |

player_glicko_rw_tier_revert − coin (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.565121 | 0.693147 | -0.128026 | [-0.140751, -0.115061] | yes |
| tier1 | 1960 | 0.525977 | 0.693147 | -0.167170 | [-0.186255, -0.147652] | yes |
| tier2 | 268 | 0.584509 | 0.693147 | -0.108638 | [-0.156324, -0.058288] | yes |
| tier3 | 2138 | 0.598576 | 0.693147 | -0.094571 | [-0.111389, -0.078477] | yes |
| international=1 | 1974 | 0.525688 | 0.693147 | -0.167460 | [-0.186312, -0.147709] | yes |
| international=0 | 2392 | 0.597664 | 0.693147 | -0.095483 | [-0.111897, -0.079075] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko+none | all | 4366 | 0.584862 | 0.201406 | 0.675332 | 0.031301 |
| player_glicko+none | tier1 | 1960 | 0.550511 | 0.186772 | 0.708418 | 0.026638 |
| player_glicko+none | tier2 | 268 | 0.590452 | 0.203388 | 0.660448 | 0.067307 |
| player_glicko+none | tier3 | 2138 | 0.615654 | 0.214573 | 0.646866 | 0.037057 |
| player_glicko+none | unknown | 0 | — | — | — | — |
| player_glicko+none | international=1 | 1974 | 0.550617 | 0.186811 | 0.707953 | 0.027032 |
| player_glicko+none | international=0 | 2392 | 0.613123 | 0.213450 | 0.648411 | 0.036354 |

player_glicko+none − coin (paired log loss):

| Section | Rows | player_glicko+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.584862 | 0.693147 | -0.108285 | [-0.119287, -0.097423] | yes |
| tier1 | 1960 | 0.550511 | 0.693147 | -0.142637 | [-0.159748, -0.125033] | yes |
| tier2 | 268 | 0.590452 | 0.693147 | -0.102695 | [-0.148419, -0.054213] | yes |
| tier3 | 2138 | 0.615654 | 0.693147 | -0.077494 | [-0.091999, -0.063213] | yes |
| international=1 | 1974 | 0.550617 | 0.693147 | -0.142530 | [-0.159866, -0.124664] | yes |
| international=0 | 2392 | 0.613123 | 0.693147 | -0.080024 | [-0.093468, -0.066049] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko+regional | all | 4366 | 0.583839 | 0.201019 | 0.676477 | 0.031994 |
| player_glicko+regional | tier1 | 1960 | 0.549538 | 0.186404 | 0.711990 | 0.028829 |
| player_glicko+regional | tier2 | 268 | 0.588121 | 0.202256 | 0.660448 | 0.078404 |
| player_glicko+regional | tier3 | 2138 | 0.614748 | 0.214262 | 0.645931 | 0.037455 |
| player_glicko+regional | unknown | 0 | — | — | — | — |
| player_glicko+regional | international=1 | 1974 | 0.549573 | 0.186412 | 0.711499 | 0.028239 |
| player_glicko+regional | international=0 | 2392 | 0.612117 | 0.213073 | 0.647575 | 0.037349 |

player_glicko+regional − coin (paired log loss):

| Section | Rows | player_glicko+regional log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.583839 | 0.693147 | -0.109308 | [-0.120308, -0.098392] | yes |
| tier1 | 1960 | 0.549538 | 0.693147 | -0.143609 | [-0.160734, -0.126215] | yes |
| tier2 | 268 | 0.588121 | 0.693147 | -0.105026 | [-0.151493, -0.056323] | yes |
| tier3 | 2138 | 0.614748 | 0.693147 | -0.078399 | [-0.092696, -0.064549] | yes |
| international=1 | 1974 | 0.549573 | 0.693147 | -0.143574 | [-0.160955, -0.126049] | yes |
| international=0 | 2392 | 0.612117 | 0.693147 | -0.081030 | [-0.094392, -0.067137] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko+calibration | all | 4366 | 0.583996 | 0.201181 | 0.675332 | 0.032996 |
| player_glicko+calibration | tier1 | 1960 | 0.548157 | 0.186152 | 0.708418 | 0.028050 |
| player_glicko+calibration | tier2 | 268 | 0.589684 | 0.202823 | 0.660448 | 0.049283 |
| player_glicko+calibration | tier3 | 2138 | 0.616140 | 0.214753 | 0.646866 | 0.036969 |
| player_glicko+calibration | unknown | 0 | — | — | — | — |
| player_glicko+calibration | international=1 | 1974 | 0.548287 | 0.186198 | 0.707953 | 0.029259 |
| player_glicko+calibration | international=0 | 2392 | 0.613466 | 0.213545 | 0.648411 | 0.036537 |

player_glicko+calibration − coin (paired log loss):

| Section | Rows | player_glicko+calibration log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.583996 | 0.693147 | -0.109151 | [-0.120260, -0.098287] | yes |
| tier1 | 1960 | 0.548157 | 0.693147 | -0.144991 | [-0.163362, -0.126285] | yes |
| tier2 | 268 | 0.589684 | 0.693147 | -0.103463 | [-0.149926, -0.055399] | yes |
| tier3 | 2138 | 0.616140 | 0.693147 | -0.077008 | [-0.090463, -0.063826] | yes |
| international=1 | 1974 | 0.548287 | 0.693147 | -0.144861 | [-0.163396, -0.126066] | yes |
| international=0 | 2392 | 0.613466 | 0.693147 | -0.079681 | [-0.092619, -0.066005] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko+form | all | 4366 | 0.584302 | 0.201188 | 0.677279 | 0.031119 |
| player_glicko+form | tier1 | 1960 | 0.549839 | 0.186558 | 0.710969 | 0.027497 |
| player_glicko+form | tier2 | 268 | 0.590281 | 0.203489 | 0.652985 | 0.065966 |
| player_glicko+form | tier3 | 2138 | 0.615147 | 0.214312 | 0.649439 | 0.036889 |
| player_glicko+form | unknown | 0 | — | — | — | — |
| player_glicko+form | international=1 | 1974 | 0.549930 | 0.186603 | 0.710486 | 0.027199 |
| player_glicko+form | international=0 | 2392 | 0.612669 | 0.213225 | 0.649875 | 0.036378 |

player_glicko+form − coin (paired log loss):

| Section | Rows | player_glicko+form log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.584302 | 0.693147 | -0.108845 | [-0.120120, -0.097857] | yes |
| tier1 | 1960 | 0.549839 | 0.693147 | -0.143308 | [-0.160303, -0.125687] | yes |
| tier2 | 268 | 0.590281 | 0.693147 | -0.102866 | [-0.148386, -0.054980] | yes |
| tier3 | 2138 | 0.615147 | 0.693147 | -0.078000 | [-0.093562, -0.063449] | yes |
| international=1 | 1974 | 0.549930 | 0.693147 | -0.143218 | [-0.160715, -0.125213] | yes |
| international=0 | 2392 | 0.612669 | 0.693147 | -0.080479 | [-0.094192, -0.065720] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko_rookie_weights+none | all | 4366 | 0.564266 | 0.192491 | 0.695946 | 0.020688 |
| player_glicko_rookie_weights+none | tier1 | 1960 | 0.524798 | 0.176845 | 0.729847 | 0.025151 |
| player_glicko_rookie_weights+none | tier2 | 268 | 0.582787 | 0.199619 | 0.671642 | 0.049640 |
| player_glicko_rookie_weights+none | tier3 | 2138 | 0.598126 | 0.205940 | 0.667914 | 0.034140 |
| player_glicko_rookie_weights+none | unknown | 0 | — | — | — | — |
| player_glicko_rookie_weights+none | international=1 | 1974 | 0.524395 | 0.176669 | 0.730243 | 0.025073 |
| player_glicko_rookie_weights+none | international=0 | 2392 | 0.597169 | 0.205548 | 0.667642 | 0.030007 |

player_glicko_rookie_weights+none − coin (paired log loss):

| Section | Rows | player_glicko_rookie_weights+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.564266 | 0.693147 | -0.128881 | [-0.141700, -0.115658] | yes |
| tier1 | 1960 | 0.524798 | 0.693147 | -0.168349 | [-0.187822, -0.148410] | yes |
| tier2 | 268 | 0.582787 | 0.693147 | -0.110360 | [-0.159403, -0.058464] | yes |
| tier3 | 2138 | 0.598126 | 0.693147 | -0.095021 | [-0.111816, -0.078673] | yes |
| international=1 | 1974 | 0.524395 | 0.693147 | -0.168752 | [-0.188500, -0.148181] | yes |
| international=0 | 2392 | 0.597169 | 0.693147 | -0.095978 | [-0.112058, -0.079411] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko_rookie_weights+regional | all | 4366 | 0.563269 | 0.192113 | 0.697549 | 0.021760 |
| player_glicko_rookie_weights+regional | tier1 | 1960 | 0.523776 | 0.176427 | 0.731378 | 0.022573 |
| player_glicko_rookie_weights+regional | tier2 | 268 | 0.582281 | 0.199274 | 0.675373 | 0.046672 |
| player_glicko_rookie_weights+regional | tier3 | 2138 | 0.597090 | 0.205596 | 0.669317 | 0.039608 |
| player_glicko_rookie_weights+regional | unknown | 0 | — | — | — | — |
| player_glicko_rookie_weights+regional | international=1 | 1974 | 0.523306 | 0.176221 | 0.732270 | 0.022673 |
| player_glicko_rookie_weights+regional | international=0 | 2392 | 0.596248 | 0.205228 | 0.668896 | 0.035046 |

player_glicko_rookie_weights+regional − coin (paired log loss):

| Section | Rows | player_glicko_rookie_weights+regional log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.563269 | 0.693147 | -0.129878 | [-0.142572, -0.116618] | yes |
| tier1 | 1960 | 0.523776 | 0.693147 | -0.169371 | [-0.189140, -0.149576] | yes |
| tier2 | 268 | 0.582281 | 0.693147 | -0.110867 | [-0.160490, -0.058365] | yes |
| tier3 | 2138 | 0.597090 | 0.693147 | -0.096057 | [-0.112492, -0.079614] | yes |
| international=1 | 1974 | 0.523306 | 0.693147 | -0.169841 | [-0.189775, -0.149581] | yes |
| international=0 | 2392 | 0.596248 | 0.693147 | -0.096899 | [-0.113008, -0.080531] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko_rookie_weights+calibration | all | 4366 | 0.564054 | 0.192441 | 0.695946 | 0.020520 |
| player_glicko_rookie_weights+calibration | tier1 | 1960 | 0.524165 | 0.176615 | 0.729847 | 0.024068 |
| player_glicko_rookie_weights+calibration | tier2 | 268 | 0.582440 | 0.199231 | 0.671642 | 0.044596 |
| player_glicko_rookie_weights+calibration | tier3 | 2138 | 0.598317 | 0.206098 | 0.667914 | 0.032283 |
| player_glicko_rookie_weights+calibration | unknown | 0 | — | — | — | — |
| player_glicko_rookie_weights+calibration | international=1 | 1974 | 0.523775 | 0.176445 | 0.730243 | 0.024324 |
| player_glicko_rookie_weights+calibration | international=0 | 2392 | 0.597294 | 0.205642 | 0.667642 | 0.029898 |

player_glicko_rookie_weights+calibration − coin (paired log loss):

| Section | Rows | player_glicko_rookie_weights+calibration log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.564054 | 0.693147 | -0.129093 | [-0.141910, -0.115970] | yes |
| tier1 | 1960 | 0.524165 | 0.693147 | -0.168982 | [-0.188882, -0.148938] | yes |
| tier2 | 268 | 0.582440 | 0.693147 | -0.110707 | [-0.160729, -0.058271] | yes |
| tier3 | 2138 | 0.598317 | 0.693147 | -0.094830 | [-0.111265, -0.078863] | yes |
| international=1 | 1974 | 0.523775 | 0.693147 | -0.169372 | [-0.189126, -0.148654] | yes |
| international=0 | 2392 | 0.597294 | 0.693147 | -0.095854 | [-0.111905, -0.079405] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko_rookie_weights+form | all | 4366 | 0.562929 | 0.191952 | 0.698809 | 0.023536 |
| player_glicko_rookie_weights+form | tier1 | 1960 | 0.524855 | 0.176840 | 0.729337 | 0.021699 |
| player_glicko_rookie_weights+form | tier2 | 268 | 0.577870 | 0.197919 | 0.671642 | 0.061531 |
| player_glicko_rookie_weights+form | tier3 | 2138 | 0.595960 | 0.205058 | 0.674228 | 0.036009 |
| player_glicko_rookie_weights+form | unknown | 0 | — | — | — | — |
| player_glicko_rookie_weights+form | international=1 | 1974 | 0.524552 | 0.176715 | 0.729230 | 0.020983 |
| player_glicko_rookie_weights+form | international=0 | 2392 | 0.594600 | 0.204526 | 0.673704 | 0.033416 |

player_glicko_rookie_weights+form − coin (paired log loss):

| Section | Rows | player_glicko_rookie_weights+form log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.562929 | 0.693147 | -0.130218 | [-0.143104, -0.117199] | yes |
| tier1 | 1960 | 0.524855 | 0.693147 | -0.168292 | [-0.188125, -0.148018] | yes |
| tier2 | 268 | 0.577870 | 0.693147 | -0.115277 | [-0.162965, -0.064755] | yes |
| tier3 | 2138 | 0.595960 | 0.693147 | -0.097187 | [-0.114250, -0.080769] | yes |
| international=1 | 1974 | 0.524552 | 0.693147 | -0.168595 | [-0.188193, -0.148578] | yes |
| international=0 | 2392 | 0.594600 | 0.693147 | -0.098548 | [-0.114712, -0.081604] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko_rw_tier_revert+none | all | 4366 | 0.565121 | 0.192751 | 0.698465 | 0.019997 |
| player_glicko_rw_tier_revert+none | tier1 | 1960 | 0.525977 | 0.177252 | 0.730867 | 0.031903 |
| player_glicko_rw_tier_revert+none | tier2 | 268 | 0.584509 | 0.200283 | 0.675373 | 0.052574 |
| player_glicko_rw_tier_revert+none | tier3 | 2138 | 0.598576 | 0.206016 | 0.671656 | 0.036068 |
| player_glicko_rw_tier_revert+none | unknown | 0 | — | — | — | — |
| player_glicko_rw_tier_revert+none | international=1 | 1974 | 0.525688 | 0.177122 | 0.731256 | 0.031721 |
| player_glicko_rw_tier_revert+none | international=0 | 2392 | 0.597664 | 0.205649 | 0.671405 | 0.032590 |

player_glicko_rw_tier_revert+none − coin (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.565121 | 0.693147 | -0.128026 | [-0.140751, -0.115061] | yes |
| tier1 | 1960 | 0.525977 | 0.693147 | -0.167170 | [-0.186255, -0.147652] | yes |
| tier2 | 268 | 0.584509 | 0.693147 | -0.108638 | [-0.156324, -0.058288] | yes |
| tier3 | 2138 | 0.598576 | 0.693147 | -0.094571 | [-0.111389, -0.078477] | yes |
| international=1 | 1974 | 0.525688 | 0.693147 | -0.167460 | [-0.186312, -0.147709] | yes |
| international=0 | 2392 | 0.597664 | 0.693147 | -0.095483 | [-0.111897, -0.079075] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko_rw_tier_revert+regional | all | 4366 | 0.564043 | 0.192347 | 0.699153 | 0.020683 |
| player_glicko_rw_tier_revert+regional | tier1 | 1960 | 0.525030 | 0.176880 | 0.731888 | 0.027855 |
| player_glicko_rw_tier_revert+regional | tier2 | 268 | 0.583493 | 0.199910 | 0.675373 | 0.051994 |
| player_glicko_rw_tier_revert+regional | tier3 | 2138 | 0.597370 | 0.205578 | 0.672123 | 0.034797 |
| player_glicko_rw_tier_revert+regional | unknown | 0 | — | — | — | — |
| player_glicko_rw_tier_revert+regional | international=1 | 1974 | 0.524661 | 0.176716 | 0.732270 | 0.027279 |
| player_glicko_rw_tier_revert+regional | international=0 | 2392 | 0.596542 | 0.205246 | 0.671823 | 0.031549 |

player_glicko_rw_tier_revert+regional − coin (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+regional log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.564043 | 0.693147 | -0.129105 | [-0.141592, -0.116110] | yes |
| tier1 | 1960 | 0.525030 | 0.693147 | -0.168118 | [-0.187416, -0.148510] | yes |
| tier2 | 268 | 0.583493 | 0.693147 | -0.109654 | [-0.157852, -0.059220] | yes |
| tier3 | 2138 | 0.597370 | 0.693147 | -0.095778 | [-0.112608, -0.079778] | yes |
| international=1 | 1974 | 0.524661 | 0.693147 | -0.168486 | [-0.187825, -0.148509] | yes |
| international=0 | 2392 | 0.596542 | 0.693147 | -0.096605 | [-0.112863, -0.080150] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko_rw_tier_revert+calibration | all | 4366 | 0.564667 | 0.192580 | 0.698465 | 0.021037 |
| player_glicko_rw_tier_revert+calibration | tier1 | 1960 | 0.525067 | 0.176923 | 0.730867 | 0.026018 |
| player_glicko_rw_tier_revert+calibration | tier2 | 268 | 0.583358 | 0.199663 | 0.675373 | 0.043121 |
| player_glicko_rw_tier_revert+calibration | tier3 | 2138 | 0.598628 | 0.206047 | 0.671656 | 0.034770 |
| player_glicko_rw_tier_revert+calibration | unknown | 0 | — | — | — | — |
| player_glicko_rw_tier_revert+calibration | international=1 | 1974 | 0.524737 | 0.176781 | 0.731256 | 0.026063 |
| player_glicko_rw_tier_revert+calibration | international=0 | 2392 | 0.597620 | 0.205619 | 0.671405 | 0.033772 |

player_glicko_rw_tier_revert+calibration − coin (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+calibration log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.564667 | 0.693147 | -0.128480 | [-0.141395, -0.115409] | yes |
| tier1 | 1960 | 0.525067 | 0.693147 | -0.168080 | [-0.187727, -0.147882] | yes |
| tier2 | 268 | 0.583358 | 0.693147 | -0.109789 | [-0.158497, -0.058571] | yes |
| tier3 | 2138 | 0.598628 | 0.693147 | -0.094519 | [-0.111423, -0.078574] | yes |
| international=1 | 1974 | 0.524737 | 0.693147 | -0.168410 | [-0.188006, -0.148023] | yes |
| international=0 | 2392 | 0.597620 | 0.693147 | -0.095527 | [-0.111876, -0.078817] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko_rw_tier_revert+form | all | 4366 | 0.563975 | 0.192309 | 0.701557 | 0.026415 |
| player_glicko_rw_tier_revert+form | tier1 | 1960 | 0.526402 | 0.177401 | 0.731378 | 0.022177 |
| player_glicko_rw_tier_revert+form | tier2 | 268 | 0.579438 | 0.198548 | 0.671642 | 0.050224 |
| player_glicko_rw_tier_revert+form | tier3 | 2138 | 0.596482 | 0.205194 | 0.677970 | 0.036082 |
| player_glicko_rw_tier_revert+form | unknown | 0 | — | — | — | — |
| player_glicko_rw_tier_revert+form | international=1 | 1974 | 0.526218 | 0.177327 | 0.731256 | 0.022136 |
| player_glicko_rw_tier_revert+form | international=0 | 2392 | 0.595135 | 0.204673 | 0.677048 | 0.034668 |

player_glicko_rw_tier_revert+form − coin (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+form log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.563975 | 0.693147 | -0.129172 | [-0.141482, -0.116451] | yes |
| tier1 | 1960 | 0.526402 | 0.693147 | -0.166745 | [-0.186299, -0.147780] | yes |
| tier2 | 268 | 0.579438 | 0.693147 | -0.113709 | [-0.160550, -0.064842] | yes |
| tier3 | 2138 | 0.596482 | 0.693147 | -0.096665 | [-0.113865, -0.080285] | yes |
| international=1 | 1974 | 0.526218 | 0.693147 | -0.166929 | [-0.185859, -0.147526] | yes |
| international=0 | 2392 | 0.595135 | 0.693147 | -0.098012 | [-0.114276, -0.081342] | yes |

player_glicko − team_elo (paired log loss):

| Section | Rows | player_glicko log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.584862 | 0.638539 | -0.053677 | [-0.061296, -0.045900] | yes |

player_glicko_rookie_weights − team_elo (paired log loss):

| Section | Rows | player_glicko_rookie_weights log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.564266 | 0.638539 | -0.074274 | [-0.083965, -0.064024] | yes |

player_glicko_rw_tier_revert − team_elo (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.565121 | 0.638539 | -0.073418 | [-0.082900, -0.063575] | yes |

player_glicko+none − team_elo (paired log loss):

| Section | Rows | player_glicko+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.584862 | 0.638539 | -0.053677 | [-0.061296, -0.045900] | yes |

player_glicko+regional − team_elo (paired log loss):

| Section | Rows | player_glicko+regional log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.583839 | 0.638539 | -0.054700 | [-0.062302, -0.047132] | yes |

player_glicko+calibration − team_elo (paired log loss):

| Section | Rows | player_glicko+calibration log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.583996 | 0.638539 | -0.054543 | [-0.062572, -0.046465] | yes |

player_glicko+form − team_elo (paired log loss):

| Section | Rows | player_glicko+form log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.584302 | 0.638539 | -0.054237 | [-0.062112, -0.046497] | yes |

player_glicko_rookie_weights+none − team_elo (paired log loss):

| Section | Rows | player_glicko_rookie_weights+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.564266 | 0.638539 | -0.074274 | [-0.083965, -0.064024] | yes |

player_glicko_rookie_weights+regional − team_elo (paired log loss):

| Section | Rows | player_glicko_rookie_weights+regional log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.563269 | 0.638539 | -0.075270 | [-0.085115, -0.065027] | yes |

player_glicko_rookie_weights+calibration − team_elo (paired log loss):

| Section | Rows | player_glicko_rookie_weights+calibration log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.564054 | 0.638539 | -0.074485 | [-0.084397, -0.064252] | yes |

player_glicko_rookie_weights+form − team_elo (paired log loss):

| Section | Rows | player_glicko_rookie_weights+form log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.562929 | 0.638539 | -0.075610 | [-0.085302, -0.065494] | yes |

player_glicko_rw_tier_revert+none − team_elo (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.565121 | 0.638539 | -0.073418 | [-0.082900, -0.063575] | yes |

player_glicko_rw_tier_revert+regional − team_elo (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+regional log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.564043 | 0.638539 | -0.074497 | [-0.084026, -0.064599] | yes |

player_glicko_rw_tier_revert+calibration − team_elo (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+calibration log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.564667 | 0.638539 | -0.073872 | [-0.083675, -0.063755] | yes |

player_glicko_rw_tier_revert+form − team_elo (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+form log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.563975 | 0.638539 | -0.074564 | [-0.084073, -0.064845] | yes |

player_glicko_rookie_weights − player_glicko (paired log loss):

| Section | Rows | player_glicko_rookie_weights log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.564266 | 0.584862 | -0.020597 | [-0.025904, -0.015054] | yes |
| tier1 | 1960 | 0.524798 | 0.550511 | -0.025713 | [-0.033304, -0.018321] | yes |
| tier2 | 268 | 0.582787 | 0.590452 | -0.007665 | [-0.019513, 0.006181] | no |
| tier3 | 2138 | 0.598126 | 0.615654 | -0.017528 | [-0.025938, -0.008518] | yes |
| international=1 | 1974 | 0.524395 | 0.550617 | -0.026222 | [-0.033343, -0.018716] | yes |
| international=0 | 2392 | 0.597169 | 0.613123 | -0.015954 | [-0.023788, -0.007793] | yes |

player_glicko_rw_tier_revert − player_glicko (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.565121 | 0.584862 | -0.019741 | [-0.024884, -0.014310] | yes |
| tier1 | 1960 | 0.525977 | 0.550511 | -0.024533 | [-0.031820, -0.017293] | yes |
| tier2 | 268 | 0.584509 | 0.590452 | -0.005943 | [-0.016427, 0.006225] | no |
| tier3 | 2138 | 0.598576 | 0.615654 | -0.017078 | [-0.025340, -0.008183] | yes |
| international=1 | 1974 | 0.525688 | 0.550617 | -0.024930 | [-0.031631, -0.017898] | yes |
| international=0 | 2392 | 0.597664 | 0.613123 | -0.015460 | [-0.023378, -0.007639] | yes |

player_glicko+none − player_glicko (paired log loss):

| Section | Rows | player_glicko+none log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.584862 | 0.584862 | 0.000000 | [0.000000, 0.000000] | no |
| tier1 | 1960 | 0.550511 | 0.550511 | 0.000000 | [0.000000, 0.000000] | no |
| tier2 | 268 | 0.590452 | 0.590452 | 0.000000 | [0.000000, 0.000000] | no |
| tier3 | 2138 | 0.615654 | 0.615654 | 0.000000 | [0.000000, 0.000000] | no |
| international=1 | 1974 | 0.550617 | 0.550617 | 0.000000 | [0.000000, 0.000000] | no |
| international=0 | 2392 | 0.613123 | 0.613123 | 0.000000 | [0.000000, 0.000000] | no |

player_glicko+regional − player_glicko (paired log loss):

| Section | Rows | player_glicko+regional log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.583839 | 0.584862 | -0.001023 | [-0.002076, -0.000012] | yes |
| tier1 | 1960 | 0.549538 | 0.550511 | -0.000973 | [-0.002521, 0.000665] | no |
| tier2 | 268 | 0.588121 | 0.590452 | -0.002331 | [-0.005608, 0.000462] | no |
| tier3 | 2138 | 0.614748 | 0.615654 | -0.000906 | [-0.002445, 0.000502] | no |
| international=1 | 1974 | 0.549573 | 0.550617 | -0.001044 | [-0.002579, 0.000418] | no |
| international=0 | 2392 | 0.612117 | 0.613123 | -0.001006 | [-0.002470, 0.000330] | no |

player_glicko+calibration − player_glicko (paired log loss):

| Section | Rows | player_glicko+calibration log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.583996 | 0.584862 | -0.000866 | [-0.002142, 0.000509] | no |
| tier1 | 1960 | 0.548157 | 0.550511 | -0.002354 | [-0.004852, 0.000142] | no |
| tier2 | 268 | 0.589684 | 0.590452 | -0.000768 | [-0.004500, 0.002695] | no |
| tier3 | 2138 | 0.616140 | 0.615654 | 0.000486 | [-0.000695, 0.001698] | no |
| international=1 | 1974 | 0.548287 | 0.550617 | -0.002330 | [-0.004800, 0.000022] | no |
| international=0 | 2392 | 0.613466 | 0.613123 | 0.000343 | [-0.000825, 0.001484] | no |

player_glicko+form − player_glicko (paired log loss):

| Section | Rows | player_glicko+form log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.584302 | 0.584862 | -0.000560 | [-0.002041, 0.000961] | no |
| tier1 | 1960 | 0.549839 | 0.550511 | -0.000671 | [-0.002256, 0.000961] | no |
| tier2 | 268 | 0.590281 | 0.590452 | -0.000171 | [-0.003415, 0.003033] | no |
| tier3 | 2138 | 0.615147 | 0.615654 | -0.000507 | [-0.002990, 0.002110] | no |
| international=1 | 1974 | 0.549930 | 0.550617 | -0.000687 | [-0.002256, 0.000982] | no |
| international=0 | 2392 | 0.612669 | 0.613123 | -0.000455 | [-0.002670, 0.001990] | no |

player_glicko_rookie_weights+none − player_glicko (paired log loss):

| Section | Rows | player_glicko_rookie_weights+none log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.564266 | 0.584862 | -0.020597 | [-0.025904, -0.015054] | yes |
| tier1 | 1960 | 0.524798 | 0.550511 | -0.025713 | [-0.033304, -0.018321] | yes |
| tier2 | 268 | 0.582787 | 0.590452 | -0.007665 | [-0.019513, 0.006181] | no |
| tier3 | 2138 | 0.598126 | 0.615654 | -0.017528 | [-0.025938, -0.008518] | yes |
| international=1 | 1974 | 0.524395 | 0.550617 | -0.026222 | [-0.033343, -0.018716] | yes |
| international=0 | 2392 | 0.597169 | 0.613123 | -0.015954 | [-0.023788, -0.007793] | yes |

player_glicko_rookie_weights+regional − player_glicko (paired log loss):

| Section | Rows | player_glicko_rookie_weights+regional log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.563269 | 0.584862 | -0.021594 | [-0.027022, -0.016004] | yes |
| tier1 | 1960 | 0.523776 | 0.550511 | -0.026734 | [-0.034506, -0.018905] | yes |
| tier2 | 268 | 0.582281 | 0.590452 | -0.008171 | [-0.020720, 0.006690] | no |
| tier3 | 2138 | 0.597090 | 0.615654 | -0.018563 | [-0.026965, -0.009588] | yes |
| international=1 | 1974 | 0.523306 | 0.550617 | -0.027311 | [-0.034874, -0.019623] | yes |
| international=0 | 2392 | 0.596248 | 0.613123 | -0.016875 | [-0.024852, -0.009040] | yes |

player_glicko_rookie_weights+calibration − player_glicko (paired log loss):

| Section | Rows | player_glicko_rookie_weights+calibration log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.564054 | 0.584862 | -0.020809 | [-0.026081, -0.015239] | yes |
| tier1 | 1960 | 0.524165 | 0.550511 | -0.026346 | [-0.034265, -0.018450] | yes |
| tier2 | 268 | 0.582440 | 0.590452 | -0.008012 | [-0.020300, 0.006267] | no |
| tier3 | 2138 | 0.598317 | 0.615654 | -0.017336 | [-0.025517, -0.008546] | yes |
| international=1 | 1974 | 0.523775 | 0.550617 | -0.026842 | [-0.034325, -0.019121] | yes |
| international=0 | 2392 | 0.597294 | 0.613123 | -0.015830 | [-0.023638, -0.007886] | yes |

player_glicko_rookie_weights+form − player_glicko (paired log loss):

| Section | Rows | player_glicko_rookie_weights+form log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.562929 | 0.584862 | -0.021933 | [-0.027176, -0.016453] | yes |
| tier1 | 1960 | 0.524855 | 0.550511 | -0.025655 | [-0.033279, -0.018042] | yes |
| tier2 | 268 | 0.577870 | 0.590452 | -0.012582 | [-0.024574, 0.002256] | no |
| tier3 | 2138 | 0.595960 | 0.615654 | -0.019694 | [-0.027806, -0.011028] | yes |
| international=1 | 1974 | 0.524552 | 0.550617 | -0.026065 | [-0.033468, -0.018309] | yes |
| international=0 | 2392 | 0.594600 | 0.613123 | -0.018524 | [-0.026197, -0.010485] | yes |

player_glicko_rw_tier_revert+none − player_glicko (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+none log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.565121 | 0.584862 | -0.019741 | [-0.024884, -0.014310] | yes |
| tier1 | 1960 | 0.525977 | 0.550511 | -0.024533 | [-0.031820, -0.017293] | yes |
| tier2 | 268 | 0.584509 | 0.590452 | -0.005943 | [-0.016427, 0.006225] | no |
| tier3 | 2138 | 0.598576 | 0.615654 | -0.017078 | [-0.025340, -0.008183] | yes |
| international=1 | 1974 | 0.525688 | 0.550617 | -0.024930 | [-0.031631, -0.017898] | yes |
| international=0 | 2392 | 0.597664 | 0.613123 | -0.015460 | [-0.023378, -0.007639] | yes |

player_glicko_rw_tier_revert+regional − player_glicko (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+regional log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.564043 | 0.584862 | -0.020820 | [-0.026087, -0.015365] | yes |
| tier1 | 1960 | 0.525030 | 0.550511 | -0.025481 | [-0.032928, -0.017778] | yes |
| tier2 | 268 | 0.583493 | 0.590452 | -0.006959 | [-0.018359, 0.005578] | no |
| tier3 | 2138 | 0.597370 | 0.615654 | -0.018284 | [-0.026631, -0.009421] | yes |
| international=1 | 1974 | 0.524661 | 0.550617 | -0.025956 | [-0.032897, -0.018633] | yes |
| international=0 | 2392 | 0.596542 | 0.613123 | -0.016581 | [-0.024537, -0.008978] | yes |

player_glicko_rw_tier_revert+calibration − player_glicko (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+calibration log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.564667 | 0.584862 | -0.020195 | [-0.025542, -0.014471] | yes |
| tier1 | 1960 | 0.525067 | 0.550511 | -0.025443 | [-0.033509, -0.017262] | yes |
| tier2 | 268 | 0.583358 | 0.590452 | -0.007094 | [-0.018820, 0.006409] | no |
| tier3 | 2138 | 0.598628 | 0.615654 | -0.017026 | [-0.025115, -0.007973] | yes |
| international=1 | 1974 | 0.524737 | 0.550617 | -0.025880 | [-0.033436, -0.018016] | yes |
| international=0 | 2392 | 0.597620 | 0.613123 | -0.015503 | [-0.023486, -0.007670] | yes |

player_glicko_rw_tier_revert+form − player_glicko (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+form log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.563975 | 0.584862 | -0.020887 | [-0.026012, -0.015335] | yes |
| tier1 | 1960 | 0.526402 | 0.550511 | -0.024108 | [-0.031417, -0.016811] | yes |
| tier2 | 268 | 0.579438 | 0.590452 | -0.011014 | [-0.022550, 0.002329] | no |
| tier3 | 2138 | 0.596482 | 0.615654 | -0.019171 | [-0.027171, -0.010573] | yes |
| international=1 | 1974 | 0.526218 | 0.550617 | -0.024399 | [-0.031450, -0.016813] | yes |
| international=0 | 2392 | 0.595135 | 0.613123 | -0.017989 | [-0.025605, -0.010009] | yes |

## Stage 2 — validation vs Kalshi

### player_glicko: Kalshi comparison and returns



#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 621 | 0.613181 | 0.613968 | -0.000787 [-0.016467, 0.013860] | no |
| series | tier1 | 528 | 0.608352 | 0.608069 | 0.000284 [-0.013848, 0.014804] | no |
| series | tier2 | 85 | 0.644624 | 0.643551 | 0.001073 [-0.042546, 0.042379] | no |
| series | tier3 | 8 | 0.597808 | 0.689027 | -0.091218 [-0.406440, 0.132080] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 528 | 0.608352 | 0.608069 | 0.000284 [-0.013848, 0.014804] | no |
| series | international=0 | 93 | 0.640597 | 0.647463 | -0.006866 [-0.054606, 0.038431] | no |
| game | all | 434 | 0.642801 | 0.632587 | 0.010214 [-0.003107, 0.023865] | no |
| game | tier1 | 340 | 0.640137 | 0.629029 | 0.011108 [-0.004773, 0.027518] | no |
| game | tier2 | 85 | 0.660177 | 0.652750 | 0.007427 [-0.019236, 0.035024] | no |
| game | tier3 | 9 | 0.579318 | 0.576544 | 0.002773 [-0.073758, 0.063999] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 340 | 0.640137 | 0.629029 | 0.011108 [-0.004773, 0.027518] | no |
| game | international=0 | 94 | 0.652435 | 0.645454 | 0.006982 [-0.019108, 0.032993] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 400 | 400 | 0.0554 | 2.51% [-10.62%, 15.81%] | $61.17 | 1.223× | 74.94% | $15.97 | 215 (185 unfilled) | 0.49% [-16.38%, 17.61%] | $48.14 |
| series | tier1 | 341 | 341 | 0.0531 | 1.35% [-11.86%, 14.62%] | $39.20 | 0.784× | 74.16% | $11.53 | 185 (156 unfilled) | -2.08% [-18.58%, 15.62%] | $28.27 |
| series | tier2 | 53 | 53 | 0.0614 | 6.89% [-33.17%, 53.54%] | $69.35 | 1.387× | 34.43% | $6.14 | 24 (29 unfilled) | 12.88% [-61.09%, 89.48%] | $73.49 |
| series | tier3 | 6 | 6 | 0.1325 | 29.69% [-73.50%, 147.49%] | $56.13 | 1.123× | 5.79% | $4.88 | 6 (0 unfilled) | 29.69% [-73.50%, 147.49%] | $56.82 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 341 | 341 | 0.0531 | 1.35% [-11.86%, 14.62%] | $39.20 | 0.784× | 74.16% | $11.53 | 185 (156 unfilled) | -2.08% [-18.58%, 15.62%] | $28.27 |
| series | international=0 | 59 | 59 | 0.0687 | 9.21% [-28.18%, 49.54%] | $77.84 | 1.557× | 34.43% | $6.78 | 30 (29 unfilled) | 16.23% [-45.17%, 87.35%] | $84.22 |
| game | all | 221 | 119 | 0.0467 | -6.61% [-20.19%, 6.76%] | $15.58 | 0.312× | 71.01% | $4.33 | 33 (188 unfilled) | -21.16% [-49.78%, 7.62%] | $41.30 |
| game | tier1 | 173 | 92 | 0.0495 | -6.51% [-21.96%, 9.78%] | $18.71 | 0.374× | 65.37% | $4.33 | 27 (146 unfilled) | -21.94% [-53.23%, 11.22%] | $40.57 |
| game | tier2 | 41 | 23 | 0.0420 | -5.71% [-33.71%, 23.46%] | $41.09 | 0.822× | 24.83% | $4.74 | 5 (36 unfilled) | -0.90% [-72.65%, 70.30%] | $51.22 |
| game | tier3 | 7 | 4 | 0.0043 | -14.48% [-62.62%, 47.90%] | $51.09 | 1.022× | 0.37% | $2.00 | 1 (6 unfilled) | -100.00% [-100.00%, -100.00%] | $49.60 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 173 | 92 | 0.0495 | -6.51% [-21.96%, 9.78%] | $18.71 | 0.374× | 65.37% | $4.33 | 27 (146 unfilled) | -21.94% [-53.23%, 11.22%] | $40.57 |
| game | international=0 | 48 | 27 | 0.0365 | -6.99% [-31.16%, 19.57%] | $41.99 | 0.840× | 24.83% | $4.74 | 6 (42 unfilled) | -17.63% [-77.39%, 46.96%] | $50.81 |
| series+game | all | 621 | 439 | 0.0523 | -0.72% [-11.40%, 9.90%] | $25.27 | 0.505× | 82.43% | $8.80 | 248 (373 unfilled) | -2.37% [-18.49%, 14.14%] | $56.17 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 280 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2025-11 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2025-12 | series | 13 | 1.000000 | 0.000000 | unfitted |
| 2026-01 | series | 79 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 148 | 1.045798 | 0.289432 | fitted |
| 2026-03 | series | 249 | 0.975290 | 0.342906 | fitted |
| 2026-03 | game | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | series | 302 | 0.985509 | 0.463294 | fitted |
| 2026-04 | game | 15 | 1.000000 | 0.000000 | unfitted |
| 2026-05 | series | 379 | 0.908484 | 0.443668 | fitted |
| 2026-05 | game | 132 | 1.078955 | -0.585585 | fitted |
| 2026-06 | series | 544 | 0.935218 | 0.509364 | fitted |
| 2026-06 | game | 330 | 0.950206 | -0.102799 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 473 | 0.622525 | 0.626718 | -0.004193 [-0.012424, 0.003573] | no |
| series | tier1 | 401 | 0.615513 | 0.617017 | -0.001505 [-0.009720, 0.006497] | no |
| series | tier2 | 64 | 0.666762 | 0.679709 | -0.012947 [-0.039881, 0.012471] | no |
| series | tier3 | 8 | 0.620129 | 0.689027 | -0.068898 [-0.269667, 0.066224] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 401 | 0.615513 | 0.617017 | -0.001505 [-0.009720, 0.006497] | no |
| series | international=0 | 72 | 0.661581 | 0.680744 | -0.019164 [-0.050868, 0.010850] | no |
| game | all | 302 | 0.628878 | 0.623361 | 0.005517 [-0.002462, 0.013910] | no |
| game | tier1 | 237 | 0.616969 | 0.611859 | 0.005110 [-0.003965, 0.014664] | no |
| game | tier2 | 56 | 0.686895 | 0.679563 | 0.007332 [-0.011406, 0.027506] | no |
| game | tier3 | 9 | 0.581502 | 0.576544 | 0.004958 [-0.005511, 0.018043] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 237 | 0.616969 | 0.611859 | 0.005110 [-0.003965, 0.014664] | no |
| game | international=0 | 65 | 0.672302 | 0.665299 | 0.007003 [-0.009603, 0.024804] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 138 | 138 | 0.0247 | 11.82% [-13.52%, 39.29%] | $88.24 | 1.765× | 46.58% | $10.69 | 71 (67 unfilled) | 12.31% [-21.27%, 50.61%] | $74.91 |
| series | tier1 | 106 | 106 | 0.0230 | 0.63% [-25.63%, 28.44%] | $57.91 | 1.158× | 46.62% | $7.89 | 53 (53 unfilled) | -13.78% [-43.27%, 16.39%] | $50.47 |
| series | tier2 | 28 | 28 | 0.0218 | 51.16% [-18.49%, 126.32%] | $67.60 | 1.352× | 16.15% | $5.61 | 14 (14 unfilled) | 105.10% [-20.72%, 241.46%] | $64.56 |
| series | tier3 | 4 | 4 | 0.0898 | 31.26% [-100.00%, 172.78%] | $56.25 | 1.125× | 4.61% | $4.59 | 4 (0 unfilled) | 31.26% [-100.00%, 172.78%] | $56.25 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 106 | 106 | 0.0230 | 0.63% [-25.63%, 28.44%] | $57.91 | 1.158× | 46.62% | $7.89 | 53 (53 unfilled) | -13.78% [-43.27%, 16.39%] | $50.47 |
| series | international=0 | 32 | 32 | 0.0303 | 48.68% [-19.76%, 117.11%] | $76.02 | 1.520× | 16.15% | $6.19 | 18 (14 unfilled) | 88.73% [-11.84%, 205.50%] | $72.62 |
| game | all | 54 | 30 | 0.0214 | -2.68% [-28.90%, 24.70%] | $34.20 | 0.684× | 41.90% | $4.73 | 4 (50 unfilled) | 38.11% [11.81%, 96.23%] | $50.56 |
| game | tier1 | 39 | 21 | 0.0210 | -4.68% [-37.92%, 29.82%] | $35.26 | 0.705× | 41.91% | $2.76 | 4 (35 unfilled) | 38.11% [11.81%, 96.23%] | $50.56 |
| game | tier2 | 15 | 9 | 0.0225 | 2.52% [-46.59%, 56.49%] | $48.47 | 0.969× | 12.07% | $4.73 | 0 (15 unfilled) | — | $50.00 |
| game | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 39 | 21 | 0.0210 | -4.68% [-37.92%, 29.82%] | $35.26 | 0.705× | 41.91% | $2.76 | 4 (35 unfilled) | 38.11% [11.81%, 96.23%] | $50.56 |
| game | international=0 | 15 | 9 | 0.0225 | 2.52% [-46.59%, 56.49%] | $48.47 | 0.969× | 12.07% | $4.73 | 0 (15 unfilled) | — | $50.00 |
| series+game | all | 192 | 150 | 0.0237 | 7.76% [-11.21%, 26.06%] | $71.22 | 1.424× | 46.50% | $8.14 | 75 (117 unfilled) | 13.67% [-18.42%, 50.24%] | $74.17 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| game | 2026-03 | 15 | 0.744029 | — | 0.669739 | -73.56% (6), $36.02 | — | 3 (3 unfilled) | -47.12% [-100.00%, -20.42%] | $44.58 | — | — | — |
| game | 2026-04 | 117 | 0.666715 | — | 0.651637 | -3.68% (47), $45.08 | — | 13 (34 unfilled) | 10.80% [-36.33%, 54.13%] | $55.11 | — | — | — |
| game | 2026-05 | 198 | 0.665984 | 0.662500 | 0.657045 | -3.27% (105), $25.77 | -2.68% (54), $34.20 | 5 (100 unfilled) | -58.93% [-100.00%, 22.99%] | $43.57 | 4 (50 unfilled) | 38.11% [11.81%, 96.23%] | $50.56 |
| game | 2026-06 | 104 | 0.557159 | 0.564868 | 0.559231 | -7.99% (63), $47.55 | — (0), $50.00 | 12 (51 unfilled) | -33.49% [-79.73%, 17.70%] | $48.04 | 0 (0 unfilled) | — | $50.00 |
| series | 2025-11 | 13 | 0.473208 | — | 0.588964 | 70.08% (11), $81.85 | — | 10 (1 unfilled) | 39.07% [-22.11%, 117.29%] | $77.25 | — | — | — |
| series | 2025-12 | 66 | 0.663611 | — | 0.640347 | -6.38% (42), $35.95 | — | 38 (4 unfilled) | -2.53% [-42.39%, 40.53%] | $37.49 | — | — | — |
| series | 2026-01 | 69 | 0.524075 | — | 0.506048 | -17.51% (48), $36.13 | — | 24 (24 unfilled) | -34.81% [-75.07%, 10.97%] | $32.44 | — | — | — |
| series | 2026-02 | 101 | 0.666687 | 0.665014 | 0.667211 | 10.59% (70), $46.75 | 61.07% (10), $58.17 | 21 (49 unfilled) | 20.91% [-26.66%, 71.14%] | $54.98 | 2 (8 unfilled) | 150.04% [92.31%, 207.22%] | $53.32 |
| series | 2026-03 | 53 | 0.645747 | 0.655848 | 0.663787 | 22.43% (26), $69.13 | -6.84% (5), $52.17 | 22 (4 unfilled) | 18.60% [-28.44%, 66.79%] | $62.12 | 4 (1 unfilled) | -36.89% [-100.00%, 88.42%] | $51.68 |
| series | 2026-04 | 77 | 0.685434 | 0.683528 | 0.690287 | 10.64% (51), $73.77 | 40.73% (26), $60.48 | 34 (17 unfilled) | 26.69% [-27.29%, 88.37%] | $83.12 | 17 (9 unfilled) | 74.29% [-15.16%, 173.89%] | $71.32 |
| series | 2026-05 | 165 | 0.622328 | 0.621061 | 0.626943 | 4.67% (96), $70.68 | 19.06% (54), $75.49 | 24 (72 unfilled) | -15.79% [-56.90%, 28.35%] | $37.47 | 16 (38 unfilled) | 9.73% [-62.53%, 98.51%] | $44.62 |
| series | 2026-06 | 77 | 0.488984 | 0.485991 | 0.484035 | -17.18% (56), $26.49 | -24.00% (43), $39.61 | 42 (14 unfilled) | -17.23% [-49.86%, 17.83%] | $35.86 | 32 (11 unfilled) | -21.80% [-58.36%, 17.25%] | $51.58 |

### player_glicko_rookie_weights: Kalshi comparison and returns



#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 621 | 0.609189 | 0.613968 | -0.004780 [-0.019407, 0.009330] | no |
| series | tier1 | 528 | 0.603370 | 0.608069 | -0.004699 [-0.017789, 0.008831] | no |
| series | tier2 | 85 | 0.650084 | 0.643551 | 0.006533 [-0.037185, 0.047965] | no |
| series | tier3 | 8 | 0.558714 | 0.689027 | -0.130313 [-0.532450, 0.148885] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 528 | 0.603370 | 0.608069 | -0.004699 [-0.017789, 0.008831] | no |
| series | international=0 | 93 | 0.642225 | 0.647463 | -0.005239 [-0.057078, 0.043611] | no |
| game | all | 434 | 0.643967 | 0.632587 | 0.011380 [-0.001351, 0.024616] | no |
| game | tier1 | 340 | 0.640791 | 0.629029 | 0.011761 [-0.002207, 0.026665] | no |
| game | tier2 | 85 | 0.665879 | 0.652750 | 0.013128 [-0.013072, 0.040615] | no |
| game | tier3 | 9 | 0.557014 | 0.576544 | -0.019530 [-0.098297, 0.068122] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 340 | 0.640791 | 0.629029 | 0.011761 [-0.002207, 0.026665] | no |
| game | international=0 | 94 | 0.655455 | 0.645454 | 0.010002 [-0.016070, 0.037185] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 397 | 397 | 0.0516 | 4.14% [-7.84%, 17.29%] | $101.33 | 2.027× | 69.83% | $21.17 | 210 (187 unfilled) | -2.18% [-18.92%, 14.00%] | $73.47 |
| series | tier1 | 336 | 336 | 0.0486 | 4.20% [-8.97%, 17.38%] | $66.12 | 1.322× | 67.86% | $16.00 | 179 (157 unfilled) | -4.77% [-20.36%, 11.62%] | $45.33 |
| series | tier2 | 56 | 56 | 0.0561 | 1.19% [-37.79%, 41.31%] | $66.06 | 1.321× | 24.72% | $6.97 | 26 (30 unfilled) | 8.79% [-55.10%, 88.07%] | $62.63 |
| series | tier3 | 5 | 5 | 0.2030 | 33.23% [-72.58%, 150.57%] | $57.27 | 1.145× | 10.00% | $5.02 | 5 (0 unfilled) | 33.23% [-72.58%, 150.57%] | $62.07 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 336 | 336 | 0.0486 | 4.20% [-8.97%, 17.38%] | $66.12 | 1.322× | 67.86% | $16.00 | 179 (157 unfilled) | -4.77% [-20.36%, 11.62%] | $45.33 |
| series | international=0 | 61 | 61 | 0.0682 | 3.81% [-33.43%, 44.48%] | $75.72 | 1.514× | 24.72% | $6.97 | 31 (30 unfilled) | 12.71% [-46.09%, 79.87%] | $78.17 |
| game | all | 215 | 114 | 0.0402 | -13.97% [-26.34%, -0.09%] | $12.88 | 0.258× | 75.20% | $4.49 | 32 (183 unfilled) | -15.41% [-44.91%, 15.97%] | $37.23 |
| game | tier1 | 169 | 88 | 0.0424 | -12.07% [-26.00%, 1.78%] | $17.47 | 0.349× | 67.88% | $4.49 | 25 (144 unfilled) | -11.41% [-44.51%, 23.46%] | $38.46 |
| game | tier2 | 40 | 23 | 0.0332 | -24.06% [-56.21%, 10.03%] | $37.20 | 0.744× | 32.95% | $5.37 | 7 (33 unfilled) | -29.62% [-100.00%, 31.24%] | $48.39 |
| game | tier3 | 6 | 3 | 0.0255 | 0.05% [-47.80%, 51.70%] | $49.84 | 0.997× | 4.78% | $2.78 | 0 (6 unfilled) | — | $50.00 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 169 | 88 | 0.0424 | -12.07% [-26.00%, 1.78%] | $17.47 | 0.349× | 67.88% | $4.49 | 25 (144 unfilled) | -11.41% [-44.51%, 23.46%] | $38.46 |
| game | international=0 | 46 | 26 | 0.0322 | -20.94% [-49.61%, 10.41%] | $37.08 | 0.742× | 33.17% | $5.37 | 7 (39 unfilled) | -29.62% [-100.00%, 31.24%] | $48.39 |
| series+game | all | 612 | 428 | 0.0476 | -2.20% [-12.42%, 7.93%] | $47.05 | 0.941× | 73.02% | $8.96 | 242 (370 unfilled) | -3.92% [-19.30%, 11.96%] | $81.88 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 280 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2025-11 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2025-12 | series | 13 | 1.000000 | 0.000000 | unfitted |
| 2026-01 | series | 79 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 148 | 1.035932 | 0.367192 | fitted |
| 2026-03 | series | 249 | 0.968216 | 0.465253 | fitted |
| 2026-03 | game | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | series | 302 | 0.975887 | 0.642729 | fitted |
| 2026-04 | game | 15 | 1.000000 | 0.000000 | unfitted |
| 2026-05 | series | 379 | 0.900763 | 0.591356 | fitted |
| 2026-05 | game | 132 | 1.128356 | -0.991081 | fitted |
| 2026-06 | series | 544 | 0.927481 | 0.622309 | fitted |
| 2026-06 | game | 330 | 0.978058 | -0.362807 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 473 | 0.619716 | 0.626718 | -0.007002 [-0.017926, 0.002963] | no |
| series | tier1 | 401 | 0.613456 | 0.617017 | -0.003561 [-0.012871, 0.006070] | no |
| series | tier2 | 64 | 0.667252 | 0.679709 | -0.012457 [-0.047260, 0.020855] | no |
| series | tier3 | 8 | 0.553176 | 0.689027 | -0.135850 [-0.493510, 0.086051] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 401 | 0.613456 | 0.617017 | -0.003561 [-0.012871, 0.006070] | no |
| series | international=0 | 72 | 0.654577 | 0.680744 | -0.026167 [-0.076586, 0.017613] | no |
| game | all | 302 | 0.631531 | 0.623361 | 0.008170 [-0.004624, 0.021144] | no |
| game | tier1 | 237 | 0.620720 | 0.611859 | 0.008862 [-0.004106, 0.022369] | no |
| game | tier2 | 56 | 0.683931 | 0.679563 | 0.004368 [-0.031088, 0.042096] | no |
| game | tier3 | 9 | 0.590157 | 0.576544 | 0.013612 [-0.019977, 0.045576] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 237 | 0.620720 | 0.611859 | 0.008862 [-0.004106, 0.022369] | no |
| game | international=0 | 65 | 0.670947 | 0.665299 | 0.005648 [-0.026238, 0.038880] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 172 | 172 | 0.0353 | 4.55% [-16.93%, 26.98%] | $76.17 | 1.523× | 62.49% | $12.42 | 88 (84 unfilled) | 0.98% [-27.36%, 31.28%] | $52.11 |
| series | tier1 | 138 | 138 | 0.0297 | -1.65% [-23.06%, 21.71%] | $48.20 | 0.964× | 60.17% | $8.85 | 69 (69 unfilled) | -12.53% [-37.12%, 13.72%] | $34.79 |
| series | tier2 | 30 | 30 | 0.0406 | 29.27% [-31.25%, 101.09%] | $70.01 | 1.400× | 22.05% | $7.12 | 15 (15 unfilled) | 54.63% [-53.60%, 177.28%] | $64.95 |
| series | tier3 | 4 | 4 | 0.1900 | 31.89% [-100.00%, 174.07%] | $55.81 | 1.116× | 6.63% | $4.55 | 4 (0 unfilled) | 31.89% [-100.00%, 174.07%] | $58.26 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 138 | 138 | 0.0297 | -1.65% [-23.06%, 21.71%] | $48.20 | 0.964× | 60.17% | $8.85 | 69 (69 unfilled) | -12.53% [-37.12%, 13.72%] | $34.79 |
| series | international=0 | 34 | 34 | 0.0582 | 29.58% [-28.53%, 93.60%] | $78.16 | 1.563× | 22.05% | $7.12 | 19 (15 unfilled) | 49.86% [-40.37%, 153.11%] | $76.12 |
| game | all | 117 | 63 | 0.0308 | -14.18% [-33.89%, 7.17%] | $16.35 | 0.327× | 69.72% | $3.78 | 13 (104 unfilled) | 3.69% [-54.23%, 75.19%] | $48.48 |
| game | tier1 | 88 | 47 | 0.0285 | -22.83% [-43.96%, -0.25%] | $17.87 | 0.357× | 69.62% | $3.89 | 10 (78 unfilled) | -27.09% [-79.73%, 41.30%] | $46.81 |
| game | tier2 | 29 | 16 | 0.0377 | 12.18% [-32.14%, 61.58%] | $45.90 | 0.918× | 21.75% | $3.78 | 3 (26 unfilled) | 107.23% [13.80%, 262.84%] | $51.78 |
| game | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 88 | 47 | 0.0285 | -22.83% [-43.96%, -0.25%] | $17.87 | 0.357× | 69.62% | $3.89 | 10 (78 unfilled) | -27.09% [-79.73%, 41.30%] | $46.81 |
| game | international=0 | 29 | 16 | 0.0377 | 12.18% [-32.14%, 61.58%] | $45.90 | 0.918× | 21.75% | $3.78 | 3 (26 unfilled) | 107.23% [13.80%, 262.84%] | $51.78 |
| series+game | all | 289 | 201 | 0.0335 | -3.01% [-16.96%, 11.64%] | $29.63 | 0.593× | 81.60% | $9.67 | 101 (188 unfilled) | 1.33% [-23.38%, 29.14%] | $52.67 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| game | 2026-03 | 15 | 0.731130 | — | 0.669739 | -73.56% (6), $36.97 | — | 3 (3 unfilled) | -47.12% [-100.00%, -20.42%] | $44.21 | — | — | — |
| game | 2026-04 | 117 | 0.670255 | — | 0.651637 | -16.09% (53), $38.53 | — | 13 (40 unfilled) | 10.80% [-36.33%, 54.13%] | $52.26 | — | — | — |
| game | 2026-05 | 198 | 0.668180 | 0.664453 | 0.657045 | -11.34% (100), $28.42 | -6.73% (99), $21.71 | 7 (93 unfilled) | -42.74% [-100.00%, 33.89%] | $44.38 | 9 (90 unfilled) | 30.42% [-38.94%, 119.54%] | $51.44 |
| game | 2026-06 | 104 | 0.555723 | 0.568852 | 0.559231 | -10.30% (56), $40.68 | -54.91% (18), $37.72 | 9 (47 unfilled) | -21.37% [-70.32%, 21.66%] | $45.28 | 4 (14 unfilled) | -55.29% [-100.00%, 81.42%] | $47.13 |
| series | 2025-11 | 13 | 0.486608 | — | 0.588964 | 70.08% (11), $72.06 | — | 10 (1 unfilled) | 39.07% [-22.11%, 117.29%] | $70.40 | — | — | — |
| series | 2025-12 | 66 | 0.656384 | — | 0.640347 | -19.37% (41), $43.00 | — | 36 (5 unfilled) | -18.51% [-52.95%, 23.78%] | $46.18 | — | — | — |
| series | 2026-01 | 69 | 0.519620 | — | 0.506048 | -7.28% (46), $43.96 | — | 24 (22 unfilled) | -24.48% [-63.57%, 21.45%] | $35.16 | — | — | — |
| series | 2026-02 | 101 | 0.662013 | 0.663137 | 0.667211 | 18.87% (66), $43.25 | 11.03% (16), $58.94 | 18 (48 unfilled) | 30.31% [-22.53%, 81.80%] | $66.83 | 4 (12 unfilled) | 25.02% [-100.00%, 150.04%] | $53.33 |
| series | 2026-03 | 53 | 0.637795 | 0.649602 | 0.663787 | 47.54% (23), $83.60 | 35.75% (9), $56.56 | 18 (5 unfilled) | 31.72% [-14.52%, 78.20%] | $65.33 | 7 (2 unfilled) | 20.54% [-54.96%, 102.11%] | $53.41 |
| series | 2026-04 | 77 | 0.686706 | 0.683758 | 0.690287 | 3.38% (50), $79.69 | 28.30% (34), $71.01 | 34 (16 unfilled) | 16.59% [-36.17%, 75.36%] | $82.42 | 21 (13 unfilled) | 56.64% [-20.18%, 142.90%] | $76.25 |
| series | 2026-05 | 165 | 0.621403 | 0.620612 | 0.626943 | 2.68% (102), $68.44 | 5.29% (66), $64.40 | 26 (76 unfilled) | -20.06% [-60.01%, 24.15%] | $35.15 | 21 (45 unfilled) | -24.67% [-73.07%, 27.84%] | $35.55 |
| series | 2026-06 | 77 | 0.477023 | 0.476226 | 0.484035 | -13.32% (58), $29.09 | -21.82% (47), $30.95 | 44 (14 unfilled) | -17.07% [-45.66%, 13.01%] | $35.64 | 35 (12 unfilled) | -23.59% [-58.73%, 14.35%] | $40.75 |

### player_glicko_rw_tier_revert: Kalshi comparison and returns



#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 621 | 0.609789 | 0.613968 | -0.004179 [-0.018948, 0.010186] | no |
| series | tier1 | 528 | 0.604367 | 0.608069 | -0.003702 [-0.017037, 0.009706] | no |
| series | tier2 | 85 | 0.647905 | 0.643551 | 0.004353 [-0.039228, 0.045910] | no |
| series | tier3 | 8 | 0.562664 | 0.689027 | -0.126362 [-0.525966, 0.152407] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 528 | 0.604367 | 0.608069 | -0.003702 [-0.017037, 0.009706] | no |
| series | international=0 | 93 | 0.640572 | 0.647463 | -0.006891 [-0.058986, 0.041349] | no |
| game | all | 434 | 0.644292 | 0.632587 | 0.011705 [-0.000254, 0.024631] | no |
| game | tier1 | 340 | 0.641215 | 0.629029 | 0.012186 [-0.001264, 0.026881] | no |
| game | tier2 | 85 | 0.664571 | 0.652750 | 0.011821 [-0.013668, 0.038043] | no |
| game | tier3 | 9 | 0.568998 | 0.576544 | -0.007546 [-0.074506, 0.057651] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 340 | 0.641215 | 0.629029 | 0.012186 [-0.001264, 0.026881] | no |
| game | international=0 | 94 | 0.655420 | 0.645454 | 0.009966 [-0.014407, 0.035640] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 396 | 396 | 0.0515 | 5.16% [-7.20%, 19.08%] | $84.26 | 1.685× | 69.35% | $16.92 | 210 (186 unfilled) | -2.15% [-18.85%, 15.06%] | $49.50 |
| series | tier1 | 338 | 338 | 0.0480 | 4.83% [-8.45%, 18.27%] | $53.77 | 1.075× | 67.36% | $12.53 | 181 (157 unfilled) | -5.14% [-20.96%, 10.20%] | $34.66 |
| series | tier2 | 53 | 53 | 0.0597 | 4.65% [-35.75%, 51.00%] | $67.76 | 1.355× | 25.13% | $7.42 | 24 (29 unfilled) | 12.93% [-56.14%, 93.34%] | $57.58 |
| series | tier3 | 5 | 5 | 0.2027 | 33.23% [-72.58%, 150.57%] | $57.27 | 1.145× | 10.00% | $5.02 | 5 (0 unfilled) | 33.23% [-72.58%, 150.57%] | $62.07 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 338 | 338 | 0.0480 | 4.83% [-8.45%, 18.27%] | $53.77 | 1.075× | 67.36% | $12.53 | 181 (157 unfilled) | -5.14% [-20.96%, 10.20%] | $34.66 |
| series | international=0 | 58 | 58 | 0.0720 | 7.10% [-30.37%, 48.74%] | $77.64 | 1.553× | 25.13% | $7.42 | 29 (29 unfilled) | 16.41% [-46.56%, 87.55%] | $71.74 |
| game | all | 204 | 111 | 0.0387 | -11.88% [-25.36%, 1.97%] | $11.91 | 0.238× | 77.33% | $4.46 | 33 (171 unfilled) | -28.38% [-55.47%, 0.10%] | $37.98 |
| game | tier1 | 158 | 86 | 0.0404 | -11.98% [-26.96%, 4.02%] | $15.91 | 0.318× | 70.13% | $4.46 | 27 (131 unfilled) | -24.46% [-54.56%, 5.06%] | $40.14 |
| game | tier2 | 41 | 23 | 0.0345 | -11.68% [-48.36%, 26.78%] | $37.65 | 0.753× | 32.68% | $4.96 | 6 (35 unfilled) | -46.01% [-100.00%, 17.40%] | $47.34 |
| game | tier3 | 5 | 2 | 0.0175 | -10.28% [-47.80%, 46.00%] | $49.84 | 0.997× | 4.78% | $3.07 | 0 (5 unfilled) | — | $50.00 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 158 | 86 | 0.0404 | -11.98% [-26.96%, 4.02%] | $15.91 | 0.318× | 70.13% | $4.46 | 27 (131 unfilled) | -24.46% [-54.56%, 5.06%] | $40.14 |
| game | international=0 | 46 | 25 | 0.0327 | -11.53% [-44.26%, 24.20%] | $37.52 | 0.750× | 32.68% | $4.96 | 6 (40 unfilled) | -46.01% [-100.00%, 17.40%] | $47.34 |
| series+game | all | 600 | 413 | 0.0472 | -0.62% [-11.43%, 10.59%] | $40.64 | 0.813× | 73.13% | $10.04 | 243 (357 unfilled) | -5.70% [-20.63%, 9.10%] | $49.70 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 280 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2025-11 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2025-12 | series | 13 | 1.000000 | 0.000000 | unfitted |
| 2026-01 | series | 79 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 148 | 1.038620 | 0.284254 | fitted |
| 2026-03 | series | 249 | 0.978695 | 0.419897 | fitted |
| 2026-03 | game | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | series | 302 | 0.989828 | 0.600828 | fitted |
| 2026-04 | game | 15 | 1.000000 | 0.000000 | unfitted |
| 2026-05 | series | 379 | 0.907572 | 0.539980 | fitted |
| 2026-05 | game | 132 | 1.060490 | -1.076749 | fitted |
| 2026-06 | series | 544 | 0.933294 | 0.617130 | fitted |
| 2026-06 | game | 330 | 0.957777 | -0.328626 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 473 | 0.620093 | 0.626718 | -0.006625 [-0.016921, 0.002667] | no |
| series | tier1 | 401 | 0.613737 | 0.617017 | -0.003280 [-0.011768, 0.005814] | no |
| series | tier2 | 64 | 0.667933 | 0.679709 | -0.011776 [-0.043429, 0.018759] | no |
| series | tier3 | 8 | 0.555967 | 0.689027 | -0.133060 [-0.489131, 0.087395] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 401 | 0.613737 | 0.617017 | -0.003280 [-0.011768, 0.005814] | no |
| series | international=0 | 72 | 0.655492 | 0.680744 | -0.025252 [-0.074808, 0.016329] | no |
| game | all | 302 | 0.632242 | 0.623361 | 0.008881 [-0.004700, 0.022761] | no |
| game | tier1 | 237 | 0.620962 | 0.611859 | 0.009103 [-0.004821, 0.023512] | no |
| game | tier2 | 56 | 0.687490 | 0.679563 | 0.007927 [-0.029424, 0.047781] | no |
| game | tier3 | 9 | 0.585498 | 0.576544 | 0.008954 [-0.017190, 0.036034] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 237 | 0.620962 | 0.611859 | 0.009103 [-0.004821, 0.023512] | no |
| game | international=0 | 65 | 0.673368 | 0.665299 | 0.008069 [-0.024997, 0.043328] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 152 | 152 | 0.0331 | 9.11% [-13.47%, 34.06%] | $61.82 | 1.236× | 63.90% | $10.28 | 81 (71 unfilled) | 2.73% [-26.67%, 36.30%] | $52.09 |
| series | tier1 | 117 | 117 | 0.0282 | 4.07% [-20.10%, 29.43%] | $41.68 | 0.834× | 61.62% | $7.87 | 61 (56 unfilled) | -10.32% [-39.11%, 18.45%] | $37.59 |
| series | tier2 | 31 | 31 | 0.0315 | 25.10% [-35.36%, 93.78%] | $65.25 | 1.305× | 25.95% | $6.59 | 16 (15 unfilled) | 44.97% [-53.09%, 156.80%] | $59.69 |
| series | tier3 | 4 | 4 | 0.1878 | 31.89% [-100.00%, 174.07%] | $56.37 | 1.127× | 6.58% | $4.60 | 4 (0 unfilled) | 31.89% [-100.00%, 174.07%] | $58.81 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 117 | 117 | 0.0282 | 4.07% [-20.10%, 29.43%] | $41.68 | 0.834× | 61.62% | $7.87 | 61 (56 unfilled) | -10.32% [-39.11%, 18.45%] | $37.59 |
| series | international=0 | 35 | 35 | 0.0493 | 25.87% [-29.71%, 88.44%] | $73.53 | 1.471× | 25.95% | $6.59 | 20 (15 unfilled) | 42.36% [-40.84%, 145.42%] | $70.49 |
| game | all | 116 | 64 | 0.0366 | -12.55% [-32.56%, 9.73%] | $17.09 | 0.342× | 69.36% | $3.59 | 12 (104 unfilled) | 33.50% [-23.10%, 98.45%] | $52.31 |
| game | tier1 | 85 | 47 | 0.0353 | -21.51% [-42.88%, 1.12%] | $18.02 | 0.360× | 69.39% | $3.75 | 9 (76 unfilled) | 9.13% [-53.14%, 67.49%] | $49.94 |
| game | tier2 | 31 | 17 | 0.0401 | 12.16% [-28.99%, 63.61%] | $47.38 | 0.948× | 22.25% | $3.59 | 3 (28 unfilled) | 107.23% [13.80%, 262.84%] | $52.39 |
| game | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 85 | 47 | 0.0353 | -21.51% [-42.88%, 1.12%] | $18.02 | 0.360× | 69.39% | $3.75 | 9 (76 unfilled) | 9.13% [-53.14%, 67.49%] | $49.94 |
| game | international=0 | 31 | 17 | 0.0401 | 12.16% [-28.99%, 63.61%] | $47.38 | 0.948× | 22.25% | $3.59 | 3 (28 unfilled) | 107.23% [13.80%, 262.84%] | $52.39 |
| series+game | all | 268 | 185 | 0.0346 | -0.24% [-14.32%, 14.71%] | $26.41 | 0.528× | 81.48% | $8.39 | 93 (175 unfilled) | 6.68% [-20.14%, 36.18%] | $56.07 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| game | 2026-03 | 15 | 0.723979 | — | 0.669739 | -60.40% (4), $40.68 | — | 3 (1 unfilled) | -47.12% [-100.00%, -20.42%] | $45.20 | — | — | — |
| game | 2026-04 | 117 | 0.670035 | — | 0.651637 | -15.77% (42), $37.64 | — | 12 (30 unfilled) | 5.96% [-43.08%, 53.66%] | $51.74 | — | — | — |
| game | 2026-05 | 198 | 0.666538 | 0.666801 | 0.657045 | -3.93% (103), $28.06 | -7.71% (108), $19.38 | 7 (96 unfilled) | -70.81% [-100.00%, -12.20%] | $42.67 | 9 (99 unfilled) | 58.51% [-1.06%, 130.27%] | $53.53 |
| game | 2026-06 | 104 | 0.561484 | 0.566446 | 0.559231 | -20.23% (55), $35.47 | -77.48% (8), $44.09 | 11 (44 unfilled) | -33.55% [-78.57%, 9.12%] | $47.53 | 3 (5 unfilled) | -40.29% [-100.00%, 81.42%] | $48.85 |
| series | 2025-11 | 13 | 0.492040 | — | 0.588964 | 69.78% (11), $78.46 | — | 10 (1 unfilled) | 38.80% [-21.65%, 115.28%] | $73.15 | — | — | — |
| series | 2025-12 | 66 | 0.660436 | — | 0.640347 | -16.84% (42), $41.50 | — | 38 (4 unfilled) | -17.87% [-52.64%, 19.17%] | $43.62 | — | — | — |
| series | 2026-01 | 69 | 0.520734 | — | 0.506048 | -2.57% (47), $41.56 | — | 24 (23 unfilled) | -29.29% [-69.14%, 17.49%] | $28.10 | — | — | — |
| series | 2026-02 | 101 | 0.661449 | 0.663807 | 0.667211 | 13.24% (67), $41.20 | 86.07% (8), $57.56 | 18 (49 unfilled) | 27.10% [-27.72%, 79.57%] | $62.04 | 2 (6 unfilled) | 150.04% [92.31%, 207.22%] | $52.23 |
| series | 2026-03 | 53 | 0.638353 | 0.651275 | 0.663787 | 44.18% (23), $74.60 | 18.50% (8), $55.31 | 18 (5 unfilled) | 27.40% [-16.91%, 72.06%] | $60.01 | 6 (2 unfilled) | -5.00% [-74.92%, 78.62%] | $53.49 |
| series | 2026-04 | 77 | 0.687782 | 0.685066 | 0.690287 | 3.40% (50), $73.60 | 24.69% (35), $61.04 | 34 (16 unfilled) | 16.62% [-35.67%, 75.10%] | $79.94 | 23 (12 unfilled) | 43.02% [-28.88%, 126.01%] | $69.83 |
| series | 2026-05 | 165 | 0.619111 | 0.619338 | 0.626943 | 7.55% (97), $81.56 | 14.79% (56), $68.70 | 24 (73 unfilled) | -13.40% [-56.88%, 33.49%] | $39.74 | 16 (40 unfilled) | -8.67% [-66.65%, 55.67%] | $39.93 |
| series | 2026-06 | 77 | 0.480667 | 0.477934 | 0.484035 | -11.80% (59), $26.13 | -25.39% (45), $28.79 | 44 (15 unfilled) | -15.41% [-45.43%, 14.56%] | $35.09 | 34 (11 unfilled) | -26.42% [-61.59%, 10.57%] | $40.58 |

### player_glicko+none: Kalshi comparison and returns

none

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 621 | 0.613181 | 0.613968 | -0.000787 [-0.016467, 0.013860] | no |
| series | tier1 | 528 | 0.608352 | 0.608069 | 0.000284 [-0.013848, 0.014804] | no |
| series | tier2 | 85 | 0.644624 | 0.643551 | 0.001073 [-0.042546, 0.042379] | no |
| series | tier3 | 8 | 0.597808 | 0.689027 | -0.091218 [-0.406440, 0.132080] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 528 | 0.608352 | 0.608069 | 0.000284 [-0.013848, 0.014804] | no |
| series | international=0 | 93 | 0.640597 | 0.647463 | -0.006866 [-0.054606, 0.038431] | no |
| game | all | 434 | 0.642801 | 0.632587 | 0.010214 [-0.003107, 0.023865] | no |
| game | tier1 | 340 | 0.640137 | 0.629029 | 0.011108 [-0.004773, 0.027518] | no |
| game | tier2 | 85 | 0.660177 | 0.652750 | 0.007427 [-0.019236, 0.035024] | no |
| game | tier3 | 9 | 0.579318 | 0.576544 | 0.002773 [-0.073758, 0.063999] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 340 | 0.640137 | 0.629029 | 0.011108 [-0.004773, 0.027518] | no |
| game | international=0 | 94 | 0.652435 | 0.645454 | 0.006982 [-0.019108, 0.032993] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 400 | 400 | 0.0554 | 2.51% [-10.62%, 15.81%] | $61.17 | 1.223× | 74.94% | $15.97 | 215 (185 unfilled) | 0.49% [-16.38%, 17.61%] | $48.14 |
| series | tier1 | 341 | 341 | 0.0531 | 1.35% [-11.86%, 14.62%] | $39.20 | 0.784× | 74.16% | $11.53 | 185 (156 unfilled) | -2.08% [-18.58%, 15.62%] | $28.27 |
| series | tier2 | 53 | 53 | 0.0614 | 6.89% [-33.17%, 53.54%] | $69.35 | 1.387× | 34.43% | $6.14 | 24 (29 unfilled) | 12.88% [-61.09%, 89.48%] | $73.49 |
| series | tier3 | 6 | 6 | 0.1325 | 29.69% [-73.50%, 147.49%] | $56.13 | 1.123× | 5.79% | $4.88 | 6 (0 unfilled) | 29.69% [-73.50%, 147.49%] | $56.82 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 341 | 341 | 0.0531 | 1.35% [-11.86%, 14.62%] | $39.20 | 0.784× | 74.16% | $11.53 | 185 (156 unfilled) | -2.08% [-18.58%, 15.62%] | $28.27 |
| series | international=0 | 59 | 59 | 0.0687 | 9.21% [-28.18%, 49.54%] | $77.84 | 1.557× | 34.43% | $6.78 | 30 (29 unfilled) | 16.23% [-45.17%, 87.35%] | $84.22 |
| game | all | 221 | 119 | 0.0467 | -6.61% [-20.19%, 6.76%] | $15.58 | 0.312× | 71.01% | $4.33 | 33 (188 unfilled) | -21.16% [-49.78%, 7.62%] | $41.30 |
| game | tier1 | 173 | 92 | 0.0495 | -6.51% [-21.96%, 9.78%] | $18.71 | 0.374× | 65.37% | $4.33 | 27 (146 unfilled) | -21.94% [-53.23%, 11.22%] | $40.57 |
| game | tier2 | 41 | 23 | 0.0420 | -5.71% [-33.71%, 23.46%] | $41.09 | 0.822× | 24.83% | $4.74 | 5 (36 unfilled) | -0.90% [-72.65%, 70.30%] | $51.22 |
| game | tier3 | 7 | 4 | 0.0043 | -14.48% [-62.62%, 47.90%] | $51.09 | 1.022× | 0.37% | $2.00 | 1 (6 unfilled) | -100.00% [-100.00%, -100.00%] | $49.60 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 173 | 92 | 0.0495 | -6.51% [-21.96%, 9.78%] | $18.71 | 0.374× | 65.37% | $4.33 | 27 (146 unfilled) | -21.94% [-53.23%, 11.22%] | $40.57 |
| game | international=0 | 48 | 27 | 0.0365 | -6.99% [-31.16%, 19.57%] | $41.99 | 0.840× | 24.83% | $4.74 | 6 (42 unfilled) | -17.63% [-77.39%, 46.96%] | $50.81 |
| series+game | all | 621 | 439 | 0.0523 | -0.72% [-11.40%, 9.90%] | $25.27 | 0.505× | 82.43% | $8.80 | 248 (373 unfilled) | -2.37% [-18.49%, 14.14%] | $56.17 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 280 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2025-11 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2025-12 | series | 13 | 1.000000 | 0.000000 | unfitted |
| 2026-01 | series | 79 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 148 | 1.045798 | 0.289432 | fitted |
| 2026-03 | series | 249 | 0.975290 | 0.342906 | fitted |
| 2026-03 | game | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | series | 302 | 0.985509 | 0.463294 | fitted |
| 2026-04 | game | 15 | 1.000000 | 0.000000 | unfitted |
| 2026-05 | series | 379 | 0.908484 | 0.443668 | fitted |
| 2026-05 | game | 132 | 1.078955 | -0.585585 | fitted |
| 2026-06 | series | 544 | 0.935218 | 0.509364 | fitted |
| 2026-06 | game | 330 | 0.950206 | -0.102799 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 473 | 0.622525 | 0.626718 | -0.004193 [-0.012424, 0.003573] | no |
| series | tier1 | 401 | 0.615513 | 0.617017 | -0.001505 [-0.009720, 0.006497] | no |
| series | tier2 | 64 | 0.666762 | 0.679709 | -0.012947 [-0.039881, 0.012471] | no |
| series | tier3 | 8 | 0.620129 | 0.689027 | -0.068898 [-0.269667, 0.066224] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 401 | 0.615513 | 0.617017 | -0.001505 [-0.009720, 0.006497] | no |
| series | international=0 | 72 | 0.661581 | 0.680744 | -0.019164 [-0.050868, 0.010850] | no |
| game | all | 302 | 0.628878 | 0.623361 | 0.005517 [-0.002462, 0.013910] | no |
| game | tier1 | 237 | 0.616969 | 0.611859 | 0.005110 [-0.003965, 0.014664] | no |
| game | tier2 | 56 | 0.686895 | 0.679563 | 0.007332 [-0.011406, 0.027506] | no |
| game | tier3 | 9 | 0.581502 | 0.576544 | 0.004958 [-0.005511, 0.018043] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 237 | 0.616969 | 0.611859 | 0.005110 [-0.003965, 0.014664] | no |
| game | international=0 | 65 | 0.672302 | 0.665299 | 0.007003 [-0.009603, 0.024804] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 138 | 138 | 0.0247 | 11.82% [-13.52%, 39.29%] | $88.24 | 1.765× | 46.58% | $10.69 | 71 (67 unfilled) | 12.31% [-21.27%, 50.61%] | $74.91 |
| series | tier1 | 106 | 106 | 0.0230 | 0.63% [-25.63%, 28.44%] | $57.91 | 1.158× | 46.62% | $7.89 | 53 (53 unfilled) | -13.78% [-43.27%, 16.39%] | $50.47 |
| series | tier2 | 28 | 28 | 0.0218 | 51.16% [-18.49%, 126.32%] | $67.60 | 1.352× | 16.15% | $5.61 | 14 (14 unfilled) | 105.10% [-20.72%, 241.46%] | $64.56 |
| series | tier3 | 4 | 4 | 0.0898 | 31.26% [-100.00%, 172.78%] | $56.25 | 1.125× | 4.61% | $4.59 | 4 (0 unfilled) | 31.26% [-100.00%, 172.78%] | $56.25 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 106 | 106 | 0.0230 | 0.63% [-25.63%, 28.44%] | $57.91 | 1.158× | 46.62% | $7.89 | 53 (53 unfilled) | -13.78% [-43.27%, 16.39%] | $50.47 |
| series | international=0 | 32 | 32 | 0.0303 | 48.68% [-19.76%, 117.11%] | $76.02 | 1.520× | 16.15% | $6.19 | 18 (14 unfilled) | 88.73% [-11.84%, 205.50%] | $72.62 |
| game | all | 54 | 30 | 0.0214 | -2.68% [-28.90%, 24.70%] | $34.20 | 0.684× | 41.90% | $4.73 | 4 (50 unfilled) | 38.11% [11.81%, 96.23%] | $50.56 |
| game | tier1 | 39 | 21 | 0.0210 | -4.68% [-37.92%, 29.82%] | $35.26 | 0.705× | 41.91% | $2.76 | 4 (35 unfilled) | 38.11% [11.81%, 96.23%] | $50.56 |
| game | tier2 | 15 | 9 | 0.0225 | 2.52% [-46.59%, 56.49%] | $48.47 | 0.969× | 12.07% | $4.73 | 0 (15 unfilled) | — | $50.00 |
| game | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 39 | 21 | 0.0210 | -4.68% [-37.92%, 29.82%] | $35.26 | 0.705× | 41.91% | $2.76 | 4 (35 unfilled) | 38.11% [11.81%, 96.23%] | $50.56 |
| game | international=0 | 15 | 9 | 0.0225 | 2.52% [-46.59%, 56.49%] | $48.47 | 0.969× | 12.07% | $4.73 | 0 (15 unfilled) | — | $50.00 |
| series+game | all | 192 | 150 | 0.0237 | 7.76% [-11.21%, 26.06%] | $71.22 | 1.424× | 46.50% | $8.14 | 75 (117 unfilled) | 13.67% [-18.42%, 50.24%] | $74.17 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| game | 2026-03 | 15 | 0.744029 | — | 0.669739 | -73.56% (6), $36.02 | — | 3 (3 unfilled) | -47.12% [-100.00%, -20.42%] | $44.58 | — | — | — |
| game | 2026-04 | 117 | 0.666715 | — | 0.651637 | -3.68% (47), $45.08 | — | 13 (34 unfilled) | 10.80% [-36.33%, 54.13%] | $55.11 | — | — | — |
| game | 2026-05 | 198 | 0.665984 | 0.662500 | 0.657045 | -3.27% (105), $25.77 | -2.68% (54), $34.20 | 5 (100 unfilled) | -58.93% [-100.00%, 22.99%] | $43.57 | 4 (50 unfilled) | 38.11% [11.81%, 96.23%] | $50.56 |
| game | 2026-06 | 104 | 0.557159 | 0.564868 | 0.559231 | -7.99% (63), $47.55 | — (0), $50.00 | 12 (51 unfilled) | -33.49% [-79.73%, 17.70%] | $48.04 | 0 (0 unfilled) | — | $50.00 |
| series | 2025-11 | 13 | 0.473208 | — | 0.588964 | 70.08% (11), $81.85 | — | 10 (1 unfilled) | 39.07% [-22.11%, 117.29%] | $77.25 | — | — | — |
| series | 2025-12 | 66 | 0.663611 | — | 0.640347 | -6.38% (42), $35.95 | — | 38 (4 unfilled) | -2.53% [-42.39%, 40.53%] | $37.49 | — | — | — |
| series | 2026-01 | 69 | 0.524075 | — | 0.506048 | -17.51% (48), $36.13 | — | 24 (24 unfilled) | -34.81% [-75.07%, 10.97%] | $32.44 | — | — | — |
| series | 2026-02 | 101 | 0.666687 | 0.665014 | 0.667211 | 10.59% (70), $46.75 | 61.07% (10), $58.17 | 21 (49 unfilled) | 20.91% [-26.66%, 71.14%] | $54.98 | 2 (8 unfilled) | 150.04% [92.31%, 207.22%] | $53.32 |
| series | 2026-03 | 53 | 0.645747 | 0.655848 | 0.663787 | 22.43% (26), $69.13 | -6.84% (5), $52.17 | 22 (4 unfilled) | 18.60% [-28.44%, 66.79%] | $62.12 | 4 (1 unfilled) | -36.89% [-100.00%, 88.42%] | $51.68 |
| series | 2026-04 | 77 | 0.685434 | 0.683528 | 0.690287 | 10.64% (51), $73.77 | 40.73% (26), $60.48 | 34 (17 unfilled) | 26.69% [-27.29%, 88.37%] | $83.12 | 17 (9 unfilled) | 74.29% [-15.16%, 173.89%] | $71.32 |
| series | 2026-05 | 165 | 0.622328 | 0.621061 | 0.626943 | 4.67% (96), $70.68 | 19.06% (54), $75.49 | 24 (72 unfilled) | -15.79% [-56.90%, 28.35%] | $37.47 | 16 (38 unfilled) | 9.73% [-62.53%, 98.51%] | $44.62 |
| series | 2026-06 | 77 | 0.488984 | 0.485991 | 0.484035 | -17.18% (56), $26.49 | -24.00% (43), $39.61 | 42 (14 unfilled) | -17.23% [-49.86%, 17.83%] | $35.86 | 32 (11 unfilled) | -21.80% [-58.36%, 17.25%] | $51.58 |

### player_glicko+regional: Kalshi comparison and returns

regional: rows=7157, ridge=4, s=0.862877, effects: EU=0.249647, CIS=0.287516, NA=-0.0818407, SA=-0.0387808, AS=0.152135, OCE=-0.155864, AF=-0.412812

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 621 | 0.611728 | 0.613968 | -0.002240 [-0.017570, 0.012320] | no |
| series | tier1 | 528 | 0.606806 | 0.608069 | -0.001263 [-0.015215, 0.012752] | no |
| series | tier2 | 85 | 0.643601 | 0.643551 | 0.000050 [-0.044612, 0.041638] | no |
| series | tier3 | 8 | 0.597938 | 0.689027 | -0.091088 [-0.407174, 0.133237] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 528 | 0.606806 | 0.608069 | -0.001263 [-0.015215, 0.012752] | no |
| series | international=0 | 93 | 0.639673 | 0.647463 | -0.007790 [-0.055934, 0.038515] | no |
| game | all | 434 | 0.640329 | 0.632587 | 0.007743 [-0.005247, 0.021069] | no |
| game | tier1 | 340 | 0.636987 | 0.629029 | 0.007957 [-0.006956, 0.024284] | no |
| game | tier2 | 85 | 0.660161 | 0.652750 | 0.007410 [-0.020059, 0.034915] | no |
| game | tier3 | 9 | 0.579318 | 0.576544 | 0.002773 [-0.073758, 0.063999] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 340 | 0.636987 | 0.629029 | 0.007957 [-0.006956, 0.024284] | no |
| game | international=0 | 94 | 0.652420 | 0.645454 | 0.006967 [-0.018971, 0.034078] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 398 | 398 | 0.0544 | -1.33% [-13.69%, 11.06%] | $60.49 | 1.210× | 70.22% | $12.20 | 210 (188 unfilled) | -4.79% [-21.16%, 12.72%] | $49.29 |
| series | tier1 | 335 | 335 | 0.0520 | -3.44% [-16.19%, 9.82%] | $37.47 | 0.749× | 66.20% | $8.37 | 179 (156 unfilled) | -8.84% [-25.26%, 8.13%] | $28.78 |
| series | tier2 | 57 | 57 | 0.0599 | 7.73% [-31.39%, 50.19%] | $72.95 | 1.459× | 35.23% | $6.47 | 25 (32 unfilled) | 15.74% [-49.30%, 93.49%] | $73.31 |
| series | tier3 | 6 | 6 | 0.1336 | 29.69% [-73.50%, 147.49%] | $55.08 | 1.102× | 6.13% | $4.82 | 6 (0 unfilled) | 29.69% [-73.50%, 147.49%] | $56.63 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 335 | 335 | 0.0520 | -3.44% [-16.19%, 9.82%] | $37.47 | 0.749× | 66.20% | $8.37 | 179 (156 unfilled) | -8.84% [-25.26%, 8.13%] | $28.78 |
| series | international=0 | 63 | 63 | 0.0669 | 9.82% [-26.55%, 47.59%] | $80.42 | 1.608× | 35.23% | $7.03 | 31 (32 unfilled) | 18.43% [-44.57%, 87.71%] | $83.70 |
| game | all | 221 | 122 | 0.0419 | -2.50% [-15.11%, 11.80%] | $25.31 | 0.506× | 56.64% | $4.47 | 33 (188 unfilled) | -26.22% [-54.50%, 3.06%] | $38.04 |
| game | tier1 | 170 | 92 | 0.0444 | -1.74% [-17.47%, 14.36%] | $29.80 | 0.596× | 47.98% | $4.47 | 27 (143 unfilled) | -28.12% [-59.65%, 4.86%] | $37.42 |
| game | tier2 | 44 | 26 | 0.0381 | -3.54% [-31.90%, 23.97%] | $41.73 | 0.835× | 25.52% | $4.75 | 5 (39 unfilled) | -0.90% [-72.65%, 70.30%] | $51.22 |
| game | tier3 | 7 | 4 | 0.0043 | -14.48% [-62.62%, 47.90%] | $51.09 | 1.022× | 0.37% | $2.00 | 1 (6 unfilled) | -100.00% [-100.00%, -100.00%] | $49.60 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 170 | 92 | 0.0444 | -1.74% [-17.47%, 14.36%] | $29.80 | 0.596× | 47.98% | $4.47 | 27 (143 unfilled) | -28.12% [-59.65%, 4.86%] | $37.42 |
| game | international=0 | 51 | 30 | 0.0335 | -5.04% [-29.60%, 20.09%] | $42.64 | 0.853× | 25.52% | $4.75 | 6 (45 unfilled) | -17.63% [-77.39%, 46.96%] | $50.81 |
| series+game | all | 619 | 437 | 0.0499 | -1.75% [-12.36%, 9.74%] | $33.38 | 0.668× | 71.06% | $7.65 | 243 (376 unfilled) | -7.69% [-22.24%, 7.74%] | $50.50 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 280 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2025-11 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2025-12 | series | 13 | 1.000000 | 0.000000 | unfitted |
| 2026-01 | series | 79 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 148 | 1.043697 | 0.237248 | fitted |
| 2026-03 | series | 249 | 0.971198 | 0.283183 | fitted |
| 2026-03 | game | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | series | 302 | 0.982806 | 0.407550 | fitted |
| 2026-04 | game | 15 | 1.000000 | 0.000000 | unfitted |
| 2026-05 | series | 379 | 0.900486 | 0.380284 | fitted |
| 2026-05 | game | 132 | 1.105102 | -0.648709 | fitted |
| 2026-06 | series | 544 | 0.948042 | 0.553018 | fitted |
| 2026-06 | game | 330 | 0.939530 | -0.017940 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 473 | 0.621794 | 0.626718 | -0.004924 [-0.012835, 0.002522] | no |
| series | tier1 | 401 | 0.614771 | 0.617017 | -0.002247 [-0.009632, 0.005143] | no |
| series | tier2 | 64 | 0.666454 | 0.679709 | -0.013255 [-0.038263, 0.010574] | no |
| series | tier3 | 8 | 0.616543 | 0.689027 | -0.072483 [-0.286236, 0.070619] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 401 | 0.614771 | 0.617017 | -0.002247 [-0.009632, 0.005143] | no |
| series | international=0 | 72 | 0.660909 | 0.680744 | -0.019836 [-0.051882, 0.008464] | no |
| game | all | 302 | 0.630188 | 0.623361 | 0.006827 [-0.001599, 0.016064] | no |
| game | tier1 | 237 | 0.618401 | 0.611859 | 0.006542 [-0.002974, 0.017376] | no |
| game | tier2 | 56 | 0.687781 | 0.679563 | 0.008218 [-0.012778, 0.030645] | no |
| game | tier3 | 9 | 0.582233 | 0.576544 | 0.005688 [-0.003033, 0.013285] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 237 | 0.618401 | 0.611859 | 0.006542 [-0.002974, 0.017376] | no |
| game | international=0 | 65 | 0.673167 | 0.665299 | 0.007868 [-0.010954, 0.027835] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 116 | 116 | 0.0249 | 24.19% [-4.62%, 55.94%] | $84.37 | 1.687× | 41.23% | $8.83 | 62 (54 unfilled) | 25.41% [-12.76%, 66.37%] | $77.34 |
| series | tier1 | 89 | 89 | 0.0229 | 11.92% [-17.45%, 43.80%] | $55.37 | 1.107× | 41.32% | $6.56 | 44 (45 unfilled) | -0.61% [-33.22%, 35.24%] | $53.98 |
| series | tier2 | 23 | 23 | 0.0199 | 70.27% [-9.46%, 160.10%] | $67.18 | 1.344× | 12.53% | $5.67 | 14 (9 unfilled) | 105.10% [-20.72%, 241.46%] | $62.26 |
| series | tier3 | 4 | 4 | 0.0984 | 31.26% [-100.00%, 172.78%] | $56.53 | 1.131× | 4.95% | $4.61 | 4 (0 unfilled) | 31.26% [-100.00%, 172.78%] | $56.53 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 89 | 89 | 0.0229 | 11.92% [-17.45%, 43.80%] | $55.37 | 1.107× | 41.32% | $6.56 | 44 (45 unfilled) | -0.61% [-33.22%, 35.24%] | $53.98 |
| series | international=0 | 27 | 27 | 0.0316 | 64.49% [-9.82%, 140.17%] | $75.92 | 1.518× | 12.53% | $6.19 | 18 (9 unfilled) | 88.73% [-11.84%, 205.50%] | $70.39 |
| game | all | 53 | 28 | 0.0270 | -8.00% [-33.82%, 19.97%] | $31.78 | 0.636× | 47.24% | $4.25 | 5 (48 unfilled) | 33.34% [12.46%, 76.07%] | $51.68 |
| game | tier1 | 38 | 20 | 0.0264 | -8.81% [-40.25%, 24.50%] | $33.58 | 0.672× | 47.23% | $2.83 | 4 (34 unfilled) | 38.11% [11.81%, 96.23%] | $51.63 |
| game | tier2 | 15 | 8 | 0.0286 | -5.92% [-55.03%, 40.96%] | $47.36 | 0.947× | 17.10% | $4.25 | 1 (14 unfilled) | 13.80% [13.80%, 13.80%] | $50.05 |
| game | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 38 | 20 | 0.0264 | -8.81% [-40.25%, 24.50%] | $33.58 | 0.672× | 47.23% | $2.83 | 4 (34 unfilled) | 38.11% [11.81%, 96.23%] | $51.63 |
| game | international=0 | 15 | 8 | 0.0286 | -5.92% [-55.03%, 40.96%] | $47.36 | 0.947× | 17.10% | $4.25 | 1 (14 unfilled) | 13.80% [13.80%, 13.80%] | $50.05 |
| series+game | all | 169 | 126 | 0.0255 | 14.17% [-5.31%, 35.04%] | $50.77 | 1.015× | 53.60% | $5.41 | 67 (102 unfilled) | 26.00% [-9.27%, 64.39%] | $78.74 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| game | 2026-03 | 15 | 0.720430 | — | 0.669739 | -60.40% (4), $40.13 | — | 3 (1 unfilled) | -47.12% [-100.00%, -20.42%] | $44.60 | — | — | — |
| game | 2026-04 | 117 | 0.667295 | — | 0.651637 | -1.49% (53), $46.95 | — | 13 (40 unfilled) | -2.08% [-48.17%, 44.36%] | $51.76 | — | — | — |
| game | 2026-05 | 198 | 0.662812 | 0.664895 | 0.657045 | 1.68% (102), $33.34 | -8.00% (53), $31.78 | 5 (97 unfilled) | -58.93% [-100.00%, 22.99%] | $42.73 | 5 (48 unfilled) | 33.34% [12.46%, 76.07%] | $51.68 |
| game | 2026-06 | 104 | 0.555637 | 0.564113 | 0.559231 | -6.51% (62), $50.78 | — (0), $50.00 | 12 (50 unfilled) | -33.49% [-79.73%, 17.70%] | $48.04 | 0 (0 unfilled) | — | $50.00 |
| series | 2025-11 | 13 | 0.475355 | — | 0.588964 | 70.08% (11), $85.84 | — | 10 (1 unfilled) | 39.07% [-22.11%, 117.29%] | $76.56 | — | — | — |
| series | 2025-12 | 66 | 0.667656 | — | 0.640347 | -15.45% (44), $29.09 | — | 40 (4 unfilled) | -12.70% [-48.68%, 27.79%] | $30.71 | — | — | — |
| series | 2026-01 | 69 | 0.524336 | — | 0.506048 | -18.63% (50), $34.08 | — | 24 (26 unfilled) | -34.81% [-75.07%, 10.97%] | $32.32 | — | — | — |
| series | 2026-02 | 101 | 0.668532 | 0.665838 | 0.667211 | 8.38% (63), $39.51 | 120.00% (6), $53.30 | 17 (46 unfilled) | 15.46% [-38.42%, 72.30%] | $54.53 | 2 (4 unfilled) | 150.04% [92.31%, 207.22%] | $51.42 |
| series | 2026-03 | 53 | 0.645844 | 0.657123 | 0.663787 | 13.19% (24), $67.74 | 150.63% (1), $52.15 | 20 (4 unfilled) | 7.13% [-40.42%, 56.30%] | $57.69 | 1 (0 unfilled) | 150.63% [150.63%, 150.63%] | $52.15 |
| series | 2026-04 | 77 | 0.687122 | 0.684865 | 0.690287 | 4.47% (49), $80.73 | 75.24% (17), $59.53 | 32 (17 unfilled) | 18.27% [-38.35%, 78.72%] | $92.46 | 12 (5 unfilled) | 130.49% [19.59%, 255.90%] | $66.33 |
| series | 2026-05 | 165 | 0.614782 | 0.618941 | 0.626943 | 1.62% (99), $95.51 | 37.11% (47), $70.45 | 25 (74 unfilled) | -17.88% [-58.27%, 27.95%] | $45.09 | 15 (32 unfilled) | 17.03% [-62.23%, 112.82%] | $46.45 |
| series | 2026-06 | 77 | 0.485196 | 0.482744 | 0.484035 | -15.60% (58), $26.75 | -24.20% (45), $45.02 | 42 (16 unfilled) | -14.05% [-46.60%, 20.19%] | $36.20 | 32 (13 unfilled) | -21.78% [-56.91%, 18.10%] | $56.77 |

### player_glicko+calibration: Kalshi comparison and returns

calibration: ridge=4; tier1/online=0: rows=3058, T=0.7744; tier1/online=1: rows=11009, T=1.1034; tier2/online=0: rows=623, T=0.8106; tier2/online=1: rows=3405, T=1.0072; tier3/online=0: rows=2386, T=1.0447; tier3/online=1: rows=17650, T=0.8844; unknown/online=0: rows=7, T=1.0000

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 621 | 0.610016 | 0.613968 | -0.003952 [-0.019595, 0.010863] | no |
| series | tier1 | 528 | 0.604470 | 0.608069 | -0.003599 [-0.017828, 0.011698] | no |
| series | tier2 | 85 | 0.645455 | 0.643551 | 0.001904 [-0.041045, 0.042703] | no |
| series | tier3 | 8 | 0.599547 | 0.689027 | -0.089480 [-0.395488, 0.128892] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 528 | 0.604470 | 0.608069 | -0.003599 [-0.017828, 0.011698] | no |
| series | international=0 | 93 | 0.641506 | 0.647463 | -0.005957 [-0.052512, 0.039026] | no |
| game | all | 434 | 0.640608 | 0.632587 | 0.008021 [-0.005806, 0.022109] | no |
| game | tier1 | 340 | 0.637052 | 0.629029 | 0.008022 [-0.008178, 0.025109] | no |
| game | tier2 | 85 | 0.660390 | 0.652750 | 0.007640 [-0.019096, 0.035663] | no |
| game | tier3 | 9 | 0.588114 | 0.576544 | 0.011569 [-0.045514, 0.057235] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 340 | 0.637052 | 0.629029 | 0.008022 [-0.008178, 0.025109] | no |
| game | international=0 | 94 | 0.653470 | 0.645454 | 0.008016 [-0.017754, 0.034081] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 402 | 402 | 0.0553 | 6.60% [-6.52%, 19.39%] | $249.38 | 4.988× | 65.35% | $28.37 | 219 (183 unfilled) | 2.89% [-14.35%, 20.22%] | $78.83 |
| series | tier1 | 342 | 342 | 0.0534 | 5.14% [-8.13%, 19.05%] | $166.55 | 3.331× | 65.36% | $22.26 | 190 (152 unfilled) | -0.58% [-17.52%, 17.52%] | $46.56 |
| series | tier2 | 55 | 55 | 0.0581 | 11.19% [-27.81%, 55.38%] | $63.52 | 1.270× | 35.05% | $5.83 | 24 (31 unfilled) | 19.27% [-48.61%, 97.92%] | $69.42 |
| series | tier3 | 5 | 5 | 0.1545 | 55.13% [-68.25%, 178.65%] | $58.92 | 1.178× | 4.14% | $5.04 | 5 (0 unfilled) | 55.13% [-68.25%, 178.65%] | $58.92 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 342 | 342 | 0.0534 | 5.14% [-8.13%, 19.05%] | $166.55 | 3.331× | 65.36% | $22.26 | 190 (152 unfilled) | -0.58% [-17.52%, 17.52%] | $46.56 |
| series | international=0 | 60 | 60 | 0.0662 | 14.87% [-20.66%, 61.04%] | $74.84 | 1.497× | 35.05% | $6.40 | 29 (31 unfilled) | 25.46% [-38.25%, 96.01%] | $81.81 |
| game | all | 218 | 115 | 0.0502 | -8.68% [-20.71%, 3.66%] | $14.98 | 0.300× | 70.09% | $4.75 | 26 (192 unfilled) | -6.20% [-38.40%, 27.65%] | $42.80 |
| game | tier1 | 175 | 91 | 0.0525 | -8.32% [-21.28%, 5.02%] | $18.66 | 0.373× | 63.67% | $4.75 | 19 (156 unfilled) | 2.38% [-33.21%, 40.24%] | $42.69 |
| game | tier2 | 41 | 23 | 0.0428 | -5.71% [-33.71%, 23.46%] | $41.35 | 0.827× | 24.34% | $4.75 | 5 (36 unfilled) | -0.90% [-72.65%, 70.30%] | $51.22 |
| game | tier3 | 2 | 1 | 0.0061 | -100.00% [-100.00%, -100.00%] | $48.91 | 0.978× | 2.18% | $0.95 | 2 (0 unfilled) | -100.00% [-100.00%, -100.00%] | $48.91 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 175 | 91 | 0.0525 | -8.32% [-21.28%, 5.02%] | $18.66 | 0.373× | 63.67% | $4.75 | 19 (156 unfilled) | 2.38% [-33.21%, 40.24%] | $42.69 |
| game | international=0 | 43 | 24 | 0.0411 | -10.14% [-36.71%, 18.66%] | $40.45 | 0.809× | 25.99% | $4.75 | 7 (36 unfilled) | -29.43% [-83.05%, 45.19%] | $50.10 |
| series+game | all | 620 | 432 | 0.0535 | 1.25% [-8.57%, 11.87%] | $111.61 | 2.232× | 76.21% | $19.62 | 245 (375 unfilled) | 1.93% [-13.70%, 17.81%] | $79.20 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 280 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2025-11 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2025-12 | series | 13 | 1.000000 | 0.000000 | unfitted |
| 2026-01 | series | 79 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 148 | 1.019221 | 0.197060 | fitted |
| 2026-03 | series | 249 | 0.968828 | 0.364692 | fitted |
| 2026-03 | game | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | series | 302 | 0.980784 | 0.452553 | fitted |
| 2026-04 | game | 15 | 1.000000 | 0.000000 | unfitted |
| 2026-05 | series | 379 | 0.912207 | 0.454278 | fitted |
| 2026-05 | game | 132 | 0.988988 | -0.433584 | fitted |
| 2026-06 | series | 544 | 0.944555 | 0.555763 | fitted |
| 2026-06 | game | 330 | 0.937798 | -0.001598 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 473 | 0.619989 | 0.626718 | -0.006728 [-0.014696, 0.001013] | no |
| series | tier1 | 401 | 0.612431 | 0.617017 | -0.004586 [-0.012594, 0.003031] | no |
| series | tier2 | 64 | 0.667511 | 0.679709 | -0.012198 [-0.038432, 0.012383] | no |
| series | tier3 | 8 | 0.618661 | 0.689027 | -0.070366 [-0.279488, 0.069032] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 401 | 0.612431 | 0.617017 | -0.004586 [-0.012594, 0.003031] | no |
| series | international=0 | 72 | 0.662083 | 0.680744 | -0.018661 [-0.051113, 0.010990] | no |
| game | all | 302 | 0.627532 | 0.623361 | 0.004171 [-0.002438, 0.010920] | no |
| game | tier1 | 237 | 0.616354 | 0.611859 | 0.004495 [-0.002946, 0.011977] | no |
| game | tier2 | 56 | 0.682101 | 0.679563 | 0.002538 [-0.012674, 0.017995] | no |
| game | tier3 | 9 | 0.582331 | 0.576544 | 0.005786 [-0.002646, 0.012272] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 237 | 0.616354 | 0.611859 | 0.004495 [-0.002946, 0.011977] | no |
| game | international=0 | 65 | 0.668287 | 0.665299 | 0.002988 [-0.010692, 0.016983] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 127 | 127 | 0.0275 | 27.95% [-0.26%, 57.61%] | $89.04 | 1.781× | 34.90% | $8.44 | 75 (52 unfilled) | 26.91% [-8.01%, 65.30%] | $83.05 |
| series | tier1 | 97 | 97 | 0.0261 | 19.12% [-8.76%, 50.83%] | $63.32 | 1.266× | 35.00% | $6.69 | 56 (41 unfilled) | 4.71% [-26.84%, 36.97%] | $62.29 |
| series | tier2 | 25 | 25 | 0.0232 | 56.60% [-17.88%, 141.80%] | $62.94 | 1.259× | 16.39% | $5.33 | 14 (11 unfilled) | 105.10% [-20.72%, 241.46%] | $60.31 |
| series | tier3 | 5 | 5 | 0.0772 | 55.13% [-68.25%, 178.65%] | $55.69 | 1.114× | 5.10% | $4.54 | 5 (0 unfilled) | 55.13% [-68.25%, 178.65%] | $55.69 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 97 | 97 | 0.0261 | 19.12% [-8.76%, 50.83%] | $63.32 | 1.266× | 35.00% | $6.69 | 56 (41 unfilled) | 4.71% [-26.84%, 36.97%] | $62.29 |
| series | international=0 | 30 | 30 | 0.0322 | 56.35% [-10.12%, 132.61%] | $70.12 | 1.402× | 16.39% | $5.72 | 19 (11 unfilled) | 91.98% [-6.36%, 203.88%] | $67.18 |
| game | all | 47 | 25 | 0.0173 | -16.07% [-48.96%, 17.17%] | $35.27 | 0.705× | 35.44% | $2.39 | 1 (46 unfilled) | 96.23% [96.23%, 96.23%] | $50.28 |
| game | tier1 | 37 | 19 | 0.0165 | -19.09% [-56.33%, 20.81%] | $37.41 | 0.748× | 32.95% | $2.50 | 1 (36 unfilled) | 96.23% [96.23%, 96.23%] | $50.28 |
| game | tier2 | 10 | 6 | 0.0204 | -4.87% [-67.23%, 71.86%] | $47.07 | 0.941× | 11.19% | $2.39 | 0 (10 unfilled) | — | $50.00 |
| game | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 37 | 19 | 0.0165 | -19.09% [-56.33%, 20.81%] | $37.41 | 0.748× | 32.95% | $2.50 | 1 (36 unfilled) | 96.23% [96.23%, 96.23%] | $50.28 |
| game | international=0 | 10 | 6 | 0.0204 | -4.87% [-67.23%, 71.86%] | $47.07 | 0.941× | 11.19% | $2.39 | 0 (10 unfilled) | — | $50.00 |
| series+game | all | 174 | 145 | 0.0248 | 16.06% [-6.27%, 39.97%] | $67.77 | 1.355× | 35.80% | $6.19 | 76 (98 unfilled) | 27.81% [-5.17%, 64.08%] | $82.92 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| game | 2026-03 | 15 | 0.726912 | — | 0.669739 | -100.00% (3), $39.92 | — | 1 (2 unfilled) | -100.00% [-100.00%, -100.00%] | $45.12 | — | — | — |
| game | 2026-04 | 117 | 0.661879 | — | 0.651637 | -3.25% (36), $46.13 | — | 10 (26 unfilled) | 27.50% [-19.45%, 77.47%] | $59.03 | — | — | — |
| game | 2026-05 | 198 | 0.668133 | 0.660920 | 0.657045 | -9.76% (119), $23.85 | -16.07% (47), $35.27 | 4 (115 unfilled) | -48.48% [-100.00%, 53.81%] | $44.52 | 1 (46 unfilled) | 96.23% [96.23%, 96.23%] | $50.28 |
| game | 2026-06 | 104 | 0.551826 | 0.563966 | 0.559231 | -5.21% (60), $43.33 | — (0), $50.00 | 11 (49 unfilled) | -13.06% [-59.21%, 39.08%] | $44.96 | 0 (0 unfilled) | — | $50.00 |
| series | 2025-11 | 13 | 0.490611 | — | 0.588964 | 65.66% (9), $91.39 | — | 8 (1 unfilled) | 26.76% [-49.51%, 119.66%] | $69.57 | — | — | — |
| series | 2025-12 | 66 | 0.672017 | — | 0.640347 | -7.91% (44), $40.49 | — | 40 (4 unfilled) | -4.40% [-38.57%, 34.94%] | $44.93 | — | — | — |
| series | 2026-01 | 69 | 0.519361 | — | 0.506048 | -3.46% (47), $46.88 | — | 21 (26 unfilled) | -20.28% [-63.41%, 32.55%] | $38.95 | — | — | — |
| series | 2026-02 | 101 | 0.660861 | 0.663738 | 0.667211 | 3.80% (73), $48.44 | 159.01% (4), $53.11 | 22 (51 unfilled) | 8.81% [-38.40%, 57.76%] | $51.92 | 2 (2 unfilled) | 150.04% [92.31%, 207.22%] | $51.26 |
| series | 2026-03 | 53 | 0.649892 | 0.656859 | 0.663787 | 9.17% (29), $59.06 | 5.05% (7), $52.32 | 26 (3 unfilled) | 2.83% [-40.32%, 44.94%] | $53.96 | 5 (2 unfilled) | 4.75% [-100.00%, 113.39%] | $52.63 |
| series | 2026-04 | 77 | 0.682809 | 0.682051 | 0.690287 | 20.16% (55), $75.90 | 33.26% (27), $57.08 | 38 (17 unfilled) | 30.37% [-22.96%, 90.51%] | $77.13 | 19 (8 unfilled) | 78.29% [-10.84%, 172.18%] | $65.01 |
| series | 2026-05 | 165 | 0.618648 | 0.619974 | 0.626943 | 13.54% (91), $121.17 | 44.98% (46), $65.63 | 22 (69 unfilled) | -6.53% [-56.86%, 44.05%] | $44.12 | 16 (30 unfilled) | 13.31% [-57.14%, 101.69%] | $48.26 |
| series | 2026-06 | 77 | 0.472841 | 0.475198 | 0.484035 | -5.92% (54), $42.07 | -2.24% (43), $53.19 | 42 (12 unfilled) | -6.28% [-38.06%, 27.85%] | $49.99 | 33 (10 unfilled) | -0.30% [-36.78%, 40.27%] | $60.79 |

### player_glicko+form: Kalshi comparison and returns

form: rows=35654, H=80, w=1.50996

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 621 | 0.614973 | 0.613968 | 0.001004 [-0.014662, 0.015932] | no |
| series | tier1 | 528 | 0.610095 | 0.608069 | 0.002027 [-0.012765, 0.016749] | no |
| series | tier2 | 85 | 0.645448 | 0.643551 | 0.001897 [-0.042883, 0.044449] | no |
| series | tier3 | 8 | 0.613079 | 0.689027 | -0.075948 [-0.397702, 0.159219] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 528 | 0.610095 | 0.608069 | 0.002027 [-0.012765, 0.016749] | no |
| series | international=0 | 93 | 0.642664 | 0.647463 | -0.004800 [-0.053161, 0.042411] | no |
| game | all | 434 | 0.645335 | 0.632587 | 0.012749 [-0.001273, 0.027448] | no |
| game | tier1 | 340 | 0.642765 | 0.629029 | 0.013736 [-0.002502, 0.031362] | no |
| game | tier2 | 85 | 0.661927 | 0.652750 | 0.009176 [-0.019554, 0.038631] | no |
| game | tier3 | 9 | 0.585725 | 0.576544 | 0.009181 [-0.079608, 0.080211] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 340 | 0.642765 | 0.629029 | 0.013736 [-0.002502, 0.031362] | no |
| game | international=0 | 94 | 0.654631 | 0.645454 | 0.009177 [-0.018160, 0.036387] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 407 | 407 | 0.0572 | 0.88% [-10.93%, 14.12%] | $30.31 | 0.606× | 78.04% | $8.83 | 217 (190 unfilled) | -0.76% [-18.40%, 17.34%] | $29.96 |
| series | tier1 | 345 | 345 | 0.0550 | -1.29% [-14.49%, 11.63%] | $19.16 | 0.383× | 80.96% | $7.63 | 185 (160 unfilled) | -5.49% [-21.52%, 10.87%] | $18.28 |
| series | tier2 | 56 | 56 | 0.0620 | 11.14% [-30.56%, 57.04%] | $71.02 | 1.420× | 29.98% | $6.42 | 26 (30 unfilled) | 25.70% [-44.83%, 110.23%] | $68.86 |
| series | tier3 | 6 | 6 | 0.1400 | 29.69% [-73.50%, 147.49%] | $54.75 | 1.095× | 10.00% | $4.89 | 6 (0 unfilled) | 29.69% [-73.50%, 147.49%] | $59.29 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 345 | 345 | 0.0550 | -1.29% [-14.49%, 11.63%] | $19.16 | 0.383× | 80.96% | $7.63 | 185 (160 unfilled) | -5.49% [-21.52%, 10.87%] | $18.28 |
| series | international=0 | 62 | 62 | 0.0696 | 12.93% [-25.29%, 55.63%] | $77.80 | 1.556× | 29.98% | $6.94 | 32 (30 unfilled) | 26.44% [-36.57%, 98.55%] | $82.27 |
| game | all | 238 | 125 | 0.0473 | -10.34% [-23.04%, 3.04%] | $15.59 | 0.312× | 71.12% | $4.42 | 31 (207 unfilled) | -15.93% [-45.62%, 13.49%] | $40.05 |
| game | tier1 | 191 | 100 | 0.0480 | -11.51% [-26.01%, 3.95%] | $17.93 | 0.359× | 67.87% | $4.42 | 26 (165 unfilled) | -18.81% [-50.47%, 13.14%] | $38.99 |
| game | tier2 | 40 | 22 | 0.0491 | -7.82% [-35.57%, 20.51%] | $43.51 | 0.870× | 22.37% | $4.79 | 5 (35 unfilled) | -0.90% [-72.65%, 70.30%] | $51.22 |
| game | tier3 | 7 | 3 | 0.0154 | 7.10% [-47.80%, 50.53%] | $50.08 | 1.002× | 4.78% | $2.61 | 0 (7 unfilled) | — | $50.00 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 191 | 100 | 0.0480 | -11.51% [-26.01%, 3.95%] | $17.93 | 0.359× | 67.87% | $4.42 | 26 (165 unfilled) | -18.81% [-50.47%, 13.14%] | $38.99 |
| game | international=0 | 47 | 25 | 0.0441 | -5.60% [-30.44%, 20.43%] | $43.58 | 0.872× | 23.38% | $4.79 | 5 (42 unfilled) | -0.90% [-72.65%, 70.30%] | $51.22 |
| series+game | all | 645 | 443 | 0.0536 | -3.24% [-13.31%, 7.31%] | $11.61 | 0.232× | 89.59% | $7.63 | 248 (397 unfilled) | -2.64% [-18.25%, 12.30%] | $33.10 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 280 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2025-11 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2025-12 | series | 13 | 1.000000 | 0.000000 | unfitted |
| 2026-01 | series | 79 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 148 | 1.055376 | 0.303497 | fitted |
| 2026-03 | series | 249 | 0.977479 | 0.311379 | fitted |
| 2026-03 | game | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | series | 302 | 0.991460 | 0.438793 | fitted |
| 2026-04 | game | 15 | 1.000000 | 0.000000 | unfitted |
| 2026-05 | series | 379 | 0.912333 | 0.411898 | fitted |
| 2026-05 | game | 132 | 1.075345 | -0.463632 | fitted |
| 2026-06 | series | 544 | 0.940312 | 0.479675 | fitted |
| 2026-06 | game | 330 | 0.957517 | -0.142625 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 473 | 0.623412 | 0.626718 | -0.003305 [-0.011180, 0.004095] | no |
| series | tier1 | 401 | 0.616072 | 0.617017 | -0.000945 [-0.008914, 0.006735] | no |
| series | tier2 | 64 | 0.668608 | 0.679709 | -0.011102 [-0.037129, 0.013535] | no |
| series | tier3 | 8 | 0.629787 | 0.689027 | -0.059240 [-0.253305, 0.071699] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 401 | 0.616072 | 0.617017 | -0.000945 [-0.008914, 0.006735] | no |
| series | international=0 | 72 | 0.664294 | 0.680744 | -0.016450 [-0.046727, 0.012435] | no |
| game | all | 302 | 0.627135 | 0.623361 | 0.003774 [-0.002928, 0.010703] | no |
| game | tier1 | 237 | 0.615282 | 0.611859 | 0.003423 [-0.004156, 0.011301] | no |
| game | tier2 | 56 | 0.684802 | 0.679563 | 0.005239 [-0.009116, 0.021248] | no |
| game | tier3 | 9 | 0.580441 | 0.576544 | 0.003897 [-0.009647, 0.020826] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 237 | 0.615282 | 0.611859 | 0.003423 [-0.004156, 0.011301] | no |
| game | international=0 | 65 | 0.670352 | 0.665299 | 0.005053 [-0.007693, 0.019023] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 134 | 134 | 0.0234 | 9.77% [-16.40%, 36.21%] | $81.33 | 1.627× | 47.48% | $9.81 | 70 (64 unfilled) | 14.99% [-21.16%, 55.03%] | $77.52 |
| series | tier1 | 105 | 105 | 0.0214 | -4.64% [-29.47%, 23.84%] | $54.94 | 1.099× | 47.47% | $7.50 | 51 (54 unfilled) | -13.83% [-42.09%, 16.96%] | $54.67 |
| series | tier2 | 24 | 24 | 0.0235 | 62.99% [-17.25%, 150.71%] | $65.38 | 1.308× | 15.44% | $5.43 | 14 (10 unfilled) | 105.10% [-20.72%, 241.46%] | $61.41 |
| series | tier3 | 5 | 5 | 0.0657 | 55.13% [-68.25%, 178.65%] | $56.57 | 1.131× | 3.27% | $4.61 | 5 (0 unfilled) | 55.13% [-68.25%, 178.65%] | $56.57 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 105 | 105 | 0.0214 | -4.64% [-29.47%, 23.84%] | $54.94 | 1.099× | 47.47% | $7.50 | 51 (54 unfilled) | -13.83% [-42.09%, 16.96%] | $54.67 |
| series | international=0 | 29 | 29 | 0.0308 | 61.63% [-8.00%, 134.85%] | $73.96 | 1.479× | 15.44% | $6.03 | 19 (10 unfilled) | 91.98% [-6.36%, 203.88%] | $69.48 |
| game | all | 40 | 23 | 0.0155 | -23.34% [-50.74%, 3.70%] | $43.24 | 0.865× | 21.03% | $3.30 | 4 (36 unfilled) | 4.46% [-100.00%, 96.23%] | $49.82 |
| game | tier1 | 32 | 18 | 0.0132 | -23.23% [-58.55%, 7.86%] | $44.35 | 0.887× | 21.02% | $2.60 | 4 (28 unfilled) | 4.46% [-100.00%, 96.23%] | $49.82 |
| game | tier2 | 8 | 5 | 0.0248 | -23.82% [-68.90%, 30.23%] | $48.76 | 0.975× | 9.04% | $3.30 | 0 (8 unfilled) | — | $50.00 |
| game | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 32 | 18 | 0.0132 | -23.23% [-58.55%, 7.86%] | $44.35 | 0.887× | 21.02% | $2.60 | 4 (28 unfilled) | 4.46% [-100.00%, 96.23%] | $49.82 |
| game | international=0 | 8 | 5 | 0.0248 | -23.82% [-68.90%, 30.23%] | $48.76 | 0.975× | 9.04% | $3.30 | 0 (8 unfilled) | — | $50.00 |
| series+game | all | 174 | 144 | 0.0216 | 2.20% [-16.90%, 23.41%] | $81.82 | 1.636× | 48.05% | $9.22 | 74 (100 unfilled) | 14.42% [-19.12%, 51.23%] | $77.20 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| game | 2026-03 | 15 | 0.737947 | — | 0.669739 | -73.56% (6), $36.46 | — | 3 (3 unfilled) | -47.12% [-100.00%, -20.42%] | $44.21 | — | — | — |
| game | 2026-04 | 117 | 0.667549 | — | 0.651637 | -8.17% (53), $45.11 | — | 13 (40 unfilled) | 10.80% [-36.33%, 54.13%] | $55.35 | — | — | — |
| game | 2026-05 | 198 | 0.669620 | 0.659898 | 0.657045 | -10.80% (113), $26.91 | -19.24% (38), $43.39 | 5 (108 unfilled) | -58.93% [-100.00%, 22.99%] | $43.22 | 3 (35 unfilled) | 39.95% [11.81%, 96.23%] | $49.93 |
| game | 2026-06 | 104 | 0.560753 | 0.564759 | 0.559231 | -5.59% (66), $45.10 | -100.00% (2), $49.83 | 10 (56 unfilled) | -19.83% [-75.01%, 29.00%] | $47.15 | 1 (1 unfilled) | -100.00% [-100.00%, -100.00%] | $49.89 |
| series | 2025-11 | 13 | 0.468076 | — | 0.588964 | 70.08% (11), $80.52 | — | 10 (1 unfilled) | 39.07% [-22.11%, 117.29%] | $78.10 | — | — | — |
| series | 2025-12 | 66 | 0.664382 | — | 0.640347 | -5.05% (40), $29.46 | — | 37 (3 unfilled) | -3.49% [-42.91%, 41.24%] | $31.06 | — | — | — |
| series | 2026-01 | 69 | 0.525102 | — | 0.506048 | -17.59% (46), $33.78 | — | 24 (22 unfilled) | -34.81% [-75.07%, 10.97%] | $29.00 | — | — | — |
| series | 2026-02 | 101 | 0.669553 | 0.665897 | 0.667211 | 4.22% (72), $47.31 | 36.95% (13), $57.88 | 20 (52 unfilled) | 14.39% [-35.44%, 65.46%] | $54.82 | 2 (11 unfilled) | 150.04% [92.31%, 207.22%] | $53.96 |
| series | 2026-03 | 53 | 0.644678 | 0.656153 | 0.663787 | 19.18% (26), $67.29 | 25.31% (2), $52.47 | 21 (5 unfilled) | 12.41% [-33.54%, 59.25%] | $60.72 | 2 (0 unfilled) | 25.31% [-100.00%, 150.63%] | $52.47 |
| series | 2026-04 | 77 | 0.686449 | 0.684194 | 0.690287 | 4.47% (54), $64.64 | 32.19% (24), $57.88 | 36 (18 unfilled) | 19.66% [-31.80%, 81.96%] | $77.03 | 18 (6 unfilled) | 64.68% [-22.52%, 169.55%] | $67.61 |
| series | 2026-05 | 165 | 0.623191 | 0.621337 | 0.626943 | 6.23% (101), $62.92 | 19.02% (54), $74.24 | 26 (75 unfilled) | -0.67% [-48.21%, 54.23%] | $38.18 | 16 (38 unfilled) | 9.73% [-62.53%, 98.51%] | $45.83 |
| series | 2026-06 | 77 | 0.496829 | 0.488814 | 0.484035 | -18.63% (57), $22.85 | -24.84% (41), $38.83 | 43 (14 unfilled) | -19.14% [-50.99%, 14.38%] | $32.60 | 32 (9 unfilled) | -19.37% [-55.19%, 22.03%] | $53.14 |

### player_glicko_rookie_weights+none: Kalshi comparison and returns

none

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 621 | 0.609189 | 0.613968 | -0.004780 [-0.019407, 0.009330] | no |
| series | tier1 | 528 | 0.603370 | 0.608069 | -0.004699 [-0.017789, 0.008831] | no |
| series | tier2 | 85 | 0.650084 | 0.643551 | 0.006533 [-0.037185, 0.047965] | no |
| series | tier3 | 8 | 0.558714 | 0.689027 | -0.130313 [-0.532450, 0.148885] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 528 | 0.603370 | 0.608069 | -0.004699 [-0.017789, 0.008831] | no |
| series | international=0 | 93 | 0.642225 | 0.647463 | -0.005239 [-0.057078, 0.043611] | no |
| game | all | 434 | 0.643967 | 0.632587 | 0.011380 [-0.001351, 0.024616] | no |
| game | tier1 | 340 | 0.640791 | 0.629029 | 0.011761 [-0.002207, 0.026665] | no |
| game | tier2 | 85 | 0.665879 | 0.652750 | 0.013128 [-0.013072, 0.040615] | no |
| game | tier3 | 9 | 0.557014 | 0.576544 | -0.019530 [-0.098297, 0.068122] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 340 | 0.640791 | 0.629029 | 0.011761 [-0.002207, 0.026665] | no |
| game | international=0 | 94 | 0.655455 | 0.645454 | 0.010002 [-0.016070, 0.037185] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 397 | 397 | 0.0516 | 4.14% [-7.84%, 17.29%] | $101.33 | 2.027× | 69.83% | $21.17 | 210 (187 unfilled) | -2.18% [-18.92%, 14.00%] | $73.47 |
| series | tier1 | 336 | 336 | 0.0486 | 4.20% [-8.97%, 17.38%] | $66.12 | 1.322× | 67.86% | $16.00 | 179 (157 unfilled) | -4.77% [-20.36%, 11.62%] | $45.33 |
| series | tier2 | 56 | 56 | 0.0561 | 1.19% [-37.79%, 41.31%] | $66.06 | 1.321× | 24.72% | $6.97 | 26 (30 unfilled) | 8.79% [-55.10%, 88.07%] | $62.63 |
| series | tier3 | 5 | 5 | 0.2030 | 33.23% [-72.58%, 150.57%] | $57.27 | 1.145× | 10.00% | $5.02 | 5 (0 unfilled) | 33.23% [-72.58%, 150.57%] | $62.07 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 336 | 336 | 0.0486 | 4.20% [-8.97%, 17.38%] | $66.12 | 1.322× | 67.86% | $16.00 | 179 (157 unfilled) | -4.77% [-20.36%, 11.62%] | $45.33 |
| series | international=0 | 61 | 61 | 0.0682 | 3.81% [-33.43%, 44.48%] | $75.72 | 1.514× | 24.72% | $6.97 | 31 (30 unfilled) | 12.71% [-46.09%, 79.87%] | $78.17 |
| game | all | 215 | 114 | 0.0402 | -13.97% [-26.34%, -0.09%] | $12.88 | 0.258× | 75.20% | $4.49 | 32 (183 unfilled) | -15.41% [-44.91%, 15.97%] | $37.23 |
| game | tier1 | 169 | 88 | 0.0424 | -12.07% [-26.00%, 1.78%] | $17.47 | 0.349× | 67.88% | $4.49 | 25 (144 unfilled) | -11.41% [-44.51%, 23.46%] | $38.46 |
| game | tier2 | 40 | 23 | 0.0332 | -24.06% [-56.21%, 10.03%] | $37.20 | 0.744× | 32.95% | $5.37 | 7 (33 unfilled) | -29.62% [-100.00%, 31.24%] | $48.39 |
| game | tier3 | 6 | 3 | 0.0255 | 0.05% [-47.80%, 51.70%] | $49.84 | 0.997× | 4.78% | $2.78 | 0 (6 unfilled) | — | $50.00 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 169 | 88 | 0.0424 | -12.07% [-26.00%, 1.78%] | $17.47 | 0.349× | 67.88% | $4.49 | 25 (144 unfilled) | -11.41% [-44.51%, 23.46%] | $38.46 |
| game | international=0 | 46 | 26 | 0.0322 | -20.94% [-49.61%, 10.41%] | $37.08 | 0.742× | 33.17% | $5.37 | 7 (39 unfilled) | -29.62% [-100.00%, 31.24%] | $48.39 |
| series+game | all | 612 | 428 | 0.0476 | -2.20% [-12.42%, 7.93%] | $47.05 | 0.941× | 73.02% | $8.96 | 242 (370 unfilled) | -3.92% [-19.30%, 11.96%] | $81.88 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 280 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2025-11 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2025-12 | series | 13 | 1.000000 | 0.000000 | unfitted |
| 2026-01 | series | 79 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 148 | 1.035932 | 0.367192 | fitted |
| 2026-03 | series | 249 | 0.968216 | 0.465253 | fitted |
| 2026-03 | game | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | series | 302 | 0.975887 | 0.642729 | fitted |
| 2026-04 | game | 15 | 1.000000 | 0.000000 | unfitted |
| 2026-05 | series | 379 | 0.900763 | 0.591356 | fitted |
| 2026-05 | game | 132 | 1.128356 | -0.991081 | fitted |
| 2026-06 | series | 544 | 0.927481 | 0.622309 | fitted |
| 2026-06 | game | 330 | 0.978058 | -0.362807 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 473 | 0.619716 | 0.626718 | -0.007002 [-0.017926, 0.002963] | no |
| series | tier1 | 401 | 0.613456 | 0.617017 | -0.003561 [-0.012871, 0.006070] | no |
| series | tier2 | 64 | 0.667252 | 0.679709 | -0.012457 [-0.047260, 0.020855] | no |
| series | tier3 | 8 | 0.553176 | 0.689027 | -0.135850 [-0.493510, 0.086051] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 401 | 0.613456 | 0.617017 | -0.003561 [-0.012871, 0.006070] | no |
| series | international=0 | 72 | 0.654577 | 0.680744 | -0.026167 [-0.076586, 0.017613] | no |
| game | all | 302 | 0.631531 | 0.623361 | 0.008170 [-0.004624, 0.021144] | no |
| game | tier1 | 237 | 0.620720 | 0.611859 | 0.008862 [-0.004106, 0.022369] | no |
| game | tier2 | 56 | 0.683931 | 0.679563 | 0.004368 [-0.031088, 0.042096] | no |
| game | tier3 | 9 | 0.590157 | 0.576544 | 0.013612 [-0.019977, 0.045576] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 237 | 0.620720 | 0.611859 | 0.008862 [-0.004106, 0.022369] | no |
| game | international=0 | 65 | 0.670947 | 0.665299 | 0.005648 [-0.026238, 0.038880] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 172 | 172 | 0.0353 | 4.55% [-16.93%, 26.98%] | $76.17 | 1.523× | 62.49% | $12.42 | 88 (84 unfilled) | 0.98% [-27.36%, 31.28%] | $52.11 |
| series | tier1 | 138 | 138 | 0.0297 | -1.65% [-23.06%, 21.71%] | $48.20 | 0.964× | 60.17% | $8.85 | 69 (69 unfilled) | -12.53% [-37.12%, 13.72%] | $34.79 |
| series | tier2 | 30 | 30 | 0.0406 | 29.27% [-31.25%, 101.09%] | $70.01 | 1.400× | 22.05% | $7.12 | 15 (15 unfilled) | 54.63% [-53.60%, 177.28%] | $64.95 |
| series | tier3 | 4 | 4 | 0.1900 | 31.89% [-100.00%, 174.07%] | $55.81 | 1.116× | 6.63% | $4.55 | 4 (0 unfilled) | 31.89% [-100.00%, 174.07%] | $58.26 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 138 | 138 | 0.0297 | -1.65% [-23.06%, 21.71%] | $48.20 | 0.964× | 60.17% | $8.85 | 69 (69 unfilled) | -12.53% [-37.12%, 13.72%] | $34.79 |
| series | international=0 | 34 | 34 | 0.0582 | 29.58% [-28.53%, 93.60%] | $78.16 | 1.563× | 22.05% | $7.12 | 19 (15 unfilled) | 49.86% [-40.37%, 153.11%] | $76.12 |
| game | all | 117 | 63 | 0.0308 | -14.18% [-33.89%, 7.17%] | $16.35 | 0.327× | 69.72% | $3.78 | 13 (104 unfilled) | 3.69% [-54.23%, 75.19%] | $48.48 |
| game | tier1 | 88 | 47 | 0.0285 | -22.83% [-43.96%, -0.25%] | $17.87 | 0.357× | 69.62% | $3.89 | 10 (78 unfilled) | -27.09% [-79.73%, 41.30%] | $46.81 |
| game | tier2 | 29 | 16 | 0.0377 | 12.18% [-32.14%, 61.58%] | $45.90 | 0.918× | 21.75% | $3.78 | 3 (26 unfilled) | 107.23% [13.80%, 262.84%] | $51.78 |
| game | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 88 | 47 | 0.0285 | -22.83% [-43.96%, -0.25%] | $17.87 | 0.357× | 69.62% | $3.89 | 10 (78 unfilled) | -27.09% [-79.73%, 41.30%] | $46.81 |
| game | international=0 | 29 | 16 | 0.0377 | 12.18% [-32.14%, 61.58%] | $45.90 | 0.918× | 21.75% | $3.78 | 3 (26 unfilled) | 107.23% [13.80%, 262.84%] | $51.78 |
| series+game | all | 289 | 201 | 0.0335 | -3.01% [-16.96%, 11.64%] | $29.63 | 0.593× | 81.60% | $9.67 | 101 (188 unfilled) | 1.33% [-23.38%, 29.14%] | $52.67 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| game | 2026-03 | 15 | 0.731130 | — | 0.669739 | -73.56% (6), $36.97 | — | 3 (3 unfilled) | -47.12% [-100.00%, -20.42%] | $44.21 | — | — | — |
| game | 2026-04 | 117 | 0.670255 | — | 0.651637 | -16.09% (53), $38.53 | — | 13 (40 unfilled) | 10.80% [-36.33%, 54.13%] | $52.26 | — | — | — |
| game | 2026-05 | 198 | 0.668180 | 0.664453 | 0.657045 | -11.34% (100), $28.42 | -6.73% (99), $21.71 | 7 (93 unfilled) | -42.74% [-100.00%, 33.89%] | $44.38 | 9 (90 unfilled) | 30.42% [-38.94%, 119.54%] | $51.44 |
| game | 2026-06 | 104 | 0.555723 | 0.568852 | 0.559231 | -10.30% (56), $40.68 | -54.91% (18), $37.72 | 9 (47 unfilled) | -21.37% [-70.32%, 21.66%] | $45.28 | 4 (14 unfilled) | -55.29% [-100.00%, 81.42%] | $47.13 |
| series | 2025-11 | 13 | 0.486608 | — | 0.588964 | 70.08% (11), $72.06 | — | 10 (1 unfilled) | 39.07% [-22.11%, 117.29%] | $70.40 | — | — | — |
| series | 2025-12 | 66 | 0.656384 | — | 0.640347 | -19.37% (41), $43.00 | — | 36 (5 unfilled) | -18.51% [-52.95%, 23.78%] | $46.18 | — | — | — |
| series | 2026-01 | 69 | 0.519620 | — | 0.506048 | -7.28% (46), $43.96 | — | 24 (22 unfilled) | -24.48% [-63.57%, 21.45%] | $35.16 | — | — | — |
| series | 2026-02 | 101 | 0.662013 | 0.663137 | 0.667211 | 18.87% (66), $43.25 | 11.03% (16), $58.94 | 18 (48 unfilled) | 30.31% [-22.53%, 81.80%] | $66.83 | 4 (12 unfilled) | 25.02% [-100.00%, 150.04%] | $53.33 |
| series | 2026-03 | 53 | 0.637795 | 0.649602 | 0.663787 | 47.54% (23), $83.60 | 35.75% (9), $56.56 | 18 (5 unfilled) | 31.72% [-14.52%, 78.20%] | $65.33 | 7 (2 unfilled) | 20.54% [-54.96%, 102.11%] | $53.41 |
| series | 2026-04 | 77 | 0.686706 | 0.683758 | 0.690287 | 3.38% (50), $79.69 | 28.30% (34), $71.01 | 34 (16 unfilled) | 16.59% [-36.17%, 75.36%] | $82.42 | 21 (13 unfilled) | 56.64% [-20.18%, 142.90%] | $76.25 |
| series | 2026-05 | 165 | 0.621403 | 0.620612 | 0.626943 | 2.68% (102), $68.44 | 5.29% (66), $64.40 | 26 (76 unfilled) | -20.06% [-60.01%, 24.15%] | $35.15 | 21 (45 unfilled) | -24.67% [-73.07%, 27.84%] | $35.55 |
| series | 2026-06 | 77 | 0.477023 | 0.476226 | 0.484035 | -13.32% (58), $29.09 | -21.82% (47), $30.95 | 44 (14 unfilled) | -17.07% [-45.66%, 13.01%] | $35.64 | 35 (12 unfilled) | -23.59% [-58.73%, 14.35%] | $40.75 |

### player_glicko_rookie_weights+regional: Kalshi comparison and returns

regional: rows=7157, ridge=4, s=0.886299, effects: EU=0.183265, CIS=0.2473, NA=-0.106407, SA=-0.0512989, AS=0.107314, OCE=-0.0962255, AF=-0.283949

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 621 | 0.608062 | 0.613968 | -0.005906 [-0.020521, 0.008607] | no |
| series | tier1 | 528 | 0.601875 | 0.608069 | -0.006193 [-0.019283, 0.007237] | no |
| series | tier2 | 85 | 0.651304 | 0.643551 | 0.007753 [-0.035790, 0.049244] | no |
| series | tier3 | 8 | 0.556945 | 0.689027 | -0.132082 [-0.533438, 0.149436] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 528 | 0.601875 | 0.608069 | -0.006193 [-0.019283, 0.007237] | no |
| series | international=0 | 93 | 0.643187 | 0.647463 | -0.004276 [-0.056257, 0.044864] | no |
| game | all | 434 | 0.641733 | 0.632587 | 0.009147 [-0.003416, 0.022383] | no |
| game | tier1 | 340 | 0.637883 | 0.629029 | 0.008853 [-0.004765, 0.023591] | no |
| game | tier2 | 85 | 0.666107 | 0.652750 | 0.013356 [-0.013197, 0.041842] | no |
| game | tier3 | 9 | 0.557014 | 0.576544 | -0.019530 [-0.098297, 0.068122] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 340 | 0.637883 | 0.629029 | 0.008853 [-0.004765, 0.023591] | no |
| game | international=0 | 94 | 0.655662 | 0.645454 | 0.010208 [-0.015534, 0.038261] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 395 | 395 | 0.0515 | 6.84% [-5.77%, 19.86%] | $131.65 | 2.633× | 65.60% | $18.93 | 210 (185 unfilled) | -0.59% [-16.81%, 16.67%] | $76.57 |
| series | tier1 | 334 | 334 | 0.0481 | 5.87% [-6.73%, 18.32%] | $85.88 | 1.718× | 61.49% | $14.44 | 179 (155 unfilled) | -3.29% [-19.24%, 13.99%] | $45.67 |
| series | tier2 | 55 | 55 | 0.0590 | 9.54% [-29.80%, 52.10%] | $65.41 | 1.308× | 29.50% | $6.94 | 26 (29 unfilled) | 11.33% [-51.73%, 89.73%] | $64.61 |
| series | tier3 | 6 | 6 | 0.1714 | 35.52% [-52.82%, 141.93%] | $57.88 | 1.158× | 10.00% | $5.06 | 5 (1 unfilled) | 33.23% [-72.58%, 150.57%] | $62.55 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 334 | 334 | 0.0481 | 5.87% [-6.73%, 18.32%] | $85.88 | 1.718× | 61.49% | $14.44 | 179 (155 unfilled) | -3.29% [-19.24%, 13.99%] | $45.67 |
| series | international=0 | 61 | 61 | 0.0701 | 12.08% [-24.27%, 51.32%] | $75.75 | 1.515× | 29.50% | $6.94 | 31 (30 unfilled) | 14.84% [-46.56%, 82.44%] | $81.29 |
| game | all | 204 | 111 | 0.0395 | -7.19% [-20.34%, 6.02%] | $15.92 | 0.318× | 69.61% | $4.48 | 32 (172 unfilled) | -23.15% [-49.29%, 3.48%] | $33.37 |
| game | tier1 | 158 | 84 | 0.0414 | -4.36% [-18.89%, 10.73%] | $22.35 | 0.447× | 58.93% | $4.48 | 26 (132 unfilled) | -24.40% [-53.84%, 4.69%] | $34.51 |
| game | tier2 | 40 | 24 | 0.0341 | -19.40% [-51.99%, 13.85%] | $36.06 | 0.721× | 35.01% | $5.37 | 6 (34 unfilled) | -17.76% [-77.46%, 48.03%] | $48.39 |
| game | tier3 | 6 | 3 | 0.0255 | 0.05% [-47.80%, 51.70%] | $49.84 | 0.997× | 4.78% | $2.78 | 0 (6 unfilled) | — | $50.00 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 158 | 84 | 0.0414 | -4.36% [-18.89%, 10.73%] | $22.35 | 0.447× | 58.93% | $4.48 | 26 (132 unfilled) | -24.40% [-53.84%, 4.69%] | $34.51 |
| game | international=0 | 46 | 27 | 0.0330 | -16.88% [-47.20%, 13.62%] | $35.93 | 0.719× | 35.24% | $5.37 | 6 (40 unfilled) | -17.76% [-77.46%, 48.03%] | $48.39 |
| series+game | all | 599 | 420 | 0.0474 | 2.08% [-8.63%, 12.70%] | $75.15 | 1.503× | 65.60% | $8.63 | 242 (357 unfilled) | -3.56% [-18.75%, 11.49%] | $72.39 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 280 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2025-11 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2025-12 | series | 13 | 1.000000 | 0.000000 | unfitted |
| 2026-01 | series | 79 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 148 | 1.031169 | 0.293463 | fitted |
| 2026-03 | series | 249 | 0.960892 | 0.372029 | fitted |
| 2026-03 | game | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | series | 302 | 0.968584 | 0.557512 | fitted |
| 2026-04 | game | 15 | 1.000000 | 0.000000 | unfitted |
| 2026-05 | series | 379 | 0.888624 | 0.508705 | fitted |
| 2026-05 | game | 132 | 1.162928 | -1.061219 | fitted |
| 2026-06 | series | 544 | 0.929362 | 0.647308 | fitted |
| 2026-06 | game | 330 | 0.963500 | -0.256352 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 473 | 0.618887 | 0.626718 | -0.007831 [-0.018083, 0.001734] | no |
| series | tier1 | 401 | 0.612568 | 0.617017 | -0.004449 [-0.013264, 0.004610] | no |
| series | tier2 | 64 | 0.667000 | 0.679709 | -0.012709 [-0.044347, 0.018082] | no |
| series | tier3 | 8 | 0.550729 | 0.689027 | -0.138297 [-0.501836, 0.089769] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 401 | 0.612568 | 0.617017 | -0.004449 [-0.013264, 0.004610] | no |
| series | international=0 | 72 | 0.654081 | 0.680744 | -0.026663 [-0.076475, 0.015271] | no |
| game | all | 302 | 0.633686 | 0.623361 | 0.010325 [-0.003075, 0.024259] | no |
| game | tier1 | 237 | 0.623089 | 0.611859 | 0.011230 [-0.001879, 0.025811] | no |
| game | tier2 | 56 | 0.685882 | 0.679563 | 0.006319 [-0.032340, 0.047592] | no |
| game | tier3 | 9 | 0.587971 | 0.576544 | 0.011427 [-0.015213, 0.036164] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 237 | 0.623089 | 0.611859 | 0.011230 [-0.001879, 0.025811] | no |
| game | international=0 | 65 | 0.672325 | 0.665299 | 0.007026 [-0.026893, 0.042681] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 159 | 159 | 0.0323 | 9.24% [-13.94%, 33.71%] | $83.95 | 1.679× | 55.50% | $11.46 | 80 (79 unfilled) | 3.05% [-27.67%, 35.82%] | $59.88 |
| series | tier1 | 124 | 124 | 0.0272 | 2.19% [-21.73%, 28.99%] | $53.69 | 1.074× | 52.02% | $8.17 | 61 (63 unfilled) | -11.59% [-39.43%, 17.68%] | $39.97 |
| series | tier2 | 31 | 31 | 0.0315 | 34.41% [-27.52%, 104.48%] | $69.86 | 1.397× | 19.02% | $6.80 | 15 (16 unfilled) | 54.63% [-53.60%, 177.28%] | $64.18 |
| series | tier3 | 4 | 4 | 0.1977 | 31.89% [-100.00%, 174.07%] | $55.27 | 1.105× | 8.21% | $4.50 | 4 (0 unfilled) | 31.89% [-100.00%, 174.07%] | $58.70 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 124 | 124 | 0.0272 | 2.19% [-21.73%, 28.99%] | $53.69 | 1.074× | 52.02% | $8.17 | 61 (63 unfilled) | -11.59% [-39.43%, 17.68%] | $39.97 |
| series | international=0 | 35 | 35 | 0.0505 | 34.12% [-23.92%, 98.56%] | $77.25 | 1.545× | 19.02% | $6.80 | 19 (16 unfilled) | 49.86% [-40.37%, 153.11%] | $75.78 |
| game | all | 100 | 54 | 0.0379 | -14.06% [-33.93%, 6.40%] | $18.08 | 0.362× | 68.88% | $3.84 | 10 (90 unfilled) | -1.81% [-48.66%, 40.03%] | $51.73 |
| game | tier1 | 71 | 37 | 0.0353 | -19.55% [-44.24%, 3.59%] | $19.41 | 0.388× | 68.89% | $3.19 | 8 (63 unfilled) | -8.71% [-72.08%, 45.77%] | $50.48 |
| game | tier2 | 29 | 17 | 0.0442 | -0.56% [-37.31%, 41.30%] | $46.56 | 0.931× | 20.61% | $3.84 | 2 (27 unfilled) | 26.37% [13.80%, 38.70%] | $51.25 |
| game | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 71 | 37 | 0.0353 | -19.55% [-44.24%, 3.59%] | $19.41 | 0.388× | 68.89% | $3.19 | 8 (63 unfilled) | -8.71% [-72.08%, 45.77%] | $50.48 |
| game | international=0 | 29 | 17 | 0.0442 | -0.56% [-37.31%, 41.30%] | $46.56 | 0.931× | 20.61% | $3.84 | 2 (27 unfilled) | 26.37% [13.80%, 38.70%] | $51.25 |
| series+game | all | 259 | 189 | 0.0345 | 0.29% [-14.18%, 15.40%] | $31.06 | 0.621× | 78.38% | $8.63 | 90 (169 unfilled) | 2.52% [-23.77%, 33.16%] | $66.21 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| game | 2026-03 | 15 | 0.713665 | — | 0.669739 | -60.40% (4), $40.79 | — | 3 (1 unfilled) | -47.12% [-100.00%, -20.42%] | $45.32 | — | — | — |
| game | 2026-04 | 117 | 0.670771 | — | 0.651637 | -12.25% (50), $38.59 | — | 14 (36 unfilled) | -13.57% [-55.94%, 31.03%] | $47.06 | — | — | — |
| game | 2026-05 | 198 | 0.665127 | 0.668432 | 0.657045 | -2.28% (94), $30.48 | -10.44% (94), $19.58 | 5 (89 unfilled) | -59.00% [-100.00%, 23.22%] | $42.88 | 7 (87 unfilled) | 15.06% [-32.93%, 54.02%] | $53.10 |
| game | 2026-06 | 104 | 0.554153 | 0.567536 | 0.559231 | -7.11% (56), $42.16 | -70.05% (6), $46.16 | 10 (46 unfilled) | -11.37% [-55.43%, 33.56%] | $45.55 | 3 (3 unfilled) | -40.29% [-100.00%, 81.42%] | $48.70 |
| series | 2025-11 | 13 | 0.487883 | — | 0.588964 | 70.08% (11), $75.78 | — | 10 (1 unfilled) | 39.07% [-22.11%, 117.29%] | $70.08 | — | — | — |
| series | 2025-12 | 66 | 0.659543 | — | 0.640347 | -16.09% (43), $35.59 | — | 38 (5 unfilled) | -14.85% [-47.86%, 21.70%] | $38.99 | — | — | — |
| series | 2026-01 | 69 | 0.521250 | — | 0.506048 | -3.51% (50), $39.64 | — | 25 (25 unfilled) | -27.77% [-65.98%, 14.97%] | $34.11 | — | — | — |
| series | 2026-02 | 101 | 0.665248 | 0.664658 | 0.667211 | 16.35% (62), $35.07 | 48.78% (10), $56.20 | 16 (46 unfilled) | 27.42% [-30.90%, 87.37%] | $66.30 | 4 (6 unfilled) | 25.02% [-100.00%, 150.04%] | $51.18 |
| series | 2026-03 | 53 | 0.637399 | 0.651867 | 0.663787 | 49.31% (24), $86.58 | 26.50% (5), $55.21 | 18 (6 unfilled) | 31.79% [-15.36%, 78.47%] | $65.53 | 4 (1 unfilled) | 4.70% [-100.00%, 109.41%] | $53.46 |
| series | 2026-04 | 77 | 0.688861 | 0.684837 | 0.690287 | 7.35% (48), $73.30 | 28.94% (31), $66.33 | 33 (15 unfilled) | 19.60% [-33.08%, 81.04%] | $77.77 | 19 (12 unfilled) | 62.77% [-21.53%, 158.58%] | $75.57 |
| series | 2026-05 | 165 | 0.614559 | 0.617653 | 0.626943 | 8.55% (99), $128.59 | 16.74% (64), $72.23 | 26 (73 unfilled) | -13.02% [-54.61%, 29.97%] | $43.33 | 17 (47 unfilled) | -14.55% [-67.51%, 46.31%] | $39.06 |
| series | 2026-06 | 77 | 0.472095 | 0.472846 | 0.484035 | -10.27% (58), $33.24 | -22.88% (49), $35.13 | 44 (14 unfilled) | -13.04% [-42.74%, 16.95%] | $38.89 | 36 (13 unfilled) | -22.75% [-57.78%, 12.70%] | $44.65 |

### player_glicko_rookie_weights+calibration: Kalshi comparison and returns

calibration: ridge=4; tier1/online=0: rows=3058, T=0.8142; tier1/online=1: rows=11009, T=1.0074; tier2/online=0: rows=623, T=0.8541; tier2/online=1: rows=3405, T=1.0009; tier3/online=0: rows=2386, T=1.0506; tier3/online=1: rows=17650, T=0.9245; unknown/online=0: rows=7, T=1.0000

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 621 | 0.607200 | 0.613968 | -0.006768 [-0.021344, 0.007554] | no |
| series | tier1 | 528 | 0.600897 | 0.608069 | -0.007172 [-0.020059, 0.006030] | no |
| series | tier2 | 85 | 0.651111 | 0.643551 | 0.007560 [-0.036577, 0.048164] | no |
| series | tier3 | 8 | 0.556668 | 0.689027 | -0.132359 [-0.530700, 0.138850] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 528 | 0.600897 | 0.608069 | -0.007172 [-0.020059, 0.006030] | no |
| series | international=0 | 93 | 0.642987 | 0.647463 | -0.004476 [-0.055551, 0.044196] | no |
| game | all | 434 | 0.642096 | 0.632587 | 0.009509 [-0.002608, 0.021619] | no |
| game | tier1 | 340 | 0.638234 | 0.629029 | 0.009205 [-0.004132, 0.023389] | no |
| game | tier2 | 85 | 0.665902 | 0.652750 | 0.013152 [-0.013044, 0.040713] | no |
| game | tier3 | 9 | 0.563127 | 0.576544 | -0.013418 [-0.078895, 0.057018] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 340 | 0.638234 | 0.629029 | 0.009205 [-0.004132, 0.023389] | no |
| game | international=0 | 94 | 0.656062 | 0.645454 | 0.010608 [-0.014826, 0.037573] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 396 | 396 | 0.0505 | 8.60% [-3.86%, 21.69%] | $234.70 | 4.694× | 57.66% | $33.37 | 221 (175 unfilled) | 2.09% [-14.63%, 20.07%] | $84.35 |
| series | tier1 | 338 | 338 | 0.0471 | 8.49% [-4.52%, 22.22%] | $164.80 | 3.296× | 56.26% | $26.87 | 191 (147 unfilled) | -0.19% [-16.04%, 15.32%] | $55.77 |
| series | tier2 | 53 | 53 | 0.0578 | 7.02% [-33.27%, 50.64%] | $61.95 | 1.239× | 25.83% | $6.84 | 25 (28 unfilled) | 13.24% [-51.70%, 91.71%] | $59.63 |
| series | tier3 | 5 | 5 | 0.1990 | 33.23% [-72.58%, 150.57%] | $56.86 | 1.137× | 10.00% | $4.98 | 5 (0 unfilled) | 33.23% [-72.58%, 150.57%] | $61.60 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 338 | 338 | 0.0471 | 8.49% [-4.52%, 22.22%] | $164.80 | 3.296× | 56.26% | $26.87 | 191 (147 unfilled) | -0.19% [-16.04%, 15.32%] | $55.77 |
| series | international=0 | 58 | 58 | 0.0700 | 9.27% [-28.07%, 51.77%] | $70.46 | 1.409× | 25.83% | $6.84 | 30 (28 unfilled) | 16.56% [-42.85%, 84.31%] | $73.76 |
| game | all | 194 | 103 | 0.0413 | -10.31% [-23.29%, 2.99%] | $16.51 | 0.330× | 68.26% | $4.82 | 28 (166 unfilled) | -1.07% [-36.74%, 33.52%] | $41.17 |
| game | tier1 | 151 | 79 | 0.0437 | -7.87% [-22.60%, 7.20%] | $22.42 | 0.448× | 58.83% | $4.82 | 22 (129 unfilled) | 3.49% [-34.86%, 42.09%] | $42.54 |
| game | tier2 | 38 | 22 | 0.0350 | -20.02% [-52.01%, 13.07%] | $37.19 | 0.744× | 32.95% | $5.37 | 6 (32 unfilled) | -17.76% [-77.46%, 48.03%] | $48.40 |
| game | tier3 | 5 | 2 | 0.0179 | -10.28% [-47.80%, 46.00%] | $49.84 | 0.997× | 4.78% | $3.09 | 0 (5 unfilled) | — | $50.00 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 151 | 79 | 0.0437 | -7.87% [-22.60%, 7.20%] | $22.42 | 0.448× | 58.83% | $4.82 | 22 (129 unfilled) | 3.49% [-34.86%, 42.09%] | $42.54 |
| game | international=0 | 43 | 24 | 0.0330 | -18.90% [-50.14%, 15.01%] | $37.06 | 0.741× | 33.18% | $5.37 | 6 (37 unfilled) | -17.76% [-77.46%, 48.03%] | $48.40 |
| series+game | all | 590 | 413 | 0.0475 | 2.41% [-8.16%, 13.75%] | $132.15 | 2.643× | 69.41% | $18.78 | 249 (341 unfilled) | 1.74% [-13.77%, 18.49%] | $96.50 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 280 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2025-11 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2025-12 | series | 13 | 1.000000 | 0.000000 | unfitted |
| 2026-01 | series | 79 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 148 | 1.024833 | 0.329313 | fitted |
| 2026-03 | series | 249 | 0.980072 | 0.520549 | fitted |
| 2026-03 | game | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | series | 302 | 0.996591 | 0.680903 | fitted |
| 2026-04 | game | 15 | 1.000000 | 0.000000 | unfitted |
| 2026-05 | series | 379 | 0.923229 | 0.636004 | fitted |
| 2026-05 | game | 132 | 0.984265 | -0.906408 | fitted |
| 2026-06 | series | 544 | 0.951776 | 0.684757 | fitted |
| 2026-06 | game | 330 | 0.956411 | -0.283980 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 473 | 0.617835 | 0.626718 | -0.008883 [-0.019954, 0.001035] | no |
| series | tier1 | 401 | 0.610927 | 0.617017 | -0.006090 [-0.015486, 0.003737] | no |
| series | tier2 | 64 | 0.669449 | 0.679709 | -0.010260 [-0.044917, 0.023681] | no |
| series | tier3 | 8 | 0.551199 | 0.689027 | -0.137827 [-0.501959, 0.089839] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 401 | 0.610927 | 0.617017 | -0.006090 [-0.015486, 0.003737] | no |
| series | international=0 | 72 | 0.656311 | 0.680744 | -0.024434 [-0.076343, 0.019459] | no |
| game | all | 302 | 0.630558 | 0.623361 | 0.007197 [-0.004945, 0.019087] | no |
| game | tier1 | 237 | 0.621034 | 0.611859 | 0.009175 [-0.003066, 0.021929] | no |
| game | tier2 | 56 | 0.677910 | 0.679563 | -0.001653 [-0.033943, 0.029357] | no |
| game | tier3 | 9 | 0.586738 | 0.576544 | 0.010194 [-0.015022, 0.033912] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 237 | 0.621034 | 0.611859 | 0.009175 [-0.003066, 0.021929] | no |
| game | international=0 | 65 | 0.665286 | 0.665299 | -0.000013 [-0.029534, 0.029081] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 180 | 180 | 0.0346 | 11.53% [-9.28%, 34.29%] | $87.23 | 1.745× | 54.32% | $11.33 | 94 (86 unfilled) | 4.41% [-23.49%, 36.09%] | $57.32 |
| series | tier1 | 143 | 143 | 0.0295 | 7.40% [-13.60%, 31.59%] | $62.41 | 1.248× | 51.08% | $9.10 | 75 (68 unfilled) | -7.16% [-33.14%, 20.38%] | $43.65 |
| series | tier2 | 33 | 33 | 0.0372 | 26.88% [-30.78%, 94.25%] | $62.18 | 1.244× | 31.06% | $6.90 | 15 (18 unfilled) | 54.63% [-53.60%, 177.28%] | $56.13 |
| series | tier3 | 4 | 4 | 0.1979 | 31.89% [-100.00%, 174.07%] | $55.65 | 1.113× | 7.43% | $4.54 | 4 (0 unfilled) | 31.89% [-100.00%, 174.07%] | $58.62 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 143 | 143 | 0.0295 | 7.40% [-13.60%, 31.59%] | $62.41 | 1.248× | 51.08% | $9.10 | 75 (68 unfilled) | -7.16% [-33.14%, 20.38%] | $43.65 |
| series | international=0 | 37 | 37 | 0.0545 | 27.42% [-24.24%, 88.17%] | $69.19 | 1.384× | 31.06% | $6.90 | 19 (18 unfilled) | 49.86% [-40.37%, 153.11%] | $65.98 |
| game | all | 105 | 56 | 0.0325 | -15.68% [-39.01%, 8.87%] | $25.87 | 0.517× | 58.80% | $4.16 | 10 (95 unfilled) | 21.48% [-55.42%, 117.17%] | $55.12 |
| game | tier1 | 83 | 43 | 0.0302 | -25.11% [-49.03%, -1.33%] | $22.69 | 0.454× | 58.88% | $3.19 | 9 (74 unfilled) | -5.68% [-68.49%, 73.84%] | $49.42 |
| game | tier2 | 22 | 13 | 0.0413 | 20.05% [-34.91%, 83.76%] | $56.92 | 1.138× | 24.64% | $4.16 | 1 (21 unfilled) | 262.84% [262.84%, 262.84%] | $55.77 |
| game | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 83 | 43 | 0.0302 | -25.11% [-49.03%, -1.33%] | $22.69 | 0.454× | 58.88% | $3.19 | 9 (74 unfilled) | -5.68% [-68.49%, 73.84%] | $49.42 |
| game | international=0 | 22 | 13 | 0.0413 | 20.05% [-34.91%, 83.76%] | $56.92 | 1.138× | 24.64% | $4.16 | 1 (21 unfilled) | 262.84% [262.84%, 262.84%] | $55.77 |
| series+game | all | 285 | 208 | 0.0339 | 1.51% [-13.61%, 17.39%] | $70.49 | 1.410× | 61.46% | $10.46 | 104 (181 unfilled) | 6.06% [-19.76%, 35.86%] | $66.57 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| game | 2026-03 | 15 | 0.718992 | — | 0.669739 | -100.00% (2), $40.50 | — | 1 (1 unfilled) | -100.00% [-100.00%, -100.00%] | $45.12 | — | — | — |
| game | 2026-04 | 117 | 0.665575 | — | 0.651637 | -6.18% (39), $43.95 | — | 12 (27 unfilled) | 38.36% [-8.36%, 80.96%] | $56.14 | — | — | — |
| game | 2026-05 | 198 | 0.668084 | 0.663117 | 0.657045 | -9.51% (98), $28.89 | -8.67% (95), $29.81 | 6 (92 unfilled) | -33.09% [-100.00%, 50.67%] | $44.70 | 6 (89 unfilled) | 73.23% [-9.95%, 185.10%] | $57.49 |
| game | 2026-06 | 104 | 0.555112 | 0.568571 | 0.559231 | -11.42% (55), $40.94 | -82.00% (10), $43.40 | 9 (46 unfilled) | -21.37% [-70.32%, 21.66%] | $45.36 | 4 (6 unfilled) | -55.29% [-100.00%, 81.42%] | $47.94 |
| series | 2025-11 | 13 | 0.497080 | — | 0.588964 | 75.10% (10), $86.98 | — | 9 (1 unfilled) | 41.37% [-27.92%, 124.26%] | $70.68 | — | — | — |
| series | 2025-12 | 66 | 0.659065 | — | 0.640347 | -12.41% (47), $43.84 | — | 43 (4 unfilled) | -9.56% [-41.66%, 27.76%] | $48.47 | — | — | — |
| series | 2026-01 | 69 | 0.516827 | — | 0.506048 | -1.92% (50), $48.08 | — | 27 (23 unfilled) | -18.33% [-55.87%, 22.70%] | $37.36 | — | — | — |
| series | 2026-02 | 101 | 0.657209 | 0.661497 | 0.667211 | 18.93% (61), $54.98 | 52.07% (12), $64.51 | 18 (43 unfilled) | 23.30% [-32.41%, 82.06%] | $62.00 | 4 (8 unfilled) | 25.02% [-100.00%, 150.04%] | $53.67 |
| series | 2026-03 | 53 | 0.640887 | 0.650144 | 0.663787 | 41.69% (26), $85.45 | 29.36% (11), $58.68 | 21 (5 unfilled) | 35.53% [-13.45%, 82.28%] | $65.40 | 8 (3 unfilled) | 16.32% [-68.37%, 99.76%] | $55.12 |
| series | 2026-04 | 77 | 0.683900 | 0.682840 | 0.690287 | 19.26% (50), $61.49 | 25.12% (38), $55.54 | 34 (16 unfilled) | 30.51% [-25.33%, 92.50%] | $69.90 | 23 (15 unfilled) | 54.18% [-24.41%, 139.58%] | $62.00 |
| series | 2026-05 | 165 | 0.619934 | 0.620003 | 0.626943 | 6.09% (96), $100.77 | 12.45% (70), $69.67 | 25 (71 unfilled) | -28.62% [-71.72%, 18.96%] | $42.24 | 20 (50 unfilled) | -26.89% [-73.89%, 28.50%] | $42.17 |
| series | 2026-06 | 77 | 0.469550 | 0.468675 | 0.484035 | -8.25% (56), $33.60 | -14.37% (49), $36.92 | 44 (12 unfilled) | -11.28% [-41.70%, 19.24%] | $40.89 | 39 (10 unfilled) | -13.47% [-47.34%, 21.40%] | $45.67 |

### player_glicko_rookie_weights+form: Kalshi comparison and returns

form: rows=35654, H=3, w=0.97085

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 621 | 0.607889 | 0.613968 | -0.006079 [-0.021382, 0.008937] | no |
| series | tier1 | 528 | 0.603425 | 0.608069 | -0.004643 [-0.018617, 0.009598] | no |
| series | tier2 | 85 | 0.638447 | 0.643551 | -0.005104 [-0.049822, 0.036600] | no |
| series | tier3 | 8 | 0.577833 | 0.689027 | -0.111194 [-0.529670, 0.183708] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 528 | 0.603425 | 0.608069 | -0.004643 [-0.018617, 0.009598] | no |
| series | international=0 | 93 | 0.633233 | 0.647463 | -0.014230 [-0.066902, 0.035217] | no |
| game | all | 434 | 0.644148 | 0.632587 | 0.011561 [-0.001646, 0.025205] | no |
| game | tier1 | 340 | 0.641009 | 0.629029 | 0.011979 [-0.002923, 0.028421] | no |
| game | tier2 | 85 | 0.663201 | 0.652750 | 0.010450 [-0.016409, 0.038462] | no |
| game | tier3 | 9 | 0.582799 | 0.576544 | 0.006255 [-0.098994, 0.103344] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 340 | 0.641009 | 0.629029 | 0.011979 [-0.002923, 0.028421] | no |
| game | international=0 | 94 | 0.655503 | 0.645454 | 0.010049 [-0.016442, 0.037835] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 390 | 390 | 0.0584 | 6.80% [-6.54%, 19.80%] | $217.72 | 4.354× | 71.01% | $47.04 | 210 (180 unfilled) | 5.77% [-10.66%, 22.49%] | $98.29 |
| series | tier1 | 336 | 336 | 0.0550 | 4.71% [-8.39%, 17.50%] | $92.09 | 1.842× | 69.50% | $23.85 | 182 (154 unfilled) | 2.08% [-12.93%, 18.60%] | $48.58 |
| series | tier2 | 47 | 47 | 0.0691 | 18.06% [-26.85%, 67.21%] | $98.37 | 1.967× | 25.00% | $9.31 | 21 (26 unfilled) | 29.18% [-47.70%, 120.10%] | $72.78 |
| series | tier3 | 7 | 7 | 0.1485 | 30.96% [-63.81%, 131.19%] | $58.77 | 1.175× | 10.00% | $5.05 | 7 (0 unfilled) | 30.96% [-63.81%, 131.19%] | $63.70 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 336 | 336 | 0.0550 | 4.71% [-8.39%, 17.50%] | $92.09 | 1.842× | 69.50% | $23.85 | 182 (154 unfilled) | 2.08% [-12.93%, 18.60%] | $48.58 |
| series | international=0 | 54 | 54 | 0.0794 | 19.72% [-21.02%, 67.01%] | $115.68 | 2.314× | 25.00% | $9.95 | 28 (26 unfilled) | 29.62% [-34.38%, 101.58%] | $93.48 |
| game | all | 251 | 133 | 0.0433 | -11.05% [-22.25%, 0.43%] | $11.67 | 0.233× | 77.25% | $4.58 | 38 (213 unfilled) | -19.77% [-48.08%, 7.63%] | $39.66 |
| game | tier1 | 205 | 108 | 0.0437 | -9.58% [-22.40%, 2.79%] | $18.37 | 0.367× | 64.98% | $4.58 | 31 (174 unfilled) | -17.54% [-48.42%, 13.40%] | $41.12 |
| game | tier2 | 41 | 23 | 0.0406 | -18.50% [-48.98%, 14.35%] | $32.37 | 0.647× | 35.27% | $4.28 | 7 (34 unfilled) | -29.62% [-100.00%, 31.24%] | $48.23 |
| game | tier3 | 5 | 2 | 0.0488 | -10.28% [-47.80%, 46.00%] | $49.83 | 0.997× | 4.78% | $2.67 | 0 (5 unfilled) | — | $50.00 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 205 | 108 | 0.0437 | -9.58% [-22.40%, 2.79%] | $18.37 | 0.367× | 64.98% | $4.58 | 31 (174 unfilled) | -17.54% [-48.42%, 13.40%] | $41.12 |
| game | international=0 | 46 | 25 | 0.0415 | -17.61% [-44.87%, 12.16%] | $32.25 | 0.645× | 35.50% | $4.28 | 7 (39 unfilled) | -29.62% [-100.00%, 31.24%] | $48.23 |
| series+game | all | 641 | 429 | 0.0525 | -0.16% [-9.51%, 9.47%] | $97.52 | 1.950× | 76.65% | $28.05 | 248 (393 unfilled) | 1.87% [-13.33%, 17.58%] | $93.17 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 280 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2025-11 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2025-12 | series | 13 | 1.000000 | 0.000000 | unfitted |
| 2026-01 | series | 79 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 148 | 1.052801 | 0.458599 | fitted |
| 2026-03 | series | 249 | 0.976986 | 0.504298 | fitted |
| 2026-03 | game | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | series | 302 | 0.993726 | 0.715989 | fitted |
| 2026-04 | game | 15 | 1.000000 | 0.000000 | unfitted |
| 2026-05 | series | 379 | 0.923758 | 0.693496 | fitted |
| 2026-05 | game | 132 | 1.048416 | -0.257310 | fitted |
| 2026-06 | series | 544 | 0.941571 | 0.702932 | fitted |
| 2026-06 | game | 330 | 0.950461 | -0.089452 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 473 | 0.618525 | 0.626718 | -0.008193 [-0.021028, 0.003103] | no |
| series | tier1 | 401 | 0.612744 | 0.617017 | -0.004273 [-0.014920, 0.007237] | no |
| series | tier2 | 64 | 0.661291 | 0.679709 | -0.018418 [-0.056686, 0.019076] | no |
| series | tier3 | 8 | 0.566137 | 0.689027 | -0.122890 [-0.501277, 0.122953] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 401 | 0.612744 | 0.617017 | -0.004273 [-0.014920, 0.007237] | no |
| series | international=0 | 72 | 0.650719 | 0.680744 | -0.030026 [-0.083732, 0.017447] | no |
| game | all | 302 | 0.625613 | 0.623361 | 0.002252 [-0.001322, 0.005993] | no |
| game | tier1 | 237 | 0.614385 | 0.611859 | 0.002526 [-0.001468, 0.006527] | no |
| game | tier2 | 56 | 0.680169 | 0.679563 | 0.000606 [-0.008311, 0.010000] | no |
| game | tier3 | 9 | 0.581824 | 0.576544 | 0.005280 [-0.009598, 0.020289] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 237 | 0.614385 | 0.611859 | 0.002526 [-0.001468, 0.006527] | no |
| game | international=0 | 65 | 0.666552 | 0.665299 | 0.001253 [-0.006815, 0.009535] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 212 | 212 | 0.0409 | 8.43% [-8.79%, 28.09%] | $65.73 | 1.315× | 75.99% | $17.46 | 100 (112 unfilled) | 12.19% [-12.89%, 40.62%] | $79.72 |
| series | tier1 | 174 | 174 | 0.0364 | 2.76% [-15.01%, 20.79%] | $33.68 | 0.674× | 73.60% | $9.79 | 79 (95 unfilled) | 0.99% [-22.47%, 25.20%] | $42.99 |
| series | tier2 | 31 | 31 | 0.0485 | 35.00% [-22.89%, 104.29%] | $89.13 | 1.783× | 21.70% | $8.35 | 14 (17 unfilled) | 65.67% [-50.08%, 190.80%] | $74.69 |
| series | tier3 | 7 | 7 | 0.1183 | 30.96% [-63.81%, 131.19%] | $54.00 | 1.080× | 10.00% | $4.89 | 7 (0 unfilled) | 30.96% [-63.81%, 131.19%] | $58.49 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 174 | 174 | 0.0364 | 2.76% [-15.01%, 20.79%] | $33.68 | 0.674× | 73.60% | $9.79 | 79 (95 unfilled) | 0.99% [-22.47%, 25.20%] | $42.99 |
| series | international=0 | 38 | 38 | 0.0613 | 34.26% [-17.60%, 92.48%] | $96.31 | 1.926× | 21.70% | $8.72 | 21 (17 unfilled) | 54.14% [-26.00%, 145.21%] | $88.13 |
| game | all | 4 | 2 | 0.0071 | 0.18% [-10.97%, 11.27%] | $49.55 | 0.991× | 0.91% | $0.95 | 0 (4 unfilled) | — | $50.00 |
| game | tier1 | 2 | 1 | 0.0053 | 11.27% [11.27%, 11.27%] | $49.77 | 0.995× | 0.47% | $0.59 | 0 (2 unfilled) | — | $50.00 |
| game | tier2 | 2 | 1 | 0.0088 | -10.97% [-10.97%, -10.97%] | $49.78 | 0.996× | 0.44% | $0.95 | 0 (2 unfilled) | — | $50.00 |
| game | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 2 | 1 | 0.0053 | 11.27% [11.27%, 11.27%] | $49.77 | 0.995× | 0.47% | $0.59 | 0 (2 unfilled) | — | $50.00 |
| game | international=0 | 2 | 1 | 0.0088 | -10.97% [-10.97%, -10.97%] | $49.78 | 0.996× | 0.44% | $0.95 | 0 (2 unfilled) | — | $50.00 |
| series+game | all | 216 | 212 | 0.0403 | 8.28% [-8.56%, 27.58%] | $64.39 | 1.288× | 76.13% | $17.22 | 100 (116 unfilled) | 12.19% [-12.89%, 40.62%] | $79.72 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| game | 2026-03 | 15 | 0.721276 | — | 0.669739 | -60.40% (4), $39.89 | — | 3 (1 unfilled) | -47.12% [-100.00%, -20.42%] | $44.34 | — | — | — |
| game | 2026-04 | 117 | 0.663240 | — | 0.651637 | -4.84% (58), $37.93 | — | 16 (42 unfilled) | 0.41% [-42.69%, 41.15%] | $50.42 | — | — | — |
| game | 2026-05 | 198 | 0.670300 | 0.657867 | 0.657045 | -11.96% (123), $23.86 | 0.18% (4), $49.55 | 8 (115 unfilled) | -49.96% [-100.00%, 20.36%] | $45.79 | 0 (4 unfilled) | — | $50.00 |
| game | 2026-06 | 104 | 0.561756 | 0.564207 | 0.559231 | -11.84% (66), $41.76 | — (0), $50.00 | 11 (55 unfilled) | -19.61% [-65.77%, 25.56%] | $48.30 | 0 (0 unfilled) | — | $50.00 |
| series | 2025-11 | 13 | 0.482756 | — | 0.588964 | 39.07% (10), $70.39 | — | 10 (0 unfilled) | 39.07% [-22.11%, 117.29%] | $68.84 | — | — | — |
| series | 2025-12 | 66 | 0.657793 | — | 0.640347 | -6.22% (38), $34.50 | — | 35 (3 unfilled) | -4.67% [-43.08%, 38.74%] | $35.85 | — | — | — |
| series | 2026-01 | 69 | 0.514139 | — | 0.506048 | 2.48% (43), $56.23 | — | 22 (21 unfilled) | -25.72% [-69.55%, 25.32%] | $36.00 | — | — | — |
| series | 2026-02 | 101 | 0.662644 | 0.662525 | 0.667211 | 12.11% (69), $66.92 | 2.92% (31), $50.83 | 21 (48 unfilled) | 27.81% [-20.73%, 78.03%] | $72.86 | 7 (24 unfilled) | 35.87% [-35.84%, 107.75%] | $56.82 |
| series | 2026-03 | 53 | 0.630208 | 0.644814 | 0.663787 | 50.66% (22), $97.62 | 54.52% (11), $64.36 | 18 (4 unfilled) | 37.43% [-12.62%, 84.22%] | $73.74 | 9 (2 unfilled) | 46.86% [-26.08%, 113.99%] | $58.81 |
| series | 2026-04 | 77 | 0.680111 | 0.679545 | 0.690287 | 11.61% (50), $98.91 | 30.39% (39), $88.56 | 34 (16 unfilled) | 28.71% [-21.68%, 89.03%] | $96.52 | 26 (13 unfilled) | 49.16% [-16.48%, 124.91%] | $92.20 |
| series | 2026-05 | 165 | 0.619530 | 0.618497 | 0.626943 | 5.21% (96), $77.16 | 8.51% (77), $59.96 | 24 (72 unfilled) | -2.02% [-46.44%, 43.29%] | $43.68 | 19 (58 unfilled) | 5.73% [-45.50%, 66.14%] | $42.19 |
| series | 2026-06 | 77 | 0.485901 | 0.481754 | 0.484035 | -10.25% (62), $24.49 | -13.74% (54), $23.39 | 46 (16 unfilled) | -13.72% [-42.66%, 18.03%] | $31.64 | 39 (15 unfilled) | -21.46% [-52.68%, 13.39%] | $33.39 |

### player_glicko_rw_tier_revert+none: Kalshi comparison and returns

none

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 621 | 0.609789 | 0.613968 | -0.004179 [-0.018948, 0.010186] | no |
| series | tier1 | 528 | 0.604367 | 0.608069 | -0.003702 [-0.017037, 0.009706] | no |
| series | tier2 | 85 | 0.647905 | 0.643551 | 0.004353 [-0.039228, 0.045910] | no |
| series | tier3 | 8 | 0.562664 | 0.689027 | -0.126362 [-0.525966, 0.152407] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 528 | 0.604367 | 0.608069 | -0.003702 [-0.017037, 0.009706] | no |
| series | international=0 | 93 | 0.640572 | 0.647463 | -0.006891 [-0.058986, 0.041349] | no |
| game | all | 434 | 0.644292 | 0.632587 | 0.011705 [-0.000254, 0.024631] | no |
| game | tier1 | 340 | 0.641215 | 0.629029 | 0.012186 [-0.001264, 0.026881] | no |
| game | tier2 | 85 | 0.664571 | 0.652750 | 0.011821 [-0.013668, 0.038043] | no |
| game | tier3 | 9 | 0.568998 | 0.576544 | -0.007546 [-0.074506, 0.057651] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 340 | 0.641215 | 0.629029 | 0.012186 [-0.001264, 0.026881] | no |
| game | international=0 | 94 | 0.655420 | 0.645454 | 0.009966 [-0.014407, 0.035640] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 396 | 396 | 0.0515 | 5.16% [-7.20%, 19.08%] | $84.26 | 1.685× | 69.35% | $16.92 | 210 (186 unfilled) | -2.15% [-18.85%, 15.06%] | $49.50 |
| series | tier1 | 338 | 338 | 0.0480 | 4.83% [-8.45%, 18.27%] | $53.77 | 1.075× | 67.36% | $12.53 | 181 (157 unfilled) | -5.14% [-20.96%, 10.20%] | $34.66 |
| series | tier2 | 53 | 53 | 0.0597 | 4.65% [-35.75%, 51.00%] | $67.76 | 1.355× | 25.13% | $7.42 | 24 (29 unfilled) | 12.93% [-56.14%, 93.34%] | $57.58 |
| series | tier3 | 5 | 5 | 0.2027 | 33.23% [-72.58%, 150.57%] | $57.27 | 1.145× | 10.00% | $5.02 | 5 (0 unfilled) | 33.23% [-72.58%, 150.57%] | $62.07 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 338 | 338 | 0.0480 | 4.83% [-8.45%, 18.27%] | $53.77 | 1.075× | 67.36% | $12.53 | 181 (157 unfilled) | -5.14% [-20.96%, 10.20%] | $34.66 |
| series | international=0 | 58 | 58 | 0.0720 | 7.10% [-30.37%, 48.74%] | $77.64 | 1.553× | 25.13% | $7.42 | 29 (29 unfilled) | 16.41% [-46.56%, 87.55%] | $71.74 |
| game | all | 204 | 111 | 0.0387 | -11.88% [-25.36%, 1.97%] | $11.91 | 0.238× | 77.33% | $4.46 | 33 (171 unfilled) | -28.38% [-55.47%, 0.10%] | $37.98 |
| game | tier1 | 158 | 86 | 0.0404 | -11.98% [-26.96%, 4.02%] | $15.91 | 0.318× | 70.13% | $4.46 | 27 (131 unfilled) | -24.46% [-54.56%, 5.06%] | $40.14 |
| game | tier2 | 41 | 23 | 0.0345 | -11.68% [-48.36%, 26.78%] | $37.65 | 0.753× | 32.68% | $4.96 | 6 (35 unfilled) | -46.01% [-100.00%, 17.40%] | $47.34 |
| game | tier3 | 5 | 2 | 0.0175 | -10.28% [-47.80%, 46.00%] | $49.84 | 0.997× | 4.78% | $3.07 | 0 (5 unfilled) | — | $50.00 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 158 | 86 | 0.0404 | -11.98% [-26.96%, 4.02%] | $15.91 | 0.318× | 70.13% | $4.46 | 27 (131 unfilled) | -24.46% [-54.56%, 5.06%] | $40.14 |
| game | international=0 | 46 | 25 | 0.0327 | -11.53% [-44.26%, 24.20%] | $37.52 | 0.750× | 32.68% | $4.96 | 6 (40 unfilled) | -46.01% [-100.00%, 17.40%] | $47.34 |
| series+game | all | 600 | 413 | 0.0472 | -0.62% [-11.43%, 10.59%] | $40.64 | 0.813× | 73.13% | $10.04 | 243 (357 unfilled) | -5.70% [-20.63%, 9.10%] | $49.70 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 280 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2025-11 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2025-12 | series | 13 | 1.000000 | 0.000000 | unfitted |
| 2026-01 | series | 79 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 148 | 1.038620 | 0.284254 | fitted |
| 2026-03 | series | 249 | 0.978695 | 0.419897 | fitted |
| 2026-03 | game | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | series | 302 | 0.989828 | 0.600828 | fitted |
| 2026-04 | game | 15 | 1.000000 | 0.000000 | unfitted |
| 2026-05 | series | 379 | 0.907572 | 0.539980 | fitted |
| 2026-05 | game | 132 | 1.060490 | -1.076749 | fitted |
| 2026-06 | series | 544 | 0.933294 | 0.617130 | fitted |
| 2026-06 | game | 330 | 0.957777 | -0.328626 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 473 | 0.620093 | 0.626718 | -0.006625 [-0.016921, 0.002667] | no |
| series | tier1 | 401 | 0.613737 | 0.617017 | -0.003280 [-0.011768, 0.005814] | no |
| series | tier2 | 64 | 0.667933 | 0.679709 | -0.011776 [-0.043429, 0.018759] | no |
| series | tier3 | 8 | 0.555967 | 0.689027 | -0.133060 [-0.489131, 0.087395] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 401 | 0.613737 | 0.617017 | -0.003280 [-0.011768, 0.005814] | no |
| series | international=0 | 72 | 0.655492 | 0.680744 | -0.025252 [-0.074808, 0.016329] | no |
| game | all | 302 | 0.632242 | 0.623361 | 0.008881 [-0.004700, 0.022761] | no |
| game | tier1 | 237 | 0.620962 | 0.611859 | 0.009103 [-0.004821, 0.023512] | no |
| game | tier2 | 56 | 0.687490 | 0.679563 | 0.007927 [-0.029424, 0.047781] | no |
| game | tier3 | 9 | 0.585498 | 0.576544 | 0.008954 [-0.017190, 0.036034] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 237 | 0.620962 | 0.611859 | 0.009103 [-0.004821, 0.023512] | no |
| game | international=0 | 65 | 0.673368 | 0.665299 | 0.008069 [-0.024997, 0.043328] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 152 | 152 | 0.0331 | 9.11% [-13.47%, 34.06%] | $61.82 | 1.236× | 63.90% | $10.28 | 81 (71 unfilled) | 2.73% [-26.67%, 36.30%] | $52.09 |
| series | tier1 | 117 | 117 | 0.0282 | 4.07% [-20.10%, 29.43%] | $41.68 | 0.834× | 61.62% | $7.87 | 61 (56 unfilled) | -10.32% [-39.11%, 18.45%] | $37.59 |
| series | tier2 | 31 | 31 | 0.0315 | 25.10% [-35.36%, 93.78%] | $65.25 | 1.305× | 25.95% | $6.59 | 16 (15 unfilled) | 44.97% [-53.09%, 156.80%] | $59.69 |
| series | tier3 | 4 | 4 | 0.1878 | 31.89% [-100.00%, 174.07%] | $56.37 | 1.127× | 6.58% | $4.60 | 4 (0 unfilled) | 31.89% [-100.00%, 174.07%] | $58.81 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 117 | 117 | 0.0282 | 4.07% [-20.10%, 29.43%] | $41.68 | 0.834× | 61.62% | $7.87 | 61 (56 unfilled) | -10.32% [-39.11%, 18.45%] | $37.59 |
| series | international=0 | 35 | 35 | 0.0493 | 25.87% [-29.71%, 88.44%] | $73.53 | 1.471× | 25.95% | $6.59 | 20 (15 unfilled) | 42.36% [-40.84%, 145.42%] | $70.49 |
| game | all | 116 | 64 | 0.0366 | -12.55% [-32.56%, 9.73%] | $17.09 | 0.342× | 69.36% | $3.59 | 12 (104 unfilled) | 33.50% [-23.10%, 98.45%] | $52.31 |
| game | tier1 | 85 | 47 | 0.0353 | -21.51% [-42.88%, 1.12%] | $18.02 | 0.360× | 69.39% | $3.75 | 9 (76 unfilled) | 9.13% [-53.14%, 67.49%] | $49.94 |
| game | tier2 | 31 | 17 | 0.0401 | 12.16% [-28.99%, 63.61%] | $47.38 | 0.948× | 22.25% | $3.59 | 3 (28 unfilled) | 107.23% [13.80%, 262.84%] | $52.39 |
| game | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 85 | 47 | 0.0353 | -21.51% [-42.88%, 1.12%] | $18.02 | 0.360× | 69.39% | $3.75 | 9 (76 unfilled) | 9.13% [-53.14%, 67.49%] | $49.94 |
| game | international=0 | 31 | 17 | 0.0401 | 12.16% [-28.99%, 63.61%] | $47.38 | 0.948× | 22.25% | $3.59 | 3 (28 unfilled) | 107.23% [13.80%, 262.84%] | $52.39 |
| series+game | all | 268 | 185 | 0.0346 | -0.24% [-14.32%, 14.71%] | $26.41 | 0.528× | 81.48% | $8.39 | 93 (175 unfilled) | 6.68% [-20.14%, 36.18%] | $56.07 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| game | 2026-03 | 15 | 0.723979 | — | 0.669739 | -60.40% (4), $40.68 | — | 3 (1 unfilled) | -47.12% [-100.00%, -20.42%] | $45.20 | — | — | — |
| game | 2026-04 | 117 | 0.670035 | — | 0.651637 | -15.77% (42), $37.64 | — | 12 (30 unfilled) | 5.96% [-43.08%, 53.66%] | $51.74 | — | — | — |
| game | 2026-05 | 198 | 0.666538 | 0.666801 | 0.657045 | -3.93% (103), $28.06 | -7.71% (108), $19.38 | 7 (96 unfilled) | -70.81% [-100.00%, -12.20%] | $42.67 | 9 (99 unfilled) | 58.51% [-1.06%, 130.27%] | $53.53 |
| game | 2026-06 | 104 | 0.561484 | 0.566446 | 0.559231 | -20.23% (55), $35.47 | -77.48% (8), $44.09 | 11 (44 unfilled) | -33.55% [-78.57%, 9.12%] | $47.53 | 3 (5 unfilled) | -40.29% [-100.00%, 81.42%] | $48.85 |
| series | 2025-11 | 13 | 0.492040 | — | 0.588964 | 69.78% (11), $78.46 | — | 10 (1 unfilled) | 38.80% [-21.65%, 115.28%] | $73.15 | — | — | — |
| series | 2025-12 | 66 | 0.660436 | — | 0.640347 | -16.84% (42), $41.50 | — | 38 (4 unfilled) | -17.87% [-52.64%, 19.17%] | $43.62 | — | — | — |
| series | 2026-01 | 69 | 0.520734 | — | 0.506048 | -2.57% (47), $41.56 | — | 24 (23 unfilled) | -29.29% [-69.14%, 17.49%] | $28.10 | — | — | — |
| series | 2026-02 | 101 | 0.661449 | 0.663807 | 0.667211 | 13.24% (67), $41.20 | 86.07% (8), $57.56 | 18 (49 unfilled) | 27.10% [-27.72%, 79.57%] | $62.04 | 2 (6 unfilled) | 150.04% [92.31%, 207.22%] | $52.23 |
| series | 2026-03 | 53 | 0.638353 | 0.651275 | 0.663787 | 44.18% (23), $74.60 | 18.50% (8), $55.31 | 18 (5 unfilled) | 27.40% [-16.91%, 72.06%] | $60.01 | 6 (2 unfilled) | -5.00% [-74.92%, 78.62%] | $53.49 |
| series | 2026-04 | 77 | 0.687782 | 0.685066 | 0.690287 | 3.40% (50), $73.60 | 24.69% (35), $61.04 | 34 (16 unfilled) | 16.62% [-35.67%, 75.10%] | $79.94 | 23 (12 unfilled) | 43.02% [-28.88%, 126.01%] | $69.83 |
| series | 2026-05 | 165 | 0.619111 | 0.619338 | 0.626943 | 7.55% (97), $81.56 | 14.79% (56), $68.70 | 24 (73 unfilled) | -13.40% [-56.88%, 33.49%] | $39.74 | 16 (40 unfilled) | -8.67% [-66.65%, 55.67%] | $39.93 |
| series | 2026-06 | 77 | 0.480667 | 0.477934 | 0.484035 | -11.80% (59), $26.13 | -25.39% (45), $28.79 | 44 (15 unfilled) | -15.41% [-45.43%, 14.56%] | $35.09 | 34 (11 unfilled) | -26.42% [-61.59%, 10.57%] | $40.58 |

### player_glicko_rw_tier_revert+regional: Kalshi comparison and returns

regional: rows=7157, ridge=4, s=0.94909, effects: EU=0.182342, CIS=0.249189, NA=-0.105781, SA=-0.0681483, AS=0.1166, OCE=-0.0912786, AF=-0.282924

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 621 | 0.609197 | 0.613968 | -0.004771 [-0.019546, 0.009500] | no |
| series | tier1 | 528 | 0.603341 | 0.608069 | -0.004727 [-0.018142, 0.008697] | no |
| series | tier2 | 85 | 0.650077 | 0.643551 | 0.006526 [-0.037469, 0.047658] | no |
| series | tier3 | 8 | 0.561298 | 0.689027 | -0.127729 [-0.526335, 0.151052] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 528 | 0.603341 | 0.608069 | -0.004727 [-0.018142, 0.008697] | no |
| series | international=0 | 93 | 0.642440 | 0.647463 | -0.005023 [-0.057296, 0.043804] | no |
| game | all | 434 | 0.643513 | 0.632587 | 0.010927 [-0.001639, 0.024373] | no |
| game | tier1 | 340 | 0.640141 | 0.629029 | 0.011112 [-0.002667, 0.026086] | no |
| game | tier2 | 85 | 0.664892 | 0.652750 | 0.012142 [-0.014249, 0.040160] | no |
| game | tier3 | 9 | 0.568998 | 0.576544 | -0.007546 [-0.074506, 0.057651] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 340 | 0.640141 | 0.629029 | 0.011112 [-0.002667, 0.026086] | no |
| game | international=0 | 94 | 0.655711 | 0.645454 | 0.010257 [-0.014562, 0.037077] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 398 | 398 | 0.0516 | 4.80% [-7.24%, 17.64%] | $73.03 | 1.461× | 70.31% | $11.98 | 210 (188 unfilled) | -2.86% [-19.01%, 13.63%] | $43.24 |
| series | tier1 | 338 | 338 | 0.0483 | 3.61% [-9.08%, 17.07%] | $54.32 | 1.086× | 64.74% | $10.35 | 180 (158 unfilled) | -6.48% [-21.75%, 9.23%] | $31.18 |
| series | tier2 | 55 | 55 | 0.0585 | 9.50% [-30.56%, 53.54%] | $58.02 | 1.160× | 27.15% | $6.16 | 25 (30 unfilled) | 15.78% [-51.83%, 93.63%] | $57.90 |
| series | tier3 | 5 | 5 | 0.2036 | 33.23% [-72.58%, 150.57%] | $57.47 | 1.149× | 10.00% | $5.04 | 5 (0 unfilled) | 33.23% [-72.58%, 150.57%] | $62.29 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 338 | 338 | 0.0483 | 3.61% [-9.08%, 17.07%] | $54.32 | 1.086× | 64.74% | $10.35 | 180 (158 unfilled) | -6.48% [-21.75%, 9.23%] | $31.18 |
| series | international=0 | 60 | 60 | 0.0705 | 11.47% [-26.49%, 50.95%] | $66.69 | 1.334× | 27.15% | $6.16 | 30 (30 unfilled) | 18.67% [-41.08%, 87.07%] | $72.41 |
| game | all | 198 | 109 | 0.0401 | -7.93% [-22.09%, 6.40%] | $13.08 | 0.262× | 75.09% | $4.64 | 33 (165 unfilled) | -36.25% [-61.53%, -11.50%] | $34.95 |
| game | tier1 | 153 | 84 | 0.0416 | -8.68% [-22.80%, 6.82%] | $17.91 | 0.358× | 66.39% | $4.64 | 28 (125 unfilled) | -36.45% [-62.94%, -10.86%] | $36.79 |
| game | tier2 | 40 | 23 | 0.0370 | -4.80% [-41.18%, 33.56%] | $36.98 | 0.740× | 34.28% | $4.98 | 5 (35 unfilled) | -35.08% [-100.00%, 40.48%] | $47.49 |
| game | tier3 | 5 | 2 | 0.0175 | -10.28% [-47.80%, 46.00%] | $49.84 | 0.997× | 4.78% | $3.07 | 0 (5 unfilled) | — | $50.00 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 153 | 84 | 0.0416 | -8.68% [-22.80%, 6.82%] | $17.91 | 0.358× | 66.39% | $4.64 | 28 (125 unfilled) | -36.45% [-62.94%, -10.86%] | $36.79 |
| game | international=0 | 45 | 25 | 0.0349 | -5.41% [-40.02%, 31.17%] | $36.85 | 0.737× | 34.28% | $4.98 | 5 (40 unfilled) | -35.08% [-100.00%, 40.48%] | $47.49 |
| series+game | all | 596 | 413 | 0.0478 | 0.58% [-9.97%, 11.79%] | $43.76 | 0.875× | 70.31% | $8.18 | 243 (353 unfilled) | -7.38% [-22.20%, 6.92%] | $45.20 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 280 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2025-11 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2025-12 | series | 13 | 1.000000 | 0.000000 | unfitted |
| 2026-01 | series | 79 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 148 | 1.029503 | 0.204808 | fitted |
| 2026-03 | series | 249 | 0.964650 | 0.329246 | fitted |
| 2026-03 | game | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | series | 302 | 0.974895 | 0.524529 | fitted |
| 2026-04 | game | 15 | 1.000000 | 0.000000 | unfitted |
| 2026-05 | series | 379 | 0.887631 | 0.449930 | fitted |
| 2026-05 | game | 132 | 1.152023 | -1.293887 | fitted |
| 2026-06 | series | 544 | 0.923366 | 0.614175 | fitted |
| 2026-06 | game | 330 | 0.962214 | -0.295051 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 473 | 0.619901 | 0.626718 | -0.006817 [-0.016371, 0.002083] | no |
| series | tier1 | 401 | 0.613538 | 0.617017 | -0.003479 [-0.011460, 0.004800] | no |
| series | tier2 | 64 | 0.667859 | 0.679709 | -0.011850 [-0.041100, 0.016446] | no |
| series | tier3 | 8 | 0.555160 | 0.689027 | -0.133867 [-0.491104, 0.086502] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 401 | 0.613538 | 0.617017 | -0.003479 [-0.011460, 0.004800] | no |
| series | international=0 | 72 | 0.655337 | 0.680744 | -0.025407 [-0.073700, 0.013749] | no |
| game | all | 302 | 0.637286 | 0.623361 | 0.013925 [-0.002728, 0.030666] | no |
| game | tier1 | 237 | 0.625344 | 0.611859 | 0.013485 [-0.002550, 0.031231] | no |
| game | tier2 | 56 | 0.696314 | 0.679563 | 0.016751 [-0.029243, 0.068543] | no |
| game | tier3 | 9 | 0.584489 | 0.576544 | 0.007944 [-0.015535, 0.032217] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 237 | 0.625344 | 0.611859 | 0.013485 [-0.002550, 0.031231] | no |
| game | international=0 | 65 | 0.680831 | 0.665299 | 0.015532 [-0.024869, 0.059982] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 133 | 133 | 0.0319 | 16.89% [-9.04%, 45.46%] | $55.80 | 1.116× | 59.87% | $8.37 | 72 (61 unfilled) | 8.32% [-23.17%, 44.16%] | $57.21 |
| series | tier1 | 101 | 101 | 0.0268 | 10.61% [-17.16%, 41.38%] | $36.45 | 0.729× | 57.57% | $6.24 | 53 (48 unfilled) | -6.58% [-37.16%, 25.11%] | $40.34 |
| series | tier2 | 28 | 28 | 0.0277 | 37.28% [-26.97%, 109.58%] | $67.07 | 1.341× | 20.80% | $6.06 | 15 (13 unfilled) | 54.34% [-51.56%, 171.28%] | $60.99 |
| series | tier3 | 4 | 4 | 0.1886 | 31.89% [-100.00%, 174.07%] | $56.70 | 1.134× | 6.06% | $4.62 | 4 (0 unfilled) | 31.89% [-100.00%, 174.07%] | $58.83 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 101 | 101 | 0.0268 | 10.61% [-17.16%, 41.38%] | $36.45 | 0.729× | 57.57% | $6.24 | 53 (48 unfilled) | -6.58% [-37.16%, 25.11%] | $40.34 |
| series | international=0 | 32 | 32 | 0.0478 | 36.61% [-22.62%, 104.28%] | $76.04 | 1.521× | 20.80% | $6.20 | 19 (13 unfilled) | 49.64% [-35.67%, 156.98%] | $72.09 |
| game | all | 119 | 66 | 0.0496 | -17.49% [-35.13%, 0.33%] | $12.39 | 0.248× | 77.20% | $3.60 | 12 (107 unfilled) | 18.89% [-27.01%, 62.90%] | $52.92 |
| game | tier1 | 86 | 47 | 0.0475 | -23.86% [-43.85%, -1.61%] | $13.57 | 0.271× | 77.16% | $3.50 | 10 (76 unfilled) | 17.43% [-38.72%, 72.71%] | $51.63 |
| game | tier2 | 33 | 19 | 0.0552 | -0.79% [-34.60%, 35.17%] | $45.74 | 0.915× | 21.65% | $3.60 | 2 (31 unfilled) | 26.37% [13.80%, 38.70%] | $51.27 |
| game | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 86 | 47 | 0.0475 | -23.86% [-43.85%, -1.61%] | $13.57 | 0.271× | 77.16% | $3.50 | 10 (76 unfilled) | 17.43% [-38.72%, 72.71%] | $51.63 |
| game | international=0 | 33 | 19 | 0.0552 | -0.79% [-34.60%, 35.17%] | $45.74 | 0.915× | 21.65% | $3.60 | 2 (31 unfilled) | 26.37% [13.80%, 38.70%] | $51.27 |
| series+game | all | 252 | 172 | 0.0403 | 0.71% [-14.67%, 17.20%] | $14.64 | 0.293× | 87.73% | $6.73 | 84 (168 unfilled) | 9.82% [-18.28%, 41.58%] | $63.25 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| game | 2026-03 | 15 | 0.712120 | — | 0.669739 | -60.40% (4), $42.22 | — | 3 (1 unfilled) | -47.12% [-100.00%, -20.42%] | $46.90 | — | — | — |
| game | 2026-04 | 117 | 0.673479 | — | 0.651637 | -11.54% (41), $35.54 | — | 14 (27 unfilled) | -13.13% [-50.95%, 26.27%] | $46.06 | — | — | — |
| game | 2026-05 | 198 | 0.665113 | 0.674438 | 0.657045 | 0.77% (98), $29.14 | -13.89% (112), $13.91 | 5 (93 unfilled) | -100.00% [-100.00%, -100.00%] | $41.54 | 9 (103 unfilled) | 39.00% [-3.88%, 85.18%] | $53.86 |
| game | 2026-06 | 104 | 0.558785 | 0.566554 | 0.559231 | -16.93% (55), $38.23 | -74.36% (7), $44.60 | 11 (44 unfilled) | -33.55% [-78.57%, 9.12%] | $48.66 | 3 (4 unfilled) | -40.29% [-100.00%, 81.42%] | $49.12 |
| series | 2025-11 | 13 | 0.492173 | — | 0.588964 | 69.78% (11), $78.38 | — | 10 (1 unfilled) | 38.80% [-21.65%, 115.28%] | $73.22 | — | — | — |
| series | 2025-12 | 66 | 0.662930 | — | 0.640347 | -15.69% (43), $37.01 | — | 38 (5 unfilled) | -14.40% [-46.95%, 20.82%] | $38.74 | — | — | — |
| series | 2026-01 | 69 | 0.523263 | — | 0.506048 | -6.23% (50), $35.49 | — | 25 (25 unfilled) | -27.77% [-66.21%, 17.20%] | $28.08 | — | — | — |
| series | 2026-02 | 101 | 0.664265 | 0.665165 | 0.667211 | 6.84% (63), $32.90 | 181.03% (3), $51.78 | 15 (48 unfilled) | 8.15% [-44.65%, 65.70%] | $59.74 | 1 (2 unfilled) | 207.22% [207.22%, 207.22%] | $50.45 |
| series | 2026-03 | 53 | 0.636769 | 0.652981 | 0.663787 | 38.27% (24), $82.26 | 109.41% (2), $52.20 | 19 (5 unfilled) | 20.80% [-25.27%, 67.68%] | $64.31 | 2 (0 unfilled) | 109.41% [67.39%, 150.63%] | $52.20 |
| series | 2026-04 | 77 | 0.692266 | 0.686840 | 0.690287 | 5.23% (49), $56.40 | 37.91% (25), $61.06 | 34 (15 unfilled) | 16.19% [-34.63%, 76.97%] | $63.25 | 17 (8 unfilled) | 78.74% [-12.31%, 179.50%] | $72.36 |
| series | 2026-05 | 165 | 0.613872 | 0.617645 | 0.626943 | 12.44% (98), $124.23 | 28.47% (55), $65.84 | 23 (75 unfilled) | -1.66% [-48.80%, 49.73%] | $47.43 | 16 (39 unfilled) | -21.65% [-77.25%, 45.51%] | $41.97 |
| series | 2026-06 | 77 | 0.475605 | 0.475654 | 0.484035 | -11.51% (60), $29.18 | -21.55% (48), $31.99 | 46 (14 unfilled) | -16.84% [-46.55%, 12.98%] | $37.45 | 36 (12 unfilled) | -22.68% [-57.44%, 15.51%] | $43.34 |

### player_glicko_rw_tier_revert+calibration: Kalshi comparison and returns

calibration: ridge=4; tier1/online=0: rows=3058, T=0.8577; tier1/online=1: rows=11009, T=1.0896; tier2/online=0: rows=623, T=0.9326; tier2/online=1: rows=3405, T=1.0704; tier3/online=0: rows=2386, T=1.1190; tier3/online=1: rows=17650, T=0.9869; unknown/online=0: rows=7, T=1.0000

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 621 | 0.608068 | 0.613968 | -0.005901 [-0.020791, 0.008861] | no |
| series | tier1 | 528 | 0.602231 | 0.608069 | -0.005837 [-0.019282, 0.007678] | no |
| series | tier2 | 85 | 0.648759 | 0.643551 | 0.005208 [-0.038825, 0.045872] | no |
| series | tier3 | 8 | 0.560906 | 0.689027 | -0.128121 [-0.524714, 0.139427] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 528 | 0.602231 | 0.608069 | -0.005837 [-0.019282, 0.007678] | no |
| series | international=0 | 93 | 0.641202 | 0.647463 | -0.006261 [-0.057817, 0.042187] | no |
| game | all | 434 | 0.642965 | 0.632587 | 0.010378 [-0.002074, 0.023332] | no |
| game | tier1 | 340 | 0.639101 | 0.629029 | 0.010072 [-0.003740, 0.025070] | no |
| game | tier2 | 85 | 0.666146 | 0.652750 | 0.013396 [-0.014307, 0.042733] | no |
| game | tier3 | 9 | 0.569992 | 0.576544 | -0.006552 [-0.071402, 0.055966] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 340 | 0.639101 | 0.629029 | 0.010072 [-0.003740, 0.025070] | no |
| game | international=0 | 94 | 0.656940 | 0.645454 | 0.011486 [-0.014900, 0.039937] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 394 | 394 | 0.0518 | 8.88% [-4.39%, 22.46%] | $172.54 | 3.451× | 62.76% | $26.67 | 215 (179 unfilled) | 2.20% [-14.92%, 18.66%] | $62.53 |
| series | tier1 | 336 | 336 | 0.0486 | 8.82% [-4.71%, 22.88%] | $117.01 | 2.340× | 62.75% | $20.73 | 186 (150 unfilled) | -0.68% [-16.64%, 15.54%] | $47.37 |
| series | tier2 | 53 | 53 | 0.0583 | 7.00% [-32.95%, 52.20%] | $64.29 | 1.286× | 25.77% | $7.30 | 24 (29 unfilled) | 18.02% [-47.19%, 96.68%] | $54.36 |
| series | tier3 | 5 | 5 | 0.1977 | 33.23% [-72.58%, 150.57%] | $56.71 | 1.134× | 10.00% | $4.97 | 5 (0 unfilled) | 33.23% [-72.58%, 150.57%] | $61.44 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 336 | 336 | 0.0486 | 8.82% [-4.71%, 22.88%] | $117.01 | 2.340× | 62.75% | $20.73 | 186 (150 unfilled) | -0.68% [-16.64%, 15.54%] | $47.37 |
| series | international=0 | 58 | 58 | 0.0703 | 9.25% [-26.60%, 53.11%] | $72.91 | 1.458× | 25.77% | $7.30 | 29 (29 unfilled) | 20.63% [-41.54%, 92.66%] | $66.90 |
| game | all | 201 | 109 | 0.0430 | -11.22% [-23.82%, 1.79%] | $15.39 | 0.308× | 70.91% | $4.50 | 30 (171 unfilled) | -13.91% [-42.26%, 16.60%] | $44.07 |
| game | tier1 | 158 | 85 | 0.0443 | -10.97% [-25.00%, 3.21%] | $20.27 | 0.405× | 63.47% | $4.50 | 24 (134 unfilled) | -12.95% [-46.98%, 20.01%] | $45.65 |
| game | tier2 | 38 | 22 | 0.0412 | -12.41% [-42.78%, 18.67%] | $38.28 | 0.766× | 30.99% | $4.48 | 6 (32 unfilled) | -17.76% [-77.46%, 48.03%] | $48.29 |
| game | tier3 | 5 | 2 | 0.0154 | -10.28% [-47.80%, 46.00%] | $49.77 | 0.995× | 4.78% | $3.06 | 0 (5 unfilled) | — | $50.00 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 158 | 85 | 0.0443 | -10.97% [-25.00%, 3.21%] | $20.27 | 0.405× | 63.47% | $4.50 | 24 (134 unfilled) | -12.95% [-46.98%, 20.01%] | $45.65 |
| game | international=0 | 43 | 24 | 0.0382 | -12.16% [-42.38%, 18.77%] | $38.10 | 0.762× | 31.31% | $4.48 | 6 (37 unfilled) | -17.76% [-77.46%, 48.03%] | $48.29 |
| series+game | all | 595 | 415 | 0.0488 | 2.12% [-8.03%, 13.48%] | $98.48 | 1.970× | 66.91% | $14.29 | 245 (350 unfilled) | 0.24% [-15.10%, 16.37%] | $66.61 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 280 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2025-11 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2025-12 | series | 13 | 1.000000 | 0.000000 | unfitted |
| 2026-01 | series | 79 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 148 | 1.027527 | 0.253969 | fitted |
| 2026-03 | series | 249 | 0.982368 | 0.454410 | fitted |
| 2026-03 | game | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | series | 302 | 0.999658 | 0.610493 | fitted |
| 2026-04 | game | 15 | 1.000000 | 0.000000 | unfitted |
| 2026-05 | series | 379 | 0.923144 | 0.567784 | fitted |
| 2026-05 | game | 132 | 0.973495 | -0.929436 | fitted |
| 2026-06 | series | 544 | 0.948619 | 0.654882 | fitted |
| 2026-06 | game | 330 | 0.957857 | -0.219153 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 473 | 0.618458 | 0.626718 | -0.008260 [-0.018586, 0.001013] | no |
| series | tier1 | 401 | 0.611560 | 0.617017 | -0.005457 [-0.014002, 0.003331] | no |
| series | tier2 | 64 | 0.669601 | 0.679709 | -0.010108 [-0.041842, 0.020841] | no |
| series | tier3 | 8 | 0.555065 | 0.689027 | -0.133961 [-0.493511, 0.087988] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 401 | 0.611560 | 0.617017 | -0.005457 [-0.014002, 0.003331] | no |
| series | international=0 | 72 | 0.656875 | 0.680744 | -0.023869 [-0.072877, 0.016951] | no |
| game | all | 302 | 0.631852 | 0.623361 | 0.008492 [-0.004906, 0.021770] | no |
| game | tier1 | 237 | 0.622077 | 0.611859 | 0.010218 [-0.003559, 0.024724] | no |
| game | tier2 | 56 | 0.681020 | 0.679563 | 0.001457 [-0.034064, 0.034692] | no |
| game | tier3 | 9 | 0.583356 | 0.576544 | 0.006811 [-0.012001, 0.025779] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 237 | 0.622077 | 0.611859 | 0.010218 [-0.003559, 0.024724] | no |
| game | international=0 | 65 | 0.667497 | 0.665299 | 0.002198 [-0.029236, 0.032965] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 151 | 151 | 0.0337 | 18.30% [-5.13%, 41.32%] | $58.96 | 1.179× | 59.14% | $8.34 | 85 (66 unfilled) | 13.53% [-15.88%, 46.04%] | $55.07 |
| series | tier1 | 117 | 117 | 0.0289 | 16.20% [-8.92%, 43.79%] | $43.08 | 0.862× | 55.23% | $6.79 | 65 (52 unfilled) | 4.63% [-24.05%, 37.08%] | $43.88 |
| series | tier2 | 30 | 30 | 0.0315 | 24.62% [-32.61%, 95.44%] | $59.59 | 1.192× | 33.91% | $6.65 | 16 (14 unfilled) | 44.97% [-53.09%, 156.80%] | $54.00 |
| series | tier3 | 4 | 4 | 0.1905 | 31.89% [-100.00%, 174.07%] | $56.83 | 1.137× | 5.83% | $4.63 | 4 (0 unfilled) | 31.89% [-100.00%, 174.07%] | $58.83 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 117 | 117 | 0.0289 | 16.20% [-8.92%, 43.79%] | $43.08 | 0.862× | 55.23% | $6.79 | 65 (52 unfilled) | 4.63% [-24.05%, 37.08%] | $43.88 |
| series | international=0 | 34 | 34 | 0.0502 | 25.47% [-30.33%, 87.62%] | $67.75 | 1.355× | 33.91% | $6.65 | 20 (14 unfilled) | 42.36% [-40.84%, 145.42%] | $63.65 |
| game | all | 111 | 61 | 0.0408 | -11.76% [-33.08%, 9.69%] | $25.13 | 0.503× | 62.56% | $4.03 | 9 (102 unfilled) | 35.15% [-44.51%, 122.15%] | $59.53 |
| game | tier1 | 87 | 47 | 0.0392 | -19.66% [-43.29%, 3.77%] | $21.81 | 0.436× | 62.60% | $3.17 | 8 (79 unfilled) | 6.28% [-63.91%, 77.12%] | $52.72 |
| game | tier2 | 24 | 14 | 0.0466 | 17.07% [-32.92%, 75.31%] | $57.61 | 1.152× | 25.21% | $4.03 | 1 (23 unfilled) | 262.84% [262.84%, 262.84%] | $56.48 |
| game | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 87 | 47 | 0.0392 | -19.66% [-43.29%, 3.77%] | $21.81 | 0.436× | 62.60% | $3.17 | 8 (79 unfilled) | 6.28% [-63.91%, 77.12%] | $52.72 |
| game | international=0 | 24 | 14 | 0.0466 | 17.07% [-32.92%, 75.31%] | $57.61 | 1.152× | 25.21% | $4.03 | 1 (23 unfilled) | 262.84% [262.84%, 262.84%] | $56.48 |
| series+game | all | 262 | 187 | 0.0367 | 5.57% [-9.72%, 22.60%] | $39.92 | 0.798× | 72.29% | $8.34 | 94 (168 unfilled) | 15.60% [-12.88%, 47.12%] | $68.52 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| game | 2026-03 | 15 | 0.716070 | — | 0.669739 | -68.47% (5), $41.59 | — | 3 (2 unfilled) | -47.12% [-100.00%, -20.42%] | $46.28 | — | — | — |
| game | 2026-04 | 117 | 0.666213 | — | 0.651637 | -4.60% (36), $43.78 | — | 12 (24 unfilled) | 38.36% [-8.36%, 80.96%] | $55.84 | — | — | — |
| game | 2026-05 | 198 | 0.669175 | 0.666175 | 0.657045 | -10.07% (108), $27.27 | -9.27% (106), $26.55 | 6 (102 unfilled) | -65.85% [-100.00%, 2.62%] | $44.25 | 6 (100 unfilled) | 73.23% [-9.95%, 185.10%] | $61.09 |
| game | 2026-06 | 104 | 0.556365 | 0.566508 | 0.559231 | -12.71% (52), $39.46 | -64.13% (5), $47.33 | 9 (43 unfilled) | -38.11% [-85.20%, 2.66%] | $48.21 | 3 (2 unfilled) | -40.29% [-100.00%, 81.42%] | $48.72 |
| series | 2025-11 | 13 | 0.500788 | — | 0.588964 | 82.12% (9), $85.73 | — | 8 (1 unfilled) | 45.18% [-28.58%, 135.94%] | $69.79 | — | — | — |
| series | 2025-12 | 66 | 0.663546 | — | 0.640347 | -8.34% (45), $43.36 | — | 41 (4 unfilled) | -4.96% [-38.39%, 33.49%] | $46.26 | — | — | — |
| series | 2026-01 | 69 | 0.517443 | — | 0.506048 | 1.03% (50), $45.50 | — | 25 (25 unfilled) | -23.16% [-61.65%, 20.45%] | $31.59 | — | — | — |
| series | 2026-02 | 101 | 0.658294 | 0.662843 | 0.667211 | 15.34% (62), $52.11 | 163.24% (5), $57.50 | 17 (45 unfilled) | 20.92% [-31.42%, 72.32%] | $61.18 | 2 (3 unfilled) | 150.04% [92.31%, 207.22%] | $52.06 |
| series | 2026-03 | 53 | 0.641755 | 0.652199 | 0.663787 | 31.80% (25), $78.67 | 42.59% (8), $54.51 | 20 (5 unfilled) | 22.87% [-28.22%, 74.05%] | $63.25 | 6 (2 unfilled) | 54.91% [-32.63%, 142.30%] | $53.68 |
| series | 2026-04 | 77 | 0.684790 | 0.683705 | 0.690287 | 20.50% (51), $58.55 | 19.91% (36), $50.45 | 35 (16 unfilled) | 31.99% [-23.38%, 94.80%] | $67.61 | 24 (12 unfilled) | 55.65% [-18.96%, 138.33%] | $59.21 |
| series | 2026-05 | 165 | 0.618075 | 0.618824 | 0.626943 | 10.99% (96), $105.37 | 31.86% (56), $66.50 | 24 (72 unfilled) | -18.66% [-59.98%, 30.83%] | $45.11 | 16 (40 unfilled) | -8.62% [-64.63%, 58.74%] | $45.77 |
| series | 2026-06 | 77 | 0.472600 | 0.470984 | 0.484035 | -13.79% (56), $30.92 | -19.65% (46), $34.84 | 45 (11 unfilled) | -13.27% [-42.95%, 17.45%] | $40.42 | 37 (9 unfilled) | -18.40% [-50.53%, 18.02%] | $45.11 |

### player_glicko_rw_tier_revert+form: Kalshi comparison and returns

form: rows=35654, H=3, w=1.03045

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 621 | 0.608556 | 0.613968 | -0.005413 [-0.020982, 0.010501] | no |
| series | tier1 | 528 | 0.604640 | 0.608069 | -0.003428 [-0.017710, 0.011002] | no |
| series | tier2 | 85 | 0.635100 | 0.643551 | -0.008452 [-0.053678, 0.033674] | no |
| series | tier3 | 8 | 0.584936 | 0.689027 | -0.104091 [-0.521145, 0.193281] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 528 | 0.604640 | 0.608069 | -0.003428 [-0.017710, 0.011002] | no |
| series | international=0 | 93 | 0.630785 | 0.647463 | -0.016679 [-0.069721, 0.032746] | no |
| game | all | 434 | 0.644494 | 0.632587 | 0.011907 [-0.001052, 0.025568] | no |
| game | tier1 | 340 | 0.641462 | 0.629029 | 0.012432 [-0.002528, 0.028754] | no |
| game | tier2 | 85 | 0.661672 | 0.652750 | 0.008922 [-0.016885, 0.036076] | no |
| game | tier3 | 9 | 0.596786 | 0.576544 | 0.020242 [-0.078192, 0.096523] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 340 | 0.641462 | 0.629029 | 0.012432 [-0.002528, 0.028754] | no |
| game | international=0 | 94 | 0.655460 | 0.645454 | 0.010006 [-0.015062, 0.036262] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 391 | 391 | 0.0593 | 5.54% [-7.45%, 19.13%] | $178.74 | 3.575× | 70.45% | $39.59 | 212 (179 unfilled) | 4.36% [-12.00%, 21.11%] | $71.92 |
| series | tier1 | 331 | 331 | 0.0566 | 3.65% [-9.32%, 17.57%] | $79.65 | 1.593× | 68.97% | $20.46 | 181 (150 unfilled) | 0.34% [-15.89%, 17.03%] | $44.07 |
| series | tier2 | 53 | 53 | 0.0643 | 13.91% [-25.28%, 58.56%] | $96.58 | 1.932× | 24.53% | $9.53 | 24 (29 unfilled) | 26.72% [-43.12%, 109.44%] | $66.44 |
| series | tier3 | 7 | 7 | 0.1502 | 30.96% [-63.81%, 131.19%] | $56.67 | 1.133× | 10.00% | $5.05 | 7 (0 unfilled) | 30.96% [-63.81%, 131.19%] | $61.43 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 331 | 331 | 0.0566 | 3.65% [-9.32%, 17.57%] | $79.65 | 1.593× | 68.97% | $20.46 | 181 (150 unfilled) | 0.34% [-15.89%, 17.03%] | $44.07 |
| series | international=0 | 60 | 60 | 0.0743 | 15.89% [-22.29%, 58.41%] | $109.48 | 2.190× | 24.53% | $9.77 | 31 (29 unfilled) | 27.68% [-30.99%, 98.22%] | $82.13 |
| game | all | 252 | 131 | 0.0407 | -12.20% [-23.67%, -0.16%] | $11.75 | 0.235× | 77.77% | $4.61 | 36 (216 unfilled) | -23.84% [-53.55%, 6.38%] | $41.72 |
| game | tier1 | 204 | 105 | 0.0408 | -11.24% [-24.23%, 1.58%] | $16.69 | 0.334× | 69.84% | $4.61 | 30 (174 unfilled) | -18.73% [-52.09%, 12.35%] | $44.31 |
| game | tier2 | 43 | 24 | 0.0405 | -16.97% [-46.08%, 12.35%] | $35.61 | 0.712× | 29.59% | $4.45 | 6 (37 unfilled) | -49.31% [-100.00%, 7.43%] | $47.08 |
| game | tier3 | 5 | 2 | 0.0373 | -10.28% [-47.80%, 46.00%] | $49.85 | 0.997× | 4.78% | $2.79 | 0 (5 unfilled) | — | $50.00 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 204 | 105 | 0.0408 | -11.24% [-24.23%, 1.58%] | $16.69 | 0.334× | 69.84% | $4.61 | 30 (174 unfilled) | -18.73% [-52.09%, 12.35%] | $44.31 |
| game | international=0 | 48 | 26 | 0.0402 | -16.28% [-44.41%, 11.56%] | $35.48 | 0.710× | 29.83% | $4.45 | 6 (42 unfilled) | -49.31% [-100.00%, 7.43%] | $47.08 |
| series+game | all | 643 | 420 | 0.0520 | -1.39% [-11.07%, 9.00%] | $80.50 | 1.610× | 76.48% | $18.64 | 248 (395 unfilled) | 0.28% [-15.07%, 15.67%] | $67.98 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 280 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2025-11 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2025-12 | series | 13 | 1.000000 | 0.000000 | unfitted |
| 2026-01 | series | 79 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 148 | 1.059396 | 0.387792 | fitted |
| 2026-03 | series | 249 | 0.991066 | 0.465783 | fitted |
| 2026-03 | game | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | series | 302 | 1.013708 | 0.683377 | fitted |
| 2026-04 | game | 15 | 1.000000 | 0.000000 | unfitted |
| 2026-05 | series | 379 | 0.937814 | 0.658842 | fitted |
| 2026-05 | game | 132 | 1.029917 | -0.223138 | fitted |
| 2026-06 | series | 544 | 0.951765 | 0.701457 | fitted |
| 2026-06 | game | 330 | 0.941810 | -0.043861 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 473 | 0.618738 | 0.626718 | -0.007980 [-0.019995, 0.002780] | no |
| series | tier1 | 401 | 0.612861 | 0.617017 | -0.004156 [-0.014025, 0.006761] | no |
| series | tier2 | 64 | 0.661513 | 0.679709 | -0.018196 [-0.053480, 0.016813] | no |
| series | tier3 | 8 | 0.571107 | 0.689027 | -0.117920 [-0.495688, 0.127983] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 401 | 0.612861 | 0.617017 | -0.004156 [-0.014025, 0.006761] | no |
| series | international=0 | 72 | 0.651468 | 0.680744 | -0.029277 [-0.081687, 0.015917] | no |
| game | all | 302 | 0.625502 | 0.623361 | 0.002141 [-0.000952, 0.005266] | no |
| game | tier1 | 237 | 0.614119 | 0.611859 | 0.002260 [-0.001178, 0.005694] | no |
| game | tier2 | 56 | 0.680745 | 0.679563 | 0.001182 [-0.006294, 0.009125] | no |
| game | tier3 | 9 | 0.581521 | 0.576544 | 0.004976 [-0.005989, 0.015419] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 237 | 0.614119 | 0.611859 | 0.002260 [-0.001178, 0.005694] | no |
| game | international=0 | 65 | 0.667007 | 0.665299 | 0.001708 [-0.005106, 0.008723] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 200 | 200 | 0.0391 | 12.13% [-5.70%, 32.00%] | $60.09 | 1.202× | 74.84% | $15.34 | 94 (106 unfilled) | 15.97% [-10.84%, 45.96%] | $70.77 |
| series | tier1 | 160 | 160 | 0.0354 | 7.23% [-11.82%, 27.08%] | $36.50 | 0.730× | 72.48% | $9.97 | 72 (88 unfilled) | 6.38% [-18.99%, 32.03%] | $46.44 |
| series | tier2 | 33 | 33 | 0.0402 | 31.81% [-22.48%, 97.12%] | $76.77 | 1.535× | 22.31% | $7.27 | 15 (18 unfilled) | 54.83% [-48.60%, 186.29%] | $63.82 |
| series | tier3 | 7 | 7 | 0.1184 | 30.96% [-63.81%, 131.19%] | $52.75 | 1.055× | 10.00% | $4.90 | 7 (0 unfilled) | 30.96% [-63.81%, 131.19%] | $57.14 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 160 | 160 | 0.0354 | 7.23% [-11.82%, 27.08%] | $36.50 | 0.730× | 72.48% | $9.97 | 72 (88 unfilled) | 6.38% [-18.99%, 32.03%] | $46.44 |
| series | international=0 | 40 | 40 | 0.0539 | 31.66% [-18.63%, 89.58%] | $81.03 | 1.621× | 22.31% | $7.52 | 22 (18 unfilled) | 47.26% [-27.36%, 138.49%] | $73.37 |
| game | all | 3 | 2 | 0.0007 | -40.84% [-100.00%, -10.97%] | $49.92 | 0.998× | 0.16% | $0.07 | 0 (3 unfilled) | — | $50.00 |
| game | tier1 | 1 | 1 | 0.0006 | -100.00% [-100.00%, -100.00%] | $49.95 | 0.999× | 0.10% | $0.04 | 0 (1 unfilled) | — | $50.00 |
| game | tier2 | 2 | 1 | 0.0007 | -10.97% [-10.97%, -10.97%] | $49.97 | 0.999× | 0.06% | $0.07 | 0 (2 unfilled) | — | $50.00 |
| game | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 1 | 1 | 0.0006 | -100.00% [-100.00%, -100.00%] | $49.95 | 0.999× | 0.10% | $0.04 | 0 (1 unfilled) | — | $50.00 |
| game | international=0 | 2 | 1 | 0.0007 | -10.97% [-10.97%, -10.97%] | $49.97 | 0.999× | 0.06% | $0.07 | 0 (2 unfilled) | — | $50.00 |
| series+game | all | 203 | 200 | 0.0385 | 11.35% [-6.24%, 30.99%] | $59.95 | 1.199× | 74.86% | $15.32 | 94 (109 unfilled) | 15.97% [-10.84%, 45.96%] | $70.77 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| game | 2026-03 | 15 | 0.713904 | — | 0.669739 | -60.40% (4), $41.98 | — | 3 (1 unfilled) | -47.12% [-100.00%, -20.42%] | $46.64 | — | — | — |
| game | 2026-04 | 117 | 0.662472 | — | 0.651637 | -5.78% (59), $37.80 | — | 15 (44 unfilled) | -3.14% [-46.64%, 41.08%] | $49.91 | — | — | — |
| game | 2026-05 | 198 | 0.668705 | 0.657906 | 0.657045 | -13.64% (125), $25.42 | -40.84% (3), $49.92 | 8 (117 unfilled) | -49.96% [-100.00%, 20.36%] | $44.24 | 0 (3 unfilled) | — | $50.00 |
| game | 2026-06 | 104 | 0.568162 | 0.563810 | 0.559231 | -12.32% (64), $37.36 | — (0), $50.00 | 10 (54 unfilled) | -26.91% [-79.37%, 20.02%] | $50.57 | 0 (0 unfilled) | — | $50.00 |
| series | 2025-11 | 13 | 0.487205 | — | 0.588964 | 39.07% (10), $74.04 | — | 10 (0 unfilled) | 39.07% [-22.11%, 117.29%] | $72.50 | — | — | — |
| series | 2025-12 | 66 | 0.662092 | — | 0.640347 | -5.87% (38), $34.38 | — | 35 (3 unfilled) | -4.29% [-40.23%, 38.90%] | $35.83 | — | — | — |
| series | 2026-01 | 69 | 0.515316 | — | 0.506048 | -7.87% (48), $60.19 | — | 27 (21 unfilled) | -27.40% [-64.69%, 17.72%] | $31.57 | — | — | — |
| series | 2026-02 | 101 | 0.662148 | 0.662807 | 0.667211 | 19.45% (66), $56.52 | 2.58% (26), $55.35 | 18 (48 unfilled) | 28.28% [-25.78%, 83.56%] | $66.21 | 5 (21 unfilled) | 61.56% [-32.71%, 146.24%] | $56.66 |
| series | 2026-03 | 53 | 0.629944 | 0.646184 | 0.663787 | 46.45% (23), $91.79 | 82.38% (8), $61.69 | 18 (5 unfilled) | 40.57% [-3.33%, 84.36%] | $72.09 | 6 (2 unfilled) | 80.12% [4.50%, 142.06%] | $57.58 |
| series | 2026-04 | 77 | 0.680096 | 0.680531 | 0.690287 | 9.44% (51), $95.44 | 28.78% (41), $78.10 | 36 (15 unfilled) | 21.52% [-27.25%, 80.38%] | $94.61 | 27 (14 unfilled) | 50.81% [-10.54%, 121.47%] | $84.52 |
| series | 2026-05 | 165 | 0.617346 | 0.616843 | 0.626943 | 4.65% (96), $82.42 | 19.11% (74), $63.30 | 22 (74 unfilled) | 7.07% [-39.83%, 58.78%] | $45.94 | 18 (56 unfilled) | 4.43% [-49.45%, 61.87%] | $44.11 |
| series | 2026-06 | 77 | 0.491312 | 0.484310 | 0.484035 | -15.18% (59), $21.83 | -17.49% (51), $21.93 | 46 (13 unfilled) | -16.06% [-46.03%, 15.42%] | $29.93 | 38 (13 unfilled) | -19.35% [-54.20%, 16.06%] | $32.43 |

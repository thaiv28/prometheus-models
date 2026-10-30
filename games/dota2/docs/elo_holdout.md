# Elo variants benchmark

## Combined summary (validation, all sections)

| Model | Series Δ log loss | Series flat ROI | Series Kelly (LoL caps) $ | Series flat ROI depth-capped | Series Kelly depth-capped $ | Game Δ log loss | Game flat ROI | Game Kelly (LoL caps) $ | Game flat ROI depth-capped | Game Kelly depth-capped $ | Series blended Δ log loss | Series blended flat ROI | Series blended Kelly (LoL caps) $ | Series blended flat ROI depth-capped | Series blended Kelly depth-capped $ | Game blended Δ log loss | Game blended flat ROI | Game blended Kelly (LoL caps) $ | Game blended flat ROI depth-capped | Game blended Kelly depth-capped $ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| team_elo | 0.024959 | -5.19% | $0.91 | -7.32% | $4.40 | 0.025598 | -4.79% | $16.81 | -20.95% | $33.66 | 0.004297 | -10.37% | $32.56 | -26.86% | $39.46 | 0.071630 | -22.87% | $10.76 | -16.98% | $44.32 |
| player_glicko | -0.000787 | 2.51% | $61.17 | 0.49% | $48.14 | 0.010214 | -6.61% | $15.58 | -21.16% | $41.30 | -0.004193 | 11.82% | $88.24 | 12.31% | $74.91 | 0.005517 | -2.68% | $34.20 | 38.11% | $50.56 |
| player_glicko_rw_tier_revert | -0.004179 | 5.16% | $84.26 | -2.15% | $49.50 | 0.011705 | -11.88% | $11.91 | -28.38% | $37.98 | -0.006625 | 9.11% | $61.82 | 2.73% | $52.09 | 0.008881 | -12.55% | $17.09 | 33.50% | $52.31 |
| team_elo+none | 0.024959 | -5.19% | $0.91 | -7.32% | $4.40 | 0.025598 | -4.79% | $16.81 | -20.95% | $33.66 | 0.004297 | -10.37% | $32.56 | -26.86% | $39.46 | 0.071630 | -22.87% | $10.76 | -16.98% | $44.32 |
| team_elo+form | 0.026139 | -5.33% | $0.64 | -7.72% | $3.97 | 0.030480 | -2.29% | $20.89 | -20.44% | $33.56 | 0.004570 | -13.07% | $31.43 | -22.36% | $41.27 | 0.043061 | -22.89% | $14.28 | -16.44% | $46.50 |
| player_glicko+none | -0.000787 | 2.51% | $61.17 | 0.49% | $48.14 | 0.010214 | -6.61% | $15.58 | -21.16% | $41.30 | -0.004193 | 11.82% | $88.24 | 12.31% | $74.91 | 0.005517 | -2.68% | $34.20 | 38.11% | $50.56 |
| player_glicko+form | 0.001004 | 0.88% | $30.31 | -0.76% | $29.96 | 0.012749 | -10.34% | $15.59 | -15.93% | $40.05 | -0.003305 | 9.77% | $81.33 | 14.99% | $77.52 | 0.003774 | -23.34% | $43.24 | 4.46% | $49.82 |
| player_glicko_rw_tier_revert+none | -0.004179 | 5.16% | $84.26 | -2.15% | $49.50 | 0.011705 | -11.88% | $11.91 | -28.38% | $37.98 | -0.006625 | 9.11% | $61.82 | 2.73% | $52.09 | 0.008881 | -12.55% | $17.09 | 33.50% | $52.31 |
| player_glicko_rw_tier_revert+form | -0.005413 | 5.54% | $178.74 | 4.36% | $71.92 | 0.011907 | -12.20% | $11.75 | -23.84% | $41.72 | -0.007980 | 12.13% | $60.09 | 15.97% | $70.77 | 0.002141 | -40.84% | $49.92 | — | $50.00 |

Series temperatures (stage 1; p′ = σ(T·logit p), T < 1 pulls odds toward 50%): team_elo Bo3 0.68, Bo5 0.61; player_glicko Bo3 0.69, Bo5 0.82; player_glicko_rw_tier_revert Bo3 0.80, Bo5 0.97; team_elo+none Bo3 0.68, Bo5 0.61; team_elo+form Bo3 0.62, Bo5 0.57; player_glicko+none Bo3 0.69, Bo5 0.82; player_glicko+form Bo3 0.66, Bo5 0.80; player_glicko_rw_tier_revert+none Bo3 0.80, Bo5 0.97; player_glicko_rw_tier_revert+form Bo3 0.76, Bo5 0.92

Parameters minimize tuning game log loss across all sections. Replay predicts before update; Replay starts at the first game. Tuning: [2023-01-01, 2025-11-01); validation: [2025-11-01, 2026-07-01). Holdout is scored only with --holdout and never selects parameters. Series use the first game prediction and independent games in Bo1/Bo3/Bo5; Bo2, unknown/unsupported lengths and unknown results are skipped. Accuracy gives 0.5 predictions half credit; ECE uses 10 equal-width bins. Log loss clips probabilities at 1e-6. Paired bootstrap uses 2,000 resamples, seed 0, clustered by match_id. Differences are the named model minus its comparator; negative favors the model. Significance requires a 95% percentile interval excluding zero. Tuning scores are selection diagnostics, not independent evidence of improvement.

Fit through 2025-10-31. Unknown host-region game rows: 2652 (including missing/un).

## Stage 1 — tuning (outcomes)

### Leaderboard

| Model | Best params | Game log loss | Series log loss | Rows |
|---|---|---:|---:|---:|
| player_glicko_rw_tier_revert | {"inactive_half_life": 0, "k": 24, "new_player": "fixed", "online_k": 0.75, "rd_info": 0.0625, "rd_new": 280, "revert_target": "tier", "rookie_maps": 800, "rookie_penalty": 600, "season_month": 10, "season_revert": 0.1, "tier3_k": 0.75} | 0.608853 | 0.570665 | 38138 |
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
| team_elo | all | 38138 | 0.650054 | 0.229090 | 0.622135 | 0.025619 |
| team_elo | tier1 | 14067 | 0.643791 | 0.225765 | 0.635992 | 0.034731 |
| team_elo | tier2 | 4028 | 0.644927 | 0.226671 | 0.628103 | 0.037367 |
| team_elo | tier3 | 20036 | 0.655442 | 0.231892 | 0.611325 | 0.017943 |
| team_elo | unknown | 7 | 0.764590 | 0.285084 | 0.285714 | 0.282428 |
| team_elo | international=1 | 14341 | 0.644014 | 0.225895 | 0.635311 | 0.034228 |
| team_elo | international=0 | 23797 | 0.653694 | 0.231016 | 0.614195 | 0.020664 |

team_elo − coin (paired log loss):

| Section | Rows | team_elo log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 38138 | 0.650054 | 0.693147 | -0.043093 | [-0.046516, -0.039911] | yes |

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

player_glicko_rw_tier_revert − team_elo (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 38138 | 0.608853 | 0.650054 | -0.041201 | [-0.044095, -0.038163] | yes |

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
| team_elo | all | 12117 | 0.638841 | 0.224311 | 0.632830 | 0.042539 |
| team_elo | tier1 | 4843 | 0.627597 | 0.218732 | 0.651559 | 0.049102 |
| team_elo | tier2 | 1352 | 0.614453 | 0.213948 | 0.651997 | 0.057498 |
| team_elo | tier3 | 5921 | 0.653560 | 0.231218 | 0.613241 | 0.038005 |
| team_elo | unknown | 1 | 0.920724 | 0.362127 | 0.000000 | 0.601770 |
| team_elo | international=1 | 4917 | 0.628345 | 0.219093 | 0.650803 | 0.048336 |
| team_elo | international=0 | 7200 | 0.646009 | 0.227875 | 0.620556 | 0.040676 |

team_elo − coin (paired log loss):

| Section | Rows | team_elo log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 12117 | 0.638841 | 0.693147 | -0.054306 | [-0.059461, -0.049065] | yes |

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

player_glicko_rw_tier_revert − team_elo (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 12117 | 0.570665 | 0.638841 | -0.068176 | [-0.074181, -0.061804] | yes |

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
| player_glicko_rw_tier_revert+form | {"inactive_half_life": 0, "k": 24, "new_player": "fixed", "online_k": 0.75, "rd_info": 0.0625, "rd_new": 280, "revert_target": "tier", "rookie_maps": 800, "rookie_penalty": 600, "season_month": 10, "season_revert": 0.1, "tier3_k": 0.75} | 0.597944 | 0.563975 | 9328 |
| player_glicko_rw_tier_revert | {"inactive_half_life": 0, "k": 24, "new_player": "fixed", "online_k": 0.75, "rd_info": 0.0625, "rd_new": 280, "revert_target": "tier", "rookie_maps": 800, "rookie_penalty": 600, "season_month": 10, "season_revert": 0.1, "tier3_k": 0.75} | 0.600167 | 0.565121 | 9328 |
| player_glicko_rw_tier_revert+none | {"inactive_half_life": 0, "k": 24, "new_player": "fixed", "online_k": 0.75, "rd_info": 0.0625, "rd_new": 280, "revert_target": "tier", "rookie_maps": 800, "rookie_penalty": 600, "season_month": 10, "season_revert": 0.1, "tier3_k": 0.75} | 0.600167 | 0.565121 | 9328 |
| player_glicko+form | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 280} | 0.609787 | 0.584302 | 9328 |
| player_glicko | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 280} | 0.610785 | 0.584862 | 9328 |
| player_glicko+none | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 280} | 0.610785 | 0.584862 | 9328 |
| team_elo+form | {"k": 32} | 0.639704 | 0.631376 | 9328 |
| team_elo | {"k": 32} | 0.646281 | 0.638539 | 9328 |
| team_elo+none | {"k": 32} | 0.646281 | 0.638539 | 9328 |

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
| team_elo | all | 9328 | 0.646281 | 0.227304 | 0.619479 | 0.024835 |
| team_elo | tier1 | 3827 | 0.640800 | 0.224468 | 0.628299 | 0.034059 |
| team_elo | tier2 | 571 | 0.642339 | 0.225251 | 0.632224 | 0.051263 |
| team_elo | tier3 | 4930 | 0.650992 | 0.229743 | 0.611156 | 0.020221 |
| team_elo | unknown | 0 | — | — | — | — |
| team_elo | international=1 | 3843 | 0.640946 | 0.224536 | 0.628806 | 0.034785 |
| team_elo | international=0 | 5485 | 0.650019 | 0.229243 | 0.612944 | 0.017865 |

team_elo − coin (paired log loss):

| Section | Rows | team_elo log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.646281 | 0.693147 | -0.046866 | [-0.054000, -0.040020] | yes |
| tier1 | 3827 | 0.640800 | 0.693147 | -0.052347 | [-0.064809, -0.039959] | yes |
| tier2 | 571 | 0.642339 | 0.693147 | -0.050808 | [-0.081670, -0.019311] | yes |
| tier3 | 4930 | 0.650992 | 0.693147 | -0.042155 | [-0.050620, -0.033970] | yes |
| international=1 | 3843 | 0.640946 | 0.693147 | -0.052201 | [-0.064320, -0.039911] | yes |
| international=0 | 5485 | 0.650019 | 0.693147 | -0.043129 | [-0.050869, -0.034665] | yes |

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
| team_elo+none | all | 9328 | 0.646281 | 0.227304 | 0.619479 | 0.024835 |
| team_elo+none | tier1 | 3827 | 0.640800 | 0.224468 | 0.628299 | 0.034059 |
| team_elo+none | tier2 | 571 | 0.642339 | 0.225251 | 0.632224 | 0.051263 |
| team_elo+none | tier3 | 4930 | 0.650992 | 0.229743 | 0.611156 | 0.020221 |
| team_elo+none | unknown | 0 | — | — | — | — |
| team_elo+none | international=1 | 3843 | 0.640946 | 0.224536 | 0.628806 | 0.034785 |
| team_elo+none | international=0 | 5485 | 0.650019 | 0.229243 | 0.612944 | 0.017865 |

team_elo+none − coin (paired log loss):

| Section | Rows | team_elo+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.646281 | 0.693147 | -0.046866 | [-0.054000, -0.040020] | yes |
| tier1 | 3827 | 0.640800 | 0.693147 | -0.052347 | [-0.064809, -0.039959] | yes |
| tier2 | 571 | 0.642339 | 0.693147 | -0.050808 | [-0.081670, -0.019311] | yes |
| tier3 | 4930 | 0.650992 | 0.693147 | -0.042155 | [-0.050620, -0.033970] | yes |
| international=1 | 3843 | 0.640946 | 0.693147 | -0.052201 | [-0.064320, -0.039911] | yes |
| international=0 | 5485 | 0.650019 | 0.693147 | -0.043129 | [-0.050869, -0.034665] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| team_elo+form | all | 9328 | 0.639704 | 0.224430 | 0.624893 | 0.023724 |
| team_elo+form | tier1 | 3827 | 0.633160 | 0.221202 | 0.633656 | 0.034937 |
| team_elo+form | tier2 | 571 | 0.643210 | 0.225889 | 0.619965 | 0.054206 |
| team_elo+form | tier3 | 4930 | 0.644378 | 0.226766 | 0.618661 | 0.021800 |
| team_elo+form | unknown | 0 | — | — | — | — |
| team_elo+form | international=1 | 3843 | 0.633234 | 0.221238 | 0.634140 | 0.034767 |
| team_elo+form | international=0 | 5485 | 0.644238 | 0.226665 | 0.618414 | 0.022428 |

team_elo+form − coin (paired log loss):

| Section | Rows | team_elo+form log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.639704 | 0.693147 | -0.053443 | [-0.061559, -0.045896] | yes |
| tier1 | 3827 | 0.633160 | 0.693147 | -0.059987 | [-0.072657, -0.047045] | yes |
| tier2 | 571 | 0.643210 | 0.693147 | -0.049937 | [-0.081948, -0.016730] | yes |
| tier3 | 4930 | 0.644378 | 0.693147 | -0.048769 | [-0.059393, -0.038720] | yes |
| international=1 | 3843 | 0.633234 | 0.693147 | -0.059913 | [-0.072866, -0.047006] | yes |
| international=0 | 5485 | 0.644238 | 0.693147 | -0.048910 | [-0.058015, -0.039133] | yes |

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

player_glicko_rw_tier_revert − team_elo (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.600167 | 0.646281 | -0.046114 | [-0.052027, -0.040414] | yes |

team_elo+none − team_elo (paired log loss):

| Section | Rows | team_elo+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.646281 | 0.646281 | 0.000000 | [0.000000, 0.000000] | no |

team_elo+form − team_elo (paired log loss):

| Section | Rows | team_elo+form log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.639704 | 0.646281 | -0.006577 | [-0.009071, -0.004228] | yes |

player_glicko+none − team_elo (paired log loss):

| Section | Rows | player_glicko+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.610785 | 0.646281 | -0.035496 | [-0.040569, -0.030402] | yes |

player_glicko+form − team_elo (paired log loss):

| Section | Rows | player_glicko+form log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.609787 | 0.646281 | -0.036494 | [-0.041798, -0.031062] | yes |

player_glicko_rw_tier_revert+none − team_elo (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.600167 | 0.646281 | -0.046114 | [-0.052027, -0.040414] | yes |

player_glicko_rw_tier_revert+form − team_elo (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+form log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.597944 | 0.646281 | -0.048337 | [-0.054231, -0.042407] | yes |

player_glicko_rw_tier_revert − player_glicko (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.600167 | 0.610785 | -0.010618 | [-0.013610, -0.007786] | yes |
| tier1 | 3827 | 0.575048 | 0.589637 | -0.014588 | [-0.018750, -0.010584] | yes |
| tier2 | 571 | 0.622421 | 0.629961 | -0.007540 | [-0.014268, -0.000397] | yes |
| tier3 | 4930 | 0.617088 | 0.624981 | -0.007893 | [-0.012439, -0.003221] | yes |
| international=1 | 3843 | 0.574763 | 0.589611 | -0.014848 | [-0.019007, -0.010735] | yes |
| international=0 | 5485 | 0.617965 | 0.625620 | -0.007655 | [-0.011382, -0.003682] | yes |

team_elo+none − player_glicko (paired log loss):

| Section | Rows | team_elo+none log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.646281 | 0.610785 | 0.035496 | [0.030402, 0.040569] | yes |
| tier1 | 3827 | 0.640800 | 0.589637 | 0.051163 | [0.042523, 0.060174] | yes |
| tier2 | 571 | 0.642339 | 0.629961 | 0.012377 | [-0.009580, 0.034577] | no |
| tier3 | 4930 | 0.650992 | 0.624981 | 0.026011 | [0.019825, 0.032332] | yes |
| international=1 | 3843 | 0.640946 | 0.589611 | 0.051335 | [0.042534, 0.060917] | yes |
| international=0 | 5485 | 0.650019 | 0.625620 | 0.024399 | [0.018435, 0.030255] | yes |

team_elo+form − player_glicko (paired log loss):

| Section | Rows | team_elo+form log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.639704 | 0.610785 | 0.028919 | [0.024015, 0.034196] | yes |
| tier1 | 3827 | 0.633160 | 0.589637 | 0.043523 | [0.035279, 0.052447] | yes |
| tier2 | 571 | 0.643210 | 0.629961 | 0.013249 | [-0.008200, 0.034669] | no |
| tier3 | 4930 | 0.644378 | 0.624981 | 0.019398 | [0.013208, 0.025525] | yes |
| international=1 | 3843 | 0.633234 | 0.589611 | 0.043622 | [0.035023, 0.052860] | yes |
| international=0 | 5485 | 0.644238 | 0.625620 | 0.018618 | [0.012501, 0.024701] | yes |

player_glicko+none − player_glicko (paired log loss):

| Section | Rows | player_glicko+none log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.610785 | 0.610785 | 0.000000 | [0.000000, 0.000000] | no |
| tier1 | 3827 | 0.589637 | 0.589637 | 0.000000 | [0.000000, 0.000000] | no |
| tier2 | 571 | 0.629961 | 0.629961 | 0.000000 | [0.000000, 0.000000] | no |
| tier3 | 4930 | 0.624981 | 0.624981 | 0.000000 | [0.000000, 0.000000] | no |
| international=1 | 3843 | 0.589611 | 0.589611 | 0.000000 | [0.000000, 0.000000] | no |
| international=0 | 5485 | 0.625620 | 0.625620 | 0.000000 | [0.000000, 0.000000] | no |

player_glicko+form − player_glicko (paired log loss):

| Section | Rows | player_glicko+form log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.609787 | 0.610785 | -0.000998 | [-0.002020, 0.000003] | no |
| tier1 | 3827 | 0.588370 | 0.589637 | -0.001266 | [-0.002435, -0.000091] | yes |
| tier2 | 571 | 0.630918 | 0.629961 | 0.000957 | [-0.001116, 0.003098] | no |
| tier3 | 4930 | 0.623964 | 0.624981 | -0.001017 | [-0.002606, 0.000537] | no |
| international=1 | 3843 | 0.588344 | 0.589611 | -0.001267 | [-0.002471, -0.000112] | yes |
| international=0 | 5485 | 0.624810 | 0.625620 | -0.000810 | [-0.002242, 0.000759] | no |

player_glicko_rw_tier_revert+none − player_glicko (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+none log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.600167 | 0.610785 | -0.010618 | [-0.013610, -0.007786] | yes |
| tier1 | 3827 | 0.575048 | 0.589637 | -0.014588 | [-0.018750, -0.010584] | yes |
| tier2 | 571 | 0.622421 | 0.629961 | -0.007540 | [-0.014268, -0.000397] | yes |
| tier3 | 4930 | 0.617088 | 0.624981 | -0.007893 | [-0.012439, -0.003221] | yes |
| international=1 | 3843 | 0.574763 | 0.589611 | -0.014848 | [-0.019007, -0.010735] | yes |
| international=0 | 5485 | 0.617965 | 0.625620 | -0.007655 | [-0.011382, -0.003682] | yes |

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
| team_elo | all | 4366 | 0.638539 | 0.224110 | 0.621507 | 0.045062 |
| team_elo | tier1 | 1960 | 0.627551 | 0.218830 | 0.635459 | 0.052820 |
| team_elo | tier2 | 268 | 0.614341 | 0.214100 | 0.652985 | 0.068690 |
| team_elo | tier3 | 2138 | 0.651646 | 0.230206 | 0.604771 | 0.038375 |
| team_elo | unknown | 0 | — | — | — | — |
| team_elo | international=1 | 1974 | 0.628065 | 0.219070 | 0.636018 | 0.054148 |
| team_elo | international=0 | 2392 | 0.647183 | 0.228269 | 0.609532 | 0.038108 |

team_elo − coin (paired log loss):

| Section | Rows | team_elo log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.638539 | 0.693147 | -0.054608 | [-0.064592, -0.044950] | yes |
| tier1 | 1960 | 0.627551 | 0.693147 | -0.065596 | [-0.081018, -0.049507] | yes |
| tier2 | 268 | 0.614341 | 0.693147 | -0.078807 | [-0.121002, -0.034488] | yes |
| tier3 | 2138 | 0.651646 | 0.693147 | -0.041501 | [-0.053079, -0.029536] | yes |
| international=1 | 1974 | 0.628065 | 0.693147 | -0.065082 | [-0.080617, -0.049636] | yes |
| international=0 | 2392 | 0.647183 | 0.693147 | -0.045964 | [-0.057242, -0.034701] | yes |

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
| team_elo+none | all | 4366 | 0.638539 | 0.224110 | 0.621507 | 0.045062 |
| team_elo+none | tier1 | 1960 | 0.627551 | 0.218830 | 0.635459 | 0.052820 |
| team_elo+none | tier2 | 268 | 0.614341 | 0.214100 | 0.652985 | 0.068690 |
| team_elo+none | tier3 | 2138 | 0.651646 | 0.230206 | 0.604771 | 0.038375 |
| team_elo+none | unknown | 0 | — | — | — | — |
| team_elo+none | international=1 | 1974 | 0.628065 | 0.219070 | 0.636018 | 0.054148 |
| team_elo+none | international=0 | 2392 | 0.647183 | 0.228269 | 0.609532 | 0.038108 |

team_elo+none − coin (paired log loss):

| Section | Rows | team_elo+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.638539 | 0.693147 | -0.054608 | [-0.064592, -0.044950] | yes |
| tier1 | 1960 | 0.627551 | 0.693147 | -0.065596 | [-0.081018, -0.049507] | yes |
| tier2 | 268 | 0.614341 | 0.693147 | -0.078807 | [-0.121002, -0.034488] | yes |
| tier3 | 2138 | 0.651646 | 0.693147 | -0.041501 | [-0.053079, -0.029536] | yes |
| international=1 | 1974 | 0.628065 | 0.693147 | -0.065082 | [-0.080617, -0.049636] | yes |
| international=0 | 2392 | 0.647183 | 0.693147 | -0.045964 | [-0.057242, -0.034701] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| team_elo+form | all | 4366 | 0.631376 | 0.220985 | 0.628149 | 0.042263 |
| team_elo+form | tier1 | 1960 | 0.617259 | 0.214473 | 0.642347 | 0.050366 |
| team_elo+form | tier2 | 268 | 0.611489 | 0.213212 | 0.641791 | 0.060455 |
| team_elo+form | tier3 | 2138 | 0.646811 | 0.227930 | 0.613424 | 0.039382 |
| team_elo+form | unknown | 0 | — | — | — | — |
| team_elo+form | international=1 | 1974 | 0.617664 | 0.214665 | 0.642857 | 0.050169 |
| team_elo+form | international=0 | 2392 | 0.642692 | 0.226201 | 0.616012 | 0.037650 |

team_elo+form − coin (paired log loss):

| Section | Rows | team_elo+form log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.631376 | 0.693147 | -0.061771 | [-0.072544, -0.051401] | yes |
| tier1 | 1960 | 0.617259 | 0.693147 | -0.075888 | [-0.091596, -0.059666] | yes |
| tier2 | 268 | 0.611489 | 0.693147 | -0.081658 | [-0.124694, -0.038046] | yes |
| tier3 | 2138 | 0.646811 | 0.693147 | -0.046336 | [-0.059872, -0.032999] | yes |
| international=1 | 1974 | 0.617664 | 0.693147 | -0.075483 | [-0.090662, -0.059774] | yes |
| international=0 | 2392 | 0.642692 | 0.693147 | -0.050455 | [-0.062734, -0.037611] | yes |

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

player_glicko_rw_tier_revert − team_elo (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.565121 | 0.638539 | -0.073418 | [-0.082900, -0.063575] | yes |

team_elo+none − team_elo (paired log loss):

| Section | Rows | team_elo+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.638539 | 0.638539 | 0.000000 | [0.000000, 0.000000] | no |

team_elo+form − team_elo (paired log loss):

| Section | Rows | team_elo+form log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.631376 | 0.638539 | -0.007163 | [-0.010639, -0.003558] | yes |

player_glicko+none − team_elo (paired log loss):

| Section | Rows | player_glicko+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.584862 | 0.638539 | -0.053677 | [-0.061296, -0.045900] | yes |

player_glicko+form − team_elo (paired log loss):

| Section | Rows | player_glicko+form log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.584302 | 0.638539 | -0.054237 | [-0.062112, -0.046497] | yes |

player_glicko_rw_tier_revert+none − team_elo (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.565121 | 0.638539 | -0.073418 | [-0.082900, -0.063575] | yes |

player_glicko_rw_tier_revert+form − team_elo (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+form log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.563975 | 0.638539 | -0.074564 | [-0.084073, -0.064845] | yes |

player_glicko_rw_tier_revert − player_glicko (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.565121 | 0.584862 | -0.019741 | [-0.024884, -0.014310] | yes |
| tier1 | 1960 | 0.525977 | 0.550511 | -0.024533 | [-0.031820, -0.017293] | yes |
| tier2 | 268 | 0.584509 | 0.590452 | -0.005943 | [-0.016427, 0.006225] | no |
| tier3 | 2138 | 0.598576 | 0.615654 | -0.017078 | [-0.025340, -0.008183] | yes |
| international=1 | 1974 | 0.525688 | 0.550617 | -0.024930 | [-0.031631, -0.017898] | yes |
| international=0 | 2392 | 0.597664 | 0.613123 | -0.015460 | [-0.023378, -0.007639] | yes |

team_elo+none − player_glicko (paired log loss):

| Section | Rows | team_elo+none log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.638539 | 0.584862 | 0.053677 | [0.045900, 0.061296] | yes |
| tier1 | 1960 | 0.627551 | 0.550511 | 0.077040 | [0.064125, 0.090206] | yes |
| tier2 | 268 | 0.614341 | 0.590452 | 0.023888 | [-0.010775, 0.057766] | no |
| tier3 | 2138 | 0.651646 | 0.615654 | 0.035993 | [0.026116, 0.045434] | yes |
| international=1 | 1974 | 0.628065 | 0.550617 | 0.077448 | [0.065380, 0.090447] | yes |
| international=0 | 2392 | 0.647183 | 0.613123 | 0.034059 | [0.024809, 0.043047] | yes |

team_elo+form − player_glicko (paired log loss):

| Section | Rows | team_elo+form log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.631376 | 0.584862 | 0.046514 | [0.038905, 0.054038] | yes |
| tier1 | 1960 | 0.617259 | 0.550511 | 0.066749 | [0.054411, 0.079209] | yes |
| tier2 | 268 | 0.611489 | 0.590452 | 0.021037 | [-0.012296, 0.053074] | no |
| tier3 | 2138 | 0.646811 | 0.615654 | 0.031157 | [0.021472, 0.040599] | yes |
| international=1 | 1974 | 0.617664 | 0.550617 | 0.067047 | [0.055049, 0.079291] | yes |
| international=0 | 2392 | 0.642692 | 0.613123 | 0.029569 | [0.019958, 0.038965] | yes |

player_glicko+none − player_glicko (paired log loss):

| Section | Rows | player_glicko+none log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.584862 | 0.584862 | 0.000000 | [0.000000, 0.000000] | no |
| tier1 | 1960 | 0.550511 | 0.550511 | 0.000000 | [0.000000, 0.000000] | no |
| tier2 | 268 | 0.590452 | 0.590452 | 0.000000 | [0.000000, 0.000000] | no |
| tier3 | 2138 | 0.615654 | 0.615654 | 0.000000 | [0.000000, 0.000000] | no |
| international=1 | 1974 | 0.550617 | 0.550617 | 0.000000 | [0.000000, 0.000000] | no |
| international=0 | 2392 | 0.613123 | 0.613123 | 0.000000 | [0.000000, 0.000000] | no |

player_glicko+form − player_glicko (paired log loss):

| Section | Rows | player_glicko+form log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.584302 | 0.584862 | -0.000560 | [-0.002041, 0.000961] | no |
| tier1 | 1960 | 0.549839 | 0.550511 | -0.000671 | [-0.002256, 0.000961] | no |
| tier2 | 268 | 0.590281 | 0.590452 | -0.000171 | [-0.003415, 0.003033] | no |
| tier3 | 2138 | 0.615147 | 0.615654 | -0.000507 | [-0.002990, 0.002110] | no |
| international=1 | 1974 | 0.549930 | 0.550617 | -0.000687 | [-0.002256, 0.000982] | no |
| international=0 | 2392 | 0.612669 | 0.613123 | -0.000455 | [-0.002670, 0.001990] | no |

player_glicko_rw_tier_revert+none − player_glicko (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+none log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.565121 | 0.584862 | -0.019741 | [-0.024884, -0.014310] | yes |
| tier1 | 1960 | 0.525977 | 0.550511 | -0.024533 | [-0.031820, -0.017293] | yes |
| tier2 | 268 | 0.584509 | 0.590452 | -0.005943 | [-0.016427, 0.006225] | no |
| tier3 | 2138 | 0.598576 | 0.615654 | -0.017078 | [-0.025340, -0.008183] | yes |
| international=1 | 1974 | 0.525688 | 0.550617 | -0.024930 | [-0.031631, -0.017898] | yes |
| international=0 | 2392 | 0.597664 | 0.613123 | -0.015460 | [-0.023378, -0.007639] | yes |

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

### team_elo: Kalshi comparison and returns



#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 621 | 0.638927 | 0.613968 | 0.024959 [0.004437, 0.046123] | yes |
| series | tier1 | 528 | 0.633060 | 0.608069 | 0.024992 [0.004066, 0.049031] | yes |
| series | tier2 | 85 | 0.679196 | 0.643551 | 0.035645 [-0.018945, 0.087856] | no |
| series | tier3 | 8 | 0.598274 | 0.689027 | -0.090753 [-0.274214, 0.090280] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 528 | 0.633060 | 0.608069 | 0.024992 [0.004066, 0.049031] | yes |
| series | international=0 | 93 | 0.672235 | 0.647463 | 0.024772 [-0.028481, 0.079213] | no |
| game | all | 434 | 0.658185 | 0.632587 | 0.025598 [-0.000090, 0.053605] | no |
| game | tier1 | 340 | 0.658734 | 0.629029 | 0.029704 [0.000501, 0.062951] | yes |
| game | tier2 | 85 | 0.664880 | 0.652750 | 0.012130 [-0.034760, 0.068643] | no |
| game | tier3 | 9 | 0.574211 | 0.576544 | -0.002334 [-0.072127, 0.141871] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 340 | 0.658734 | 0.629029 | 0.029704 [0.000501, 0.062951] | yes |
| game | international=0 | 94 | 0.656199 | 0.645454 | 0.010745 [-0.032599, 0.065887] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 428 | 428 | 0.0782 | -5.19% [-17.20%, 6.65%] | $0.91 | 0.018× | 98.94% | $7.26 | 224 (204 unfilled) | -7.32% [-23.54%, 10.03%] | $4.40 |
| series | tier1 | 359 | 359 | 0.0781 | -9.26% [-20.99%, 3.45%] | $1.64 | 0.033× | 97.97% | $7.26 | 187 (172 unfilled) | -14.86% [-29.61%, -0.04%] | $2.80 |
| series | tier2 | 63 | 63 | 0.0775 | 10.58% [-27.14%, 54.19%] | $27.56 | 0.551× | 67.33% | $4.80 | 32 (31 unfilled) | 26.70% [-37.04%, 94.80%] | $65.43 |
| series | tier3 | 6 | 6 | 0.0926 | 71.05% [-31.88%, 173.87%] | $65.81 | 1.316× | 6.82% | $5.79 | 5 (1 unfilled) | 55.13% [-68.25%, 178.65%] | $58.38 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 359 | 359 | 0.0781 | -9.26% [-20.99%, 3.45%] | $1.64 | 0.033× | 97.97% | $7.26 | 187 (172 unfilled) | -14.86% [-29.61%, -0.04%] | $2.80 |
| series | international=0 | 69 | 69 | 0.0788 | 15.86% [-20.45%, 56.33%] | $36.25 | 0.725× | 67.33% | $4.80 | 37 (32 unfilled) | 30.56% [-25.24%, 92.99%] | $75.98 |
| game | all | 281 | 148 | 0.0776 | -4.79% [-17.44%, 7.92%] | $16.81 | 0.336× | 70.70% | $5.18 | 48 (233 unfilled) | -20.95% [-49.57%, 12.23%] | $33.66 |
| game | tier1 | 231 | 120 | 0.0812 | -5.76% [-18.85%, 7.85%] | $18.90 | 0.378× | 69.23% | $5.18 | 42 (189 unfilled) | -16.86% [-49.03%, 21.09%] | $36.25 |
| game | tier2 | 42 | 24 | 0.0681 | -2.25% [-33.08%, 31.15%] | $46.91 | 0.938× | 21.70% | $4.52 | 4 (38 unfilled) | -24.15% [-100.00%, 52.79%] | $52.04 |
| game | tier3 | 8 | 4 | 0.0236 | 9.83% [-63.89%, 48.68%] | $47.34 | 0.947× | 8.91% | $2.65 | 2 (6 unfilled) | -100.00% [-100.00%, -100.00%] | $45.00 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 231 | 120 | 0.0812 | -5.76% [-18.85%, 7.85%] | $18.90 | 0.378× | 69.23% | $5.18 | 42 (189 unfilled) | -16.86% [-49.03%, 21.09%] | $36.25 |
| game | international=0 | 50 | 28 | 0.0610 | -0.32% [-27.61%, 30.18%] | $44.39 | 0.888× | 21.70% | $4.52 | 6 (44 unfilled) | -49.48% [-100.00%, 28.05%] | $46.83 |
| series+game | all | 709 | 462 | 0.0780 | -5.03% [-15.17%, 5.21%] | $0.64 | 0.013× | 99.24% | $7.26 | 272 (437 unfilled) | -9.72% [-23.92%, 5.20%] | $14.17 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 280 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2025-11 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2025-12 | series | 13 | 1.000000 | 0.000000 | unfitted |
| 2026-01 | series | 79 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 148 | 1.079932 | 0.314278 | fitted |
| 2026-03 | series | 249 | 0.988987 | 0.290507 | fitted |
| 2026-03 | game | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | series | 302 | 0.966050 | 0.247919 | fitted |
| 2026-04 | game | 15 | 1.000000 | 0.000000 | unfitted |
| 2026-05 | series | 379 | 0.842147 | 0.005589 | fitted |
| 2026-05 | game | 132 | 1.602751 | -1.181073 | fitted |
| 2026-06 | series | 544 | 0.887192 | 0.187990 | fitted |
| 2026-06 | game | 330 | 0.891823 | 0.172138 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 473 | 0.631014 | 0.626718 | 0.004297 [-0.001281, 0.009694] | no |
| series | tier1 | 401 | 0.623438 | 0.617017 | 0.006421 [0.000779, 0.012126] | yes |
| series | tier2 | 64 | 0.674687 | 0.679709 | -0.005022 [-0.022705, 0.011021] | no |
| series | tier3 | 8 | 0.661381 | 0.689027 | -0.027645 [-0.094786, 0.032139] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 401 | 0.623438 | 0.617017 | 0.006421 [0.000779, 0.012126] | yes |
| series | international=0 | 72 | 0.673209 | 0.680744 | -0.007536 [-0.024460, 0.008606] | no |
| game | all | 302 | 0.694991 | 0.623361 | 0.071630 [0.028904, 0.119895] | yes |
| game | tier1 | 237 | 0.684274 | 0.611859 | 0.072415 [0.023728, 0.128574] | yes |
| game | tier2 | 56 | 0.758026 | 0.679563 | 0.078463 [-0.015432, 0.186886] | no |
| game | tier3 | 9 | 0.584979 | 0.576544 | 0.008435 [-0.014447, 0.040580] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 237 | 0.684274 | 0.611859 | 0.072415 [0.023728, 0.128574] | yes |
| game | international=0 | 65 | 0.734065 | 0.665299 | 0.068766 [-0.011325, 0.157219] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 84 | 84 | 0.0125 | -10.37% [-40.93%, 22.30%] | $32.56 | 0.651× | 44.34% | $4.08 | 46 (38 unfilled) | -26.86% [-62.43%, 11.76%] | $39.46 |
| series | tier1 | 71 | 71 | 0.0127 | -14.38% [-43.27%, 16.85%] | $28.86 | 0.577× | 49.53% | $4.08 | 38 (33 unfilled) | -35.71% [-66.04%, -0.72%] | $35.06 |
| series | tier2 | 10 | 10 | 0.0078 | 8.42% [-100.00%, 166.15%] | $55.02 | 1.100× | 6.38% | $1.09 | 5 (5 unfilled) | 11.20% [-100.00%, 233.59%] | $54.92 |
| series | tier3 | 3 | 3 | 0.0238 | 21.33% [-100.00%, 262.84%] | $51.22 | 1.024× | 2.39% | $1.89 | 3 (0 unfilled) | 21.33% [-100.00%, 262.84%] | $51.22 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 71 | 71 | 0.0127 | -14.38% [-43.27%, 16.85%] | $28.86 | 0.577× | 49.53% | $4.08 | 38 (33 unfilled) | -35.71% [-66.04%, -0.72%] | $35.06 |
| series | international=0 | 13 | 13 | 0.0115 | 11.40% [-100.00%, 124.86%] | $56.36 | 1.127× | 6.38% | $2.08 | 8 (5 unfilled) | 14.99% [-100.00%, 174.15%] | $56.27 |
| game | all | 146 | 76 | 0.0902 | -22.87% [-38.55%, -7.32%] | $10.76 | 0.215× | 82.53% | $3.82 | 17 (129 unfilled) | -16.98% [-72.70%, 47.16%] | $44.32 |
| game | tier1 | 102 | 53 | 0.0964 | -23.17% [-42.27%, -4.17%] | $16.09 | 0.322× | 75.44% | $2.94 | 13 (89 unfilled) | -10.95% [-81.48%, 72.27%] | $45.95 |
| game | tier2 | 44 | 23 | 0.0758 | -22.18% [-45.73%, 1.48%] | $33.57 | 0.671× | 38.53% | $3.82 | 4 (40 unfilled) | -36.97% [-100.00%, 26.37%] | $48.23 |
| game | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 102 | 53 | 0.0964 | -23.17% [-42.27%, -4.17%] | $16.09 | 0.322× | 75.44% | $2.94 | 13 (89 unfilled) | -10.95% [-81.48%, 72.27%] | $45.95 |
| game | international=0 | 44 | 23 | 0.0758 | -22.18% [-45.73%, 1.48%] | $33.57 | 0.671× | 38.53% | $3.82 | 4 (40 unfilled) | -36.97% [-100.00%, 26.37%] | $48.23 |
| series+game | all | 230 | 146 | 0.0618 | -18.27% [-31.98%, -4.18%] | $6.66 | 0.133× | 88.92% | $4.08 | 63 (167 unfilled) | -24.22% [-52.95%, 7.00%] | $33.86 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| game | 2026-03 | 15 | 0.675914 | — | 0.669739 | -2.33% (7), $45.76 | — | 4 (3 unfilled) | 22.09% [-20.42%, 67.39%] | $56.02 | — | — | — |
| game | 2026-04 | 117 | 0.712359 | — | 0.651637 | -16.52% (72), $25.11 | — | 17 (55 unfilled) | -10.41% [-45.86%, 29.81%] | $52.59 | — | — | — |
| game | 2026-05 | 198 | 0.657934 | 0.762139 | 0.657045 | 5.00% (125), $63.82 | -20.78% (134), $10.84 | 7 (118 unfilled) | 12.61% [-68.10%, 76.97%] | $49.74 | 13 (121 unfilled) | -28.02% [-75.03%, 16.69%] | $40.56 |
| game | 2026-06 | 104 | 0.595158 | 0.567152 | 0.559231 | -9.93% (77), $29.27 | -45.89% (12), $49.71 | 20 (57 unfilled) | -49.97% [-92.79%, 15.56%] | $29.07 | 4 (8 unfilled) | 17.92% [-100.00%, 252.94%] | $54.67 |
| series | 2025-11 | 13 | 0.501859 | — | 0.588964 | 3.57% (10), $63.46 | — | 10 (0 unfilled) | 3.57% [-45.33%, 45.69%] | $59.37 | — | — | — |
| series | 2025-12 | 66 | 0.668110 | — | 0.640347 | -0.38% (37), $33.93 | — | 34 (3 unfilled) | 1.68% [-37.67%, 45.38%] | $38.69 | — | — | — |
| series | 2026-01 | 69 | 0.531783 | — | 0.506048 | -15.30% (59), $23.02 | — | 27 (32 unfilled) | -15.81% [-52.86%, 29.08%] | $30.83 | — | — | — |
| series | 2026-02 | 101 | 0.671897 | 0.666830 | 0.667211 | 0.09% (70), $39.32 | 13.40% (20), $51.11 | 16 (54 unfilled) | 0.79% [-59.33%, 60.13%] | $51.38 | 4 (16 unfilled) | 67.47% [-51.57%, 172.76%] | $54.92 |
| series | 2026-03 | 53 | 0.679309 | 0.665057 | 0.663787 | -11.62% (34), $43.17 | 33.74% (6), $48.32 | 27 (7 unfilled) | -2.48% [-37.75%, 30.60%] | $47.20 | 5 (1 unfilled) | 27.68% [-64.66%, 120.36%] | $47.32 |
| series | 2026-04 | 77 | 0.745891 | 0.698515 | 0.690287 | -2.36% (52), $16.54 | -73.38% (9), $45.30 | 38 (14 unfilled) | 8.81% [-36.47%, 63.53%] | $31.48 | 4 (5 unfilled) | -40.33% [-100.00%, 78.57%] | $48.61 |
| series | 2026-05 | 165 | 0.629918 | 0.626687 | 0.626943 | 6.62% (108), $67.68 | 49.77% (16), $57.64 | 30 (78 unfilled) | -12.05% [-53.00%, 38.76%] | $40.95 | 7 (9 unfilled) | -20.72% [-100.00%, 138.15%] | $56.31 |
| series | 2026-06 | 77 | 0.574367 | 0.502376 | 0.484035 | -26.36% (58), $10.47 | -44.71% (33), $31.51 | 42 (16 unfilled) | -28.94% [-59.85%, 3.39%] | $16.45 | 26 (7 unfilled) | -51.11% [-86.74%, -4.33%] | $34.52 |

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

### team_elo+none: Kalshi comparison and returns

none

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 621 | 0.638927 | 0.613968 | 0.024959 [0.004437, 0.046123] | yes |
| series | tier1 | 528 | 0.633060 | 0.608069 | 0.024992 [0.004066, 0.049031] | yes |
| series | tier2 | 85 | 0.679196 | 0.643551 | 0.035645 [-0.018945, 0.087856] | no |
| series | tier3 | 8 | 0.598274 | 0.689027 | -0.090753 [-0.274214, 0.090280] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 528 | 0.633060 | 0.608069 | 0.024992 [0.004066, 0.049031] | yes |
| series | international=0 | 93 | 0.672235 | 0.647463 | 0.024772 [-0.028481, 0.079213] | no |
| game | all | 434 | 0.658185 | 0.632587 | 0.025598 [-0.000090, 0.053605] | no |
| game | tier1 | 340 | 0.658734 | 0.629029 | 0.029704 [0.000501, 0.062951] | yes |
| game | tier2 | 85 | 0.664880 | 0.652750 | 0.012130 [-0.034760, 0.068643] | no |
| game | tier3 | 9 | 0.574211 | 0.576544 | -0.002334 [-0.072127, 0.141871] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 340 | 0.658734 | 0.629029 | 0.029704 [0.000501, 0.062951] | yes |
| game | international=0 | 94 | 0.656199 | 0.645454 | 0.010745 [-0.032599, 0.065887] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 428 | 428 | 0.0782 | -5.19% [-17.20%, 6.65%] | $0.91 | 0.018× | 98.94% | $7.26 | 224 (204 unfilled) | -7.32% [-23.54%, 10.03%] | $4.40 |
| series | tier1 | 359 | 359 | 0.0781 | -9.26% [-20.99%, 3.45%] | $1.64 | 0.033× | 97.97% | $7.26 | 187 (172 unfilled) | -14.86% [-29.61%, -0.04%] | $2.80 |
| series | tier2 | 63 | 63 | 0.0775 | 10.58% [-27.14%, 54.19%] | $27.56 | 0.551× | 67.33% | $4.80 | 32 (31 unfilled) | 26.70% [-37.04%, 94.80%] | $65.43 |
| series | tier3 | 6 | 6 | 0.0926 | 71.05% [-31.88%, 173.87%] | $65.81 | 1.316× | 6.82% | $5.79 | 5 (1 unfilled) | 55.13% [-68.25%, 178.65%] | $58.38 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 359 | 359 | 0.0781 | -9.26% [-20.99%, 3.45%] | $1.64 | 0.033× | 97.97% | $7.26 | 187 (172 unfilled) | -14.86% [-29.61%, -0.04%] | $2.80 |
| series | international=0 | 69 | 69 | 0.0788 | 15.86% [-20.45%, 56.33%] | $36.25 | 0.725× | 67.33% | $4.80 | 37 (32 unfilled) | 30.56% [-25.24%, 92.99%] | $75.98 |
| game | all | 281 | 148 | 0.0776 | -4.79% [-17.44%, 7.92%] | $16.81 | 0.336× | 70.70% | $5.18 | 48 (233 unfilled) | -20.95% [-49.57%, 12.23%] | $33.66 |
| game | tier1 | 231 | 120 | 0.0812 | -5.76% [-18.85%, 7.85%] | $18.90 | 0.378× | 69.23% | $5.18 | 42 (189 unfilled) | -16.86% [-49.03%, 21.09%] | $36.25 |
| game | tier2 | 42 | 24 | 0.0681 | -2.25% [-33.08%, 31.15%] | $46.91 | 0.938× | 21.70% | $4.52 | 4 (38 unfilled) | -24.15% [-100.00%, 52.79%] | $52.04 |
| game | tier3 | 8 | 4 | 0.0236 | 9.83% [-63.89%, 48.68%] | $47.34 | 0.947× | 8.91% | $2.65 | 2 (6 unfilled) | -100.00% [-100.00%, -100.00%] | $45.00 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 231 | 120 | 0.0812 | -5.76% [-18.85%, 7.85%] | $18.90 | 0.378× | 69.23% | $5.18 | 42 (189 unfilled) | -16.86% [-49.03%, 21.09%] | $36.25 |
| game | international=0 | 50 | 28 | 0.0610 | -0.32% [-27.61%, 30.18%] | $44.39 | 0.888× | 21.70% | $4.52 | 6 (44 unfilled) | -49.48% [-100.00%, 28.05%] | $46.83 |
| series+game | all | 709 | 462 | 0.0780 | -5.03% [-15.17%, 5.21%] | $0.64 | 0.013× | 99.24% | $7.26 | 272 (437 unfilled) | -9.72% [-23.92%, 5.20%] | $14.17 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 280 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2025-11 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2025-12 | series | 13 | 1.000000 | 0.000000 | unfitted |
| 2026-01 | series | 79 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 148 | 1.079932 | 0.314278 | fitted |
| 2026-03 | series | 249 | 0.988987 | 0.290507 | fitted |
| 2026-03 | game | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | series | 302 | 0.966050 | 0.247919 | fitted |
| 2026-04 | game | 15 | 1.000000 | 0.000000 | unfitted |
| 2026-05 | series | 379 | 0.842147 | 0.005589 | fitted |
| 2026-05 | game | 132 | 1.602751 | -1.181073 | fitted |
| 2026-06 | series | 544 | 0.887192 | 0.187990 | fitted |
| 2026-06 | game | 330 | 0.891823 | 0.172138 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 473 | 0.631014 | 0.626718 | 0.004297 [-0.001281, 0.009694] | no |
| series | tier1 | 401 | 0.623438 | 0.617017 | 0.006421 [0.000779, 0.012126] | yes |
| series | tier2 | 64 | 0.674687 | 0.679709 | -0.005022 [-0.022705, 0.011021] | no |
| series | tier3 | 8 | 0.661381 | 0.689027 | -0.027645 [-0.094786, 0.032139] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 401 | 0.623438 | 0.617017 | 0.006421 [0.000779, 0.012126] | yes |
| series | international=0 | 72 | 0.673209 | 0.680744 | -0.007536 [-0.024460, 0.008606] | no |
| game | all | 302 | 0.694991 | 0.623361 | 0.071630 [0.028904, 0.119895] | yes |
| game | tier1 | 237 | 0.684274 | 0.611859 | 0.072415 [0.023728, 0.128574] | yes |
| game | tier2 | 56 | 0.758026 | 0.679563 | 0.078463 [-0.015432, 0.186886] | no |
| game | tier3 | 9 | 0.584979 | 0.576544 | 0.008435 [-0.014447, 0.040580] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 237 | 0.684274 | 0.611859 | 0.072415 [0.023728, 0.128574] | yes |
| game | international=0 | 65 | 0.734065 | 0.665299 | 0.068766 [-0.011325, 0.157219] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 84 | 84 | 0.0125 | -10.37% [-40.93%, 22.30%] | $32.56 | 0.651× | 44.34% | $4.08 | 46 (38 unfilled) | -26.86% [-62.43%, 11.76%] | $39.46 |
| series | tier1 | 71 | 71 | 0.0127 | -14.38% [-43.27%, 16.85%] | $28.86 | 0.577× | 49.53% | $4.08 | 38 (33 unfilled) | -35.71% [-66.04%, -0.72%] | $35.06 |
| series | tier2 | 10 | 10 | 0.0078 | 8.42% [-100.00%, 166.15%] | $55.02 | 1.100× | 6.38% | $1.09 | 5 (5 unfilled) | 11.20% [-100.00%, 233.59%] | $54.92 |
| series | tier3 | 3 | 3 | 0.0238 | 21.33% [-100.00%, 262.84%] | $51.22 | 1.024× | 2.39% | $1.89 | 3 (0 unfilled) | 21.33% [-100.00%, 262.84%] | $51.22 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 71 | 71 | 0.0127 | -14.38% [-43.27%, 16.85%] | $28.86 | 0.577× | 49.53% | $4.08 | 38 (33 unfilled) | -35.71% [-66.04%, -0.72%] | $35.06 |
| series | international=0 | 13 | 13 | 0.0115 | 11.40% [-100.00%, 124.86%] | $56.36 | 1.127× | 6.38% | $2.08 | 8 (5 unfilled) | 14.99% [-100.00%, 174.15%] | $56.27 |
| game | all | 146 | 76 | 0.0902 | -22.87% [-38.55%, -7.32%] | $10.76 | 0.215× | 82.53% | $3.82 | 17 (129 unfilled) | -16.98% [-72.70%, 47.16%] | $44.32 |
| game | tier1 | 102 | 53 | 0.0964 | -23.17% [-42.27%, -4.17%] | $16.09 | 0.322× | 75.44% | $2.94 | 13 (89 unfilled) | -10.95% [-81.48%, 72.27%] | $45.95 |
| game | tier2 | 44 | 23 | 0.0758 | -22.18% [-45.73%, 1.48%] | $33.57 | 0.671× | 38.53% | $3.82 | 4 (40 unfilled) | -36.97% [-100.00%, 26.37%] | $48.23 |
| game | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 102 | 53 | 0.0964 | -23.17% [-42.27%, -4.17%] | $16.09 | 0.322× | 75.44% | $2.94 | 13 (89 unfilled) | -10.95% [-81.48%, 72.27%] | $45.95 |
| game | international=0 | 44 | 23 | 0.0758 | -22.18% [-45.73%, 1.48%] | $33.57 | 0.671× | 38.53% | $3.82 | 4 (40 unfilled) | -36.97% [-100.00%, 26.37%] | $48.23 |
| series+game | all | 230 | 146 | 0.0618 | -18.27% [-31.98%, -4.18%] | $6.66 | 0.133× | 88.92% | $4.08 | 63 (167 unfilled) | -24.22% [-52.95%, 7.00%] | $33.86 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| game | 2026-03 | 15 | 0.675914 | — | 0.669739 | -2.33% (7), $45.76 | — | 4 (3 unfilled) | 22.09% [-20.42%, 67.39%] | $56.02 | — | — | — |
| game | 2026-04 | 117 | 0.712359 | — | 0.651637 | -16.52% (72), $25.11 | — | 17 (55 unfilled) | -10.41% [-45.86%, 29.81%] | $52.59 | — | — | — |
| game | 2026-05 | 198 | 0.657934 | 0.762139 | 0.657045 | 5.00% (125), $63.82 | -20.78% (134), $10.84 | 7 (118 unfilled) | 12.61% [-68.10%, 76.97%] | $49.74 | 13 (121 unfilled) | -28.02% [-75.03%, 16.69%] | $40.56 |
| game | 2026-06 | 104 | 0.595158 | 0.567152 | 0.559231 | -9.93% (77), $29.27 | -45.89% (12), $49.71 | 20 (57 unfilled) | -49.97% [-92.79%, 15.56%] | $29.07 | 4 (8 unfilled) | 17.92% [-100.00%, 252.94%] | $54.67 |
| series | 2025-11 | 13 | 0.501859 | — | 0.588964 | 3.57% (10), $63.46 | — | 10 (0 unfilled) | 3.57% [-45.33%, 45.69%] | $59.37 | — | — | — |
| series | 2025-12 | 66 | 0.668110 | — | 0.640347 | -0.38% (37), $33.93 | — | 34 (3 unfilled) | 1.68% [-37.67%, 45.38%] | $38.69 | — | — | — |
| series | 2026-01 | 69 | 0.531783 | — | 0.506048 | -15.30% (59), $23.02 | — | 27 (32 unfilled) | -15.81% [-52.86%, 29.08%] | $30.83 | — | — | — |
| series | 2026-02 | 101 | 0.671897 | 0.666830 | 0.667211 | 0.09% (70), $39.32 | 13.40% (20), $51.11 | 16 (54 unfilled) | 0.79% [-59.33%, 60.13%] | $51.38 | 4 (16 unfilled) | 67.47% [-51.57%, 172.76%] | $54.92 |
| series | 2026-03 | 53 | 0.679309 | 0.665057 | 0.663787 | -11.62% (34), $43.17 | 33.74% (6), $48.32 | 27 (7 unfilled) | -2.48% [-37.75%, 30.60%] | $47.20 | 5 (1 unfilled) | 27.68% [-64.66%, 120.36%] | $47.32 |
| series | 2026-04 | 77 | 0.745891 | 0.698515 | 0.690287 | -2.36% (52), $16.54 | -73.38% (9), $45.30 | 38 (14 unfilled) | 8.81% [-36.47%, 63.53%] | $31.48 | 4 (5 unfilled) | -40.33% [-100.00%, 78.57%] | $48.61 |
| series | 2026-05 | 165 | 0.629918 | 0.626687 | 0.626943 | 6.62% (108), $67.68 | 49.77% (16), $57.64 | 30 (78 unfilled) | -12.05% [-53.00%, 38.76%] | $40.95 | 7 (9 unfilled) | -20.72% [-100.00%, 138.15%] | $56.31 |
| series | 2026-06 | 77 | 0.574367 | 0.502376 | 0.484035 | -26.36% (58), $10.47 | -44.71% (33), $31.51 | 42 (16 unfilled) | -28.94% [-59.85%, 3.39%] | $16.45 | 26 (7 unfilled) | -51.11% [-86.74%, -4.33%] | $34.52 |

### team_elo+form: Kalshi comparison and returns

form: rows=35654, H=80, w=3.43379

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 621 | 0.640107 | 0.613968 | 0.026139 [0.005689, 0.047107] | yes |
| series | tier1 | 528 | 0.634710 | 0.608069 | 0.026641 [0.005753, 0.049836] | yes |
| series | tier2 | 85 | 0.676022 | 0.643551 | 0.032471 [-0.022802, 0.083457] | no |
| series | tier3 | 8 | 0.614770 | 0.689027 | -0.074256 [-0.266366, 0.106587] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 528 | 0.634710 | 0.608069 | 0.026641 [0.005753, 0.049836] | yes |
| series | international=0 | 93 | 0.670753 | 0.647463 | 0.023290 [-0.029271, 0.076515] | no |
| game | all | 434 | 0.663067 | 0.632587 | 0.030480 [0.003839, 0.059558] | yes |
| game | tier1 | 340 | 0.664419 | 0.629029 | 0.035390 [0.004365, 0.070566] | yes |
| game | tier2 | 85 | 0.666316 | 0.652750 | 0.013566 [-0.033013, 0.068971] | no |
| game | tier3 | 9 | 0.581296 | 0.576544 | 0.004751 [-0.085377, 0.122258] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 340 | 0.664419 | 0.629029 | 0.035390 [0.004365, 0.070566] | yes |
| game | international=0 | 94 | 0.658176 | 0.645454 | 0.012722 [-0.030039, 0.065394] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 435 | 435 | 0.0807 | -5.33% [-17.25%, 7.29%] | $0.64 | 0.013× | 99.45% | $9.72 | 227 (208 unfilled) | -7.72% [-23.73%, 9.30%] | $3.97 |
| series | tier1 | 363 | 363 | 0.0817 | -9.03% [-21.25%, 4.08%] | $1.19 | 0.024× | 98.90% | $9.72 | 189 (174 unfilled) | -13.92% [-28.90%, 1.76%] | $3.16 |
| series | tier2 | 66 | 66 | 0.0746 | 7.96% [-30.39%, 49.77%] | $28.53 | 0.571× | 64.22% | $4.80 | 33 (33 unfilled) | 18.07% [-41.65%, 82.78%] | $52.81 |
| series | tier3 | 6 | 6 | 0.0921 | 71.05% [-31.88%, 173.87%] | $62.15 | 1.243× | 0.00% | $5.06 | 5 (1 unfilled) | 55.13% [-68.25%, 178.65%] | $62.15 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 363 | 363 | 0.0817 | -9.03% [-21.25%, 4.08%] | $1.19 | 0.024× | 98.90% | $9.72 | 189 (174 unfilled) | -13.92% [-28.90%, 1.76%] | $3.16 |
| series | international=0 | 72 | 72 | 0.0760 | 13.23% [-24.33%, 53.48%] | $35.48 | 0.710× | 64.22% | $4.80 | 38 (34 unfilled) | 22.96% [-32.09%, 85.14%] | $65.68 |
| game | all | 298 | 160 | 0.0793 | -2.29% [-13.61%, 9.89%] | $20.89 | 0.418× | 65.37% | $5.68 | 52 (246 unfilled) | -20.44% [-46.91%, 9.30%] | $33.56 |
| game | tier1 | 248 | 132 | 0.0825 | -3.77% [-15.86%, 9.23%] | $22.72 | 0.454× | 64.92% | $5.68 | 47 (201 unfilled) | -18.45% [-46.98%, 13.79%] | $35.64 |
| game | tier2 | 44 | 25 | 0.0683 | 5.95% [-20.08%, 35.87%] | $46.86 | 0.937× | 21.77% | $4.52 | 3 (41 unfilled) | 1.70% [-100.00%, 68.69%] | $52.75 |
| game | tier3 | 6 | 3 | 0.0285 | -1.63% [-100.00%, 50.53%] | $48.60 | 0.972× | 6.71% | $2.89 | 2 (4 unfilled) | -100.00% [-100.00%, -100.00%] | $45.00 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 248 | 132 | 0.0825 | -3.77% [-15.86%, 9.23%] | $22.72 | 0.454× | 64.92% | $5.68 | 47 (201 unfilled) | -18.45% [-46.98%, 13.79%] | $35.64 |
| game | international=0 | 50 | 28 | 0.0636 | 5.04% [-21.54%, 33.58%] | $45.53 | 0.911× | 21.77% | $4.52 | 5 (45 unfilled) | -39.18% [-100.00%, 52.79%] | $47.48 |
| series+game | all | 733 | 479 | 0.0802 | -4.10% [-13.99%, 5.51%] | $0.59 | 0.012× | 99.48% | $9.72 | 279 (454 unfilled) | -10.09% [-24.57%, 4.56%] | $12.09 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 280 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2025-11 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2025-12 | series | 13 | 1.000000 | 0.000000 | unfitted |
| 2026-01 | series | 79 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 148 | 1.096811 | 0.327499 | fitted |
| 2026-03 | series | 249 | 0.988394 | 0.245344 | fitted |
| 2026-03 | game | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | series | 302 | 0.970404 | 0.223224 | fitted |
| 2026-04 | game | 15 | 1.000000 | 0.000000 | unfitted |
| 2026-05 | series | 379 | 0.840170 | -0.006334 | fitted |
| 2026-05 | game | 132 | 1.472594 | -0.858991 | fitted |
| 2026-06 | series | 544 | 0.893917 | 0.183436 | fitted |
| 2026-06 | game | 330 | 0.898056 | 0.129546 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 473 | 0.631287 | 0.626718 | 0.004570 [-0.000988, 0.009981] | no |
| series | tier1 | 401 | 0.623520 | 0.617017 | 0.006502 [0.001020, 0.012202] | yes |
| series | tier2 | 64 | 0.675734 | 0.679709 | -0.003975 [-0.021059, 0.011745] | no |
| series | tier3 | 8 | 0.665064 | 0.689027 | -0.023962 [-0.088515, 0.033601] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 401 | 0.623520 | 0.617017 | 0.006502 [0.001020, 0.012202] | yes |
| series | international=0 | 72 | 0.674549 | 0.680744 | -0.006196 [-0.022427, 0.009543] | no |
| game | all | 302 | 0.666422 | 0.623361 | 0.043061 [0.013047, 0.075478] | yes |
| game | tier1 | 237 | 0.655208 | 0.611859 | 0.043349 [0.009086, 0.081581] | yes |
| game | tier2 | 56 | 0.726839 | 0.679563 | 0.047276 [-0.019350, 0.122468] | no |
| game | tier3 | 9 | 0.585799 | 0.576544 | 0.009255 [-0.005994, 0.031643] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 237 | 0.655208 | 0.611859 | 0.043349 [0.009086, 0.081581] | yes |
| game | international=0 | 65 | 0.707311 | 0.665299 | 0.042012 [-0.014973, 0.102134] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 86 | 86 | 0.0123 | -13.07% [-41.95%, 18.05%] | $31.43 | 0.629× | 44.30% | $3.51 | 44 (42 unfilled) | -22.36% [-58.33%, 20.82%] | $41.27 |
| series | tier1 | 74 | 74 | 0.0125 | -22.73% [-50.62%, 8.14%] | $27.04 | 0.541× | 51.18% | $3.50 | 36 (38 unfilled) | -39.24% [-69.83%, -3.65%] | $36.38 |
| series | tier2 | 9 | 9 | 0.0071 | 54.35% [-66.12%, 205.65%] | $56.92 | 1.138× | 3.82% | $1.08 | 5 (4 unfilled) | 72.50% [-100.00%, 257.14%] | $55.82 |
| series | tier3 | 3 | 3 | 0.0233 | 21.33% [-100.00%, 262.84%] | $50.90 | 1.018× | 1.77% | $2.17 | 3 (0 unfilled) | 21.33% [-100.00%, 262.84%] | $50.90 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 74 | 74 | 0.0125 | -22.73% [-50.62%, 8.14%] | $27.04 | 0.541× | 51.18% | $3.50 | 36 (38 unfilled) | -39.24% [-69.83%, -3.65%] | $36.38 |
| series | international=0 | 12 | 12 | 0.0112 | 46.09% [-69.62%, 175.54%] | $57.94 | 1.159× | 3.82% | $2.47 | 8 (4 unfilled) | 53.31% [-61.91%, 206.97%] | $56.81 |
| game | all | 119 | 63 | 0.0742 | -22.89% [-40.07%, -6.09%] | $14.28 | 0.286× | 75.84% | $3.32 | 13 (106 unfilled) | -16.44% [-79.44%, 65.76%] | $46.50 |
| game | tier1 | 77 | 39 | 0.0888 | -27.17% [-48.65%, -4.46%] | $20.52 | 0.410× | 68.07% | $2.93 | 9 (68 unfilled) | -7.50% [-85.59%, 122.47%] | $48.59 |
| game | tier2 | 42 | 24 | 0.0474 | -14.98% [-38.32%, 8.15%] | $35.00 | 0.700× | 32.79% | $3.32 | 4 (38 unfilled) | -36.97% [-100.00%, 26.37%] | $47.84 |
| game | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 77 | 39 | 0.0888 | -27.17% [-48.65%, -4.46%] | $20.52 | 0.410× | 68.07% | $2.93 | 9 (68 unfilled) | -7.50% [-85.59%, 122.47%] | $48.59 |
| game | international=0 | 42 | 24 | 0.0474 | -14.98% [-38.32%, 8.15%] | $35.00 | 0.700× | 32.79% | $3.32 | 4 (38 unfilled) | -36.97% [-100.00%, 26.37%] | $47.84 |
| series+game | all | 205 | 138 | 0.0482 | -18.74% [-33.81%, -3.76%] | $8.35 | 0.167× | 85.55% | $3.50 | 57 (148 unfilled) | -21.03% [-50.66%, 12.49%] | $35.70 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| game | 2026-03 | 15 | 0.670180 | — | 0.669739 | 14.84% (11), $51.45 | — | 5 (6 unfilled) | 28.49% [-8.67%, 64.60%] | $56.22 | — | — | — |
| game | 2026-04 | 117 | 0.715689 | — | 0.651637 | -16.94% (78), $28.22 | — | 20 (58 unfilled) | -14.45% [-44.61%, 20.86%] | $50.18 | — | — | — |
| game | 2026-05 | 198 | 0.663669 | 0.718498 | 0.657045 | 10.27% (129), $65.67 | -22.99% (113), $13.52 | 7 (122 unfilled) | 12.77% [-68.00%, 76.59%] | $51.63 | 11 (102 unfilled) | -44.84% [-86.17%, -1.98%] | $40.41 |
| game | 2026-06 | 104 | 0.601695 | 0.567277 | 0.559231 | -10.59% (80), $27.79 | -21.01% (6), $52.94 | 20 (60 unfilled) | -49.97% [-92.79%, 15.56%] | $29.16 | 2 (4 unfilled) | 134.74% [-100.00%, 371.70%] | $57.55 |
| series | 2025-11 | 13 | 0.489997 | — | 0.588964 | 28.14% (9), $65.85 | — | 9 (0 unfilled) | 28.14% [-10.57%, 58.67%] | $61.73 | — | — | — |
| series | 2025-12 | 66 | 0.670397 | — | 0.640347 | -2.40% (40), $46.01 | — | 37 (3 unfilled) | -0.67% [-41.55%, 44.58%] | $47.74 | — | — | — |
| series | 2026-01 | 69 | 0.534347 | — | 0.506048 | -22.10% (59), $19.99 | — | 26 (33 unfilled) | -27.96% [-70.67%, 18.75%] | $27.99 | — | — | — |
| series | 2026-02 | 101 | 0.678211 | 0.669022 | 0.667211 | 0.48% (76), $36.76 | 0.61% (26), $45.64 | 17 (59 unfilled) | 4.33% [-51.49%, 63.77%] | $50.66 | 5 (21 unfilled) | 62.98% [-27.83%, 151.93%] | $55.24 |
| series | 2026-03 | 53 | 0.675847 | 0.663553 | 0.663787 | -8.51% (33), $45.78 | 0.12% (4), $47.55 | 27 (6 unfilled) | -1.94% [-37.54%, 34.12%] | $44.51 | 2 (2 unfilled) | 19.05% [-100.00%, 138.10%] | $47.28 |
| series | 2026-04 | 77 | 0.742000 | 0.696692 | 0.690287 | 4.05% (53), $17.84 | -31.67% (8), $48.08 | 38 (15 unfilled) | 11.91% [-36.74%, 65.98%] | $33.75 | 5 (3 unfilled) | 9.27% [-100.00%, 132.39%] | $49.01 |
| series | 2026-05 | 165 | 0.628846 | 0.627106 | 0.626943 | 7.24% (109), $64.71 | 49.77% (16), $58.22 | 31 (78 unfilled) | -6.03% [-49.56%, 43.00%] | $45.12 | 6 (10 unfilled) | -7.51% [-100.00%, 177.47%] | $56.21 |
| series | 2026-06 | 77 | 0.581920 | 0.503137 | 0.484035 | -33.95% (56), $5.96 | -52.54% (32), $32.29 | 42 (14 unfilled) | -36.27% [-65.60%, -3.15%] | $13.11 | 26 (6 unfilled) | -51.11% [-88.60%, -5.92%] | $35.75 |

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

## Holdout

### Leaderboard (frozen stage-1 parameters)

| Model | Best params | Game log loss | Series log loss | Rows |
|---|---|---:|---:|---:|
| player_glicko_rw_tier_revert+form | {"inactive_half_life": 0, "k": 24, "new_player": "fixed", "online_k": 0.75, "rd_info": 0.0625, "rd_new": 280, "revert_target": "tier", "rookie_maps": 800, "rookie_penalty": 600, "season_month": 10, "season_revert": 0.1, "tier3_k": 0.75} | 0.595487 | 0.556607 | 3835 |
| player_glicko_rw_tier_revert | {"inactive_half_life": 0, "k": 24, "new_player": "fixed", "online_k": 0.75, "rd_info": 0.0625, "rd_new": 280, "revert_target": "tier", "rookie_maps": 800, "rookie_penalty": 600, "season_month": 10, "season_revert": 0.1, "tier3_k": 0.75} | 0.598823 | 0.561710 | 3835 |
| player_glicko_rw_tier_revert+none | {"inactive_half_life": 0, "k": 24, "new_player": "fixed", "online_k": 0.75, "rd_info": 0.0625, "rd_new": 280, "revert_target": "tier", "rookie_maps": 800, "rookie_penalty": 600, "season_month": 10, "season_revert": 0.1, "tier3_k": 0.75} | 0.598823 | 0.561710 | 3835 |
| player_glicko+form | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 280} | 0.604004 | 0.575241 | 3835 |
| player_glicko | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 280} | 0.606097 | 0.578916 | 3835 |
| player_glicko+none | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 280} | 0.606097 | 0.578916 | 3835 |
| team_elo+form | {"k": 32} | 0.650247 | 0.632336 | 3835 |
| team_elo | {"k": 32} | 0.659026 | 0.647045 | 3835 |
| team_elo+none | {"k": 32} | 0.659026 | 0.647045 | 3835 |

### Games

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| coin | all | 3835 | 0.693147 | 0.250000 | 0.500000 | 0.071838 |
| coin | tier1 | 1152 | 0.693147 | 0.250000 | 0.500000 | 0.080729 |
| coin | tier2 | 200 | 0.693147 | 0.250000 | 0.500000 | 0.065000 |
| coin | tier3 | 2483 | 0.693147 | 0.250000 | 0.500000 | 0.068264 |
| coin | unknown | 0 | — | — | — | — |
| coin | international=1 | 1152 | 0.693147 | 0.250000 | 0.500000 | 0.080729 |
| coin | international=0 | 2683 | 0.693147 | 0.250000 | 0.500000 | 0.068021 |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| team_elo | all | 3835 | 0.659026 | 0.232573 | 0.610169 | 0.058999 |
| team_elo | tier1 | 1152 | 0.673932 | 0.237878 | 0.605903 | 0.077655 |
| team_elo | tier2 | 200 | 0.670778 | 0.236033 | 0.642500 | 0.080394 |
| team_elo | tier3 | 2483 | 0.651164 | 0.229834 | 0.609545 | 0.055810 |
| team_elo | unknown | 0 | — | — | — | — |
| team_elo | international=1 | 1152 | 0.673932 | 0.237878 | 0.605903 | 0.077655 |
| team_elo | international=0 | 2683 | 0.652626 | 0.230296 | 0.612001 | 0.055664 |

team_elo − coin (paired log loss):

| Section | Rows | team_elo log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 3835 | 0.659026 | 0.693147 | -0.034121 | [-0.045607, -0.023439] | yes |
| tier1 | 1152 | 0.673932 | 0.693147 | -0.019215 | [-0.047229, 0.006976] | no |
| tier2 | 200 | 0.670778 | 0.693147 | -0.022369 | [-0.075974, 0.031038] | no |
| tier3 | 2483 | 0.651164 | 0.693147 | -0.041983 | [-0.052617, -0.031282] | yes |
| international=1 | 1152 | 0.673932 | 0.693147 | -0.019215 | [-0.047229, 0.006976] | no |
| international=0 | 2683 | 0.652626 | 0.693147 | -0.040521 | [-0.051080, -0.029077] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko | all | 3835 | 0.606097 | 0.209893 | 0.667536 | 0.032233 |
| player_glicko | tier1 | 1152 | 0.582794 | 0.199753 | 0.694010 | 0.031171 |
| player_glicko | tier2 | 200 | 0.629029 | 0.219546 | 0.675000 | 0.057001 |
| player_glicko | tier3 | 2483 | 0.615061 | 0.213821 | 0.654652 | 0.042942 |
| player_glicko | unknown | 0 | — | — | — | — |
| player_glicko | international=1 | 1152 | 0.582794 | 0.199753 | 0.694010 | 0.031171 |
| player_glicko | international=0 | 2683 | 0.616102 | 0.214248 | 0.656168 | 0.040814 |

player_glicko − coin (paired log loss):

| Section | Rows | player_glicko log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 3835 | 0.606097 | 0.693147 | -0.087050 | [-0.099796, -0.075197] | yes |
| tier1 | 1152 | 0.582794 | 0.693147 | -0.110353 | [-0.134412, -0.087394] | yes |
| tier2 | 200 | 0.629029 | 0.693147 | -0.064118 | [-0.112259, -0.014864] | yes |
| tier3 | 2483 | 0.615061 | 0.693147 | -0.078086 | [-0.092586, -0.063740] | yes |
| international=1 | 1152 | 0.582794 | 0.693147 | -0.110353 | [-0.134412, -0.087394] | yes |
| international=0 | 2683 | 0.616102 | 0.693147 | -0.077045 | [-0.091183, -0.062761] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko_rw_tier_revert | all | 3835 | 0.598823 | 0.206366 | 0.678488 | 0.037067 |
| player_glicko_rw_tier_revert | tier1 | 1152 | 0.577042 | 0.197328 | 0.704427 | 0.037362 |
| player_glicko_rw_tier_revert | tier2 | 200 | 0.625981 | 0.218230 | 0.650000 | 0.060262 |
| player_glicko_rw_tier_revert | tier3 | 2483 | 0.606741 | 0.209604 | 0.668747 | 0.047953 |
| player_glicko_rw_tier_revert | unknown | 0 | — | — | — | — |
| player_glicko_rw_tier_revert | international=1 | 1152 | 0.577042 | 0.197328 | 0.704427 | 0.037362 |
| player_glicko_rw_tier_revert | international=0 | 2683 | 0.608175 | 0.210247 | 0.667350 | 0.043538 |

player_glicko_rw_tier_revert − coin (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 3835 | 0.598823 | 0.693147 | -0.094324 | [-0.107131, -0.082170] | yes |
| tier1 | 1152 | 0.577042 | 0.693147 | -0.116105 | [-0.139152, -0.093686] | yes |
| tier2 | 200 | 0.625981 | 0.693147 | -0.067166 | [-0.113165, -0.023733] | yes |
| tier3 | 2483 | 0.606741 | 0.693147 | -0.086407 | [-0.100952, -0.071451] | yes |
| international=1 | 1152 | 0.577042 | 0.693147 | -0.116105 | [-0.139152, -0.093686] | yes |
| international=0 | 2683 | 0.608175 | 0.693147 | -0.084972 | [-0.098883, -0.070545] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| team_elo+none | all | 3835 | 0.659026 | 0.232573 | 0.610169 | 0.058999 |
| team_elo+none | tier1 | 1152 | 0.673932 | 0.237878 | 0.605903 | 0.077655 |
| team_elo+none | tier2 | 200 | 0.670778 | 0.236033 | 0.642500 | 0.080394 |
| team_elo+none | tier3 | 2483 | 0.651164 | 0.229834 | 0.609545 | 0.055810 |
| team_elo+none | unknown | 0 | — | — | — | — |
| team_elo+none | international=1 | 1152 | 0.673932 | 0.237878 | 0.605903 | 0.077655 |
| team_elo+none | international=0 | 2683 | 0.652626 | 0.230296 | 0.612001 | 0.055664 |

team_elo+none − coin (paired log loss):

| Section | Rows | team_elo+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 3835 | 0.659026 | 0.693147 | -0.034121 | [-0.045607, -0.023439] | yes |
| tier1 | 1152 | 0.673932 | 0.693147 | -0.019215 | [-0.047229, 0.006976] | no |
| tier2 | 200 | 0.670778 | 0.693147 | -0.022369 | [-0.075974, 0.031038] | no |
| tier3 | 2483 | 0.651164 | 0.693147 | -0.041983 | [-0.052617, -0.031282] | yes |
| international=1 | 1152 | 0.673932 | 0.693147 | -0.019215 | [-0.047229, 0.006976] | no |
| international=0 | 2683 | 0.652626 | 0.693147 | -0.040521 | [-0.051080, -0.029077] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| team_elo+form | all | 3835 | 0.650247 | 0.228736 | 0.623859 | 0.054490 |
| team_elo+form | tier1 | 1152 | 0.668303 | 0.235760 | 0.610677 | 0.068447 |
| team_elo+form | tier2 | 200 | 0.670251 | 0.235839 | 0.650000 | 0.080849 |
| team_elo+form | tier3 | 2483 | 0.640258 | 0.224904 | 0.627870 | 0.052756 |
| team_elo+form | unknown | 0 | — | — | — | — |
| team_elo+form | international=1 | 1152 | 0.668303 | 0.235760 | 0.610677 | 0.068447 |
| team_elo+form | international=0 | 2683 | 0.642494 | 0.225719 | 0.629519 | 0.051723 |

team_elo+form − coin (paired log loss):

| Section | Rows | team_elo+form log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 3835 | 0.650247 | 0.693147 | -0.042901 | [-0.055728, -0.030779] | yes |
| tier1 | 1152 | 0.668303 | 0.693147 | -0.024845 | [-0.052438, 0.001771] | no |
| tier2 | 200 | 0.670251 | 0.693147 | -0.022896 | [-0.076478, 0.029374] | no |
| tier3 | 2483 | 0.640258 | 0.693147 | -0.052889 | [-0.065463, -0.039953] | yes |
| international=1 | 1152 | 0.668303 | 0.693147 | -0.024845 | [-0.052438, 0.001771] | no |
| international=0 | 2683 | 0.642494 | 0.693147 | -0.050653 | [-0.063315, -0.037333] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko+none | all | 3835 | 0.606097 | 0.209893 | 0.667536 | 0.032233 |
| player_glicko+none | tier1 | 1152 | 0.582794 | 0.199753 | 0.694010 | 0.031171 |
| player_glicko+none | tier2 | 200 | 0.629029 | 0.219546 | 0.675000 | 0.057001 |
| player_glicko+none | tier3 | 2483 | 0.615061 | 0.213821 | 0.654652 | 0.042942 |
| player_glicko+none | unknown | 0 | — | — | — | — |
| player_glicko+none | international=1 | 1152 | 0.582794 | 0.199753 | 0.694010 | 0.031171 |
| player_glicko+none | international=0 | 2683 | 0.616102 | 0.214248 | 0.656168 | 0.040814 |

player_glicko+none − coin (paired log loss):

| Section | Rows | player_glicko+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 3835 | 0.606097 | 0.693147 | -0.087050 | [-0.099796, -0.075197] | yes |
| tier1 | 1152 | 0.582794 | 0.693147 | -0.110353 | [-0.134412, -0.087394] | yes |
| tier2 | 200 | 0.629029 | 0.693147 | -0.064118 | [-0.112259, -0.014864] | yes |
| tier3 | 2483 | 0.615061 | 0.693147 | -0.078086 | [-0.092586, -0.063740] | yes |
| international=1 | 1152 | 0.582794 | 0.693147 | -0.110353 | [-0.134412, -0.087394] | yes |
| international=0 | 2683 | 0.616102 | 0.693147 | -0.077045 | [-0.091183, -0.062761] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko+form | all | 3835 | 0.604004 | 0.208968 | 0.667014 | 0.029810 |
| player_glicko+form | tier1 | 1152 | 0.581779 | 0.199338 | 0.692274 | 0.027252 |
| player_glicko+form | tier2 | 200 | 0.628600 | 0.219350 | 0.665000 | 0.051424 |
| player_glicko+form | tier3 | 2483 | 0.612335 | 0.212600 | 0.655457 | 0.041102 |
| player_glicko+form | unknown | 0 | — | — | — | — |
| player_glicko+form | international=1 | 1152 | 0.581779 | 0.199338 | 0.692274 | 0.027252 |
| player_glicko+form | international=0 | 2683 | 0.613547 | 0.213103 | 0.656168 | 0.039193 |

player_glicko+form − coin (paired log loss):

| Section | Rows | player_glicko+form log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 3835 | 0.604004 | 0.693147 | -0.089143 | [-0.102567, -0.076909] | yes |
| tier1 | 1152 | 0.581779 | 0.693147 | -0.111368 | [-0.135891, -0.088115] | yes |
| tier2 | 200 | 0.628600 | 0.693147 | -0.064547 | [-0.113128, -0.015419] | yes |
| tier3 | 2483 | 0.612335 | 0.693147 | -0.080813 | [-0.095986, -0.065582] | yes |
| international=1 | 1152 | 0.581779 | 0.693147 | -0.111368 | [-0.135891, -0.088115] | yes |
| international=0 | 2683 | 0.613547 | 0.693147 | -0.079600 | [-0.094343, -0.064608] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko_rw_tier_revert+none | all | 3835 | 0.598823 | 0.206366 | 0.678488 | 0.037067 |
| player_glicko_rw_tier_revert+none | tier1 | 1152 | 0.577042 | 0.197328 | 0.704427 | 0.037362 |
| player_glicko_rw_tier_revert+none | tier2 | 200 | 0.625981 | 0.218230 | 0.650000 | 0.060262 |
| player_glicko_rw_tier_revert+none | tier3 | 2483 | 0.606741 | 0.209604 | 0.668747 | 0.047953 |
| player_glicko_rw_tier_revert+none | unknown | 0 | — | — | — | — |
| player_glicko_rw_tier_revert+none | international=1 | 1152 | 0.577042 | 0.197328 | 0.704427 | 0.037362 |
| player_glicko_rw_tier_revert+none | international=0 | 2683 | 0.608175 | 0.210247 | 0.667350 | 0.043538 |

player_glicko_rw_tier_revert+none − coin (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 3835 | 0.598823 | 0.693147 | -0.094324 | [-0.107131, -0.082170] | yes |
| tier1 | 1152 | 0.577042 | 0.693147 | -0.116105 | [-0.139152, -0.093686] | yes |
| tier2 | 200 | 0.625981 | 0.693147 | -0.067166 | [-0.113165, -0.023733] | yes |
| tier3 | 2483 | 0.606741 | 0.693147 | -0.086407 | [-0.100952, -0.071451] | yes |
| international=1 | 1152 | 0.577042 | 0.693147 | -0.116105 | [-0.139152, -0.093686] | yes |
| international=0 | 2683 | 0.608175 | 0.693147 | -0.084972 | [-0.098883, -0.070545] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko_rw_tier_revert+form | all | 3835 | 0.595487 | 0.204912 | 0.683963 | 0.030275 |
| player_glicko_rw_tier_revert+form | tier1 | 1152 | 0.575240 | 0.196647 | 0.701823 | 0.024544 |
| player_glicko_rw_tier_revert+form | tier2 | 200 | 0.626275 | 0.218172 | 0.655000 | 0.037223 |
| player_glicko_rw_tier_revert+form | tier3 | 2483 | 0.602401 | 0.207678 | 0.678010 | 0.041463 |
| player_glicko_rw_tier_revert+form | unknown | 0 | — | — | — | — |
| player_glicko_rw_tier_revert+form | international=1 | 1152 | 0.575240 | 0.196647 | 0.701823 | 0.024544 |
| player_glicko_rw_tier_revert+form | international=0 | 2683 | 0.604181 | 0.208461 | 0.676295 | 0.038055 |

player_glicko_rw_tier_revert+form − coin (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+form log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 3835 | 0.595487 | 0.693147 | -0.097660 | [-0.111186, -0.085032] | yes |
| tier1 | 1152 | 0.575240 | 0.693147 | -0.117907 | [-0.141963, -0.094571] | yes |
| tier2 | 200 | 0.626275 | 0.693147 | -0.066872 | [-0.114421, -0.022514] | yes |
| tier3 | 2483 | 0.602401 | 0.693147 | -0.090746 | [-0.106219, -0.075198] | yes |
| international=1 | 1152 | 0.575240 | 0.693147 | -0.117907 | [-0.141963, -0.094571] | yes |
| international=0 | 2683 | 0.604181 | 0.693147 | -0.088966 | [-0.103398, -0.073884] | yes |

player_glicko − team_elo (paired log loss):

| Section | Rows | player_glicko log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 3835 | 0.606097 | 0.659026 | -0.052930 | [-0.063754, -0.042857] | yes |

player_glicko_rw_tier_revert − team_elo (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 3835 | 0.598823 | 0.659026 | -0.060204 | [-0.071679, -0.049774] | yes |

team_elo+none − team_elo (paired log loss):

| Section | Rows | team_elo+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 3835 | 0.659026 | 0.659026 | 0.000000 | [0.000000, 0.000000] | no |

team_elo+form − team_elo (paired log loss):

| Section | Rows | team_elo+form log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 3835 | 0.650247 | 0.659026 | -0.008780 | [-0.012337, -0.005124] | yes |

player_glicko+none − team_elo (paired log loss):

| Section | Rows | player_glicko+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 3835 | 0.606097 | 0.659026 | -0.052930 | [-0.063754, -0.042857] | yes |

player_glicko+form − team_elo (paired log loss):

| Section | Rows | player_glicko+form log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 3835 | 0.604004 | 0.659026 | -0.055022 | [-0.066035, -0.044748] | yes |

player_glicko_rw_tier_revert+none − team_elo (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 3835 | 0.598823 | 0.659026 | -0.060204 | [-0.071679, -0.049774] | yes |

player_glicko_rw_tier_revert+form − team_elo (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+form log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 3835 | 0.595487 | 0.659026 | -0.063539 | [-0.075177, -0.052959] | yes |

player_glicko_rw_tier_revert − player_glicko (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 3835 | 0.598823 | 0.606097 | -0.007274 | [-0.011773, -0.002397] | yes |
| tier1 | 1152 | 0.577042 | 0.582794 | -0.005752 | [-0.012197, 0.001965] | no |
| tier2 | 200 | 0.625981 | 0.629029 | -0.003048 | [-0.018310, 0.012902] | no |
| tier3 | 2483 | 0.606741 | 0.615061 | -0.008320 | [-0.014389, -0.002018] | yes |
| international=1 | 1152 | 0.577042 | 0.582794 | -0.005752 | [-0.012197, 0.001965] | no |
| international=0 | 2683 | 0.608175 | 0.616102 | -0.007927 | [-0.013773, -0.002162] | yes |

team_elo+none − player_glicko (paired log loss):

| Section | Rows | team_elo+none log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 3835 | 0.659026 | 0.606097 | 0.052930 | [0.042857, 0.063754] | yes |
| tier1 | 1152 | 0.673932 | 0.582794 | 0.091138 | [0.065972, 0.117149] | yes |
| tier2 | 200 | 0.670778 | 0.629029 | 0.041749 | [0.002796, 0.083589] | yes |
| tier3 | 2483 | 0.651164 | 0.615061 | 0.036103 | [0.027018, 0.045574] | yes |
| international=1 | 1152 | 0.673932 | 0.582794 | 0.091138 | [0.065972, 0.117149] | yes |
| international=0 | 2683 | 0.652626 | 0.616102 | 0.036524 | [0.027056, 0.045854] | yes |

team_elo+form − player_glicko (paired log loss):

| Section | Rows | team_elo+form log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 3835 | 0.650247 | 0.606097 | 0.044150 | [0.034262, 0.054927] | yes |
| tier1 | 1152 | 0.668303 | 0.582794 | 0.085508 | [0.059937, 0.111047] | yes |
| tier2 | 200 | 0.670251 | 0.629029 | 0.041222 | [0.001890, 0.083827] | yes |
| tier3 | 2483 | 0.640258 | 0.615061 | 0.025197 | [0.015588, 0.034578] | yes |
| international=1 | 1152 | 0.668303 | 0.582794 | 0.085508 | [0.059937, 0.111047] | yes |
| international=0 | 2683 | 0.642494 | 0.616102 | 0.026392 | [0.017209, 0.035795] | yes |

player_glicko+none − player_glicko (paired log loss):

| Section | Rows | player_glicko+none log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 3835 | 0.606097 | 0.606097 | 0.000000 | [0.000000, 0.000000] | no |
| tier1 | 1152 | 0.582794 | 0.582794 | 0.000000 | [0.000000, 0.000000] | no |
| tier2 | 200 | 0.629029 | 0.629029 | 0.000000 | [0.000000, 0.000000] | no |
| tier3 | 2483 | 0.615061 | 0.615061 | 0.000000 | [0.000000, 0.000000] | no |
| international=1 | 1152 | 0.582794 | 0.582794 | 0.000000 | [0.000000, 0.000000] | no |
| international=0 | 2683 | 0.616102 | 0.616102 | 0.000000 | [0.000000, 0.000000] | no |

player_glicko+form − player_glicko (paired log loss):

| Section | Rows | player_glicko+form log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 3835 | 0.604004 | 0.606097 | -0.002093 | [-0.003632, -0.000560] | yes |
| tier1 | 1152 | 0.581779 | 0.582794 | -0.001016 | [-0.002530, 0.000504] | no |
| tier2 | 200 | 0.628600 | 0.629029 | -0.000429 | [-0.002785, 0.001991] | no |
| tier3 | 2483 | 0.612335 | 0.615061 | -0.002726 | [-0.005100, -0.000491] | yes |
| international=1 | 1152 | 0.581779 | 0.582794 | -0.001016 | [-0.002530, 0.000504] | no |
| international=0 | 2683 | 0.613547 | 0.616102 | -0.002555 | [-0.004702, -0.000361] | yes |

player_glicko_rw_tier_revert+none − player_glicko (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+none log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 3835 | 0.598823 | 0.606097 | -0.007274 | [-0.011773, -0.002397] | yes |
| tier1 | 1152 | 0.577042 | 0.582794 | -0.005752 | [-0.012197, 0.001965] | no |
| tier2 | 200 | 0.625981 | 0.629029 | -0.003048 | [-0.018310, 0.012902] | no |
| tier3 | 2483 | 0.606741 | 0.615061 | -0.008320 | [-0.014389, -0.002018] | yes |
| international=1 | 1152 | 0.577042 | 0.582794 | -0.005752 | [-0.012197, 0.001965] | no |
| international=0 | 2683 | 0.608175 | 0.616102 | -0.007927 | [-0.013773, -0.002162] | yes |

player_glicko_rw_tier_revert+form − player_glicko (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+form log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 3835 | 0.595487 | 0.606097 | -0.010609 | [-0.015241, -0.005763] | yes |
| tier1 | 1152 | 0.575240 | 0.582794 | -0.007554 | [-0.014412, 0.000040] | no |
| tier2 | 200 | 0.626275 | 0.629029 | -0.002754 | [-0.019212, 0.013933] | no |
| tier3 | 2483 | 0.602401 | 0.615061 | -0.012660 | [-0.018779, -0.006398] | yes |
| international=1 | 1152 | 0.575240 | 0.582794 | -0.007554 | [-0.014412, 0.000040] | no |
| international=0 | 2683 | 0.604181 | 0.616102 | -0.011921 | [-0.017630, -0.006265] | yes |

### Series

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| coin | all | 1875 | 0.693147 | 0.250000 | 0.500000 | 0.103733 |
| coin | tier1 | 505 | 0.693147 | 0.250000 | 0.500000 | 0.141584 |
| coin | tier2 | 75 | 0.693147 | 0.250000 | 0.500000 | 0.073333 |
| coin | tier3 | 1295 | 0.693147 | 0.250000 | 0.500000 | 0.090734 |
| coin | unknown | 0 | — | — | — | — |
| coin | international=1 | 505 | 0.693147 | 0.250000 | 0.500000 | 0.141584 |
| coin | international=0 | 1370 | 0.693147 | 0.250000 | 0.500000 | 0.089781 |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| team_elo | all | 1875 | 0.647045 | 0.227197 | 0.619200 | 0.084074 |
| team_elo | tier1 | 505 | 0.657559 | 0.229605 | 0.621782 | 0.112683 |
| team_elo | tier2 | 75 | 0.634475 | 0.218637 | 0.693333 | 0.085259 |
| team_elo | tier3 | 1295 | 0.643673 | 0.226753 | 0.613900 | 0.079315 |
| team_elo | unknown | 0 | — | — | — | — |
| team_elo | international=1 | 505 | 0.657559 | 0.229605 | 0.621782 | 0.112683 |
| team_elo | international=0 | 1370 | 0.643170 | 0.226309 | 0.618248 | 0.077190 |

team_elo − coin (paired log loss):

| Section | Rows | team_elo log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 1875 | 0.647045 | 0.693147 | -0.046102 | [-0.059237, -0.031914] | yes |
| tier1 | 505 | 0.657559 | 0.693147 | -0.035588 | [-0.072722, 0.004750] | no |
| tier2 | 75 | 0.634475 | 0.693147 | -0.058672 | [-0.146555, 0.032800] | no |
| tier3 | 1295 | 0.643673 | 0.693147 | -0.049474 | [-0.062388, -0.035915] | yes |
| international=1 | 505 | 0.657559 | 0.693147 | -0.035588 | [-0.072722, 0.004750] | no |
| international=0 | 1370 | 0.643170 | 0.693147 | -0.049978 | [-0.063220, -0.036749] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko | all | 1875 | 0.578916 | 0.198815 | 0.681067 | 0.063902 |
| player_glicko | tier1 | 505 | 0.535555 | 0.179446 | 0.741584 | 0.070835 |
| player_glicko | tier2 | 75 | 0.579156 | 0.199788 | 0.720000 | 0.079857 |
| player_glicko | tier3 | 1295 | 0.595812 | 0.206312 | 0.655212 | 0.064713 |
| player_glicko | unknown | 0 | — | — | — | — |
| player_glicko | international=1 | 505 | 0.535555 | 0.179446 | 0.741584 | 0.070835 |
| player_glicko | international=0 | 1370 | 0.594900 | 0.205955 | 0.658759 | 0.061844 |

player_glicko − coin (paired log loss):

| Section | Rows | player_glicko log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 1875 | 0.578916 | 0.693147 | -0.114231 | [-0.129248, -0.099038] | yes |
| tier1 | 505 | 0.535555 | 0.693147 | -0.157593 | [-0.189820, -0.122043] | yes |
| tier2 | 75 | 0.579156 | 0.693147 | -0.113991 | [-0.186970, -0.038174] | yes |
| tier3 | 1295 | 0.595812 | 0.693147 | -0.097335 | [-0.115370, -0.079576] | yes |
| international=1 | 505 | 0.535555 | 0.693147 | -0.157593 | [-0.189820, -0.122043] | yes |
| international=0 | 1370 | 0.594900 | 0.693147 | -0.098247 | [-0.114779, -0.081012] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko_rw_tier_revert | all | 1875 | 0.561710 | 0.190226 | 0.710400 | 0.057551 |
| player_glicko_rw_tier_revert | tier1 | 505 | 0.516051 | 0.171550 | 0.755446 | 0.055826 |
| player_glicko_rw_tier_revert | tier2 | 75 | 0.577161 | 0.199159 | 0.666667 | 0.081264 |
| player_glicko_rw_tier_revert | tier3 | 1295 | 0.578621 | 0.196991 | 0.695367 | 0.065275 |
| player_glicko_rw_tier_revert | unknown | 0 | — | — | — | — |
| player_glicko_rw_tier_revert | international=1 | 505 | 0.516051 | 0.171550 | 0.755446 | 0.055826 |
| player_glicko_rw_tier_revert | international=0 | 1370 | 0.578541 | 0.197110 | 0.693796 | 0.062172 |

player_glicko_rw_tier_revert − coin (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 1875 | 0.561710 | 0.693147 | -0.131437 | [-0.147828, -0.114566] | yes |
| tier1 | 505 | 0.516051 | 0.693147 | -0.177096 | [-0.211398, -0.140291] | yes |
| tier2 | 75 | 0.577161 | 0.693147 | -0.115986 | [-0.191277, -0.039276] | yes |
| tier3 | 1295 | 0.578621 | 0.693147 | -0.114526 | [-0.135316, -0.094261] | yes |
| international=1 | 505 | 0.516051 | 0.693147 | -0.177096 | [-0.211398, -0.140291] | yes |
| international=0 | 1370 | 0.578541 | 0.693147 | -0.114606 | [-0.133548, -0.095377] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| team_elo+none | all | 1875 | 0.647045 | 0.227197 | 0.619200 | 0.084074 |
| team_elo+none | tier1 | 505 | 0.657559 | 0.229605 | 0.621782 | 0.112683 |
| team_elo+none | tier2 | 75 | 0.634475 | 0.218637 | 0.693333 | 0.085259 |
| team_elo+none | tier3 | 1295 | 0.643673 | 0.226753 | 0.613900 | 0.079315 |
| team_elo+none | unknown | 0 | — | — | — | — |
| team_elo+none | international=1 | 505 | 0.657559 | 0.229605 | 0.621782 | 0.112683 |
| team_elo+none | international=0 | 1370 | 0.643170 | 0.226309 | 0.618248 | 0.077190 |

team_elo+none − coin (paired log loss):

| Section | Rows | team_elo+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 1875 | 0.647045 | 0.693147 | -0.046102 | [-0.059237, -0.031914] | yes |
| tier1 | 505 | 0.657559 | 0.693147 | -0.035588 | [-0.072722, 0.004750] | no |
| tier2 | 75 | 0.634475 | 0.693147 | -0.058672 | [-0.146555, 0.032800] | no |
| tier3 | 1295 | 0.643673 | 0.693147 | -0.049474 | [-0.062388, -0.035915] | yes |
| international=1 | 505 | 0.657559 | 0.693147 | -0.035588 | [-0.072722, 0.004750] | no |
| international=0 | 1370 | 0.643170 | 0.693147 | -0.049978 | [-0.063220, -0.036749] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| team_elo+form | all | 1875 | 0.632336 | 0.220833 | 0.645867 | 0.078825 |
| team_elo+form | tier1 | 505 | 0.642803 | 0.224322 | 0.644554 | 0.103861 |
| team_elo+form | tier2 | 75 | 0.630488 | 0.217768 | 0.680000 | 0.120072 |
| team_elo+form | tier3 | 1295 | 0.628361 | 0.219650 | 0.644402 | 0.076084 |
| team_elo+form | unknown | 0 | — | — | — | — |
| team_elo+form | international=1 | 505 | 0.642803 | 0.224322 | 0.644554 | 0.103861 |
| team_elo+form | international=0 | 1370 | 0.628477 | 0.219547 | 0.646350 | 0.073550 |

team_elo+form − coin (paired log loss):

| Section | Rows | team_elo+form log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 1875 | 0.632336 | 0.693147 | -0.060812 | [-0.075393, -0.045853] | yes |
| tier1 | 505 | 0.642803 | 0.693147 | -0.050344 | [-0.086047, -0.012249] | yes |
| tier2 | 75 | 0.630488 | 0.693147 | -0.062659 | [-0.143554, 0.021868] | no |
| tier3 | 1295 | 0.628361 | 0.693147 | -0.064786 | [-0.081261, -0.048264] | yes |
| international=1 | 505 | 0.642803 | 0.693147 | -0.050344 | [-0.086047, -0.012249] | yes |
| international=0 | 1370 | 0.628477 | 0.693147 | -0.064670 | [-0.080318, -0.048779] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko+none | all | 1875 | 0.578916 | 0.198815 | 0.681067 | 0.063902 |
| player_glicko+none | tier1 | 505 | 0.535555 | 0.179446 | 0.741584 | 0.070835 |
| player_glicko+none | tier2 | 75 | 0.579156 | 0.199788 | 0.720000 | 0.079857 |
| player_glicko+none | tier3 | 1295 | 0.595812 | 0.206312 | 0.655212 | 0.064713 |
| player_glicko+none | unknown | 0 | — | — | — | — |
| player_glicko+none | international=1 | 505 | 0.535555 | 0.179446 | 0.741584 | 0.070835 |
| player_glicko+none | international=0 | 1370 | 0.594900 | 0.205955 | 0.658759 | 0.061844 |

player_glicko+none − coin (paired log loss):

| Section | Rows | player_glicko+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 1875 | 0.578916 | 0.693147 | -0.114231 | [-0.129248, -0.099038] | yes |
| tier1 | 505 | 0.535555 | 0.693147 | -0.157593 | [-0.189820, -0.122043] | yes |
| tier2 | 75 | 0.579156 | 0.693147 | -0.113991 | [-0.186970, -0.038174] | yes |
| tier3 | 1295 | 0.595812 | 0.693147 | -0.097335 | [-0.115370, -0.079576] | yes |
| international=1 | 505 | 0.535555 | 0.693147 | -0.157593 | [-0.189820, -0.122043] | yes |
| international=0 | 1370 | 0.594900 | 0.693147 | -0.098247 | [-0.114779, -0.081012] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko+form | all | 1875 | 0.575241 | 0.197097 | 0.688000 | 0.060654 |
| player_glicko+form | tier1 | 505 | 0.534780 | 0.178998 | 0.743564 | 0.071756 |
| player_glicko+form | tier2 | 75 | 0.578208 | 0.199061 | 0.706667 | 0.071094 |
| player_glicko+form | tier3 | 1295 | 0.590848 | 0.204041 | 0.665251 | 0.064077 |
| player_glicko+form | unknown | 0 | — | — | — | — |
| player_glicko+form | international=1 | 505 | 0.534780 | 0.178998 | 0.743564 | 0.071756 |
| player_glicko+form | international=0 | 1370 | 0.590156 | 0.203768 | 0.667518 | 0.060556 |

player_glicko+form − coin (paired log loss):

| Section | Rows | player_glicko+form log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 1875 | 0.575241 | 0.693147 | -0.117906 | [-0.133403, -0.102411] | yes |
| tier1 | 505 | 0.534780 | 0.693147 | -0.158367 | [-0.190679, -0.122479] | yes |
| tier2 | 75 | 0.578208 | 0.693147 | -0.114939 | [-0.184658, -0.043524] | yes |
| tier3 | 1295 | 0.590848 | 0.693147 | -0.102299 | [-0.120433, -0.083615] | yes |
| international=1 | 505 | 0.534780 | 0.693147 | -0.158367 | [-0.190679, -0.122479] | yes |
| international=0 | 1370 | 0.590156 | 0.693147 | -0.102991 | [-0.120453, -0.084710] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko_rw_tier_revert+none | all | 1875 | 0.561710 | 0.190226 | 0.710400 | 0.057551 |
| player_glicko_rw_tier_revert+none | tier1 | 505 | 0.516051 | 0.171550 | 0.755446 | 0.055826 |
| player_glicko_rw_tier_revert+none | tier2 | 75 | 0.577161 | 0.199159 | 0.666667 | 0.081264 |
| player_glicko_rw_tier_revert+none | tier3 | 1295 | 0.578621 | 0.196991 | 0.695367 | 0.065275 |
| player_glicko_rw_tier_revert+none | unknown | 0 | — | — | — | — |
| player_glicko_rw_tier_revert+none | international=1 | 505 | 0.516051 | 0.171550 | 0.755446 | 0.055826 |
| player_glicko_rw_tier_revert+none | international=0 | 1370 | 0.578541 | 0.197110 | 0.693796 | 0.062172 |

player_glicko_rw_tier_revert+none − coin (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 1875 | 0.561710 | 0.693147 | -0.131437 | [-0.147828, -0.114566] | yes |
| tier1 | 505 | 0.516051 | 0.693147 | -0.177096 | [-0.211398, -0.140291] | yes |
| tier2 | 75 | 0.577161 | 0.693147 | -0.115986 | [-0.191277, -0.039276] | yes |
| tier3 | 1295 | 0.578621 | 0.693147 | -0.114526 | [-0.135316, -0.094261] | yes |
| international=1 | 505 | 0.516051 | 0.693147 | -0.177096 | [-0.211398, -0.140291] | yes |
| international=0 | 1370 | 0.578541 | 0.693147 | -0.114606 | [-0.133548, -0.095377] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko_rw_tier_revert+form | all | 1875 | 0.556607 | 0.188020 | 0.714667 | 0.059021 |
| player_glicko_rw_tier_revert+form | tier1 | 505 | 0.513991 | 0.170588 | 0.757426 | 0.061289 |
| player_glicko_rw_tier_revert+form | tier2 | 75 | 0.573778 | 0.197276 | 0.666667 | 0.076642 |
| player_glicko_rw_tier_revert+form | tier3 | 1295 | 0.572231 | 0.194281 | 0.700772 | 0.063880 |
| player_glicko_rw_tier_revert+form | unknown | 0 | — | — | — | — |
| player_glicko_rw_tier_revert+form | international=1 | 505 | 0.513991 | 0.170588 | 0.757426 | 0.061289 |
| player_glicko_rw_tier_revert+form | international=0 | 1370 | 0.572315 | 0.194445 | 0.698905 | 0.062107 |

player_glicko_rw_tier_revert+form − coin (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+form log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 1875 | 0.556607 | 0.693147 | -0.136541 | [-0.152992, -0.119887] | yes |
| tier1 | 505 | 0.513991 | 0.693147 | -0.179156 | [-0.214391, -0.143168] | yes |
| tier2 | 75 | 0.573778 | 0.693147 | -0.119369 | [-0.190456, -0.044685] | yes |
| tier3 | 1295 | 0.572231 | 0.693147 | -0.120917 | [-0.142321, -0.100011] | yes |
| international=1 | 505 | 0.513991 | 0.693147 | -0.179156 | [-0.214391, -0.143168] | yes |
| international=0 | 1370 | 0.572315 | 0.693147 | -0.120832 | [-0.139690, -0.100603] | yes |

player_glicko − team_elo (paired log loss):

| Section | Rows | player_glicko log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 1875 | 0.578916 | 0.647045 | -0.068129 | [-0.082219, -0.054075] | yes |

player_glicko_rw_tier_revert − team_elo (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 1875 | 0.561710 | 0.647045 | -0.085335 | [-0.100763, -0.069017] | yes |

team_elo+none − team_elo (paired log loss):

| Section | Rows | team_elo+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 1875 | 0.647045 | 0.647045 | 0.000000 | [0.000000, 0.000000] | no |

team_elo+form − team_elo (paired log loss):

| Section | Rows | team_elo+form log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 1875 | 0.632336 | 0.647045 | -0.014710 | [-0.020886, -0.008055] | yes |

player_glicko+none − team_elo (paired log loss):

| Section | Rows | player_glicko+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 1875 | 0.578916 | 0.647045 | -0.068129 | [-0.082219, -0.054075] | yes |

player_glicko+form − team_elo (paired log loss):

| Section | Rows | player_glicko+form log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 1875 | 0.575241 | 0.647045 | -0.071804 | [-0.085875, -0.057404] | yes |

player_glicko_rw_tier_revert+none − team_elo (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 1875 | 0.561710 | 0.647045 | -0.085335 | [-0.100763, -0.069017] | yes |

player_glicko_rw_tier_revert+form − team_elo (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+form log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 1875 | 0.556607 | 0.647045 | -0.090438 | [-0.105496, -0.074324] | yes |

player_glicko_rw_tier_revert − player_glicko (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 1875 | 0.561710 | 0.578916 | -0.017206 | [-0.024737, -0.008651] | yes |
| tier1 | 505 | 0.516051 | 0.535555 | -0.019503 | [-0.032497, -0.004648] | yes |
| tier2 | 75 | 0.577161 | 0.579156 | -0.001995 | [-0.019507, 0.015229] | no |
| tier3 | 1295 | 0.578621 | 0.595812 | -0.017191 | [-0.027370, -0.007230] | yes |
| international=1 | 505 | 0.516051 | 0.535555 | -0.019503 | [-0.032497, -0.004648] | yes |
| international=0 | 1370 | 0.578541 | 0.594900 | -0.016359 | [-0.025826, -0.006660] | yes |

team_elo+none − player_glicko (paired log loss):

| Section | Rows | team_elo+none log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 1875 | 0.647045 | 0.578916 | 0.068129 | [0.054075, 0.082219] | yes |
| tier1 | 505 | 0.657559 | 0.535555 | 0.122004 | [0.084673, 0.158495] | yes |
| tier2 | 75 | 0.634475 | 0.579156 | 0.055319 | [-0.022255, 0.142712] | no |
| tier3 | 1295 | 0.643673 | 0.595812 | 0.047861 | [0.035765, 0.060885] | yes |
| international=1 | 505 | 0.657559 | 0.535555 | 0.122004 | [0.084673, 0.158495] | yes |
| international=0 | 1370 | 0.643170 | 0.594900 | 0.048270 | [0.034956, 0.060449] | yes |

team_elo+form − player_glicko (paired log loss):

| Section | Rows | team_elo+form log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 1875 | 0.632336 | 0.578916 | 0.053419 | [0.039596, 0.067129] | yes |
| tier1 | 505 | 0.642803 | 0.535555 | 0.107248 | [0.072567, 0.141626] | yes |
| tier2 | 75 | 0.630488 | 0.579156 | 0.051332 | [-0.022778, 0.134829] | no |
| tier3 | 1295 | 0.628361 | 0.595812 | 0.032549 | [0.019271, 0.046578] | yes |
| international=1 | 505 | 0.642803 | 0.535555 | 0.107248 | [0.072567, 0.141626] | yes |
| international=0 | 1370 | 0.628477 | 0.594900 | 0.033577 | [0.019862, 0.046608] | yes |

player_glicko+none − player_glicko (paired log loss):

| Section | Rows | player_glicko+none log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 1875 | 0.578916 | 0.578916 | 0.000000 | [0.000000, 0.000000] | no |
| tier1 | 505 | 0.535555 | 0.535555 | 0.000000 | [0.000000, 0.000000] | no |
| tier2 | 75 | 0.579156 | 0.579156 | 0.000000 | [0.000000, 0.000000] | no |
| tier3 | 1295 | 0.595812 | 0.595812 | 0.000000 | [0.000000, 0.000000] | no |
| international=1 | 505 | 0.535555 | 0.535555 | 0.000000 | [0.000000, 0.000000] | no |
| international=0 | 1370 | 0.594900 | 0.594900 | 0.000000 | [0.000000, 0.000000] | no |

player_glicko+form − player_glicko (paired log loss):

| Section | Rows | player_glicko+form log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 1875 | 0.575241 | 0.578916 | -0.003675 | [-0.006514, -0.000778] | yes |
| tier1 | 505 | 0.534780 | 0.535555 | -0.000774 | [-0.003514, 0.002173] | no |
| tier2 | 75 | 0.578208 | 0.579156 | -0.000948 | [-0.005847, 0.003904] | no |
| tier3 | 1295 | 0.590848 | 0.595812 | -0.004964 | [-0.008773, -0.001039] | yes |
| international=1 | 505 | 0.534780 | 0.535555 | -0.000774 | [-0.003514, 0.002173] | no |
| international=0 | 1370 | 0.590156 | 0.594900 | -0.004744 | [-0.008299, -0.000914] | yes |

player_glicko_rw_tier_revert+none − player_glicko (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+none log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 1875 | 0.561710 | 0.578916 | -0.017206 | [-0.024737, -0.008651] | yes |
| tier1 | 505 | 0.516051 | 0.535555 | -0.019503 | [-0.032497, -0.004648] | yes |
| tier2 | 75 | 0.577161 | 0.579156 | -0.001995 | [-0.019507, 0.015229] | no |
| tier3 | 1295 | 0.578621 | 0.595812 | -0.017191 | [-0.027370, -0.007230] | yes |
| international=1 | 505 | 0.516051 | 0.535555 | -0.019503 | [-0.032497, -0.004648] | yes |
| international=0 | 1370 | 0.578541 | 0.594900 | -0.016359 | [-0.025826, -0.006660] | yes |

player_glicko_rw_tier_revert+form − player_glicko (paired log loss):

| Section | Rows | player_glicko_rw_tier_revert+form log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 1875 | 0.556607 | 0.578916 | -0.022310 | [-0.030000, -0.013928] | yes |
| tier1 | 505 | 0.513991 | 0.535555 | -0.021564 | [-0.035035, -0.006572] | yes |
| tier2 | 75 | 0.573778 | 0.579156 | -0.005378 | [-0.026980, 0.013976] | no |
| tier3 | 1295 | 0.572231 | 0.595812 | -0.023581 | [-0.033557, -0.013601] | yes |
| international=1 | 505 | 0.513991 | 0.535555 | -0.021564 | [-0.035035, -0.006572] | yes |
| international=0 | 1370 | 0.572315 | 0.594900 | -0.022585 | [-0.032069, -0.013092] | yes |

## Holdout vs Kalshi

### team_elo: Kalshi comparison and returns



#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 557 | 0.624381 | 0.568306 | 0.056075 [0.023719, 0.087901] | yes |
| series | tier1 | 195 | 0.650117 | 0.544117 | 0.105999 [0.041729, 0.173095] | yes |
| series | tier2 | 73 | 0.639729 | 0.567515 | 0.072213 [-0.026432, 0.183692] | no |
| series | tier3 | 289 | 0.603139 | 0.584827 | 0.018312 [-0.013822, 0.051872] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 195 | 0.650117 | 0.544117 | 0.105999 [0.041729, 0.173095] | yes |
| series | international=0 | 362 | 0.610518 | 0.581336 | 0.029182 [-0.003802, 0.063370] | no |
| game | all | 773 | 0.659963 | 0.609217 | 0.050746 [0.027100, 0.077394] | yes |
| game | tier1 | 291 | 0.690466 | 0.601557 | 0.088909 [0.039684, 0.141099] | yes |
| game | tier2 | 145 | 0.671054 | 0.619558 | 0.051497 [0.007560, 0.104515] | yes |
| game | tier3 | 337 | 0.628851 | 0.611382 | 0.017469 [-0.013430, 0.049292] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 291 | 0.690466 | 0.601557 | 0.088909 [0.039684, 0.141099] | yes |
| game | international=0 | 482 | 0.641547 | 0.613841 | 0.027706 [0.002642, 0.055712] | yes |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 449 | 449 | 0.1201 | -7.74% [-18.61%, 3.72%] | $1.17 | 0.023× | 99.13% | $8.44 | 283 (166 unfilled) | -12.43% [-26.63%, 1.94%] | $1.70 |
| series | tier1 | 155 | 155 | 0.1336 | -15.08% [-33.90%, 6.81%] | $8.82 | 0.176× | 92.23% | $4.86 | 103 (52 unfilled) | -25.85% [-46.85%, -2.16%] | $5.50 |
| series | tier2 | 66 | 66 | 0.1416 | -9.28% [-37.24%, 21.66%] | $23.99 | 0.480× | 64.26% | $6.38 | 37 (29 unfilled) | -9.97% [-46.29%, 24.70%] | $30.88 |
| series | tier3 | 228 | 228 | 0.1048 | -2.30% [-17.64%, 13.47%] | $33.59 | 0.672× | 84.38% | $20.94 | 143 (85 unfilled) | -3.39% [-23.18%, 18.50%] | $25.86 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 155 | 155 | 0.1336 | -15.08% [-33.90%, 6.81%] | $8.82 | 0.176× | 92.23% | $4.86 | 103 (52 unfilled) | -25.85% [-46.85%, -2.16%] | $5.50 |
| series | international=0 | 294 | 294 | 0.1130 | -3.87% [-17.27%, 10.00%] | $14.45 | 0.289× | 93.97% | $23.32 | 180 (114 unfilled) | -4.75% [-22.79%, 12.79%] | $17.12 |
| game | all | 586 | 317 | 0.1040 | -5.55% [-13.88%, 2.94%] | $5.12 | 0.102× | 91.14% | $4.79 | 225 (361 unfilled) | -13.60% [-27.07%, 0.25%] | $5.15 |
| game | tier1 | 211 | 116 | 0.1175 | -10.68% [-24.45%, 2.86%] | $7.03 | 0.141× | 88.32% | $4.07 | 101 (110 unfilled) | -26.72% [-44.85%, -7.03%] | $8.99 |
| game | tier2 | 126 | 66 | 0.1081 | -4.43% [-21.58%, 12.31%] | $27.76 | 0.555× | 61.73% | $4.82 | 36 (90 unfilled) | -11.29% [-42.82%, 23.81%] | $36.11 |
| game | tier3 | 249 | 135 | 0.0905 | -1.77% [-14.69%, 10.98%] | $44.26 | 0.885× | 60.97% | $10.23 | 88 (161 unfilled) | 0.53% [-21.99%, 22.10%] | $42.86 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 211 | 116 | 0.1175 | -10.68% [-24.45%, 2.86%] | $7.03 | 0.141× | 88.32% | $4.07 | 101 (110 unfilled) | -26.72% [-44.85%, -7.03%] | $8.99 |
| game | international=0 | 375 | 201 | 0.0964 | -2.67% [-14.12%, 7.77%] | $27.67 | 0.553× | 77.00% | $10.86 | 124 (251 unfilled) | -2.92% [-20.71%, 15.84%] | $31.77 |
| series+game | all | 1035 | 490 | 0.1110 | -6.50% [-14.32%, 1.73%] | $1.53 | 0.031× | 99.12% | $16.14 | 508 (527 unfilled) | -12.95% [-23.22%, -2.20%] | $3.62 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 0 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-07 | series | 621 | 0.989131 | 0.137673 | fitted |
| 2026-07 | game | 434 | 1.177095 | 0.129060 | fitted |
| 2026-08 | series | 621 | 0.989131 | 0.137673 | fitted |
| 2026-08 | game | 434 | 1.177095 | 0.129060 | fitted |
| 2026-09 | series | 621 | 0.989131 | 0.137673 | fitted |
| 2026-09 | game | 434 | 1.177095 | 0.129060 | fitted |
| 2026-10 | series | 621 | 0.989131 | 0.137673 | fitted |
| 2026-10 | game | 434 | 1.177095 | 0.129060 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 557 | 0.567886 | 0.568306 | -0.000420 [-0.004657, 0.003503] | no |
| series | tier1 | 195 | 0.548052 | 0.544117 | 0.003935 [-0.004162, 0.012070] | no |
| series | tier2 | 73 | 0.565288 | 0.567515 | -0.002227 [-0.015788, 0.010142] | no |
| series | tier3 | 289 | 0.581924 | 0.584827 | -0.002902 [-0.007386, 0.001613] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 195 | 0.548052 | 0.544117 | 0.003935 [-0.004162, 0.012070] | no |
| series | international=0 | 362 | 0.578570 | 0.581336 | -0.002766 [-0.007130, 0.001500] | no |
| game | all | 773 | 0.606771 | 0.609217 | -0.002445 [-0.006854, 0.001969] | no |
| game | tier1 | 291 | 0.604289 | 0.601557 | 0.002732 [-0.005499, 0.011799] | no |
| game | tier2 | 145 | 0.616455 | 0.619558 | -0.003103 [-0.011039, 0.005143] | no |
| game | tier3 | 337 | 0.604748 | 0.611382 | -0.006634 [-0.012468, -0.000600] | yes |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 291 | 0.604289 | 0.601557 | 0.002732 [-0.005499, 0.011799] | no |
| game | international=0 | 482 | 0.608270 | 0.613841 | -0.005571 [-0.010192, -0.000715] | yes |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 86 | 86 | 0.0167 | -27.58% [-53.37%, 2.50%] | $22.31 | 0.446× | 60.18% | $4.37 | 63 (23 unfilled) | -34.39% [-62.33%, -2.70%] | $26.68 |
| series | tier1 | 39 | 39 | 0.0207 | -32.04% [-69.81%, 11.37%] | $23.91 | 0.478× | 53.71% | $4.13 | 31 (8 unfilled) | -42.02% [-80.87%, 6.19%] | $25.52 |
| series | tier2 | 17 | 17 | 0.0182 | -11.91% [-79.50%, 76.51%] | $50.33 | 1.007× | 7.01% | $3.95 | 10 (7 unfilled) | -27.17% [-100.00%, 47.11%] | $51.82 |
| series | tier3 | 30 | 30 | 0.0107 | -30.70% [-71.22%, 14.93%] | $46.41 | 0.928× | 16.28% | $3.51 | 22 (8 unfilled) | -26.96% [-75.42%, 25.25%] | $50.84 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 39 | 39 | 0.0207 | -32.04% [-69.81%, 11.37%] | $23.91 | 0.478× | 53.71% | $4.13 | 31 (8 unfilled) | -42.02% [-80.87%, 6.19%] | $25.52 |
| series | international=0 | 47 | 47 | 0.0134 | -23.88% [-61.01%, 18.74%] | $46.74 | 0.935× | 15.69% | $4.11 | 32 (15 unfilled) | -27.02% [-66.14%, 18.23%] | $52.69 |
| game | all | 170 | 103 | 0.0124 | 0.06% [-10.03%, 10.21%] | $57.10 | 1.142× | 20.60% | $5.58 | 64 (106 unfilled) | -0.08% [-17.34%, 16.27%] | $53.94 |
| game | tier1 | 76 | 43 | 0.0142 | -7.86% [-24.31%, 7.07%] | $44.61 | 0.892× | 17.66% | $4.29 | 31 (45 unfilled) | -13.01% [-40.30%, 11.85%] | $45.32 |
| game | tier2 | 30 | 19 | 0.0131 | 7.71% [-11.97%, 27.62%] | $55.04 | 1.101× | 1.97% | $4.58 | 7 (23 unfilled) | 18.28% [-24.22%, 47.60%] | $53.85 |
| game | tier3 | 64 | 41 | 0.0100 | 5.86% [-10.41%, 20.92%] | $58.10 | 1.162× | 9.09% | $4.37 | 26 (38 unfilled) | 10.41% [-13.28%, 32.59%] | $55.45 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 76 | 43 | 0.0142 | -7.86% [-24.31%, 7.07%] | $44.61 | 0.892× | 17.66% | $4.29 | 31 (45 unfilled) | -13.01% [-40.30%, 11.85%] | $45.32 |
| game | international=0 | 94 | 60 | 0.0110 | 6.45% [-6.33%, 19.50%] | $63.95 | 1.279× | 9.09% | $5.46 | 33 (61 unfilled) | 12.08% [-10.01%, 30.70%] | $59.64 |
| series+game | all | 256 | 166 | 0.0139 | -9.38% [-22.10%, 2.76%] | $27.94 | 0.559× | 56.89% | $3.66 | 127 (129 unfilled) | -17.31% [-35.30%, 1.76%] | $30.58 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| game | 2026-07 | 104 | 0.775204 | 0.679670 | 0.670295 | -22.50% (80), $20.41 | -33.23% (13), $42.45 | 20 (60 unfilled) | -13.45% [-61.77%, 35.30%] | $42.38 | 4 (9 unfilled) | 1.47% [-100.00%, 40.71%] | $48.43 |
| game | 2026-08 | 261 | 0.650138 | 0.612811 | 0.620045 | 6.48% (210), $83.44 | 6.21% (50), $61.69 | 61 (149 unfilled) | -8.74% [-31.50%, 13.56%] | $34.07 | 16 (34 unfilled) | 4.36% [-38.22%, 42.49%] | $53.50 |
| game | 2026-09 | 211 | 0.621158 | 0.578856 | 0.584628 | -6.00% (162), $31.70 | 6.22% (55), $58.58 | 66 (96 unfilled) | -12.53% [-37.06%, 13.18%] | $28.25 | 20 (35 unfilled) | 12.96% [-12.46%, 34.39%] | $58.31 |
| game | 2026-10 | 197 | 0.653703 | 0.590184 | 0.588963 | -13.77% (134), $13.12 | -4.04% (52), $46.46 | 78 (56 unfilled) | -18.33% [-41.45%, 5.09%] | $18.77 | 24 (28 unfilled) | -14.17% [-43.76%, 9.74%] | $44.58 |
| series | 2026-07 | 79 | 0.763888 | 0.690002 | 0.689503 | 4.10% (57), $49.38 | -24.23% (13), $43.21 | 36 (21 unfilled) | 2.72% [-40.60%, 51.84%] | $38.28 | 10 (3 unfilled) | -31.18% [-100.00%, 61.59%] | $43.15 |
| series | 2026-08 | 147 | 0.627992 | 0.569583 | 0.570451 | -2.93% (127), $51.26 | -26.17% (31), $31.98 | 85 (42 unfilled) | -7.36% [-30.54%, 16.28%] | $36.47 | 25 (6 unfilled) | -30.02% [-75.54%, 26.48%] | $32.20 |
| series | 2026-09 | 145 | 0.584242 | 0.526694 | 0.527022 | -12.10% (115), $12.89 | -21.08% (23), $47.13 | 73 (42 unfilled) | -7.86% [-34.66%, 22.07%] | $34.57 | 14 (9 unfilled) | -15.12% [-74.15%, 51.89%] | $51.13 |
| series | 2026-10 | 186 | 0.593565 | 0.546790 | 0.547318 | -12.96% (150), $6.68 | -40.07% (19), $42.98 | 89 (61 unfilled) | -27.12% [-50.99%, -1.84%] | $5.75 | 14 (5 unfilled) | -63.72% [-100.00%, -12.13%] | $46.73 |

### player_glicko: Kalshi comparison and returns



#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 557 | 0.546155 | 0.568306 | -0.022151 [-0.044412, -0.002057] | yes |
| series | tier1 | 195 | 0.544881 | 0.544117 | 0.000764 [-0.035287, 0.035750] | no |
| series | tier2 | 73 | 0.582032 | 0.567515 | 0.014517 [-0.040636, 0.066745] | no |
| series | tier3 | 289 | 0.537953 | 0.584827 | -0.046874 [-0.076718, -0.016314] | yes |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 195 | 0.544881 | 0.544117 | 0.000764 [-0.035287, 0.035750] | no |
| series | international=0 | 362 | 0.546842 | 0.581336 | -0.034494 [-0.060822, -0.007207] | yes |
| game | all | 773 | 0.604249 | 0.609217 | -0.004968 [-0.019211, 0.009481] | no |
| game | tier1 | 291 | 0.608513 | 0.601557 | 0.006956 [-0.012524, 0.029435] | no |
| game | tier2 | 145 | 0.640710 | 0.619558 | 0.021153 [-0.010594, 0.052222] | no |
| game | tier3 | 337 | 0.584879 | 0.611382 | -0.026503 [-0.052018, -0.001206] | yes |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 291 | 0.608513 | 0.601557 | 0.006956 [-0.012524, 0.029435] | no |
| game | international=0 | 482 | 0.601674 | 0.613841 | -0.012167 [-0.033188, 0.008869] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 430 | 430 | 0.0881 | 6.70% [-4.66%, 18.33%] | $826.54 | 16.531× | 76.77% | $217.61 | 282 (148 unfilled) | 5.76% [-7.35%, 21.26%] | $138.31 |
| series | tier1 | 144 | 144 | 0.0812 | -6.75% [-28.26%, 16.45%] | $31.72 | 0.634× | 71.51% | $6.39 | 97 (47 unfilled) | -5.57% [-31.68%, 24.64%] | $35.63 |
| series | tier2 | 58 | 58 | 0.0856 | -11.83% [-40.80%, 20.55%] | $26.89 | 0.538× | 61.52% | $6.49 | 37 (21 unfilled) | -19.93% [-52.04%, 16.01%] | $22.40 |
| series | tier3 | 228 | 228 | 0.0932 | 19.96% [5.73%, 35.65%] | $2093.86 | 41.877× | 46.36% | $239.80 | 148 (80 unfilled) | 19.68% [2.02%, 37.70%] | $370.41 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 144 | 144 | 0.0812 | -6.75% [-28.26%, 16.45%] | $31.72 | 0.634× | 71.51% | $6.39 | 97 (47 unfilled) | -5.57% [-31.68%, 24.64%] | $35.63 |
| series | international=0 | 286 | 286 | 0.0916 | 13.49% [0.40%, 25.92%] | $2081.79 | 41.636× | 53.74% | $244.35 | 185 (101 unfilled) | 11.72% [-4.26%, 28.22%] | $199.72 |
| game | all | 516 | 284 | 0.0699 | 1.93% [-6.81%, 10.61%] | $77.24 | 1.545× | 59.31% | $15.87 | 196 (320 unfilled) | -6.08% [-20.14%, 9.08%] | $22.89 |
| game | tier1 | 161 | 93 | 0.0608 | -9.57% [-23.86%, 5.34%] | $23.61 | 0.472× | 57.18% | $3.51 | 72 (89 unfilled) | -19.24% [-41.27%, 3.75%] | $22.01 |
| game | tier2 | 111 | 56 | 0.0658 | -12.10% [-29.34%, 6.11%] | $33.74 | 0.675× | 34.83% | $2.72 | 33 (78 unfilled) | -11.49% [-44.65%, 22.09%] | $49.28 |
| game | tier3 | 244 | 135 | 0.0777 | 15.93% [4.21%, 28.28%] | $239.80 | 4.796× | 35.60% | $34.26 | 91 (153 unfilled) | 6.32% [-14.48%, 27.56%] | $52.28 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 161 | 93 | 0.0608 | -9.57% [-23.86%, 5.34%] | $23.61 | 0.472× | 57.18% | $3.51 | 72 (89 unfilled) | -19.24% [-41.27%, 3.75%] | $22.01 |
| game | international=0 | 355 | 191 | 0.0740 | 7.15% [-3.30%, 17.32%] | $161.17 | 3.223× | 40.63% | $23.03 | 124 (231 unfilled) | 1.57% [-16.47%, 19.63%] | $50.12 |
| series+game | all | 946 | 471 | 0.0782 | 4.10% [-4.35%, 12.48%] | $1017.69 | 20.354× | 60.79% | $141.97 | 478 (468 unfilled) | 0.91% [-9.88%, 12.02%] | $162.90 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 0 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-07 | series | 621 | 1.053140 | 0.561857 | fitted |
| 2026-07 | game | 434 | 1.193713 | 0.013709 | fitted |
| 2026-08 | series | 621 | 1.053140 | 0.561857 | fitted |
| 2026-08 | game | 434 | 1.193713 | 0.013709 | fitted |
| 2026-09 | series | 621 | 1.053140 | 0.561857 | fitted |
| 2026-09 | game | 434 | 1.193713 | 0.013709 | fitted |
| 2026-10 | series | 621 | 1.053140 | 0.561857 | fitted |
| 2026-10 | game | 434 | 1.193713 | 0.013709 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 557 | 0.543744 | 0.568306 | -0.024562 [-0.036698, -0.013612] | yes |
| series | tier1 | 195 | 0.532350 | 0.544117 | -0.011768 [-0.031254, 0.006621] | no |
| series | tier2 | 73 | 0.564806 | 0.567515 | -0.002710 [-0.031239, 0.025139] | no |
| series | tier3 | 289 | 0.546112 | 0.584827 | -0.038715 [-0.055345, -0.021557] | yes |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 195 | 0.532350 | 0.544117 | -0.011768 [-0.031254, 0.006621] | no |
| series | international=0 | 362 | 0.549882 | 0.581336 | -0.031454 [-0.046040, -0.016443] | yes |
| game | all | 773 | 0.606846 | 0.609217 | -0.002370 [-0.006244, 0.001986] | no |
| game | tier1 | 291 | 0.602199 | 0.601557 | 0.000643 [-0.006483, 0.008703] | no |
| game | tier2 | 145 | 0.618401 | 0.619558 | -0.001156 [-0.009253, 0.007075] | no |
| game | tier3 | 337 | 0.605887 | 0.611382 | -0.005494 [-0.011054, -0.000067] | yes |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 291 | 0.602199 | 0.601557 | 0.000643 [-0.006483, 0.008703] | no |
| game | international=0 | 482 | 0.609652 | 0.613841 | -0.004189 [-0.008538, 0.000420] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 339 | 339 | 0.0440 | 13.17% [0.98%, 27.03%] | $1540.78 | 30.816× | 65.55% | $149.80 | 218 (121 unfilled) | 10.30% [-5.92%, 26.49%] | $205.97 |
| series | tier1 | 106 | 106 | 0.0402 | 4.81% [-19.48%, 33.10%] | $104.26 | 2.085× | 33.65% | $8.95 | 71 (35 unfilled) | 3.88% [-28.43%, 40.29%] | $74.25 |
| series | tier2 | 51 | 51 | 0.0342 | -16.72% [-46.51%, 16.68%] | $46.38 | 0.928× | 41.81% | $7.60 | 32 (19 unfilled) | -33.52% [-64.06%, -1.85%] | $36.09 |
| series | tier3 | 182 | 182 | 0.0489 | 26.46% [10.18%, 43.47%] | $883.69 | 17.674× | 42.04% | $93.88 | 115 (67 unfilled) | 26.54% [5.89%, 48.49%] | $218.28 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 106 | 106 | 0.0402 | 4.81% [-19.48%, 33.10%] | $104.26 | 2.085× | 33.65% | $8.95 | 71 (35 unfilled) | 3.88% [-28.43%, 40.29%] | $74.25 |
| series | international=0 | 233 | 233 | 0.0457 | 16.97% [1.74%, 32.44%] | $780.90 | 15.618× | 64.32% | $138.21 | 147 (86 unfilled) | 13.41% [-4.95%, 32.20%] | $149.91 |
| game | all | 146 | 93 | 0.0081 | -0.08% [-7.92%, 7.20%] | $60.24 | 1.205× | 15.10% | $5.95 | 49 (97 unfilled) | 2.64% [-11.57%, 15.31%] | $57.00 |
| game | tier1 | 57 | 36 | 0.0055 | 0.97% [-11.07%, 11.21%] | $52.50 | 1.050× | 7.14% | $5.39 | 21 (36 unfilled) | -10.53% [-36.58%, 10.52%] | $48.93 |
| game | tier2 | 37 | 22 | 0.0116 | 1.83% [-12.08%, 15.42%] | $50.71 | 1.014× | 16.89% | $4.92 | 9 (28 unfilled) | 15.26% [-15.70%, 34.04%] | $53.17 |
| game | tier3 | 52 | 35 | 0.0085 | -2.58% [-18.08%, 10.77%] | $56.27 | 1.125× | 5.10% | $4.37 | 19 (33 unfilled) | 11.17% [-8.65%, 25.49%] | $54.73 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 57 | 36 | 0.0055 | 0.97% [-11.07%, 11.21%] | $52.50 | 1.050× | 7.14% | $5.39 | 21 (36 unfilled) | -10.53% [-36.58%, 10.52%] | $48.93 |
| game | international=0 | 89 | 57 | 0.0098 | -0.75% [-11.60%, 8.99%] | $57.32 | 1.146× | 15.10% | $5.34 | 28 (61 unfilled) | 12.49% [-3.31%, 25.14%] | $58.17 |
| series+game | all | 485 | 367 | 0.0332 | 9.24% [-0.05%, 18.17%] | $1624.35 | 32.487× | 56.25% | $166.85 | 267 (218 unfilled) | 8.92% [-4.64%, 23.44%] | $225.60 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| game | 2026-07 | 104 | 0.682114 | 0.673500 | 0.670295 | 8.55% (64), $61.03 | -51.36% (5), $46.93 | 17 (47 unfilled) | 8.94% [-43.81%, 59.44%] | $48.67 | 0 (5 unfilled) | — | $48.98 |
| game | 2026-08 | 261 | 0.603722 | 0.616372 | 0.620045 | 8.64% (168), $68.83 | 4.25% (32), $56.35 | 50 (118 unfilled) | 6.28% [-18.38%, 32.15%] | $54.68 | 6 (26 unfilled) | -22.92% [-63.97%, 17.41%] | $50.50 |
| game | 2026-09 | 211 | 0.572991 | 0.580522 | 0.584628 | 2.56% (155), $89.12 | -0.25% (64), $51.94 | 63 (92 unfilled) | -6.63% [-31.34%, 17.92%] | $53.37 | 22 (42 unfilled) | 14.12% [-3.75%, 27.13%] | $56.45 |
| game | 2026-10 | 197 | 0.597318 | 0.587234 | 0.588963 | -10.82% (129), $25.30 | 2.79% (45), $54.85 | 66 (63 unfilled) | -18.76% [-43.20%, 6.99%] | $20.10 | 21 (24 unfilled) | -2.13% [-25.73%, 16.06%] | $50.99 |
| series | 2026-07 | 79 | 0.649772 | 0.660027 | 0.689503 | 36.93% (62), $220.13 | 40.41% (50), $132.43 | 44 (18 unfilled) | 43.42% [-1.32%, 91.62%] | $138.55 | 34 (16 unfilled) | 42.46% [-6.07%, 96.89%] | $72.92 |
| series | 2026-08 | 147 | 0.534462 | 0.537652 | 0.570451 | 6.20% (117), $130.89 | 13.57% (91), $166.47 | 75 (42 unfilled) | -3.45% [-28.68%, 21.27%] | $42.68 | 59 (32 unfilled) | -0.08% [-28.18%, 29.20%] | $75.26 |
| series | 2026-09 | 145 | 0.525182 | 0.511327 | 0.527022 | 3.94% (109), $36.36 | -0.79% (94), $51.38 | 77 (32 unfilled) | 9.52% [-16.92%, 37.01%] | $83.45 | 66 (28 unfilled) | 4.47% [-23.24%, 33.51%] | $65.06 |
| series | 2026-10 | 186 | 0.527737 | 0.524441 | 0.547318 | -3.98% (142), $67.35 | 12.32% (104), $184.61 | 86 (56 unfilled) | -8.85% [-31.97%, 15.16%] | $44.62 | 59 (45 unfilled) | 8.67% [-20.78%, 38.31%] | $87.67 |

### player_glicko_rw_tier_revert: Kalshi comparison and returns



#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 557 | 0.543716 | 0.568306 | -0.024590 [-0.046699, -0.004257] | yes |
| series | tier1 | 195 | 0.538012 | 0.544117 | -0.006105 [-0.039654, 0.028367] | no |
| series | tier2 | 73 | 0.580883 | 0.567515 | 0.013368 [-0.034711, 0.058896] | no |
| series | tier3 | 289 | 0.538176 | 0.584827 | -0.046650 [-0.078024, -0.013496] | yes |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 195 | 0.538012 | 0.544117 | -0.006105 [-0.039654, 0.028367] | no |
| series | international=0 | 362 | 0.546789 | 0.581336 | -0.034547 [-0.062357, -0.006932] | yes |
| game | all | 773 | 0.602363 | 0.609217 | -0.006854 [-0.019974, 0.006534] | no |
| game | tier1 | 291 | 0.608996 | 0.601557 | 0.007440 [-0.009703, 0.027434] | no |
| game | tier2 | 145 | 0.630162 | 0.619558 | 0.010604 [-0.014096, 0.034441] | no |
| game | tier3 | 337 | 0.584674 | 0.611382 | -0.026708 [-0.050514, -0.002940] | yes |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 291 | 0.608996 | 0.601557 | 0.007440 [-0.009703, 0.027434] | no |
| game | international=0 | 482 | 0.598358 | 0.613841 | -0.015483 [-0.034882, 0.003779] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 430 | 430 | 0.0832 | 7.19% [-4.09%, 19.35%] | $3127.36 | 62.547× | 58.93% | $248.78 | 280 (150 unfilled) | 5.59% [-8.99%, 20.04%] | $265.67 |
| series | tier1 | 146 | 146 | 0.0723 | -1.44% [-22.77%, 20.59%] | $61.97 | 1.239× | 66.31% | $6.76 | 98 (48 unfilled) | 2.00% [-24.24%, 31.57%] | $66.32 |
| series | tier2 | 61 | 61 | 0.0658 | -18.13% [-47.18%, 14.55%] | $27.55 | 0.551× | 56.43% | $5.87 | 36 (25 unfilled) | -33.16% [-63.14%, 2.16%] | $20.29 |
| series | tier3 | 223 | 223 | 0.0951 | 19.81% [5.48%, 34.71%] | $2696.46 | 53.929× | 48.98% | $248.78 | 146 (77 unfilled) | 17.61% [-0.66%, 36.01%] | $410.99 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 146 | 146 | 0.0723 | -1.44% [-22.77%, 20.59%] | $61.97 | 1.239× | 66.31% | $6.76 | 98 (48 unfilled) | 2.00% [-24.24%, 31.57%] | $66.32 |
| series | international=0 | 284 | 284 | 0.0888 | 11.63% [-1.86%, 24.93%] | $2595.05 | 51.901× | 50.77% | $248.78 | 182 (102 unfilled) | 7.52% [-8.08%, 24.38%] | $179.01 |
| game | all | 488 | 272 | 0.0600 | 1.50% [-8.23%, 11.12%] | $77.36 | 1.547× | 57.48% | $18.01 | 192 (296 unfilled) | -7.02% [-22.34%, 8.48%] | $27.23 |
| game | tier1 | 147 | 87 | 0.0511 | -10.39% [-29.20%, 7.89%] | $21.93 | 0.439× | 58.81% | $3.73 | 70 (77 unfilled) | -20.63% [-45.18%, 4.61%] | $22.82 |
| game | tier2 | 101 | 53 | 0.0481 | -14.10% [-34.69%, 5.85%] | $40.12 | 0.802× | 27.07% | $4.58 | 30 (71 unfilled) | -22.21% [-56.16%, 14.72%] | $48.90 |
| game | tier3 | 240 | 132 | 0.0704 | 15.37% [1.47%, 29.76%] | $215.85 | 4.317× | 39.57% | $30.37 | 92 (148 unfilled) | 8.33% [-14.80%, 29.75%] | $60.57 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 147 | 87 | 0.0511 | -10.39% [-29.20%, 7.89%] | $21.93 | 0.439× | 58.81% | $3.73 | 70 (77 unfilled) | -20.63% [-45.18%, 4.61%] | $22.82 |
| game | international=0 | 341 | 185 | 0.0638 | 6.63% [-4.30%, 18.04%] | $172.61 | 3.452× | 41.53% | $26.17 | 122 (219 unfilled) | 0.79% [-18.45%, 20.25%] | $58.22 |
| series+game | all | 918 | 456 | 0.0709 | 4.16% [-4.70%, 13.61%] | $742.85 | 14.857× | 66.95% | $106.92 | 472 (446 unfilled) | 0.46% [-10.97%, 12.00%] | $220.60 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 0 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-07 | series | 621 | 1.045637 | 0.626616 | fitted |
| 2026-07 | game | 434 | 1.207276 | -0.178366 | fitted |
| 2026-08 | series | 621 | 1.045637 | 0.626616 | fitted |
| 2026-08 | game | 434 | 1.207276 | -0.178366 | fitted |
| 2026-09 | series | 621 | 1.045637 | 0.626616 | fitted |
| 2026-09 | game | 434 | 1.207276 | -0.178366 | fitted |
| 2026-10 | series | 621 | 1.045637 | 0.626616 | fitted |
| 2026-10 | game | 434 | 1.207276 | -0.178366 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 557 | 0.541719 | 0.568306 | -0.026587 [-0.040588, -0.014411] | yes |
| series | tier1 | 195 | 0.529737 | 0.544117 | -0.014380 [-0.034819, 0.005901] | no |
| series | tier2 | 73 | 0.567849 | 0.567515 | 0.000333 [-0.028840, 0.027472] | no |
| series | tier3 | 289 | 0.543204 | 0.584827 | -0.041622 [-0.061481, -0.021379] | yes |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 195 | 0.529737 | 0.544117 | -0.014380 [-0.034819, 0.005901] | no |
| series | international=0 | 362 | 0.548174 | 0.581336 | -0.033162 [-0.050409, -0.016130] | yes |
| game | all | 773 | 0.613090 | 0.609217 | 0.003874 [-0.001775, 0.009474] | no |
| game | tier1 | 291 | 0.604725 | 0.601557 | 0.003168 [-0.006121, 0.013187] | no |
| game | tier2 | 145 | 0.619516 | 0.619558 | -0.000041 [-0.010200, 0.010520] | no |
| game | tier3 | 337 | 0.617549 | 0.611382 | 0.006168 [-0.002451, 0.014785] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 291 | 0.604725 | 0.601557 | 0.003168 [-0.006121, 0.013187] | no |
| game | international=0 | 482 | 0.618141 | 0.613841 | 0.004300 [-0.002876, 0.011637] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 354 | 354 | 0.0486 | 16.71% [4.40%, 30.44%] | $3064.04 | 61.281× | 62.89% | $248.78 | 229 (125 unfilled) | 13.43% [-2.22%, 29.53%] | $246.62 |
| series | tier1 | 114 | 114 | 0.0412 | 8.56% [-15.46%, 33.84%] | $95.66 | 1.913× | 46.99% | $9.42 | 80 (34 unfilled) | 8.18% [-20.81%, 42.36%] | $65.98 |
| series | tier2 | 50 | 50 | 0.0326 | -11.09% [-41.38%, 26.39%] | $45.40 | 0.908× | 32.44% | $6.42 | 29 (21 unfilled) | -39.78% [-69.52%, -8.05%] | $36.67 |
| series | tier3 | 190 | 190 | 0.0572 | 28.95% [12.89%, 44.70%] | $1939.82 | 38.796× | 43.46% | $192.44 | 120 (70 unfilled) | 29.88% [9.16%, 50.35%] | $265.92 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 114 | 114 | 0.0412 | 8.56% [-15.46%, 33.84%] | $95.66 | 1.913× | 46.99% | $9.42 | 80 (34 unfilled) | 8.18% [-20.81%, 42.36%] | $65.98 |
| series | international=0 | 240 | 240 | 0.0521 | 20.58% [6.34%, 35.34%] | $1668.42 | 33.368× | 62.39% | $224.02 | 149 (91 unfilled) | 16.25% [-1.17%, 34.08%] | $201.25 |
| game | all | 262 | 155 | 0.0125 | -7.26% [-14.80%, 0.14%] | $24.00 | 0.480× | 53.43% | $4.27 | 99 (163 unfilled) | -4.57% [-16.71%, 7.28%] | $46.24 |
| game | tier1 | 104 | 63 | 0.0104 | -3.16% [-14.22%, 7.93%] | $39.90 | 0.798× | 22.63% | $4.70 | 43 (61 unfilled) | -0.66% [-19.24%, 15.76%] | $44.61 |
| game | tier2 | 54 | 30 | 0.0136 | -10.56% [-26.30%, 3.73%] | $45.76 | 0.915× | 17.40% | $5.04 | 16 (38 unfilled) | -10.05% [-40.11%, 16.50%] | $51.49 |
| game | tier3 | 104 | 62 | 0.0140 | -9.63% [-23.66%, 3.57%] | $33.02 | 0.660× | 38.86% | $3.39 | 40 (64 unfilled) | -6.58% [-27.44%, 12.53%] | $50.24 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 104 | 63 | 0.0104 | -3.16% [-14.22%, 7.93%] | $39.90 | 0.798× | 22.63% | $4.70 | 43 (61 unfilled) | -0.66% [-19.24%, 15.76%] | $44.61 |
| game | international=0 | 158 | 92 | 0.0139 | -9.95% [-20.22%, 0.22%] | $30.30 | 0.606× | 45.47% | $3.71 | 56 (102 unfilled) | -7.57% [-25.65%, 8.67%] | $51.82 |
| series+game | all | 616 | 398 | 0.0332 | 6.61% [-0.58%, 13.74%] | $2243.42 | 44.868× | 42.77% | $237.65 | 328 (288 unfilled) | 8.05% [-3.04%, 20.13%] | $266.88 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| game | 2026-07 | 104 | 0.655158 | 0.680951 | 0.670295 | 24.76% (63), $89.50 | -22.92% (13), $47.39 | 15 (48 unfilled) | 22.38% [-33.99%, 76.49%] | $58.27 | 3 (10 unfilled) | -47.80% [-100.00%, 56.59%] | $50.46 |
| game | 2026-08 | 261 | 0.606333 | 0.624652 | 0.620045 | 1.58% (171), $47.08 | -10.86% (69), $34.78 | 49 (122 unfilled) | 5.21% [-22.32%, 30.96%] | $53.66 | 16 (53 unfilled) | -2.77% [-37.61%, 27.15%] | $48.45 |
| game | 2026-09 | 211 | 0.575022 | 0.586690 | 0.584628 | 1.82% (143), $97.38 | -8.04% (104), $37.28 | 66 (77 unfilled) | -9.85% [-35.00%, 14.83%] | $52.36 | 41 (63 unfilled) | -9.55% [-29.60%, 10.26%] | $45.51 |
| game | 2026-10 | 197 | 0.598515 | 0.590224 | 0.588963 | -12.19% (111), $23.04 | -0.22% (76), $49.64 | 62 (49 unfilled) | -20.68% [-48.91%, 11.79%] | $20.81 | 39 (37 unfilled) | 3.28% [-14.32%, 17.80%] | $51.96 |
| series | 2026-07 | 79 | 0.637400 | 0.649375 | 0.689503 | 41.01% (63), $244.85 | 51.16% (51), $153.30 | 43 (20 unfilled) | 46.76% [3.33%, 93.11%] | $119.14 | 34 (17 unfilled) | 57.10% [9.21%, 112.97%] | $71.10 |
| series | 2026-08 | 147 | 0.533651 | 0.535233 | 0.570451 | 1.60% (118), $91.71 | 10.84% (97), $172.20 | 76 (42 unfilled) | -12.67% [-35.80%, 12.88%] | $34.43 | 61 (36 unfilled) | -4.44% [-30.17%, 24.16%] | $62.85 |
| series | 2026-09 | 145 | 0.525825 | 0.513115 | 0.527022 | 3.93% (114), $70.60 | 10.08% (98), $73.04 | 79 (35 unfilled) | 9.19% [-16.62%, 37.23%] | $118.60 | 68 (30 unfilled) | 15.65% [-11.72%, 45.72%] | $86.64 |
| series | 2026-10 | 186 | 0.525827 | 0.523419 | 0.547318 | -0.98% (135), $114.13 | 11.72% (108), $211.37 | 82 (53 unfilled) | -2.56% [-27.02%, 21.63%] | $67.51 | 66 (42 unfilled) | 5.17% [-20.35%, 34.41%] | $93.35 |

### team_elo+none: Kalshi comparison and returns

none

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 557 | 0.624381 | 0.568306 | 0.056075 [0.023719, 0.087901] | yes |
| series | tier1 | 195 | 0.650117 | 0.544117 | 0.105999 [0.041729, 0.173095] | yes |
| series | tier2 | 73 | 0.639729 | 0.567515 | 0.072213 [-0.026432, 0.183692] | no |
| series | tier3 | 289 | 0.603139 | 0.584827 | 0.018312 [-0.013822, 0.051872] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 195 | 0.650117 | 0.544117 | 0.105999 [0.041729, 0.173095] | yes |
| series | international=0 | 362 | 0.610518 | 0.581336 | 0.029182 [-0.003802, 0.063370] | no |
| game | all | 773 | 0.659963 | 0.609217 | 0.050746 [0.027100, 0.077394] | yes |
| game | tier1 | 291 | 0.690466 | 0.601557 | 0.088909 [0.039684, 0.141099] | yes |
| game | tier2 | 145 | 0.671054 | 0.619558 | 0.051497 [0.007560, 0.104515] | yes |
| game | tier3 | 337 | 0.628851 | 0.611382 | 0.017469 [-0.013430, 0.049292] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 291 | 0.690466 | 0.601557 | 0.088909 [0.039684, 0.141099] | yes |
| game | international=0 | 482 | 0.641547 | 0.613841 | 0.027706 [0.002642, 0.055712] | yes |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 449 | 449 | 0.1201 | -7.74% [-18.61%, 3.72%] | $1.17 | 0.023× | 99.13% | $8.44 | 283 (166 unfilled) | -12.43% [-26.63%, 1.94%] | $1.70 |
| series | tier1 | 155 | 155 | 0.1336 | -15.08% [-33.90%, 6.81%] | $8.82 | 0.176× | 92.23% | $4.86 | 103 (52 unfilled) | -25.85% [-46.85%, -2.16%] | $5.50 |
| series | tier2 | 66 | 66 | 0.1416 | -9.28% [-37.24%, 21.66%] | $23.99 | 0.480× | 64.26% | $6.38 | 37 (29 unfilled) | -9.97% [-46.29%, 24.70%] | $30.88 |
| series | tier3 | 228 | 228 | 0.1048 | -2.30% [-17.64%, 13.47%] | $33.59 | 0.672× | 84.38% | $20.94 | 143 (85 unfilled) | -3.39% [-23.18%, 18.50%] | $25.86 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 155 | 155 | 0.1336 | -15.08% [-33.90%, 6.81%] | $8.82 | 0.176× | 92.23% | $4.86 | 103 (52 unfilled) | -25.85% [-46.85%, -2.16%] | $5.50 |
| series | international=0 | 294 | 294 | 0.1130 | -3.87% [-17.27%, 10.00%] | $14.45 | 0.289× | 93.97% | $23.32 | 180 (114 unfilled) | -4.75% [-22.79%, 12.79%] | $17.12 |
| game | all | 586 | 317 | 0.1040 | -5.55% [-13.88%, 2.94%] | $5.12 | 0.102× | 91.14% | $4.79 | 225 (361 unfilled) | -13.60% [-27.07%, 0.25%] | $5.15 |
| game | tier1 | 211 | 116 | 0.1175 | -10.68% [-24.45%, 2.86%] | $7.03 | 0.141× | 88.32% | $4.07 | 101 (110 unfilled) | -26.72% [-44.85%, -7.03%] | $8.99 |
| game | tier2 | 126 | 66 | 0.1081 | -4.43% [-21.58%, 12.31%] | $27.76 | 0.555× | 61.73% | $4.82 | 36 (90 unfilled) | -11.29% [-42.82%, 23.81%] | $36.11 |
| game | tier3 | 249 | 135 | 0.0905 | -1.77% [-14.69%, 10.98%] | $44.26 | 0.885× | 60.97% | $10.23 | 88 (161 unfilled) | 0.53% [-21.99%, 22.10%] | $42.86 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 211 | 116 | 0.1175 | -10.68% [-24.45%, 2.86%] | $7.03 | 0.141× | 88.32% | $4.07 | 101 (110 unfilled) | -26.72% [-44.85%, -7.03%] | $8.99 |
| game | international=0 | 375 | 201 | 0.0964 | -2.67% [-14.12%, 7.77%] | $27.67 | 0.553× | 77.00% | $10.86 | 124 (251 unfilled) | -2.92% [-20.71%, 15.84%] | $31.77 |
| series+game | all | 1035 | 490 | 0.1110 | -6.50% [-14.32%, 1.73%] | $1.53 | 0.031× | 99.12% | $16.14 | 508 (527 unfilled) | -12.95% [-23.22%, -2.20%] | $3.62 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 0 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-07 | series | 621 | 0.989131 | 0.137673 | fitted |
| 2026-07 | game | 434 | 1.177095 | 0.129060 | fitted |
| 2026-08 | series | 621 | 0.989131 | 0.137673 | fitted |
| 2026-08 | game | 434 | 1.177095 | 0.129060 | fitted |
| 2026-09 | series | 621 | 0.989131 | 0.137673 | fitted |
| 2026-09 | game | 434 | 1.177095 | 0.129060 | fitted |
| 2026-10 | series | 621 | 0.989131 | 0.137673 | fitted |
| 2026-10 | game | 434 | 1.177095 | 0.129060 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 557 | 0.567886 | 0.568306 | -0.000420 [-0.004657, 0.003503] | no |
| series | tier1 | 195 | 0.548052 | 0.544117 | 0.003935 [-0.004162, 0.012070] | no |
| series | tier2 | 73 | 0.565288 | 0.567515 | -0.002227 [-0.015788, 0.010142] | no |
| series | tier3 | 289 | 0.581924 | 0.584827 | -0.002902 [-0.007386, 0.001613] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 195 | 0.548052 | 0.544117 | 0.003935 [-0.004162, 0.012070] | no |
| series | international=0 | 362 | 0.578570 | 0.581336 | -0.002766 [-0.007130, 0.001500] | no |
| game | all | 773 | 0.606771 | 0.609217 | -0.002445 [-0.006854, 0.001969] | no |
| game | tier1 | 291 | 0.604289 | 0.601557 | 0.002732 [-0.005499, 0.011799] | no |
| game | tier2 | 145 | 0.616455 | 0.619558 | -0.003103 [-0.011039, 0.005143] | no |
| game | tier3 | 337 | 0.604748 | 0.611382 | -0.006634 [-0.012468, -0.000600] | yes |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 291 | 0.604289 | 0.601557 | 0.002732 [-0.005499, 0.011799] | no |
| game | international=0 | 482 | 0.608270 | 0.613841 | -0.005571 [-0.010192, -0.000715] | yes |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 86 | 86 | 0.0167 | -27.58% [-53.37%, 2.50%] | $22.31 | 0.446× | 60.18% | $4.37 | 63 (23 unfilled) | -34.39% [-62.33%, -2.70%] | $26.68 |
| series | tier1 | 39 | 39 | 0.0207 | -32.04% [-69.81%, 11.37%] | $23.91 | 0.478× | 53.71% | $4.13 | 31 (8 unfilled) | -42.02% [-80.87%, 6.19%] | $25.52 |
| series | tier2 | 17 | 17 | 0.0182 | -11.91% [-79.50%, 76.51%] | $50.33 | 1.007× | 7.01% | $3.95 | 10 (7 unfilled) | -27.17% [-100.00%, 47.11%] | $51.82 |
| series | tier3 | 30 | 30 | 0.0107 | -30.70% [-71.22%, 14.93%] | $46.41 | 0.928× | 16.28% | $3.51 | 22 (8 unfilled) | -26.96% [-75.42%, 25.25%] | $50.84 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 39 | 39 | 0.0207 | -32.04% [-69.81%, 11.37%] | $23.91 | 0.478× | 53.71% | $4.13 | 31 (8 unfilled) | -42.02% [-80.87%, 6.19%] | $25.52 |
| series | international=0 | 47 | 47 | 0.0134 | -23.88% [-61.01%, 18.74%] | $46.74 | 0.935× | 15.69% | $4.11 | 32 (15 unfilled) | -27.02% [-66.14%, 18.23%] | $52.69 |
| game | all | 170 | 103 | 0.0124 | 0.06% [-10.03%, 10.21%] | $57.10 | 1.142× | 20.60% | $5.58 | 64 (106 unfilled) | -0.08% [-17.34%, 16.27%] | $53.94 |
| game | tier1 | 76 | 43 | 0.0142 | -7.86% [-24.31%, 7.07%] | $44.61 | 0.892× | 17.66% | $4.29 | 31 (45 unfilled) | -13.01% [-40.30%, 11.85%] | $45.32 |
| game | tier2 | 30 | 19 | 0.0131 | 7.71% [-11.97%, 27.62%] | $55.04 | 1.101× | 1.97% | $4.58 | 7 (23 unfilled) | 18.28% [-24.22%, 47.60%] | $53.85 |
| game | tier3 | 64 | 41 | 0.0100 | 5.86% [-10.41%, 20.92%] | $58.10 | 1.162× | 9.09% | $4.37 | 26 (38 unfilled) | 10.41% [-13.28%, 32.59%] | $55.45 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 76 | 43 | 0.0142 | -7.86% [-24.31%, 7.07%] | $44.61 | 0.892× | 17.66% | $4.29 | 31 (45 unfilled) | -13.01% [-40.30%, 11.85%] | $45.32 |
| game | international=0 | 94 | 60 | 0.0110 | 6.45% [-6.33%, 19.50%] | $63.95 | 1.279× | 9.09% | $5.46 | 33 (61 unfilled) | 12.08% [-10.01%, 30.70%] | $59.64 |
| series+game | all | 256 | 166 | 0.0139 | -9.38% [-22.10%, 2.76%] | $27.94 | 0.559× | 56.89% | $3.66 | 127 (129 unfilled) | -17.31% [-35.30%, 1.76%] | $30.58 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| game | 2026-07 | 104 | 0.775204 | 0.679670 | 0.670295 | -22.50% (80), $20.41 | -33.23% (13), $42.45 | 20 (60 unfilled) | -13.45% [-61.77%, 35.30%] | $42.38 | 4 (9 unfilled) | 1.47% [-100.00%, 40.71%] | $48.43 |
| game | 2026-08 | 261 | 0.650138 | 0.612811 | 0.620045 | 6.48% (210), $83.44 | 6.21% (50), $61.69 | 61 (149 unfilled) | -8.74% [-31.50%, 13.56%] | $34.07 | 16 (34 unfilled) | 4.36% [-38.22%, 42.49%] | $53.50 |
| game | 2026-09 | 211 | 0.621158 | 0.578856 | 0.584628 | -6.00% (162), $31.70 | 6.22% (55), $58.58 | 66 (96 unfilled) | -12.53% [-37.06%, 13.18%] | $28.25 | 20 (35 unfilled) | 12.96% [-12.46%, 34.39%] | $58.31 |
| game | 2026-10 | 197 | 0.653703 | 0.590184 | 0.588963 | -13.77% (134), $13.12 | -4.04% (52), $46.46 | 78 (56 unfilled) | -18.33% [-41.45%, 5.09%] | $18.77 | 24 (28 unfilled) | -14.17% [-43.76%, 9.74%] | $44.58 |
| series | 2026-07 | 79 | 0.763888 | 0.690002 | 0.689503 | 4.10% (57), $49.38 | -24.23% (13), $43.21 | 36 (21 unfilled) | 2.72% [-40.60%, 51.84%] | $38.28 | 10 (3 unfilled) | -31.18% [-100.00%, 61.59%] | $43.15 |
| series | 2026-08 | 147 | 0.627992 | 0.569583 | 0.570451 | -2.93% (127), $51.26 | -26.17% (31), $31.98 | 85 (42 unfilled) | -7.36% [-30.54%, 16.28%] | $36.47 | 25 (6 unfilled) | -30.02% [-75.54%, 26.48%] | $32.20 |
| series | 2026-09 | 145 | 0.584242 | 0.526694 | 0.527022 | -12.10% (115), $12.89 | -21.08% (23), $47.13 | 73 (42 unfilled) | -7.86% [-34.66%, 22.07%] | $34.57 | 14 (9 unfilled) | -15.12% [-74.15%, 51.89%] | $51.13 |
| series | 2026-10 | 186 | 0.593565 | 0.546790 | 0.547318 | -12.96% (150), $6.68 | -40.07% (19), $42.98 | 89 (61 unfilled) | -27.12% [-50.99%, -1.84%] | $5.75 | 14 (5 unfilled) | -63.72% [-100.00%, -12.13%] | $46.73 |

### team_elo+form: Kalshi comparison and returns

form: rows=35654, H=80, w=3.43379

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 557 | 0.615478 | 0.568306 | 0.047172 [0.015988, 0.076894] | yes |
| series | tier1 | 195 | 0.639332 | 0.544117 | 0.095215 [0.035741, 0.157982] | yes |
| series | tier2 | 73 | 0.636030 | 0.567515 | 0.068515 [-0.027371, 0.174183] | no |
| series | tier3 | 289 | 0.594192 | 0.584827 | 0.009365 [-0.021295, 0.041744] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 195 | 0.639332 | 0.544117 | 0.095215 [0.035741, 0.157982] | yes |
| series | international=0 | 362 | 0.602629 | 0.581336 | 0.021293 [-0.010041, 0.053893] | no |
| game | all | 773 | 0.658321 | 0.609217 | 0.049104 [0.024591, 0.075290] | yes |
| game | tier1 | 291 | 0.686384 | 0.601557 | 0.084827 [0.035574, 0.136455] | yes |
| game | tier2 | 145 | 0.673574 | 0.619558 | 0.054017 [0.007388, 0.107994] | yes |
| game | tier3 | 337 | 0.627526 | 0.611382 | 0.016144 [-0.015314, 0.046945] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 291 | 0.686384 | 0.601557 | 0.084827 [0.035574, 0.136455] | yes |
| game | international=0 | 482 | 0.641378 | 0.613841 | 0.027537 [0.001349, 0.055854] | yes |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 455 | 455 | 0.1169 | -3.00% [-14.88%, 8.85%] | $2.51 | 0.050× | 98.83% | $9.64 | 288 (167 unfilled) | -6.29% [-21.02%, 8.82%] | $5.58 |
| series | tier1 | 159 | 159 | 0.1310 | -8.43% [-27.94%, 14.24%] | $9.91 | 0.198× | 91.84% | $4.96 | 106 (53 unfilled) | -14.76% [-38.84%, 12.83%] | $6.38 |
| series | tier2 | 66 | 66 | 0.1438 | -8.52% [-37.73%, 23.70%] | $25.20 | 0.504× | 61.48% | $6.19 | 37 (29 unfilled) | -9.99% [-43.95%, 24.49%] | $35.66 |
| series | tier3 | 230 | 230 | 0.0994 | 2.34% [-13.04%, 18.06%] | $53.63 | 1.073× | 81.27% | $25.05 | 145 (85 unfilled) | 0.87% [-18.73%, 20.71%] | $47.31 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 159 | 159 | 0.1310 | -8.43% [-27.94%, 14.24%] | $9.91 | 0.198× | 91.84% | $4.96 | 106 (53 unfilled) | -14.76% [-38.84%, 12.83%] | $6.38 |
| series | international=0 | 296 | 296 | 0.1093 | -0.08% [-13.19%, 13.60%] | $24.59 | 0.492× | 92.15% | $27.46 | 182 (114 unfilled) | -1.34% [-18.80%, 15.99%] | $36.99 |
| game | all | 599 | 326 | 0.1065 | -3.72% [-11.92%, 4.47%] | $5.53 | 0.111× | 92.20% | $5.86 | 230 (369 unfilled) | -9.86% [-23.68%, 2.87%] | $7.27 |
| game | tier1 | 211 | 117 | 0.1229 | -7.24% [-20.94%, 6.27%] | $11.11 | 0.222× | 83.08% | $5.00 | 98 (113 unfilled) | -22.09% [-41.02%, -2.69%] | $11.73 |
| game | tier2 | 130 | 67 | 0.1105 | -3.93% [-21.44%, 13.21%] | $27.28 | 0.546× | 63.46% | $4.97 | 38 (92 unfilled) | -4.21% [-37.35%, 29.07%] | $38.03 |
| game | tier3 | 258 | 142 | 0.0911 | -0.73% [-13.21%, 11.60%] | $32.42 | 0.648× | 67.48% | $9.78 | 94 (164 unfilled) | 0.61% [-19.99%, 21.10%] | $41.79 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 211 | 117 | 0.1229 | -7.24% [-20.94%, 6.27%] | $11.11 | 0.222× | 83.08% | $5.00 | 98 (113 unfilled) | -22.09% [-41.02%, -2.69%] | $11.73 |
| game | international=0 | 388 | 209 | 0.0976 | -1.80% [-12.05%, 8.12%] | $19.04 | 0.381× | 81.22% | $9.96 | 132 (256 unfilled) | -0.79% [-17.96%, 17.37%] | $32.94 |
| series+game | all | 1054 | 501 | 0.1110 | -3.41% [-11.32%, 4.55%] | $2.75 | 0.055× | 98.92% | $17.31 | 518 (536 unfilled) | -7.87% [-19.00%, 2.91%] | $7.02 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 0 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-07 | series | 621 | 0.991512 | 0.123281 | fitted |
| 2026-07 | game | 434 | 1.183044 | 0.070660 | fitted |
| 2026-08 | series | 621 | 0.991512 | 0.123281 | fitted |
| 2026-08 | game | 434 | 1.183044 | 0.070660 | fitted |
| 2026-09 | series | 621 | 0.991512 | 0.123281 | fitted |
| 2026-09 | game | 434 | 1.183044 | 0.070660 | fitted |
| 2026-10 | series | 621 | 0.991512 | 0.123281 | fitted |
| 2026-10 | game | 434 | 1.183044 | 0.070660 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 557 | 0.567092 | 0.568306 | -0.001214 [-0.004834, 0.002169] | no |
| series | tier1 | 195 | 0.546606 | 0.544117 | 0.002489 [-0.004453, 0.009381] | no |
| series | tier2 | 73 | 0.565190 | 0.567515 | -0.002326 [-0.013835, 0.008521] | no |
| series | tier3 | 289 | 0.581394 | 0.584827 | -0.003432 [-0.007190, 0.000474] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 195 | 0.546606 | 0.544117 | 0.002489 [-0.004453, 0.009381] | no |
| series | international=0 | 362 | 0.578127 | 0.581336 | -0.003209 [-0.007074, 0.000515] | no |
| game | all | 773 | 0.606543 | 0.609217 | -0.002673 [-0.006630, 0.001452] | no |
| game | tier1 | 291 | 0.602746 | 0.601557 | 0.001189 [-0.006077, 0.009191] | no |
| game | tier2 | 145 | 0.617051 | 0.619558 | -0.002506 [-0.009938, 0.005116] | no |
| game | tier3 | 337 | 0.605301 | 0.611382 | -0.006080 [-0.011473, -0.000409] | yes |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 291 | 0.602746 | 0.601557 | 0.001189 [-0.006077, 0.009191] | no |
| game | international=0 | 482 | 0.608836 | 0.613841 | -0.005005 [-0.009354, -0.000352] | yes |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 68 | 68 | 0.0133 | -28.65% [-58.08%, 4.54%] | $29.54 | 0.591× | 43.82% | $2.82 | 47 (21 unfilled) | -35.92% [-66.53%, -1.67%] | $33.16 |
| series | tier1 | 32 | 32 | 0.0163 | -46.56% [-78.96%, -7.97%] | $30.65 | 0.613× | 38.69% | $2.74 | 25 (7 unfilled) | -61.19% [-88.85%, -25.89%] | $31.98 |
| series | tier2 | 15 | 15 | 0.0148 | -9.58% [-86.05%, 88.56%] | $49.59 | 0.992× | 4.52% | $3.06 | 9 (6 unfilled) | -19.04% [-100.00%, 62.78%] | $50.22 |
| series | tier3 | 21 | 21 | 0.0076 | -15.17% [-64.21%, 42.67%] | $48.66 | 0.973× | 8.38% | $2.91 | 13 (8 unfilled) | 0.73% [-64.79%, 76.72%] | $51.81 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 32 | 32 | 0.0163 | -46.56% [-78.96%, -7.97%] | $30.65 | 0.613× | 38.69% | $2.74 | 25 (7 unfilled) | -61.19% [-88.85%, -25.89%] | $31.98 |
| series | international=0 | 36 | 36 | 0.0106 | -12.83% [-58.70%, 39.35%] | $48.24 | 0.965× | 9.17% | $3.14 | 22 (14 unfilled) | -7.37% [-58.98%, 50.10%] | $52.05 |
| game | all | 151 | 93 | 0.0084 | -0.45% [-9.48%, 8.49%] | $59.95 | 1.199× | 10.86% | $5.36 | 53 (98 unfilled) | 3.35% [-13.21%, 17.50%] | $53.62 |
| game | tier1 | 59 | 34 | 0.0086 | -4.54% [-18.94%, 8.67%] | $48.81 | 0.976× | 13.20% | $4.32 | 22 (37 unfilled) | -6.31% [-32.37%, 16.27%] | $44.25 |
| game | tier2 | 31 | 19 | 0.0089 | -1.16% [-17.98%, 14.23%] | $53.46 | 1.069× | 4.17% | $4.87 | 8 (23 unfilled) | 16.44% [-18.82%, 41.26%] | $53.42 |
| game | tier3 | 61 | 40 | 0.0079 | 3.86% [-12.80%, 18.85%] | $57.28 | 1.146× | 6.21% | $4.61 | 23 (38 unfilled) | 8.04% [-17.32%, 28.87%] | $56.66 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 59 | 34 | 0.0086 | -4.54% [-18.94%, 8.67%] | $48.81 | 0.976× | 13.20% | $4.32 | 22 (37 unfilled) | -6.31% [-32.37%, 16.27%] | $44.25 |
| game | international=0 | 92 | 59 | 0.0082 | 2.17% [-9.69%, 13.69%] | $61.40 | 1.228× | 6.21% | $5.58 | 31 (61 unfilled) | 10.21% [-10.21%, 27.48%] | $60.42 |
| series+game | all | 219 | 148 | 0.0099 | -9.38% [-20.57%, 2.03%] | $34.66 | 0.693× | 42.71% | $3.68 | 100 (119 unfilled) | -15.36% [-32.96%, 2.51%] | $35.75 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| game | 2026-07 | 104 | 0.770438 | 0.676452 | 0.670295 | -20.21% (75), $18.11 | -33.42% (8), $47.21 | 16 (59 unfilled) | -9.81% [-62.82%, 43.61%] | $41.64 | 3 (5 unfilled) | 35.73% [25.69%, 40.71%] | $49.97 |
| game | 2026-08 | 261 | 0.646701 | 0.613976 | 0.620045 | 5.87% (217), $101.48 | 10.66% (34), $54.09 | 65 (152 unfilled) | -11.99% [-32.90%, 8.75%] | $32.33 | 9 (25 unfilled) | -8.64% [-43.96%, 28.01%] | $47.83 |
| game | 2026-09 | 211 | 0.618938 | 0.579388 | 0.584628 | -1.29% (171), $36.96 | 1.07% (61), $54.89 | 73 (98 unfilled) | -4.66% [-29.33%, 19.09%] | $37.96 | 23 (38 unfilled) | 14.41% [-8.51%, 32.69%] | $57.33 |
| game | 2026-10 | 197 | 0.656709 | 0.588876 | 0.588963 | -12.99% (136), $10.95 | -4.76% (48), $53.46 | 76 (60 unfilled) | -13.06% [-36.81%, 10.44%] | $20.37 | 18 (30 unfilled) | -10.20% [-41.39%, 13.69%] | $48.92 |
| series | 2026-07 | 79 | 0.744069 | 0.688514 | 0.689503 | 23.35% (64), $57.11 | 22.93% (8), $45.70 | 44 (20 unfilled) | 28.60% [-17.46%, 79.21%] | $49.22 | 6 (2 unfilled) | 14.33% [-100.00%, 141.30%] | $45.48 |
| series | 2026-08 | 147 | 0.616796 | 0.568533 | 0.570451 | -0.92% (123), $53.90 | -51.16% (27), $38.28 | 81 (42 unfilled) | -4.52% [-28.20%, 19.56%] | $42.95 | 21 (6 unfilled) | -56.14% [-91.45%, -15.84%] | $38.44 |
| series | 2026-09 | 145 | 0.576579 | 0.526009 | 0.527022 | -12.14% (114), $13.62 | -27.66% (21), $48.51 | 72 (42 unfilled) | -8.57% [-34.85%, 21.59%] | $42.92 | 12 (9 unfilled) | -25.69% [-83.21%, 39.38%] | $50.70 |
| series | 2026-10 | 186 | 0.590144 | 0.546407 | 0.547318 | -8.86% (154), $9.27 | -14.17% (12), $43.54 | 91 (63 unfilled) | -22.92% [-45.51%, 2.16%] | $7.97 | 8 (4 unfilled) | -36.11% [-100.00%, 48.64%] | $46.91 |

### player_glicko+none: Kalshi comparison and returns

none

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 557 | 0.546155 | 0.568306 | -0.022151 [-0.044412, -0.002057] | yes |
| series | tier1 | 195 | 0.544881 | 0.544117 | 0.000764 [-0.035287, 0.035750] | no |
| series | tier2 | 73 | 0.582032 | 0.567515 | 0.014517 [-0.040636, 0.066745] | no |
| series | tier3 | 289 | 0.537953 | 0.584827 | -0.046874 [-0.076718, -0.016314] | yes |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 195 | 0.544881 | 0.544117 | 0.000764 [-0.035287, 0.035750] | no |
| series | international=0 | 362 | 0.546842 | 0.581336 | -0.034494 [-0.060822, -0.007207] | yes |
| game | all | 773 | 0.604249 | 0.609217 | -0.004968 [-0.019211, 0.009481] | no |
| game | tier1 | 291 | 0.608513 | 0.601557 | 0.006956 [-0.012524, 0.029435] | no |
| game | tier2 | 145 | 0.640710 | 0.619558 | 0.021153 [-0.010594, 0.052222] | no |
| game | tier3 | 337 | 0.584879 | 0.611382 | -0.026503 [-0.052018, -0.001206] | yes |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 291 | 0.608513 | 0.601557 | 0.006956 [-0.012524, 0.029435] | no |
| game | international=0 | 482 | 0.601674 | 0.613841 | -0.012167 [-0.033188, 0.008869] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 430 | 430 | 0.0881 | 6.70% [-4.66%, 18.33%] | $826.54 | 16.531× | 76.77% | $217.61 | 282 (148 unfilled) | 5.76% [-7.35%, 21.26%] | $138.31 |
| series | tier1 | 144 | 144 | 0.0812 | -6.75% [-28.26%, 16.45%] | $31.72 | 0.634× | 71.51% | $6.39 | 97 (47 unfilled) | -5.57% [-31.68%, 24.64%] | $35.63 |
| series | tier2 | 58 | 58 | 0.0856 | -11.83% [-40.80%, 20.55%] | $26.89 | 0.538× | 61.52% | $6.49 | 37 (21 unfilled) | -19.93% [-52.04%, 16.01%] | $22.40 |
| series | tier3 | 228 | 228 | 0.0932 | 19.96% [5.73%, 35.65%] | $2093.86 | 41.877× | 46.36% | $239.80 | 148 (80 unfilled) | 19.68% [2.02%, 37.70%] | $370.41 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 144 | 144 | 0.0812 | -6.75% [-28.26%, 16.45%] | $31.72 | 0.634× | 71.51% | $6.39 | 97 (47 unfilled) | -5.57% [-31.68%, 24.64%] | $35.63 |
| series | international=0 | 286 | 286 | 0.0916 | 13.49% [0.40%, 25.92%] | $2081.79 | 41.636× | 53.74% | $244.35 | 185 (101 unfilled) | 11.72% [-4.26%, 28.22%] | $199.72 |
| game | all | 516 | 284 | 0.0699 | 1.93% [-6.81%, 10.61%] | $77.24 | 1.545× | 59.31% | $15.87 | 196 (320 unfilled) | -6.08% [-20.14%, 9.08%] | $22.89 |
| game | tier1 | 161 | 93 | 0.0608 | -9.57% [-23.86%, 5.34%] | $23.61 | 0.472× | 57.18% | $3.51 | 72 (89 unfilled) | -19.24% [-41.27%, 3.75%] | $22.01 |
| game | tier2 | 111 | 56 | 0.0658 | -12.10% [-29.34%, 6.11%] | $33.74 | 0.675× | 34.83% | $2.72 | 33 (78 unfilled) | -11.49% [-44.65%, 22.09%] | $49.28 |
| game | tier3 | 244 | 135 | 0.0777 | 15.93% [4.21%, 28.28%] | $239.80 | 4.796× | 35.60% | $34.26 | 91 (153 unfilled) | 6.32% [-14.48%, 27.56%] | $52.28 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 161 | 93 | 0.0608 | -9.57% [-23.86%, 5.34%] | $23.61 | 0.472× | 57.18% | $3.51 | 72 (89 unfilled) | -19.24% [-41.27%, 3.75%] | $22.01 |
| game | international=0 | 355 | 191 | 0.0740 | 7.15% [-3.30%, 17.32%] | $161.17 | 3.223× | 40.63% | $23.03 | 124 (231 unfilled) | 1.57% [-16.47%, 19.63%] | $50.12 |
| series+game | all | 946 | 471 | 0.0782 | 4.10% [-4.35%, 12.48%] | $1017.69 | 20.354× | 60.79% | $141.97 | 478 (468 unfilled) | 0.91% [-9.88%, 12.02%] | $162.90 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 0 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-07 | series | 621 | 1.053140 | 0.561857 | fitted |
| 2026-07 | game | 434 | 1.193713 | 0.013709 | fitted |
| 2026-08 | series | 621 | 1.053140 | 0.561857 | fitted |
| 2026-08 | game | 434 | 1.193713 | 0.013709 | fitted |
| 2026-09 | series | 621 | 1.053140 | 0.561857 | fitted |
| 2026-09 | game | 434 | 1.193713 | 0.013709 | fitted |
| 2026-10 | series | 621 | 1.053140 | 0.561857 | fitted |
| 2026-10 | game | 434 | 1.193713 | 0.013709 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 557 | 0.543744 | 0.568306 | -0.024562 [-0.036698, -0.013612] | yes |
| series | tier1 | 195 | 0.532350 | 0.544117 | -0.011768 [-0.031254, 0.006621] | no |
| series | tier2 | 73 | 0.564806 | 0.567515 | -0.002710 [-0.031239, 0.025139] | no |
| series | tier3 | 289 | 0.546112 | 0.584827 | -0.038715 [-0.055345, -0.021557] | yes |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 195 | 0.532350 | 0.544117 | -0.011768 [-0.031254, 0.006621] | no |
| series | international=0 | 362 | 0.549882 | 0.581336 | -0.031454 [-0.046040, -0.016443] | yes |
| game | all | 773 | 0.606846 | 0.609217 | -0.002370 [-0.006244, 0.001986] | no |
| game | tier1 | 291 | 0.602199 | 0.601557 | 0.000643 [-0.006483, 0.008703] | no |
| game | tier2 | 145 | 0.618401 | 0.619558 | -0.001156 [-0.009253, 0.007075] | no |
| game | tier3 | 337 | 0.605887 | 0.611382 | -0.005494 [-0.011054, -0.000067] | yes |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 291 | 0.602199 | 0.601557 | 0.000643 [-0.006483, 0.008703] | no |
| game | international=0 | 482 | 0.609652 | 0.613841 | -0.004189 [-0.008538, 0.000420] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 339 | 339 | 0.0440 | 13.17% [0.98%, 27.03%] | $1540.78 | 30.816× | 65.55% | $149.80 | 218 (121 unfilled) | 10.30% [-5.92%, 26.49%] | $205.97 |
| series | tier1 | 106 | 106 | 0.0402 | 4.81% [-19.48%, 33.10%] | $104.26 | 2.085× | 33.65% | $8.95 | 71 (35 unfilled) | 3.88% [-28.43%, 40.29%] | $74.25 |
| series | tier2 | 51 | 51 | 0.0342 | -16.72% [-46.51%, 16.68%] | $46.38 | 0.928× | 41.81% | $7.60 | 32 (19 unfilled) | -33.52% [-64.06%, -1.85%] | $36.09 |
| series | tier3 | 182 | 182 | 0.0489 | 26.46% [10.18%, 43.47%] | $883.69 | 17.674× | 42.04% | $93.88 | 115 (67 unfilled) | 26.54% [5.89%, 48.49%] | $218.28 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 106 | 106 | 0.0402 | 4.81% [-19.48%, 33.10%] | $104.26 | 2.085× | 33.65% | $8.95 | 71 (35 unfilled) | 3.88% [-28.43%, 40.29%] | $74.25 |
| series | international=0 | 233 | 233 | 0.0457 | 16.97% [1.74%, 32.44%] | $780.90 | 15.618× | 64.32% | $138.21 | 147 (86 unfilled) | 13.41% [-4.95%, 32.20%] | $149.91 |
| game | all | 146 | 93 | 0.0081 | -0.08% [-7.92%, 7.20%] | $60.24 | 1.205× | 15.10% | $5.95 | 49 (97 unfilled) | 2.64% [-11.57%, 15.31%] | $57.00 |
| game | tier1 | 57 | 36 | 0.0055 | 0.97% [-11.07%, 11.21%] | $52.50 | 1.050× | 7.14% | $5.39 | 21 (36 unfilled) | -10.53% [-36.58%, 10.52%] | $48.93 |
| game | tier2 | 37 | 22 | 0.0116 | 1.83% [-12.08%, 15.42%] | $50.71 | 1.014× | 16.89% | $4.92 | 9 (28 unfilled) | 15.26% [-15.70%, 34.04%] | $53.17 |
| game | tier3 | 52 | 35 | 0.0085 | -2.58% [-18.08%, 10.77%] | $56.27 | 1.125× | 5.10% | $4.37 | 19 (33 unfilled) | 11.17% [-8.65%, 25.49%] | $54.73 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 57 | 36 | 0.0055 | 0.97% [-11.07%, 11.21%] | $52.50 | 1.050× | 7.14% | $5.39 | 21 (36 unfilled) | -10.53% [-36.58%, 10.52%] | $48.93 |
| game | international=0 | 89 | 57 | 0.0098 | -0.75% [-11.60%, 8.99%] | $57.32 | 1.146× | 15.10% | $5.34 | 28 (61 unfilled) | 12.49% [-3.31%, 25.14%] | $58.17 |
| series+game | all | 485 | 367 | 0.0332 | 9.24% [-0.05%, 18.17%] | $1624.35 | 32.487× | 56.25% | $166.85 | 267 (218 unfilled) | 8.92% [-4.64%, 23.44%] | $225.60 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| game | 2026-07 | 104 | 0.682114 | 0.673500 | 0.670295 | 8.55% (64), $61.03 | -51.36% (5), $46.93 | 17 (47 unfilled) | 8.94% [-43.81%, 59.44%] | $48.67 | 0 (5 unfilled) | — | $48.98 |
| game | 2026-08 | 261 | 0.603722 | 0.616372 | 0.620045 | 8.64% (168), $68.83 | 4.25% (32), $56.35 | 50 (118 unfilled) | 6.28% [-18.38%, 32.15%] | $54.68 | 6 (26 unfilled) | -22.92% [-63.97%, 17.41%] | $50.50 |
| game | 2026-09 | 211 | 0.572991 | 0.580522 | 0.584628 | 2.56% (155), $89.12 | -0.25% (64), $51.94 | 63 (92 unfilled) | -6.63% [-31.34%, 17.92%] | $53.37 | 22 (42 unfilled) | 14.12% [-3.75%, 27.13%] | $56.45 |
| game | 2026-10 | 197 | 0.597318 | 0.587234 | 0.588963 | -10.82% (129), $25.30 | 2.79% (45), $54.85 | 66 (63 unfilled) | -18.76% [-43.20%, 6.99%] | $20.10 | 21 (24 unfilled) | -2.13% [-25.73%, 16.06%] | $50.99 |
| series | 2026-07 | 79 | 0.649772 | 0.660027 | 0.689503 | 36.93% (62), $220.13 | 40.41% (50), $132.43 | 44 (18 unfilled) | 43.42% [-1.32%, 91.62%] | $138.55 | 34 (16 unfilled) | 42.46% [-6.07%, 96.89%] | $72.92 |
| series | 2026-08 | 147 | 0.534462 | 0.537652 | 0.570451 | 6.20% (117), $130.89 | 13.57% (91), $166.47 | 75 (42 unfilled) | -3.45% [-28.68%, 21.27%] | $42.68 | 59 (32 unfilled) | -0.08% [-28.18%, 29.20%] | $75.26 |
| series | 2026-09 | 145 | 0.525182 | 0.511327 | 0.527022 | 3.94% (109), $36.36 | -0.79% (94), $51.38 | 77 (32 unfilled) | 9.52% [-16.92%, 37.01%] | $83.45 | 66 (28 unfilled) | 4.47% [-23.24%, 33.51%] | $65.06 |
| series | 2026-10 | 186 | 0.527737 | 0.524441 | 0.547318 | -3.98% (142), $67.35 | 12.32% (104), $184.61 | 86 (56 unfilled) | -8.85% [-31.97%, 15.16%] | $44.62 | 59 (45 unfilled) | 8.67% [-20.78%, 38.31%] | $87.67 |

### player_glicko+form: Kalshi comparison and returns

form: rows=35654, H=80, w=1.50996

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 557 | 0.545487 | 0.568306 | -0.022818 [-0.044871, -0.002442] | yes |
| series | tier1 | 195 | 0.544295 | 0.544117 | 0.000178 [-0.036294, 0.035585] | no |
| series | tier2 | 73 | 0.581350 | 0.567515 | 0.013834 [-0.040561, 0.065546] | no |
| series | tier3 | 289 | 0.537233 | 0.584827 | -0.047593 [-0.077268, -0.017593] | yes |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 195 | 0.544295 | 0.544117 | 0.000178 [-0.036294, 0.035585] | no |
| series | international=0 | 362 | 0.546130 | 0.581336 | -0.035206 [-0.061344, -0.008605] | yes |
| game | all | 773 | 0.603524 | 0.609217 | -0.005692 [-0.020155, 0.008865] | no |
| game | tier1 | 291 | 0.606862 | 0.601557 | 0.005305 [-0.014873, 0.028177] | no |
| game | tier2 | 145 | 0.640936 | 0.619558 | 0.021379 [-0.009863, 0.051737] | no |
| game | tier3 | 337 | 0.584545 | 0.611382 | -0.026836 [-0.052840, -0.001225] | yes |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 291 | 0.606862 | 0.601557 | 0.005305 [-0.014873, 0.028177] | no |
| game | international=0 | 482 | 0.601509 | 0.613841 | -0.012332 [-0.033530, 0.008689] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 433 | 433 | 0.0876 | 7.53% [-4.84%, 19.36%] | $841.39 | 16.828× | 76.23% | $228.50 | 287 (146 unfilled) | 7.21% [-6.39%, 21.92%] | $182.23 |
| series | tier1 | 145 | 145 | 0.0824 | -7.62% [-29.27%, 13.39%] | $34.65 | 0.693× | 71.39% | $7.37 | 99 (46 unfilled) | -6.53% [-32.17%, 21.87%] | $40.33 |
| series | tier2 | 59 | 59 | 0.0848 | -12.19% [-41.56%, 21.22%] | $29.40 | 0.588× | 59.80% | $6.79 | 39 (20 unfilled) | -18.84% [-50.19%, 14.14%] | $26.72 |
| series | tier3 | 229 | 229 | 0.0916 | 22.28% [7.61%, 37.26%] | $1747.00 | 34.940× | 47.55% | $213.43 | 149 (80 unfilled) | 23.24% [4.54%, 41.58%] | $378.57 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 145 | 145 | 0.0824 | -7.62% [-29.27%, 13.39%] | $34.65 | 0.693× | 71.39% | $7.37 | 99 (46 unfilled) | -6.53% [-32.17%, 21.87%] | $40.33 |
| series | international=0 | 288 | 288 | 0.0902 | 15.19% [1.93%, 29.87%] | $1777.08 | 35.542× | 55.66% | $244.35 | 188 (100 unfilled) | 14.47% [-1.91%, 30.85%] | $240.26 |
| game | all | 518 | 281 | 0.0716 | 3.56% [-4.42%, 12.10%] | $92.14 | 1.843× | 60.83% | $19.68 | 192 (326 unfilled) | -4.27% [-17.92%, 10.33%] | $26.07 |
| game | tier1 | 163 | 92 | 0.0632 | -6.36% [-21.02%, 8.68%] | $26.14 | 0.523× | 52.13% | $4.25 | 69 (94 unfilled) | -16.73% [-38.69%, 6.71%] | $22.96 |
| game | tier2 | 108 | 54 | 0.0679 | -9.63% [-25.96%, 8.26%] | $34.48 | 0.690× | 34.26% | $2.82 | 32 (76 unfilled) | -8.67% [-42.18%, 28.24%] | $49.29 |
| game | tier3 | 247 | 135 | 0.0786 | 15.88% [3.77%, 27.94%] | $250.63 | 5.013× | 36.59% | $35.44 | 91 (156 unfilled) | 6.77% [-14.56%, 27.19%] | $57.31 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 163 | 92 | 0.0632 | -6.36% [-21.02%, 8.68%] | $26.14 | 0.523× | 52.13% | $4.25 | 69 (94 unfilled) | -16.73% [-38.69%, 6.71%] | $22.96 |
| game | international=0 | 355 | 189 | 0.0754 | 8.11% [-1.63%, 18.08%] | $170.86 | 3.417× | 43.23% | $24.17 | 123 (232 unfilled) | 2.74% [-14.22%, 20.16%] | $54.54 |
| series+game | all | 951 | 477 | 0.0788 | 5.37% [-2.86%, 13.75%] | $1079.36 | 21.587× | 61.09% | $153.34 | 479 (472 unfilled) | 2.62% [-8.78%, 13.75%] | $232.32 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 0 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-07 | series | 621 | 1.056900 | 0.518007 | fitted |
| 2026-07 | game | 434 | 1.203516 | -0.059028 | fitted |
| 2026-08 | series | 621 | 1.056900 | 0.518007 | fitted |
| 2026-08 | game | 434 | 1.203516 | -0.059028 | fitted |
| 2026-09 | series | 621 | 1.056900 | 0.518007 | fitted |
| 2026-09 | game | 434 | 1.203516 | -0.059028 | fitted |
| 2026-10 | series | 621 | 1.056900 | 0.518007 | fitted |
| 2026-10 | game | 434 | 1.203516 | -0.059028 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 557 | 0.544204 | 0.568306 | -0.024102 [-0.035092, -0.014064] | yes |
| series | tier1 | 195 | 0.531697 | 0.544117 | -0.012420 [-0.030185, 0.004647] | no |
| series | tier2 | 73 | 0.563441 | 0.567515 | -0.004074 [-0.030405, 0.021332] | no |
| series | tier3 | 289 | 0.547784 | 0.584827 | -0.037043 [-0.052273, -0.021373] | yes |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 195 | 0.531697 | 0.544117 | -0.012420 [-0.030185, 0.004647] | no |
| series | international=0 | 362 | 0.550941 | 0.581336 | -0.030394 [-0.043567, -0.016867] | yes |
| game | all | 773 | 0.609170 | 0.609217 | -0.000047 [-0.004492, 0.004549] | no |
| game | tier1 | 291 | 0.603541 | 0.601557 | 0.001984 [-0.005930, 0.010603] | no |
| game | tier2 | 145 | 0.618539 | 0.619558 | -0.001019 [-0.009659, 0.007962] | no |
| game | tier3 | 337 | 0.610000 | 0.611382 | -0.001382 [-0.007407, 0.004560] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 291 | 0.603541 | 0.601557 | 0.001984 [-0.005930, 0.010603] | no |
| game | international=0 | 482 | 0.612569 | 0.613841 | -0.001273 [-0.006280, 0.003906] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 320 | 320 | 0.0396 | 13.32% [-0.68%, 27.37%] | $1613.11 | 32.262× | 62.72% | $157.75 | 205 (115 unfilled) | 12.28% [-4.18%, 30.12%] | $199.35 |
| series | tier1 | 101 | 101 | 0.0361 | 6.78% [-19.33%, 35.13%] | $122.11 | 2.442× | 32.83% | $12.07 | 66 (35 unfilled) | 6.81% [-30.83%, 46.37%] | $81.30 |
| series | tier2 | 46 | 46 | 0.0312 | -13.18% [-46.18%, 26.61%] | $49.83 | 0.997× | 39.73% | $7.92 | 27 (19 unfilled) | -26.72% [-61.25%, 9.72%] | $38.77 |
| series | tier3 | 173 | 173 | 0.0438 | 24.25% [8.39%, 41.09%] | $658.81 | 13.176× | 38.06% | $69.06 | 112 (61 unfilled) | 24.97% [3.68%, 46.23%] | $186.65 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 101 | 101 | 0.0361 | 6.78% [-19.33%, 35.13%] | $122.11 | 2.442× | 32.83% | $12.07 | 66 (35 unfilled) | 6.81% [-30.83%, 46.37%] | $81.30 |
| series | international=0 | 219 | 219 | 0.0412 | 16.35% [2.05%, 31.68%] | $632.38 | 12.648× | 61.52% | $101.87 | 139 (80 unfilled) | 14.88% [-4.30%, 33.91%] | $139.32 |
| game | all | 175 | 108 | 0.0088 | -4.93% [-13.72%, 2.42%] | $38.72 | 0.774× | 27.93% | $4.41 | 55 (120 unfilled) | -0.84% [-15.18%, 11.66%] | $50.78 |
| game | tier1 | 77 | 49 | 0.0068 | -6.80% [-18.90%, 4.80%] | $43.74 | 0.875× | 13.59% | $4.64 | 28 (49 unfilled) | -13.70% [-37.55%, 5.57%] | $44.45 |
| game | tier2 | 40 | 22 | 0.0124 | 1.93% [-10.70%, 14.49%] | $50.31 | 1.006× | 19.00% | $5.26 | 9 (31 unfilled) | 15.26% [-15.70%, 34.04%] | $54.33 |
| game | tier3 | 58 | 37 | 0.0089 | -7.18% [-24.50%, 7.83%] | $43.81 | 0.876× | 15.71% | $3.86 | 18 (40 unfilled) | 11.08% [-10.94%, 27.45%] | $52.53 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 77 | 49 | 0.0068 | -6.80% [-18.90%, 4.80%] | $43.74 | 0.875× | 13.59% | $4.64 | 28 (49 unfilled) | -13.70% [-37.55%, 5.57%] | $44.45 |
| game | international=0 | 98 | 59 | 0.0103 | -3.47% [-14.93%, 6.72%] | $44.27 | 0.885× | 22.05% | $4.68 | 27 (71 unfilled) | 12.47% [-5.39%, 26.04%] | $57.05 |
| series+game | all | 495 | 359 | 0.0287 | 6.95% [-1.47%, 15.54%] | $1187.31 | 23.746× | 47.97% | $123.97 | 260 (235 unfilled) | 9.55% [-3.87%, 23.97%] | $218.61 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| game | 2026-07 | 104 | 0.681616 | 0.674837 | 0.670295 | 9.20% (63), $58.21 | -47.77% (5), $43.77 | 15 (48 unfilled) | 7.50% [-50.60%, 60.48%] | $49.29 | 0 (5 unfilled) | — | $48.98 |
| game | 2026-08 | 261 | 0.602346 | 0.619476 | 0.620045 | 10.12% (170), $87.41 | -12.64% (43), $49.46 | 50 (120 unfilled) | 9.74% [-14.44%, 34.72%] | $59.66 | 8 (35 unfilled) | -26.17% [-67.40%, 10.80%] | $48.42 |
| game | 2026-09 | 211 | 0.571686 | 0.583254 | 0.584628 | 4.93% (155), $91.48 | -4.19% (72), $45.66 | 63 (92 unfilled) | -2.39% [-27.46%, 21.72%] | $57.26 | 22 (50 unfilled) | 4.74% [-17.29%, 23.87%] | $52.94 |
| game | 2026-10 | 197 | 0.597961 | 0.588607 | 0.588963 | -9.39% (130), $24.26 | 4.04% (55), $49.21 | 64 (66 unfilled) | -19.75% [-42.69%, 4.49%] | $19.46 | 25 (30 unfilled) | 2.33% [-19.17%, 17.99%] | $50.52 |
| series | 2026-07 | 79 | 0.648177 | 0.661234 | 0.689503 | 36.12% (64), $219.72 | 33.17% (50), $120.28 | 45 (19 unfilled) | 45.17% [3.31%, 93.50%] | $151.66 | 34 (16 unfilled) | 36.22% [-12.67%, 93.06%] | $70.19 |
| series | 2026-08 | 147 | 0.533702 | 0.538351 | 0.570451 | 9.25% (116), $142.39 | 19.22% (84), $172.44 | 76 (40 unfilled) | 0.33% [-23.45%, 25.83%] | $48.76 | 54 (30 unfilled) | 9.12% [-20.09%, 38.72%] | $81.04 |
| series | 2026-09 | 145 | 0.524016 | 0.510616 | 0.527022 | 4.37% (112), $37.69 | 1.68% (88), $48.71 | 80 (32 unfilled) | 9.91% [-15.19%, 37.57%] | $85.33 | 61 (27 unfilled) | 8.59% [-20.87%, 40.71%] | $59.13 |
| series | 2026-10 | 186 | 0.527925 | 0.525308 | 0.547318 | -4.35% (141), $57.18 | 8.58% (98), $197.25 | 86 (55 unfilled) | -9.09% [-32.86%, 16.89%] | $43.55 | 56 (42 unfilled) | 4.79% [-26.18%, 37.77%] | $91.65 |

### player_glicko_rw_tier_revert+none: Kalshi comparison and returns

none

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 557 | 0.543716 | 0.568306 | -0.024590 [-0.046699, -0.004257] | yes |
| series | tier1 | 195 | 0.538012 | 0.544117 | -0.006105 [-0.039654, 0.028367] | no |
| series | tier2 | 73 | 0.580883 | 0.567515 | 0.013368 [-0.034711, 0.058896] | no |
| series | tier3 | 289 | 0.538176 | 0.584827 | -0.046650 [-0.078024, -0.013496] | yes |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 195 | 0.538012 | 0.544117 | -0.006105 [-0.039654, 0.028367] | no |
| series | international=0 | 362 | 0.546789 | 0.581336 | -0.034547 [-0.062357, -0.006932] | yes |
| game | all | 773 | 0.602363 | 0.609217 | -0.006854 [-0.019974, 0.006534] | no |
| game | tier1 | 291 | 0.608996 | 0.601557 | 0.007440 [-0.009703, 0.027434] | no |
| game | tier2 | 145 | 0.630162 | 0.619558 | 0.010604 [-0.014096, 0.034441] | no |
| game | tier3 | 337 | 0.584674 | 0.611382 | -0.026708 [-0.050514, -0.002940] | yes |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 291 | 0.608996 | 0.601557 | 0.007440 [-0.009703, 0.027434] | no |
| game | international=0 | 482 | 0.598358 | 0.613841 | -0.015483 [-0.034882, 0.003779] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 430 | 430 | 0.0832 | 7.19% [-4.09%, 19.35%] | $3127.36 | 62.547× | 58.93% | $248.78 | 280 (150 unfilled) | 5.59% [-8.99%, 20.04%] | $265.67 |
| series | tier1 | 146 | 146 | 0.0723 | -1.44% [-22.77%, 20.59%] | $61.97 | 1.239× | 66.31% | $6.76 | 98 (48 unfilled) | 2.00% [-24.24%, 31.57%] | $66.32 |
| series | tier2 | 61 | 61 | 0.0658 | -18.13% [-47.18%, 14.55%] | $27.55 | 0.551× | 56.43% | $5.87 | 36 (25 unfilled) | -33.16% [-63.14%, 2.16%] | $20.29 |
| series | tier3 | 223 | 223 | 0.0951 | 19.81% [5.48%, 34.71%] | $2696.46 | 53.929× | 48.98% | $248.78 | 146 (77 unfilled) | 17.61% [-0.66%, 36.01%] | $410.99 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 146 | 146 | 0.0723 | -1.44% [-22.77%, 20.59%] | $61.97 | 1.239× | 66.31% | $6.76 | 98 (48 unfilled) | 2.00% [-24.24%, 31.57%] | $66.32 |
| series | international=0 | 284 | 284 | 0.0888 | 11.63% [-1.86%, 24.93%] | $2595.05 | 51.901× | 50.77% | $248.78 | 182 (102 unfilled) | 7.52% [-8.08%, 24.38%] | $179.01 |
| game | all | 488 | 272 | 0.0600 | 1.50% [-8.23%, 11.12%] | $77.36 | 1.547× | 57.48% | $18.01 | 192 (296 unfilled) | -7.02% [-22.34%, 8.48%] | $27.23 |
| game | tier1 | 147 | 87 | 0.0511 | -10.39% [-29.20%, 7.89%] | $21.93 | 0.439× | 58.81% | $3.73 | 70 (77 unfilled) | -20.63% [-45.18%, 4.61%] | $22.82 |
| game | tier2 | 101 | 53 | 0.0481 | -14.10% [-34.69%, 5.85%] | $40.12 | 0.802× | 27.07% | $4.58 | 30 (71 unfilled) | -22.21% [-56.16%, 14.72%] | $48.90 |
| game | tier3 | 240 | 132 | 0.0704 | 15.37% [1.47%, 29.76%] | $215.85 | 4.317× | 39.57% | $30.37 | 92 (148 unfilled) | 8.33% [-14.80%, 29.75%] | $60.57 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 147 | 87 | 0.0511 | -10.39% [-29.20%, 7.89%] | $21.93 | 0.439× | 58.81% | $3.73 | 70 (77 unfilled) | -20.63% [-45.18%, 4.61%] | $22.82 |
| game | international=0 | 341 | 185 | 0.0638 | 6.63% [-4.30%, 18.04%] | $172.61 | 3.452× | 41.53% | $26.17 | 122 (219 unfilled) | 0.79% [-18.45%, 20.25%] | $58.22 |
| series+game | all | 918 | 456 | 0.0709 | 4.16% [-4.70%, 13.61%] | $742.85 | 14.857× | 66.95% | $106.92 | 472 (446 unfilled) | 0.46% [-10.97%, 12.00%] | $220.60 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 0 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-07 | series | 621 | 1.045637 | 0.626616 | fitted |
| 2026-07 | game | 434 | 1.207276 | -0.178366 | fitted |
| 2026-08 | series | 621 | 1.045637 | 0.626616 | fitted |
| 2026-08 | game | 434 | 1.207276 | -0.178366 | fitted |
| 2026-09 | series | 621 | 1.045637 | 0.626616 | fitted |
| 2026-09 | game | 434 | 1.207276 | -0.178366 | fitted |
| 2026-10 | series | 621 | 1.045637 | 0.626616 | fitted |
| 2026-10 | game | 434 | 1.207276 | -0.178366 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 557 | 0.541719 | 0.568306 | -0.026587 [-0.040588, -0.014411] | yes |
| series | tier1 | 195 | 0.529737 | 0.544117 | -0.014380 [-0.034819, 0.005901] | no |
| series | tier2 | 73 | 0.567849 | 0.567515 | 0.000333 [-0.028840, 0.027472] | no |
| series | tier3 | 289 | 0.543204 | 0.584827 | -0.041622 [-0.061481, -0.021379] | yes |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 195 | 0.529737 | 0.544117 | -0.014380 [-0.034819, 0.005901] | no |
| series | international=0 | 362 | 0.548174 | 0.581336 | -0.033162 [-0.050409, -0.016130] | yes |
| game | all | 773 | 0.613090 | 0.609217 | 0.003874 [-0.001775, 0.009474] | no |
| game | tier1 | 291 | 0.604725 | 0.601557 | 0.003168 [-0.006121, 0.013187] | no |
| game | tier2 | 145 | 0.619516 | 0.619558 | -0.000041 [-0.010200, 0.010520] | no |
| game | tier3 | 337 | 0.617549 | 0.611382 | 0.006168 [-0.002451, 0.014785] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 291 | 0.604725 | 0.601557 | 0.003168 [-0.006121, 0.013187] | no |
| game | international=0 | 482 | 0.618141 | 0.613841 | 0.004300 [-0.002876, 0.011637] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 354 | 354 | 0.0486 | 16.71% [4.40%, 30.44%] | $3064.04 | 61.281× | 62.89% | $248.78 | 229 (125 unfilled) | 13.43% [-2.22%, 29.53%] | $246.62 |
| series | tier1 | 114 | 114 | 0.0412 | 8.56% [-15.46%, 33.84%] | $95.66 | 1.913× | 46.99% | $9.42 | 80 (34 unfilled) | 8.18% [-20.81%, 42.36%] | $65.98 |
| series | tier2 | 50 | 50 | 0.0326 | -11.09% [-41.38%, 26.39%] | $45.40 | 0.908× | 32.44% | $6.42 | 29 (21 unfilled) | -39.78% [-69.52%, -8.05%] | $36.67 |
| series | tier3 | 190 | 190 | 0.0572 | 28.95% [12.89%, 44.70%] | $1939.82 | 38.796× | 43.46% | $192.44 | 120 (70 unfilled) | 29.88% [9.16%, 50.35%] | $265.92 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 114 | 114 | 0.0412 | 8.56% [-15.46%, 33.84%] | $95.66 | 1.913× | 46.99% | $9.42 | 80 (34 unfilled) | 8.18% [-20.81%, 42.36%] | $65.98 |
| series | international=0 | 240 | 240 | 0.0521 | 20.58% [6.34%, 35.34%] | $1668.42 | 33.368× | 62.39% | $224.02 | 149 (91 unfilled) | 16.25% [-1.17%, 34.08%] | $201.25 |
| game | all | 262 | 155 | 0.0125 | -7.26% [-14.80%, 0.14%] | $24.00 | 0.480× | 53.43% | $4.27 | 99 (163 unfilled) | -4.57% [-16.71%, 7.28%] | $46.24 |
| game | tier1 | 104 | 63 | 0.0104 | -3.16% [-14.22%, 7.93%] | $39.90 | 0.798× | 22.63% | $4.70 | 43 (61 unfilled) | -0.66% [-19.24%, 15.76%] | $44.61 |
| game | tier2 | 54 | 30 | 0.0136 | -10.56% [-26.30%, 3.73%] | $45.76 | 0.915× | 17.40% | $5.04 | 16 (38 unfilled) | -10.05% [-40.11%, 16.50%] | $51.49 |
| game | tier3 | 104 | 62 | 0.0140 | -9.63% [-23.66%, 3.57%] | $33.02 | 0.660× | 38.86% | $3.39 | 40 (64 unfilled) | -6.58% [-27.44%, 12.53%] | $50.24 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 104 | 63 | 0.0104 | -3.16% [-14.22%, 7.93%] | $39.90 | 0.798× | 22.63% | $4.70 | 43 (61 unfilled) | -0.66% [-19.24%, 15.76%] | $44.61 |
| game | international=0 | 158 | 92 | 0.0139 | -9.95% [-20.22%, 0.22%] | $30.30 | 0.606× | 45.47% | $3.71 | 56 (102 unfilled) | -7.57% [-25.65%, 8.67%] | $51.82 |
| series+game | all | 616 | 398 | 0.0332 | 6.61% [-0.58%, 13.74%] | $2243.42 | 44.868× | 42.77% | $237.65 | 328 (288 unfilled) | 8.05% [-3.04%, 20.13%] | $266.88 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| game | 2026-07 | 104 | 0.655158 | 0.680951 | 0.670295 | 24.76% (63), $89.50 | -22.92% (13), $47.39 | 15 (48 unfilled) | 22.38% [-33.99%, 76.49%] | $58.27 | 3 (10 unfilled) | -47.80% [-100.00%, 56.59%] | $50.46 |
| game | 2026-08 | 261 | 0.606333 | 0.624652 | 0.620045 | 1.58% (171), $47.08 | -10.86% (69), $34.78 | 49 (122 unfilled) | 5.21% [-22.32%, 30.96%] | $53.66 | 16 (53 unfilled) | -2.77% [-37.61%, 27.15%] | $48.45 |
| game | 2026-09 | 211 | 0.575022 | 0.586690 | 0.584628 | 1.82% (143), $97.38 | -8.04% (104), $37.28 | 66 (77 unfilled) | -9.85% [-35.00%, 14.83%] | $52.36 | 41 (63 unfilled) | -9.55% [-29.60%, 10.26%] | $45.51 |
| game | 2026-10 | 197 | 0.598515 | 0.590224 | 0.588963 | -12.19% (111), $23.04 | -0.22% (76), $49.64 | 62 (49 unfilled) | -20.68% [-48.91%, 11.79%] | $20.81 | 39 (37 unfilled) | 3.28% [-14.32%, 17.80%] | $51.96 |
| series | 2026-07 | 79 | 0.637400 | 0.649375 | 0.689503 | 41.01% (63), $244.85 | 51.16% (51), $153.30 | 43 (20 unfilled) | 46.76% [3.33%, 93.11%] | $119.14 | 34 (17 unfilled) | 57.10% [9.21%, 112.97%] | $71.10 |
| series | 2026-08 | 147 | 0.533651 | 0.535233 | 0.570451 | 1.60% (118), $91.71 | 10.84% (97), $172.20 | 76 (42 unfilled) | -12.67% [-35.80%, 12.88%] | $34.43 | 61 (36 unfilled) | -4.44% [-30.17%, 24.16%] | $62.85 |
| series | 2026-09 | 145 | 0.525825 | 0.513115 | 0.527022 | 3.93% (114), $70.60 | 10.08% (98), $73.04 | 79 (35 unfilled) | 9.19% [-16.62%, 37.23%] | $118.60 | 68 (30 unfilled) | 15.65% [-11.72%, 45.72%] | $86.64 |
| series | 2026-10 | 186 | 0.525827 | 0.523419 | 0.547318 | -0.98% (135), $114.13 | 11.72% (108), $211.37 | 82 (53 unfilled) | -2.56% [-27.02%, 21.63%] | $67.51 | 66 (42 unfilled) | 5.17% [-20.35%, 34.41%] | $93.35 |

### player_glicko_rw_tier_revert+form: Kalshi comparison and returns

form: rows=35654, H=3, w=1.03045

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 557 | 0.542018 | 0.568306 | -0.026288 [-0.047807, -0.005926] | yes |
| series | tier1 | 195 | 0.536096 | 0.544117 | -0.008021 [-0.042735, 0.027206] | no |
| series | tier2 | 73 | 0.578255 | 0.567515 | 0.010740 [-0.040537, 0.058122] | no |
| series | tier3 | 289 | 0.536861 | 0.584827 | -0.047966 [-0.078415, -0.015720] | yes |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 195 | 0.536096 | 0.544117 | -0.008021 [-0.042735, 0.027206] | no |
| series | international=0 | 362 | 0.545208 | 0.581336 | -0.036127 [-0.063482, -0.008715] | yes |
| game | all | 773 | 0.600056 | 0.609217 | -0.009161 [-0.022465, 0.004527] | no |
| game | tier1 | 291 | 0.605850 | 0.601557 | 0.004293 [-0.013360, 0.024622] | no |
| game | tier2 | 145 | 0.631484 | 0.619558 | 0.011926 [-0.013590, 0.037309] | no |
| game | tier3 | 337 | 0.581531 | 0.611382 | -0.029851 [-0.052736, -0.006804] | yes |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 291 | 0.605850 | 0.601557 | 0.004293 [-0.013360, 0.024622] | no |
| game | international=0 | 482 | 0.596558 | 0.613841 | -0.017283 [-0.036557, 0.001494] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 442 | 442 | 0.0832 | 7.37% [-3.60%, 19.37%] | $2951.89 | 59.038× | 58.75% | $248.78 | 288 (154 unfilled) | 4.28% [-9.66%, 18.73%] | $230.89 |
| series | tier1 | 155 | 155 | 0.0723 | -3.10% [-22.95%, 17.69%] | $62.83 | 1.257× | 62.30% | $7.52 | 107 (48 unfilled) | -5.17% [-29.29%, 20.64%] | $65.78 |
| series | tier2 | 60 | 60 | 0.0708 | -13.32% [-40.93%, 19.90%] | $27.16 | 0.543× | 56.86% | $5.43 | 35 (25 unfilled) | -25.34% [-55.20%, 6.98%] | $25.05 |
| series | tier3 | 227 | 227 | 0.0940 | 20.03% [5.48%, 35.54%] | $1636.81 | 32.736× | 54.73% | $238.16 | 146 (81 unfilled) | 18.37% [-0.60%, 37.05%] | $328.56 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 155 | 155 | 0.0723 | -3.10% [-22.95%, 17.69%] | $62.83 | 1.257× | 62.30% | $7.52 | 107 (48 unfilled) | -5.17% [-29.29%, 20.64%] | $65.78 |
| series | international=0 | 287 | 287 | 0.0892 | 13.03% [-0.29%, 26.66%] | $1847.76 | 36.955× | 49.57% | $244.35 | 181 (106 unfilled) | 9.88% [-6.82%, 26.90%] | $182.53 |
| game | all | 481 | 265 | 0.0636 | 5.20% [-4.25%, 14.31%] | $134.75 | 2.695× | 61.22% | $26.90 | 185 (296 unfilled) | -0.99% [-15.56%, 14.50%] | $32.92 |
| game | tier1 | 146 | 82 | 0.0553 | -1.65% [-17.77%, 15.68%] | $32.14 | 0.643× | 45.32% | $4.68 | 64 (82 unfilled) | -11.23% [-36.17%, 15.13%] | $29.42 |
| game | tier2 | 95 | 51 | 0.0547 | -8.42% [-28.35%, 12.41%] | $36.14 | 0.723× | 27.73% | $4.17 | 32 (63 unfilled) | 0.39% [-33.75%, 34.90%] | $46.71 |
| game | tier3 | 240 | 132 | 0.0723 | 14.78% [1.93%, 27.25%] | $278.13 | 5.563× | 36.33% | $38.52 | 89 (151 unfilled) | 5.91% [-14.00%, 26.30%] | $59.74 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 146 | 82 | 0.0553 | -1.65% [-17.77%, 15.68%] | $32.14 | 0.643× | 45.32% | $4.68 | 64 (82 unfilled) | -11.23% [-36.17%, 15.13%] | $29.42 |
| game | international=0 | 335 | 183 | 0.0673 | 8.20% [-2.36%, 18.95%] | $200.75 | 4.015× | 47.54% | $31.98 | 121 (214 unfilled) | 4.45% [-12.70%, 21.91%] | $56.44 |
| series+game | all | 923 | 468 | 0.0730 | 6.24% [-2.83%, 14.90%] | $897.15 | 17.943× | 60.56% | $141.99 | 473 (450 unfilled) | 2.22% [-9.27%, 13.69%] | $224.68 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 0 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-07 | series | 621 | 1.062209 | 0.658057 | fitted |
| 2026-07 | game | 434 | 1.200287 | -0.056692 | fitted |
| 2026-08 | series | 621 | 1.062209 | 0.658057 | fitted |
| 2026-08 | game | 434 | 1.200287 | -0.056692 | fitted |
| 2026-09 | series | 621 | 1.062209 | 0.658057 | fitted |
| 2026-09 | game | 434 | 1.200287 | -0.056692 | fitted |
| 2026-10 | series | 621 | 1.062209 | 0.658057 | fitted |
| 2026-10 | game | 434 | 1.200287 | -0.056692 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 557 | 0.539321 | 0.568306 | -0.028985 [-0.043092, -0.016200] | yes |
| series | tier1 | 195 | 0.527293 | 0.544117 | -0.016825 [-0.038379, 0.004951] | no |
| series | tier2 | 73 | 0.565250 | 0.567515 | -0.002265 [-0.034499, 0.027624] | no |
| series | tier3 | 289 | 0.540888 | 0.584827 | -0.043939 [-0.063692, -0.022778] | yes |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 195 | 0.527293 | 0.544117 | -0.016825 [-0.038379, 0.004951] | no |
| series | international=0 | 362 | 0.545801 | 0.581336 | -0.035535 [-0.053184, -0.017681] | yes |
| game | all | 773 | 0.609135 | 0.609217 | -0.000081 [-0.004463, 0.004507] | no |
| game | tier1 | 291 | 0.603306 | 0.601557 | 0.001749 [-0.005990, 0.010383] | no |
| game | tier2 | 145 | 0.618668 | 0.619558 | -0.000890 [-0.009751, 0.007954] | no |
| game | tier3 | 337 | 0.610068 | 0.611382 | -0.001314 [-0.007460, 0.004785] | no |
| game | unknown | 0 | — | — | — | — |
| game | international=1 | 291 | 0.603306 | 0.601557 | 0.001749 [-0.005990, 0.010383] | no |
| game | international=0 | 482 | 0.612655 | 0.613841 | -0.001186 [-0.006110, 0.003969] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 361 | 361 | 0.0525 | 13.21% [1.51%, 25.23%] | $3310.11 | 66.202× | 62.19% | $248.78 | 228 (133 unfilled) | 14.54% [-0.41%, 31.40%] | $325.29 |
| series | tier1 | 120 | 120 | 0.0448 | 0.63% [-21.89%, 24.02%] | $131.40 | 2.628× | 35.76% | $13.77 | 80 (40 unfilled) | 3.83% [-23.92%, 35.33%] | $81.67 |
| series | tier2 | 49 | 49 | 0.0378 | -5.14% [-37.22%, 31.90%] | $46.37 | 0.927× | 33.52% | $6.30 | 28 (21 unfilled) | -19.09% [-56.16%, 20.08%] | $42.69 |
| series | tier3 | 192 | 192 | 0.0612 | 25.78% [10.11%, 42.31%] | $1273.14 | 25.463× | 49.01% | $145.29 | 120 (72 unfilled) | 29.59% [10.68%, 49.29%] | $276.68 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 120 | 120 | 0.0448 | 0.63% [-21.89%, 24.02%] | $131.40 | 2.628× | 35.76% | $13.77 | 80 (40 unfilled) | 3.83% [-23.92%, 35.33%] | $81.67 |
| series | international=0 | 241 | 241 | 0.0564 | 19.47% [5.60%, 34.29%] | $1081.49 | 21.630× | 66.35% | $189.94 | 148 (93 unfilled) | 20.33% [2.54%, 38.98%] | $245.83 |
| game | all | 174 | 108 | 0.0088 | -3.78% [-11.55%, 3.62%] | $38.55 | 0.771× | 29.81% | $4.22 | 57 (117 unfilled) | 2.29% [-11.86%, 13.68%] | $51.99 |
| game | tier1 | 76 | 48 | 0.0064 | -4.16% [-16.10%, 6.82%] | $43.97 | 0.879× | 14.64% | $4.61 | 28 (48 unfilled) | -9.83% [-31.84%, 9.57%] | $46.06 |
| game | tier2 | 40 | 23 | 0.0126 | 2.00% [-12.02%, 15.46%] | $51.00 | 1.020× | 18.69% | $5.26 | 10 (30 unfilled) | 17.62% [-10.63%, 34.80%] | $53.47 |
| game | tier3 | 58 | 37 | 0.0092 | -7.27% [-23.82%, 7.35%] | $42.79 | 0.856× | 17.31% | $3.82 | 19 (39 unfilled) | 12.02% [-8.30%, 26.81%] | $52.79 |
| game | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| game | international=1 | 76 | 48 | 0.0064 | -4.16% [-16.10%, 6.82%] | $43.97 | 0.879× | 14.64% | $4.61 | 28 (48 unfilled) | -9.83% [-31.84%, 9.57%] | $46.06 |
| game | international=0 | 98 | 60 | 0.0106 | -3.49% [-14.74%, 7.24%] | $43.77 | 0.875× | 24.04% | $4.57 | 29 (69 unfilled) | 13.96% [-2.44%, 26.61%] | $56.44 |
| series+game | all | 535 | 395 | 0.0383 | 7.75% [-0.56%, 16.07%] | $2455.23 | 49.105× | 49.18% | $248.78 | 285 (250 unfilled) | 12.12% [-0.51%, 25.85%] | $335.27 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| game | 2026-07 | 104 | 0.659162 | 0.675720 | 0.670295 | 25.38% (67), $84.06 | -47.77% (5), $43.72 | 15 (52 unfilled) | 22.38% [-33.99%, 76.49%] | $56.86 | 0 (5 unfilled) | — | $48.98 |
| game | 2026-08 | 261 | 0.600795 | 0.619605 | 0.620045 | 4.85% (172), $81.48 | -9.41% (40), $48.06 | 47 (125 unfilled) | 12.66% [-15.31%, 42.81%] | $54.19 | 7 (33 unfilled) | -15.47% [-53.08%, 20.78%] | $48.43 |
| game | 2026-09 | 211 | 0.570817 | 0.582894 | 0.584628 | 7.42% (137), $89.41 | -4.98% (71), $46.00 | 65 (72 unfilled) | -0.87% [-24.70%, 22.20%] | $51.74 | 22 (49 unfilled) | 4.03% [-18.92%, 22.94%] | $53.26 |
| game | 2026-10 | 197 | 0.599191 | 0.588220 | 0.588963 | -9.94% (105), $27.01 | 5.37% (58), $49.98 | 58 (47 unfilled) | -18.16% [-42.01%, 9.34%] | $25.66 | 28 (30 unfilled) | 5.33% [-13.65%, 19.66%] | $51.43 |
| series | 2026-07 | 79 | 0.631750 | 0.645274 | 0.689503 | 38.34% (62), $260.66 | 43.61% (55), $161.93 | 42 (20 unfilled) | 42.96% [1.14%, 90.92%] | $138.45 | 37 (18 unfilled) | 54.38% [8.25%, 105.09%] | $78.59 |
| series | 2026-08 | 147 | 0.531811 | 0.531725 | 0.570451 | 2.49% (118), $97.31 | 12.07% (97), $197.75 | 77 (41 unfilled) | -10.01% [-34.08%, 14.93%] | $34.61 | 63 (34 unfilled) | -3.61% [-30.60%, 26.73%] | $71.96 |
| series | 2026-09 | 145 | 0.523819 | 0.511188 | 0.527022 | 3.88% (117), $48.05 | 11.53% (96), $62.99 | 80 (37 unfilled) | 9.91% [-15.25%, 36.85%] | $112.05 | 63 (33 unfilled) | 21.40% [-7.15%, 51.92%] | $91.58 |
| series | 2026-10 | 186 | 0.526161 | 0.522255 | 0.547318 | 0.92% (145), $75.17 | 0.76% (113), $182.19 | 89 (56 unfilled) | -6.64% [-29.40%, 18.02%] | $61.11 | 65 (48 unfilled) | 2.81% [-22.54%, 28.73%] | $102.62 |

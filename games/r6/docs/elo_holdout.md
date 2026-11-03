# R6 Elo backtest

## Combined summary (validation, all sections)

| Model | Series Δ log loss | Series flat ROI | Series Kelly (LoL caps) $ | Series flat ROI depth-capped | Series Kelly depth-capped $ | Map Δ log loss | Map flat ROI | Map Kelly (LoL caps) $ | Map flat ROI depth-capped | Map Kelly depth-capped $ | Series blended Δ log loss | Series blended flat ROI | Series blended Kelly (LoL caps) $ | Series blended flat ROI depth-capped | Series blended Kelly depth-capped $ | Map blended Δ log loss | Map blended flat ROI | Map blended Kelly (LoL caps) $ | Map blended flat ROI depth-capped | Map blended Kelly depth-capped $ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| team_elo | 0.093656 | -5.55% | $4.18 | -12.28% | $9.91 | 0.084554 | -6.88% | $19.85 | -33.74% | $42.98 | 0.005457 | -21.40% | $44.38 | -2.60% | $63.42 | — | — | $50.00 | — | $50.00 |
| player_round_glicko | 0.025265 | -0.12% | $5.00 | -9.14% | $17.86 | 0.001314 | 19.86% | $103.21 | -40.74% | $45.96 | 0.009485 | -24.24% | $31.19 | -17.18% | $40.35 | — | — | $50.00 | — | $50.00 |
| player_round_glicko_rookie | 0.020165 | -1.51% | $7.66 | -6.82% | $21.48 | -0.003576 | 19.44% | $98.96 | -40.74% | $45.94 | 0.006674 | -15.65% | $35.50 | -12.09% | $45.86 | — | — | $50.00 | — | $50.00 |
| team_elo+none | 0.093656 | -5.55% | $4.18 | -12.28% | $9.91 | 0.084554 | -6.88% | $19.85 | -33.74% | $42.98 | 0.005457 | -21.40% | $44.38 | -2.60% | $63.42 | — | — | $50.00 | — | $50.00 |
| team_elo+calibration | 0.068889 | 0.86% | $5.29 | -4.72% | $22.35 | 0.012166 | 18.77% | $47.87 | -48.09% | $41.34 | 0.007054 | -23.99% | $38.15 | -8.35% | $59.71 | — | — | $50.00 | — | $50.00 |
| player_round_glicko+none | 0.025265 | -0.12% | $5.00 | -9.14% | $17.86 | 0.001314 | 19.86% | $103.21 | -40.74% | $45.96 | 0.009485 | -24.24% | $31.19 | -17.18% | $40.35 | — | — | $50.00 | — | $50.00 |
| player_round_glicko+calibration | 0.024288 | -5.26% | $6.41 | -9.80% | $21.51 | -0.009761 | 17.93% | $97.30 | -50.79% | $44.11 | 0.008759 | -21.76% | $27.64 | -29.69% | $37.39 | — | — | $50.00 | — | $50.00 |
| player_round_glicko_rookie+none | 0.020165 | -1.51% | $7.66 | -6.82% | $21.48 | -0.003576 | 19.44% | $98.96 | -40.74% | $45.94 | 0.006674 | -15.65% | $35.50 | -12.09% | $45.86 | — | — | $50.00 | — | $50.00 |
| player_round_glicko_rookie+calibration | 0.019594 | -5.16% | $10.61 | -8.77% | $31.66 | -0.015746 | 19.70% | $107.80 | -50.79% | $44.27 | 0.006067 | -18.44% | $32.47 | -22.82% | $40.68 | — | — | $50.00 | — | $50.00 |

Series temperatures (stage 1; p′ = σ(T·logit p), T < 1 pulls odds toward 50%): team_elo Bo3 0.63, Bo5 0.40; player_round_glicko_rookie Bo3 0.70, Bo5 0.63; player_round_glicko Bo3 0.77, Bo5 0.64; team_elo+none Bo3 0.63, Bo5 0.40; team_elo+calibration Bo3 0.73, Bo5 0.40; player_round_glicko+none Bo3 0.77, Bo5 0.64; player_round_glicko+calibration Bo3 0.75, Bo5 0.63; player_round_glicko_rookie+none Bo3 0.70, Bo5 0.63; player_round_glicko_rookie+calibration Bo3 0.75, Bo5 0.67

Parameters minimize tuning map log loss across all sections. Replay predicts before update; Replay starts at the first map. Tuning: [2023-01-01, 2026-01-01); validation: [2026-01-01, 2026-07-01). Holdout is scored only with --holdout and never selects parameters. Series use the first map prediction and independent maps in Bo1/Bo3/Bo5; Bo2, unknown/unsupported lengths and unknown results are skipped. Accuracy gives 0.5 predictions half credit; ECE uses 10 equal-width bins. Log loss clips probabilities at 1e-6. Paired bootstrap uses 2,000 resamples, seed 0, clustered by match_id. Differences are the named model minus its comparator; negative favors the model. Significance requires a 95% percentile interval excluding zero. Tuning scores are selection diagnostics, not independent evidence of improvement.

Fit through 2025-12-31. Unknown host-region map rows: 6505 (including missing/un).

## Stage 1 — tuning (outcomes)

### Leaderboard

| Model | Best params | Map log loss | Series log loss | Rows |
|---|---|---:|---:|---:|
| player_round_glicko_rookie | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 280, "rookie_maps": 3200, "rookie_penalty": 225, "tau": 0.75} | 0.581759 | 0.564220 | 50153 |
| player_round_glicko | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 280, "tau": 0.75} | 0.589793 | 0.575660 | 50153 |
| team_elo | {"k": 64} | 0.635894 | 0.630922 | 50153 |

Kalshi uses the first hourly bid/ask (midpoint for log loss, ask/bid for bets) ending ≥30 min after the market opened and ≥2 h before the scheduled start, with a spread ≤ 0.06: a price a bot could trade before the series. Markets without such a quote are skipped. oriented to team1 using aliases. One contract per event, preferring team1. Compare identical rows; map predictions use the first map's pre-match chance. Missing links, aliases or candles are skipped; unplayed maps are not in the rows. Returns use frozen stage-1 parameters. Each bet buys $1 of contracts, fees extra; order fees ceil to a cent (0.07 × contracts × price × (1−price)). Edge selection uses unrounded per-contract fees. ROI divides profit by stake plus fees; intervals resample matches 2,000 times. Unlimited depth and depth-capped returns are shown together. Depth uses 0.5 of acceptable-price tape volume in the 6 hours after the quote, missing tapes give zero fills. Partial Kelly fills are allowed; flat bets require the full $1 stake. Kelly uses LoL caps and rounded-fee affordability, from a $50 seed. Each slice runs independently. Tape volume is a fill proxy; no slippage is modeled.

## Quote-time robustness

| Quote rule | Model | Kind | Rows | Raw Δ log loss | Blended Δ log loss | Raw flat ROI depth-capped | Blended flat ROI depth-capped |
|---|---|---|---:|---:|---:|---:|---:|
| tradeable | team_elo | series | 244 | 0.093656 | 0.005457 | -12.28% | -2.60% |
| tradeable | team_elo | map | 109 | 0.084554 | — | -33.74% | — |
| tradeable | player_round_glicko | series | 244 | 0.025265 | 0.009485 | -9.14% | -17.18% |
| tradeable | player_round_glicko | map | 109 | 0.001314 | — | -40.74% | — |
| tradeable | player_round_glicko_rookie | series | 244 | 0.020165 | 0.006674 | -6.82% | -12.09% |
| tradeable | player_round_glicko_rookie | map | 109 | -0.003576 | — | -40.74% | — |
| tradeable | team_elo+none | series | 244 | 0.093656 | 0.005457 | -12.28% | -2.60% |
| tradeable | team_elo+none | map | 109 | 0.084554 | — | -33.74% | — |
| tradeable | team_elo+calibration | series | 244 | 0.068889 | 0.007054 | -4.72% | -8.35% |
| tradeable | team_elo+calibration | map | 109 | 0.012166 | — | -48.09% | — |
| tradeable | player_round_glicko+none | series | 244 | 0.025265 | 0.009485 | -9.14% | -17.18% |
| tradeable | player_round_glicko+none | map | 109 | 0.001314 | — | -40.74% | — |
| tradeable | player_round_glicko+calibration | series | 244 | 0.024288 | 0.008759 | -9.80% | -29.69% |
| tradeable | player_round_glicko+calibration | map | 109 | -0.009761 | — | -50.79% | — |
| tradeable | player_round_glicko_rookie+none | series | 244 | 0.020165 | 0.006674 | -6.82% | -12.09% |
| tradeable | player_round_glicko_rookie+none | map | 109 | -0.003576 | — | -40.74% | — |
| tradeable | player_round_glicko_rookie+calibration | series | 244 | 0.019594 | 0.006067 | -8.77% | -22.82% |
| tradeable | player_round_glicko_rookie+calibration | map | 109 | -0.015746 | — | -50.79% | — |
| hours24 | team_elo | series | 109 | 0.116217 | — | -33.29% | — |
| hours24 | team_elo | map | 44 | 0.118343 | — | 34.30% | — |
| hours24 | player_round_glicko | series | 109 | 0.006323 | — | -21.37% | — |
| hours24 | player_round_glicko | map | 44 | -0.039777 | — | -100.00% | — |
| hours24 | player_round_glicko_rookie | series | 109 | 0.000483 | — | -14.26% | — |
| hours24 | player_round_glicko_rookie | map | 44 | -0.039804 | — | -100.00% | — |
| hours24 | team_elo+none | series | 109 | 0.116217 | — | -33.29% | — |
| hours24 | team_elo+none | map | 44 | 0.118343 | — | 34.30% | — |
| hours24 | team_elo+calibration | series | 109 | 0.093531 | — | -19.61% | — |
| hours24 | team_elo+calibration | map | 44 | -0.003006 | — | -100.00% | — |
| hours24 | player_round_glicko+none | series | 109 | 0.006323 | — | -21.37% | — |
| hours24 | player_round_glicko+none | map | 44 | -0.039777 | — | -100.00% | — |
| hours24 | player_round_glicko+calibration | series | 109 | 0.013510 | — | -21.38% | — |
| hours24 | player_round_glicko+calibration | map | 44 | -0.056343 | — | -100.00% | — |
| hours24 | player_round_glicko_rookie+none | series | 109 | 0.000483 | — | -14.26% | — |
| hours24 | player_round_glicko_rookie+none | map | 44 | -0.039804 | — | -100.00% | — |
| hours24 | player_round_glicko_rookie+calibration | series | 109 | 0.008512 | — | -18.53% | — |
| hours24 | player_round_glicko_rookie+calibration | map | 44 | -0.059007 | — | -100.00% | — |
| hours6 | team_elo | series | 225 | 0.094132 | 0.010331 | 6.81% | -11.46% |
| hours6 | team_elo | map | 101 | 0.096022 | — | -19.45% | — |
| hours6 | player_round_glicko | series | 225 | 0.020227 | 0.014016 | -10.41% | -16.62% |
| hours6 | player_round_glicko | map | 101 | 0.000572 | — | -27.07% | — |
| hours6 | player_round_glicko_rookie | series | 225 | 0.014415 | 0.013427 | -8.19% | -17.53% |
| hours6 | player_round_glicko_rookie | map | 101 | -0.003735 | — | -17.47% | — |
| hours6 | team_elo+none | series | 225 | 0.094132 | 0.010331 | 6.81% | -11.46% |
| hours6 | team_elo+none | map | 101 | 0.096022 | — | -19.45% | — |
| hours6 | team_elo+calibration | series | 225 | 0.067086 | 0.012754 | -4.94% | -8.73% |
| hours6 | team_elo+calibration | map | 101 | 0.013732 | — | -4.06% | — |
| hours6 | player_round_glicko+none | series | 225 | 0.020227 | 0.014016 | -10.41% | -16.62% |
| hours6 | player_round_glicko+none | map | 101 | 0.000572 | — | -27.07% | — |
| hours6 | player_round_glicko+calibration | series | 225 | 0.020486 | 0.015613 | -12.24% | -21.61% |
| hours6 | player_round_glicko+calibration | map | 101 | -0.011870 | — | -29.35% | — |
| hours6 | player_round_glicko_rookie+none | series | 225 | 0.014415 | 0.013427 | -8.19% | -17.53% |
| hours6 | player_round_glicko_rookie+none | map | 101 | -0.003735 | — | -17.47% | — |
| hours6 | player_round_glicko_rookie+calibration | series | 225 | 0.015348 | 0.014313 | -8.79% | -17.42% |
| hours6 | player_round_glicko_rookie+calibration | map | 101 | -0.017202 | — | -22.54% | — |

### Maps

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| coin | all | 50153 | 0.693147 | 0.250000 | 0.500000 | 0.052788 |
| coin | tier1 | 1659 | 0.693147 | 0.250000 | 0.500000 | 0.009343 |
| coin | tier2 | 4707 | 0.693147 | 0.250000 | 0.500000 | 0.072127 |
| coin | tier3 | 43764 | 0.693147 | 0.250000 | 0.500000 | 0.052235 |
| coin | unknown | 23 | 0.693147 | 0.250000 | 0.500000 | 0.282609 |
| coin | international=1 | 1755 | 0.693147 | 0.250000 | 0.500000 | 0.012251 |
| coin | international=0 | 48398 | 0.693147 | 0.250000 | 0.500000 | 0.054258 |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| team_elo | all | 50153 | 0.635894 | 0.222732 | 0.633771 | 0.032752 |
| team_elo | tier1 | 1659 | 0.696300 | 0.246118 | 0.593731 | 0.070784 |
| team_elo | tier2 | 4707 | 0.641215 | 0.224815 | 0.631825 | 0.049632 |
| team_elo | tier3 | 43764 | 0.633129 | 0.221665 | 0.635374 | 0.032313 |
| team_elo | unknown | 23 | 0.451231 | 0.138459 | 0.869565 | 0.239073 |
| team_elo | international=1 | 1755 | 0.690917 | 0.243840 | 0.600570 | 0.064115 |
| team_elo | international=0 | 48398 | 0.633899 | 0.221966 | 0.634975 | 0.033375 |

team_elo − coin (paired log loss):

| Section | Rows | team_elo log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 50153 | 0.635894 | 0.693147 | -0.057253 | [-0.060483, -0.053932] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko | all | 50153 | 0.589793 | 0.203093 | 0.677248 | 0.020570 |
| player_round_glicko | tier1 | 1659 | 0.658933 | 0.233656 | 0.585895 | 0.041848 |
| player_round_glicko | tier2 | 4707 | 0.593134 | 0.204837 | 0.669641 | 0.027492 |
| player_round_glicko | tier3 | 43764 | 0.586936 | 0.201797 | 0.681451 | 0.020850 |
| player_round_glicko | unknown | 23 | 0.354103 | 0.107263 | 0.826087 | 0.158745 |
| player_round_glicko | international=1 | 1755 | 0.654937 | 0.231013 | 0.594017 | 0.040509 |
| player_round_glicko | international=0 | 48398 | 0.587430 | 0.202080 | 0.680266 | 0.021509 |

player_round_glicko − coin (paired log loss):

| Section | Rows | player_round_glicko log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 50153 | 0.589793 | 0.693147 | -0.103355 | [-0.106956, -0.099787] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko_rookie | all | 50153 | 0.581759 | 0.199163 | 0.687646 | 0.019445 |
| player_round_glicko_rookie | tier1 | 1659 | 0.662395 | 0.234084 | 0.586197 | 0.044157 |
| player_round_glicko_rookie | tier2 | 4707 | 0.584580 | 0.200969 | 0.679626 | 0.023083 |
| player_round_glicko_rookie | tier3 | 43764 | 0.578530 | 0.197697 | 0.692281 | 0.020007 |
| player_round_glicko_rookie | unknown | 23 | 0.332459 | 0.100859 | 0.826087 | 0.175366 |
| player_round_glicko_rookie | international=1 | 1755 | 0.658186 | 0.230820 | 0.596011 | 0.042243 |
| player_round_glicko_rookie | international=0 | 48398 | 0.578988 | 0.198015 | 0.690969 | 0.020301 |

player_round_glicko_rookie − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 50153 | 0.581759 | 0.693147 | -0.111388 | [-0.115480, -0.107335] | yes |

player_round_glicko_rookie − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 50153 | 0.581759 | 0.635894 | -0.054135 | [-0.057565, -0.050820] | yes |

player_round_glicko − team_elo (paired log loss):

| Section | Rows | player_round_glicko log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 50153 | 0.589793 | 0.635894 | -0.046101 | [-0.049058, -0.043178] | yes |

player_round_glicko − player_round_glicko_rookie (paired log loss):

| Section | Rows | player_round_glicko log loss | player_round_glicko_rookie log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 50153 | 0.589793 | 0.581759 | 0.008033 | [0.006825, 0.009250] | yes |
| tier1 | 1659 | 0.658933 | 0.662395 | -0.003463 | [-0.009456, 0.000868] | no |
| tier2 | 4707 | 0.593134 | 0.584580 | 0.008554 | [0.005743, 0.011345] | yes |
| tier3 | 43764 | 0.586936 | 0.578530 | 0.008406 | [0.007026, 0.009714] | yes |
| unknown | 23 | 0.354103 | 0.332459 | 0.021644 | [-0.014558, 0.052140] | no |
| international=1 | 1755 | 0.654937 | 0.658186 | -0.003250 | [-0.009321, 0.001896] | no |
| international=0 | 48398 | 0.587430 | 0.578988 | 0.008443 | [0.007249, 0.009667] | yes |

### Series

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| coin | all | 35144 | 0.693147 | 0.250000 | 0.500000 | 0.053323 |
| coin | tier1 | 818 | 0.693147 | 0.250000 | 0.500000 | 0.007335 |
| coin | tier2 | 3188 | 0.693147 | 0.250000 | 0.500000 | 0.070891 |
| coin | tier3 | 31128 | 0.693147 | 0.250000 | 0.500000 | 0.052686 |
| coin | unknown | 10 | 0.693147 | 0.250000 | 0.500000 | 0.200000 |
| coin | international=1 | 885 | 0.693147 | 0.250000 | 0.500000 | 0.011864 |
| coin | international=0 | 34259 | 0.693147 | 0.250000 | 0.500000 | 0.054394 |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| team_elo | all | 35144 | 0.630922 | 0.220622 | 0.635998 | 0.036055 |
| team_elo | tier1 | 818 | 0.701468 | 0.246603 | 0.588020 | 0.067899 |
| team_elo | tier2 | 3188 | 0.631722 | 0.220605 | 0.637077 | 0.048433 |
| team_elo | tier3 | 31128 | 0.629044 | 0.219967 | 0.637095 | 0.035974 |
| team_elo | unknown | 10 | 0.451097 | 0.138887 | 0.800000 | 0.348707 |
| team_elo | international=1 | 885 | 0.693902 | 0.243560 | 0.597740 | 0.057129 |
| team_elo | international=0 | 34259 | 0.629295 | 0.220029 | 0.636986 | 0.036854 |

team_elo − coin (paired log loss):

| Section | Rows | team_elo log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 35144 | 0.630922 | 0.693147 | -0.062226 | [-0.066030, -0.058355] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko | all | 35144 | 0.575660 | 0.197029 | 0.689563 | 0.024174 |
| player_round_glicko | tier1 | 818 | 0.651399 | 0.228625 | 0.594132 | 0.060441 |
| player_round_glicko | tier2 | 3188 | 0.572756 | 0.196322 | 0.686951 | 0.031155 |
| player_round_glicko | tier3 | 31128 | 0.574026 | 0.196295 | 0.692303 | 0.024645 |
| player_round_glicko | unknown | 10 | 0.391993 | 0.122400 | 0.800000 | 0.174684 |
| player_round_glicko | international=1 | 885 | 0.645453 | 0.225056 | 0.606215 | 0.057819 |
| player_round_glicko | international=0 | 34259 | 0.573857 | 0.196305 | 0.691716 | 0.025005 |

player_round_glicko − coin (paired log loss):

| Section | Rows | player_round_glicko log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 35144 | 0.575660 | 0.693147 | -0.117487 | [-0.121952, -0.113200] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko_rookie | all | 35144 | 0.564220 | 0.191498 | 0.704573 | 0.022334 |
| player_round_glicko_rookie | tier1 | 818 | 0.656802 | 0.229088 | 0.594132 | 0.052837 |
| player_round_glicko_rookie | tier2 | 3188 | 0.560539 | 0.190937 | 0.702635 | 0.026531 |
| player_round_glicko_rookie | tier3 | 31128 | 0.562213 | 0.190587 | 0.707643 | 0.022884 |
| player_round_glicko_rookie | unknown | 10 | 0.410537 | 0.130639 | 0.800000 | 0.131985 |
| player_round_glicko_rookie | international=1 | 885 | 0.650676 | 0.224417 | 0.610734 | 0.047497 |
| player_round_glicko_rookie | international=0 | 34259 | 0.561986 | 0.190648 | 0.706997 | 0.023217 |

player_round_glicko_rookie − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 35144 | 0.564220 | 0.693147 | -0.128927 | [-0.133808, -0.124011] | yes |

player_round_glicko_rookie − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 35144 | 0.564220 | 0.630922 | -0.066702 | [-0.070656, -0.062792] | yes |

player_round_glicko − team_elo (paired log loss):

| Section | Rows | player_round_glicko log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 35144 | 0.575660 | 0.630922 | -0.055261 | [-0.058704, -0.051867] | yes |

player_round_glicko − player_round_glicko_rookie (paired log loss):

| Section | Rows | player_round_glicko log loss | player_round_glicko_rookie log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 35144 | 0.575660 | 0.564220 | 0.011440 | [0.009911, 0.012962] | yes |
| tier1 | 818 | 0.651399 | 0.656802 | -0.005403 | [-0.014885, 0.001361] | no |
| tier2 | 3188 | 0.572756 | 0.560539 | 0.012217 | [0.008527, 0.015637] | yes |
| tier3 | 31128 | 0.574026 | 0.562213 | 0.011813 | [0.010035, 0.013597] | yes |
| unknown | 10 | 0.391993 | 0.410537 | -0.018543 | [-0.074782, 0.020933] | no |
| international=1 | 885 | 0.645453 | 0.650676 | -0.005223 | [-0.015187, 0.003602] | no |
| international=0 | 34259 | 0.573857 | 0.561986 | 0.011871 | [0.010169, 0.013519] | yes |

## Stage 2 — validation (outcomes)

### Leaderboard (frozen stage-1 parameters)

| Model | Best params | Map log loss | Series log loss | Rows |
|---|---|---:|---:|---:|
| player_round_glicko_rookie+calibration | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 280, "rookie_maps": 3200, "rookie_penalty": 225, "tau": 0.75} | 0.568787 | 0.551487 | 9782 |
| player_round_glicko_rookie | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 280, "rookie_maps": 3200, "rookie_penalty": 225, "tau": 0.75} | 0.569667 | 0.552086 | 9782 |
| player_round_glicko_rookie+none | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 280, "rookie_maps": 3200, "rookie_penalty": 225, "tau": 0.75} | 0.569667 | 0.552086 | 9782 |
| player_round_glicko+calibration | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 280, "tau": 0.75} | 0.577029 | 0.562958 | 9782 |
| player_round_glicko | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 280, "tau": 0.75} | 0.577429 | 0.563146 | 9782 |
| player_round_glicko+none | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 280, "tau": 0.75} | 0.577429 | 0.563146 | 9782 |
| team_elo+calibration | {"k": 64} | 0.631718 | 0.628573 | 9782 |
| team_elo | {"k": 64} | 0.633978 | 0.630108 | 9782 |
| team_elo+none | {"k": 64} | 0.633978 | 0.630108 | 9782 |

### Maps

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| coin | all | 9782 | 0.693147 | 0.250000 | 0.500000 | 0.036189 |
| coin | tier1 | 393 | 0.693147 | 0.250000 | 0.500000 | 0.006361 |
| coin | tier2 | 757 | 0.693147 | 0.250000 | 0.500000 | 0.040291 |
| coin | tier3 | 8632 | 0.693147 | 0.250000 | 0.500000 | 0.037766 |
| coin | unknown | 0 | — | — | — | — |
| coin | international=1 | 593 | 0.693147 | 0.250000 | 0.500000 | 0.026138 |
| coin | international=0 | 9189 | 0.693147 | 0.250000 | 0.500000 | 0.036838 |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| team_elo | all | 9782 | 0.633978 | 0.221383 | 0.639082 | 0.030860 |
| team_elo | tier1 | 393 | 0.720566 | 0.257890 | 0.550891 | 0.115167 |
| team_elo | tier2 | 757 | 0.628460 | 0.216739 | 0.641347 | 0.067392 |
| team_elo | tier3 | 8632 | 0.630520 | 0.220128 | 0.642899 | 0.027493 |
| team_elo | unknown | 0 | — | — | — | — |
| team_elo | international=1 | 593 | 0.669988 | 0.236103 | 0.612142 | 0.065684 |
| team_elo | international=0 | 9189 | 0.631654 | 0.220433 | 0.640821 | 0.029426 |

team_elo − coin (paired log loss):

| Section | Rows | team_elo log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9782 | 0.633978 | 0.693147 | -0.059169 | [-0.067043, -0.051231] | yes |
| tier1 | 393 | 0.720566 | 0.693147 | 0.027419 | [-0.014208, 0.070436] | no |
| tier2 | 757 | 0.628460 | 0.693147 | -0.064687 | [-0.101593, -0.026522] | yes |
| tier3 | 8632 | 0.630520 | 0.693147 | -0.062627 | [-0.070670, -0.054447] | yes |
| international=1 | 593 | 0.669988 | 0.693147 | -0.023159 | [-0.057308, 0.010946] | no |
| international=0 | 9189 | 0.631654 | 0.693147 | -0.061493 | [-0.069102, -0.053778] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko | all | 9782 | 0.577429 | 0.197589 | 0.685749 | 0.017135 |
| player_round_glicko | tier1 | 393 | 0.668939 | 0.233630 | 0.615776 | 0.045089 |
| player_round_glicko | tier2 | 757 | 0.547117 | 0.185880 | 0.730515 | 0.032326 |
| player_round_glicko | tier3 | 8632 | 0.575921 | 0.196975 | 0.685009 | 0.019128 |
| player_round_glicko | unknown | 0 | — | — | — | — |
| player_round_glicko | international=1 | 593 | 0.633702 | 0.219269 | 0.644182 | 0.031562 |
| player_round_glicko | international=0 | 9189 | 0.573797 | 0.196190 | 0.688432 | 0.017863 |

player_round_glicko − coin (paired log loss):

| Section | Rows | player_round_glicko log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9782 | 0.577429 | 0.693147 | -0.115718 | [-0.124056, -0.107018] | yes |
| tier1 | 393 | 0.668939 | 0.693147 | -0.024208 | [-0.063216, 0.016204] | no |
| tier2 | 757 | 0.547117 | 0.693147 | -0.146031 | [-0.178186, -0.113466] | yes |
| tier3 | 8632 | 0.575921 | 0.693147 | -0.117226 | [-0.126192, -0.108497] | yes |
| international=1 | 593 | 0.633702 | 0.693147 | -0.059445 | [-0.095951, -0.024109] | yes |
| international=0 | 9189 | 0.573797 | 0.693147 | -0.119350 | [-0.128181, -0.110426] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko_rookie | all | 9782 | 0.569667 | 0.193665 | 0.695921 | 0.018178 |
| player_round_glicko_rookie | tier1 | 393 | 0.677440 | 0.233891 | 0.613232 | 0.056598 |
| player_round_glicko_rookie | tier2 | 757 | 0.538149 | 0.183109 | 0.730515 | 0.032434 |
| player_round_glicko_rookie | tier3 | 8632 | 0.567525 | 0.192759 | 0.696652 | 0.019736 |
| player_round_glicko_rookie | unknown | 0 | — | — | — | — |
| player_round_glicko_rookie | international=1 | 593 | 0.636911 | 0.218211 | 0.644182 | 0.043287 |
| player_round_glicko_rookie | international=0 | 9189 | 0.565328 | 0.192081 | 0.699260 | 0.017566 |

player_round_glicko_rookie − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9782 | 0.569667 | 0.693147 | -0.123480 | [-0.132521, -0.113648] | yes |
| tier1 | 393 | 0.677440 | 0.693147 | -0.015707 | [-0.061185, 0.032688] | no |
| tier2 | 757 | 0.538149 | 0.693147 | -0.154998 | [-0.188403, -0.121835] | yes |
| tier3 | 8632 | 0.567525 | 0.693147 | -0.125622 | [-0.135478, -0.115719] | yes |
| international=1 | 593 | 0.636911 | 0.693147 | -0.056236 | [-0.096337, -0.015288] | yes |
| international=0 | 9189 | 0.565328 | 0.693147 | -0.127819 | [-0.137958, -0.117703] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| team_elo+none | all | 9782 | 0.633978 | 0.221383 | 0.639082 | 0.030860 |
| team_elo+none | tier1 | 393 | 0.720566 | 0.257890 | 0.550891 | 0.115167 |
| team_elo+none | tier2 | 757 | 0.628460 | 0.216739 | 0.641347 | 0.067392 |
| team_elo+none | tier3 | 8632 | 0.630520 | 0.220128 | 0.642899 | 0.027493 |
| team_elo+none | unknown | 0 | — | — | — | — |
| team_elo+none | international=1 | 593 | 0.669988 | 0.236103 | 0.612142 | 0.065684 |
| team_elo+none | international=0 | 9189 | 0.631654 | 0.220433 | 0.640821 | 0.029426 |

team_elo+none − coin (paired log loss):

| Section | Rows | team_elo+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9782 | 0.633978 | 0.693147 | -0.059169 | [-0.067043, -0.051231] | yes |
| tier1 | 393 | 0.720566 | 0.693147 | 0.027419 | [-0.014208, 0.070436] | no |
| tier2 | 757 | 0.628460 | 0.693147 | -0.064687 | [-0.101593, -0.026522] | yes |
| tier3 | 8632 | 0.630520 | 0.693147 | -0.062627 | [-0.070670, -0.054447] | yes |
| international=1 | 593 | 0.669988 | 0.693147 | -0.023159 | [-0.057308, 0.010946] | no |
| international=0 | 9189 | 0.631654 | 0.693147 | -0.061493 | [-0.069102, -0.053778] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| team_elo+calibration | all | 9782 | 0.631718 | 0.220783 | 0.639082 | 0.023005 |
| team_elo+calibration | tier1 | 393 | 0.689942 | 0.247323 | 0.550891 | 0.039119 |
| team_elo+calibration | tier2 | 757 | 0.620059 | 0.215110 | 0.641347 | 0.064549 |
| team_elo+calibration | tier3 | 8632 | 0.630089 | 0.220072 | 0.642899 | 0.023858 |
| team_elo+calibration | unknown | 0 | — | — | — | — |
| team_elo+calibration | international=1 | 593 | 0.650946 | 0.229620 | 0.612142 | 0.026066 |
| team_elo+calibration | international=0 | 9189 | 0.630477 | 0.220213 | 0.640821 | 0.023571 |

team_elo+calibration − coin (paired log loss):

| Section | Rows | team_elo+calibration log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9782 | 0.631718 | 0.693147 | -0.061430 | [-0.068511, -0.054250] | yes |
| tier1 | 393 | 0.689942 | 0.693147 | -0.003205 | [-0.025642, 0.019372] | no |
| tier2 | 757 | 0.620059 | 0.693147 | -0.073088 | [-0.103881, -0.042310] | yes |
| tier3 | 8632 | 0.630089 | 0.693147 | -0.063058 | [-0.070434, -0.055523] | yes |
| international=1 | 593 | 0.650946 | 0.693147 | -0.042201 | [-0.064909, -0.017946] | yes |
| international=0 | 9189 | 0.630477 | 0.693147 | -0.062671 | [-0.069643, -0.055636] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko+none | all | 9782 | 0.577429 | 0.197589 | 0.685749 | 0.017135 |
| player_round_glicko+none | tier1 | 393 | 0.668939 | 0.233630 | 0.615776 | 0.045089 |
| player_round_glicko+none | tier2 | 757 | 0.547117 | 0.185880 | 0.730515 | 0.032326 |
| player_round_glicko+none | tier3 | 8632 | 0.575921 | 0.196975 | 0.685009 | 0.019128 |
| player_round_glicko+none | unknown | 0 | — | — | — | — |
| player_round_glicko+none | international=1 | 593 | 0.633702 | 0.219269 | 0.644182 | 0.031562 |
| player_round_glicko+none | international=0 | 9189 | 0.573797 | 0.196190 | 0.688432 | 0.017863 |

player_round_glicko+none − coin (paired log loss):

| Section | Rows | player_round_glicko+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9782 | 0.577429 | 0.693147 | -0.115718 | [-0.124056, -0.107018] | yes |
| tier1 | 393 | 0.668939 | 0.693147 | -0.024208 | [-0.063216, 0.016204] | no |
| tier2 | 757 | 0.547117 | 0.693147 | -0.146031 | [-0.178186, -0.113466] | yes |
| tier3 | 8632 | 0.575921 | 0.693147 | -0.117226 | [-0.126192, -0.108497] | yes |
| international=1 | 593 | 0.633702 | 0.693147 | -0.059445 | [-0.095951, -0.024109] | yes |
| international=0 | 9189 | 0.573797 | 0.693147 | -0.119350 | [-0.128181, -0.110426] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko+calibration | all | 9782 | 0.577029 | 0.197474 | 0.685749 | 0.014677 |
| player_round_glicko+calibration | tier1 | 393 | 0.663130 | 0.232550 | 0.615776 | 0.047564 |
| player_round_glicko+calibration | tier2 | 757 | 0.546954 | 0.185837 | 0.730515 | 0.032038 |
| player_round_glicko+calibration | tier3 | 8632 | 0.575746 | 0.196898 | 0.685009 | 0.016505 |
| player_round_glicko+calibration | unknown | 0 | — | — | — | — |
| player_round_glicko+calibration | international=1 | 593 | 0.630129 | 0.218593 | 0.644182 | 0.026433 |
| player_round_glicko+calibration | international=0 | 9189 | 0.573602 | 0.196111 | 0.688432 | 0.015175 |

player_round_glicko+calibration − coin (paired log loss):

| Section | Rows | player_round_glicko+calibration log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9782 | 0.577029 | 0.693147 | -0.116118 | [-0.124533, -0.107283] | yes |
| tier1 | 393 | 0.663130 | 0.693147 | -0.030017 | [-0.061603, 0.001801] | no |
| tier2 | 757 | 0.546954 | 0.693147 | -0.146193 | [-0.179109, -0.112811] | yes |
| tier3 | 8632 | 0.575746 | 0.693147 | -0.117401 | [-0.126530, -0.108383] | yes |
| international=1 | 593 | 0.630129 | 0.693147 | -0.063018 | [-0.096539, -0.030660] | yes |
| international=0 | 9189 | 0.573602 | 0.693147 | -0.119545 | [-0.128660, -0.110441] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko_rookie+none | all | 9782 | 0.569667 | 0.193665 | 0.695921 | 0.018178 |
| player_round_glicko_rookie+none | tier1 | 393 | 0.677440 | 0.233891 | 0.613232 | 0.056598 |
| player_round_glicko_rookie+none | tier2 | 757 | 0.538149 | 0.183109 | 0.730515 | 0.032434 |
| player_round_glicko_rookie+none | tier3 | 8632 | 0.567525 | 0.192759 | 0.696652 | 0.019736 |
| player_round_glicko_rookie+none | unknown | 0 | — | — | — | — |
| player_round_glicko_rookie+none | international=1 | 593 | 0.636911 | 0.218211 | 0.644182 | 0.043287 |
| player_round_glicko_rookie+none | international=0 | 9189 | 0.565328 | 0.192081 | 0.699260 | 0.017566 |

player_round_glicko_rookie+none − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9782 | 0.569667 | 0.693147 | -0.123480 | [-0.132521, -0.113648] | yes |
| tier1 | 393 | 0.677440 | 0.693147 | -0.015707 | [-0.061185, 0.032688] | no |
| tier2 | 757 | 0.538149 | 0.693147 | -0.154998 | [-0.188403, -0.121835] | yes |
| tier3 | 8632 | 0.567525 | 0.693147 | -0.125622 | [-0.135478, -0.115719] | yes |
| international=1 | 593 | 0.636911 | 0.693147 | -0.056236 | [-0.096337, -0.015288] | yes |
| international=0 | 9189 | 0.565328 | 0.693147 | -0.127819 | [-0.137958, -0.117703] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko_rookie+calibration | all | 9782 | 0.568787 | 0.193592 | 0.695921 | 0.021077 |
| player_round_glicko_rookie+calibration | tier1 | 393 | 0.666409 | 0.232571 | 0.613232 | 0.041159 |
| player_round_glicko_rookie+calibration | tier2 | 757 | 0.538367 | 0.183143 | 0.730515 | 0.031369 |
| player_round_glicko_rookie+calibration | tier3 | 8632 | 0.567011 | 0.192734 | 0.696652 | 0.024382 |
| player_round_glicko_rookie+calibration | unknown | 0 | — | — | — | — |
| player_round_glicko_rookie+calibration | international=1 | 593 | 0.628856 | 0.217249 | 0.644182 | 0.027911 |
| player_round_glicko_rookie+calibration | international=0 | 9189 | 0.564911 | 0.192065 | 0.699260 | 0.022109 |

player_round_glicko_rookie+calibration − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie+calibration log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9782 | 0.568787 | 0.693147 | -0.124360 | [-0.132927, -0.115064] | yes |
| tier1 | 393 | 0.666409 | 0.693147 | -0.026738 | [-0.059327, 0.008088] | no |
| tier2 | 757 | 0.538367 | 0.693147 | -0.154780 | [-0.187714, -0.122280] | yes |
| tier3 | 8632 | 0.567011 | 0.693147 | -0.126137 | [-0.135540, -0.116679] | yes |
| international=1 | 593 | 0.628856 | 0.693147 | -0.064292 | [-0.097594, -0.031669] | yes |
| international=0 | 9189 | 0.564911 | 0.693147 | -0.128236 | [-0.137938, -0.118546] | yes |

player_round_glicko − team_elo (paired log loss):

| Section | Rows | player_round_glicko log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9782 | 0.577429 | 0.633978 | -0.056549 | [-0.063107, -0.049410] | yes |

player_round_glicko_rookie − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9782 | 0.569667 | 0.633978 | -0.064311 | [-0.071964, -0.056331] | yes |

team_elo+none − team_elo (paired log loss):

| Section | Rows | team_elo+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9782 | 0.633978 | 0.633978 | 0.000000 | [0.000000, 0.000000] | no |

team_elo+calibration − team_elo (paired log loss):

| Section | Rows | team_elo+calibration log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9782 | 0.631718 | 0.633978 | -0.002261 | [-0.003575, -0.001011] | yes |

player_round_glicko+none − team_elo (paired log loss):

| Section | Rows | player_round_glicko+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9782 | 0.577429 | 0.633978 | -0.056549 | [-0.063107, -0.049410] | yes |

player_round_glicko+calibration − team_elo (paired log loss):

| Section | Rows | player_round_glicko+calibration log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9782 | 0.577029 | 0.633978 | -0.056950 | [-0.063572, -0.049760] | yes |

player_round_glicko_rookie+none − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9782 | 0.569667 | 0.633978 | -0.064311 | [-0.071964, -0.056331] | yes |

player_round_glicko_rookie+calibration − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie+calibration log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9782 | 0.568787 | 0.633978 | -0.065191 | [-0.072617, -0.057538] | yes |

player_round_glicko − player_round_glicko_rookie (paired log loss):

| Section | Rows | player_round_glicko log loss | player_round_glicko_rookie log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9782 | 0.577429 | 0.569667 | 0.007761 | [0.004919, 0.010381] | yes |
| tier1 | 393 | 0.668939 | 0.677440 | -0.008501 | [-0.021314, 0.001065] | no |
| tier2 | 757 | 0.547117 | 0.538149 | 0.008968 | [0.004852, 0.013169] | yes |
| tier3 | 8632 | 0.575921 | 0.567525 | 0.008396 | [0.005375, 0.011306] | yes |
| international=1 | 593 | 0.633702 | 0.636911 | -0.003209 | [-0.012770, 0.004735] | no |
| international=0 | 9189 | 0.573797 | 0.565328 | 0.008469 | [0.005483, 0.011254] | yes |

team_elo+none − player_round_glicko_rookie (paired log loss):

| Section | Rows | team_elo+none log loss | player_round_glicko_rookie log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9782 | 0.633978 | 0.569667 | 0.064311 | [0.056331, 0.071964] | yes |
| tier1 | 393 | 0.720566 | 0.677440 | 0.043126 | [0.001458, 0.081349] | yes |
| tier2 | 757 | 0.628460 | 0.538149 | 0.090312 | [0.057887, 0.121819] | yes |
| tier3 | 8632 | 0.630520 | 0.567525 | 0.062995 | [0.054732, 0.071189] | yes |
| international=1 | 593 | 0.669988 | 0.636911 | 0.033077 | [0.001627, 0.062694] | yes |
| international=0 | 9189 | 0.631654 | 0.565328 | 0.066326 | [0.058503, 0.074593] | yes |

team_elo+calibration − player_round_glicko_rookie (paired log loss):

| Section | Rows | team_elo+calibration log loss | player_round_glicko_rookie log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9782 | 0.631718 | 0.569667 | 0.062050 | [0.054398, 0.069482] | yes |
| tier1 | 393 | 0.689942 | 0.677440 | 0.012502 | [-0.027917, 0.048100] | no |
| tier2 | 757 | 0.620059 | 0.538149 | 0.081911 | [0.052475, 0.109990] | yes |
| tier3 | 8632 | 0.630089 | 0.567525 | 0.062564 | [0.054264, 0.070569] | yes |
| international=1 | 593 | 0.650946 | 0.636911 | 0.014035 | [-0.015884, 0.042532] | no |
| international=0 | 9189 | 0.630477 | 0.565328 | 0.065149 | [0.057686, 0.073262] | yes |

player_round_glicko+none − player_round_glicko_rookie (paired log loss):

| Section | Rows | player_round_glicko+none log loss | player_round_glicko_rookie log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9782 | 0.577429 | 0.569667 | 0.007761 | [0.004919, 0.010381] | yes |
| tier1 | 393 | 0.668939 | 0.677440 | -0.008501 | [-0.021314, 0.001065] | no |
| tier2 | 757 | 0.547117 | 0.538149 | 0.008968 | [0.004852, 0.013169] | yes |
| tier3 | 8632 | 0.575921 | 0.567525 | 0.008396 | [0.005375, 0.011306] | yes |
| international=1 | 593 | 0.633702 | 0.636911 | -0.003209 | [-0.012770, 0.004735] | no |
| international=0 | 9189 | 0.573797 | 0.565328 | 0.008469 | [0.005483, 0.011254] | yes |

player_round_glicko+calibration − player_round_glicko_rookie (paired log loss):

| Section | Rows | player_round_glicko+calibration log loss | player_round_glicko_rookie log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9782 | 0.577029 | 0.569667 | 0.007361 | [0.004519, 0.009920] | yes |
| tier1 | 393 | 0.663130 | 0.677440 | -0.014309 | [-0.033966, 0.001380] | no |
| tier2 | 757 | 0.546954 | 0.538149 | 0.008805 | [0.004772, 0.012910] | yes |
| tier3 | 8632 | 0.575746 | 0.567525 | 0.008221 | [0.005240, 0.011070] | yes |
| international=1 | 593 | 0.630129 | 0.636911 | -0.006783 | [-0.020488, 0.004754] | no |
| international=0 | 9189 | 0.573602 | 0.565328 | 0.008274 | [0.005339, 0.010960] | yes |

player_round_glicko_rookie+none − player_round_glicko_rookie (paired log loss):

| Section | Rows | player_round_glicko_rookie+none log loss | player_round_glicko_rookie log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9782 | 0.569667 | 0.569667 | 0.000000 | [0.000000, 0.000000] | no |
| tier1 | 393 | 0.677440 | 0.677440 | 0.000000 | [0.000000, 0.000000] | no |
| tier2 | 757 | 0.538149 | 0.538149 | 0.000000 | [0.000000, 0.000000] | no |
| tier3 | 8632 | 0.567525 | 0.567525 | 0.000000 | [0.000000, 0.000000] | no |
| international=1 | 593 | 0.636911 | 0.636911 | 0.000000 | [0.000000, 0.000000] | no |
| international=0 | 9189 | 0.565328 | 0.565328 | 0.000000 | [0.000000, 0.000000] | no |

player_round_glicko_rookie+calibration − player_round_glicko_rookie (paired log loss):

| Section | Rows | player_round_glicko_rookie+calibration log loss | player_round_glicko_rookie log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9782 | 0.568787 | 0.569667 | -0.000880 | [-0.001653, -0.000189] | yes |
| tier1 | 393 | 0.666409 | 0.677440 | -0.011030 | [-0.026000, 0.002012] | no |
| tier2 | 757 | 0.538367 | 0.538149 | 0.000218 | [-0.000608, 0.001016] | no |
| tier3 | 8632 | 0.567011 | 0.567525 | -0.000514 | [-0.001071, 0.000037] | no |
| international=1 | 593 | 0.628856 | 0.636911 | -0.008056 | [-0.017790, 0.000575] | no |
| international=0 | 9189 | 0.564911 | 0.565328 | -0.000417 | [-0.000924, 0.000102] | no |

### Series

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| coin | all | 6949 | 0.693147 | 0.250000 | 0.500000 | 0.032307 |
| coin | tier1 | 172 | 0.693147 | 0.250000 | 0.500000 | 0.000000 |
| coin | tier2 | 486 | 0.693147 | 0.250000 | 0.500000 | 0.037037 |
| coin | tier3 | 6291 | 0.693147 | 0.250000 | 0.500000 | 0.032825 |
| coin | unknown | 0 | — | — | — | — |
| coin | international=1 | 274 | 0.693147 | 0.250000 | 0.500000 | 0.036496 |
| coin | international=0 | 6675 | 0.693147 | 0.250000 | 0.500000 | 0.032135 |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| team_elo | all | 6949 | 0.630108 | 0.219654 | 0.645273 | 0.030278 |
| team_elo | tier1 | 172 | 0.687887 | 0.245217 | 0.584302 | 0.086202 |
| team_elo | tier2 | 486 | 0.619725 | 0.210992 | 0.659465 | 0.078869 |
| team_elo | tier3 | 6291 | 0.629330 | 0.219624 | 0.645843 | 0.026990 |
| team_elo | unknown | 0 | — | — | — | — |
| team_elo | international=1 | 274 | 0.638133 | 0.223854 | 0.627737 | 0.065156 |
| team_elo | international=0 | 6675 | 0.629778 | 0.219482 | 0.645993 | 0.029647 |

team_elo − coin (paired log loss):

| Section | Rows | team_elo log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6949 | 0.630108 | 0.693147 | -0.063039 | [-0.072171, -0.054646] | yes |
| tier1 | 172 | 0.687887 | 0.693147 | -0.005260 | [-0.070741, 0.059371] | no |
| tier2 | 486 | 0.619725 | 0.693147 | -0.073422 | [-0.117855, -0.026908] | yes |
| tier3 | 6291 | 0.629330 | 0.693147 | -0.063817 | [-0.072379, -0.054575] | yes |
| international=1 | 274 | 0.638133 | 0.693147 | -0.055015 | [-0.101340, -0.002647] | yes |
| international=0 | 6675 | 0.629778 | 0.693147 | -0.063369 | [-0.071985, -0.054614] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko | all | 6949 | 0.563146 | 0.191436 | 0.702619 | 0.019904 |
| player_round_glicko | tier1 | 172 | 0.622423 | 0.213534 | 0.680233 | 0.067745 |
| player_round_glicko | tier2 | 486 | 0.534850 | 0.180526 | 0.742798 | 0.045101 |
| player_round_glicko | tier3 | 6291 | 0.563711 | 0.191674 | 0.700127 | 0.022684 |
| player_round_glicko | unknown | 0 | — | — | — | — |
| player_round_glicko | international=1 | 274 | 0.592051 | 0.203298 | 0.689781 | 0.069850 |
| player_round_glicko | international=0 | 6675 | 0.561959 | 0.190949 | 0.703146 | 0.020501 |

player_round_glicko − coin (paired log loss):

| Section | Rows | player_round_glicko log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6949 | 0.563146 | 0.693147 | -0.130001 | [-0.139940, -0.119890] | yes |
| tier1 | 172 | 0.622423 | 0.693147 | -0.070724 | [-0.134446, 0.003309] | no |
| tier2 | 486 | 0.534850 | 0.693147 | -0.158297 | [-0.196380, -0.117926] | yes |
| tier3 | 6291 | 0.563711 | 0.693147 | -0.129436 | [-0.139726, -0.118997] | yes |
| international=1 | 274 | 0.592051 | 0.693147 | -0.101096 | [-0.157355, -0.045186] | yes |
| international=0 | 6675 | 0.561959 | 0.693147 | -0.131188 | [-0.140774, -0.120436] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko_rookie | all | 6949 | 0.552086 | 0.185911 | 0.713916 | 0.018564 |
| player_round_glicko_rookie | tier1 | 172 | 0.626719 | 0.213182 | 0.674419 | 0.046264 |
| player_round_glicko_rookie | tier2 | 486 | 0.525397 | 0.177670 | 0.736626 | 0.031157 |
| player_round_glicko_rookie | tier3 | 6291 | 0.552107 | 0.185802 | 0.713241 | 0.020957 |
| player_round_glicko_rookie | unknown | 0 | — | — | — | — |
| player_round_glicko_rookie | international=1 | 274 | 0.583029 | 0.198492 | 0.689781 | 0.038599 |
| player_round_glicko_rookie | international=0 | 6675 | 0.550816 | 0.185395 | 0.714906 | 0.019138 |

player_round_glicko_rookie − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6949 | 0.552086 | 0.693147 | -0.141061 | [-0.152614, -0.129700] | yes |
| tier1 | 172 | 0.626719 | 0.693147 | -0.066428 | [-0.133890, 0.012246] | no |
| tier2 | 486 | 0.525397 | 0.693147 | -0.167750 | [-0.206376, -0.127725] | yes |
| tier3 | 6291 | 0.552107 | 0.693147 | -0.141040 | [-0.152816, -0.129302] | yes |
| international=1 | 274 | 0.583029 | 0.693147 | -0.110118 | [-0.168157, -0.050738] | yes |
| international=0 | 6675 | 0.550816 | 0.693147 | -0.142331 | [-0.153298, -0.130611] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| team_elo+none | all | 6949 | 0.630108 | 0.219654 | 0.645273 | 0.030278 |
| team_elo+none | tier1 | 172 | 0.687887 | 0.245217 | 0.584302 | 0.086202 |
| team_elo+none | tier2 | 486 | 0.619725 | 0.210992 | 0.659465 | 0.078869 |
| team_elo+none | tier3 | 6291 | 0.629330 | 0.219624 | 0.645843 | 0.026990 |
| team_elo+none | unknown | 0 | — | — | — | — |
| team_elo+none | international=1 | 274 | 0.638133 | 0.223854 | 0.627737 | 0.065156 |
| team_elo+none | international=0 | 6675 | 0.629778 | 0.219482 | 0.645993 | 0.029647 |

team_elo+none − coin (paired log loss):

| Section | Rows | team_elo+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6949 | 0.630108 | 0.693147 | -0.063039 | [-0.072171, -0.054646] | yes |
| tier1 | 172 | 0.687887 | 0.693147 | -0.005260 | [-0.070741, 0.059371] | no |
| tier2 | 486 | 0.619725 | 0.693147 | -0.073422 | [-0.117855, -0.026908] | yes |
| tier3 | 6291 | 0.629330 | 0.693147 | -0.063817 | [-0.072379, -0.054575] | yes |
| international=1 | 274 | 0.638133 | 0.693147 | -0.055015 | [-0.101340, -0.002647] | yes |
| international=0 | 6675 | 0.629778 | 0.693147 | -0.063369 | [-0.071985, -0.054614] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| team_elo+calibration | all | 6949 | 0.628573 | 0.219291 | 0.645273 | 0.027358 |
| team_elo+calibration | tier1 | 172 | 0.670458 | 0.238547 | 0.584302 | 0.028801 |
| team_elo+calibration | tier2 | 486 | 0.610598 | 0.209709 | 0.659465 | 0.077043 |
| team_elo+calibration | tier3 | 6291 | 0.628816 | 0.219505 | 0.645843 | 0.028921 |
| team_elo+calibration | unknown | 0 | — | — | — | — |
| team_elo+calibration | international=1 | 274 | 0.626821 | 0.219566 | 0.627737 | 0.044975 |
| team_elo+calibration | international=0 | 6675 | 0.628645 | 0.219280 | 0.645993 | 0.027119 |

team_elo+calibration − coin (paired log loss):

| Section | Rows | team_elo+calibration log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6949 | 0.628573 | 0.693147 | -0.064574 | [-0.072987, -0.056885] | yes |
| tier1 | 172 | 0.670458 | 0.693147 | -0.022689 | [-0.062269, 0.018143] | no |
| tier2 | 486 | 0.610598 | 0.693147 | -0.082549 | [-0.120790, -0.043493] | yes |
| tier3 | 6291 | 0.628816 | 0.693147 | -0.064331 | [-0.072616, -0.055456] | yes |
| international=1 | 274 | 0.626821 | 0.693147 | -0.066326 | [-0.098465, -0.028890] | yes |
| international=0 | 6675 | 0.628645 | 0.693147 | -0.064502 | [-0.072663, -0.056241] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko+none | all | 6949 | 0.563146 | 0.191436 | 0.702619 | 0.019904 |
| player_round_glicko+none | tier1 | 172 | 0.622423 | 0.213534 | 0.680233 | 0.067745 |
| player_round_glicko+none | tier2 | 486 | 0.534850 | 0.180526 | 0.742798 | 0.045101 |
| player_round_glicko+none | tier3 | 6291 | 0.563711 | 0.191674 | 0.700127 | 0.022684 |
| player_round_glicko+none | unknown | 0 | — | — | — | — |
| player_round_glicko+none | international=1 | 274 | 0.592051 | 0.203298 | 0.689781 | 0.069850 |
| player_round_glicko+none | international=0 | 6675 | 0.561959 | 0.190949 | 0.703146 | 0.020501 |

player_round_glicko+none − coin (paired log loss):

| Section | Rows | player_round_glicko+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6949 | 0.563146 | 0.693147 | -0.130001 | [-0.139940, -0.119890] | yes |
| tier1 | 172 | 0.622423 | 0.693147 | -0.070724 | [-0.134446, 0.003309] | no |
| tier2 | 486 | 0.534850 | 0.693147 | -0.158297 | [-0.196380, -0.117926] | yes |
| tier3 | 6291 | 0.563711 | 0.693147 | -0.129436 | [-0.139726, -0.118997] | yes |
| international=1 | 274 | 0.592051 | 0.693147 | -0.101096 | [-0.157355, -0.045186] | yes |
| international=0 | 6675 | 0.561959 | 0.693147 | -0.131188 | [-0.140774, -0.120436] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko+calibration | all | 6949 | 0.562958 | 0.191370 | 0.702619 | 0.017949 |
| player_round_glicko+calibration | tier1 | 172 | 0.620598 | 0.214232 | 0.680233 | 0.062048 |
| player_round_glicko+calibration | tier2 | 486 | 0.535130 | 0.180627 | 0.742798 | 0.043787 |
| player_round_glicko+calibration | tier3 | 6291 | 0.563532 | 0.191574 | 0.700127 | 0.019912 |
| player_round_glicko+calibration | unknown | 0 | — | — | — | — |
| player_round_glicko+calibration | international=1 | 274 | 0.590842 | 0.203718 | 0.689781 | 0.037115 |
| player_round_glicko+calibration | international=0 | 6675 | 0.561814 | 0.190863 | 0.703146 | 0.017759 |

player_round_glicko+calibration − coin (paired log loss):

| Section | Rows | player_round_glicko+calibration log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6949 | 0.562958 | 0.693147 | -0.130189 | [-0.140312, -0.119973] | yes |
| tier1 | 172 | 0.620598 | 0.693147 | -0.072549 | [-0.122968, -0.015976] | yes |
| tier2 | 486 | 0.535130 | 0.693147 | -0.158017 | [-0.196273, -0.116728] | yes |
| tier3 | 6291 | 0.563532 | 0.693147 | -0.129615 | [-0.140103, -0.119064] | yes |
| international=1 | 274 | 0.590842 | 0.693147 | -0.102305 | [-0.151369, -0.050585] | yes |
| international=0 | 6675 | 0.561814 | 0.693147 | -0.131333 | [-0.141164, -0.120357] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko_rookie+none | all | 6949 | 0.552086 | 0.185911 | 0.713916 | 0.018564 |
| player_round_glicko_rookie+none | tier1 | 172 | 0.626719 | 0.213182 | 0.674419 | 0.046264 |
| player_round_glicko_rookie+none | tier2 | 486 | 0.525397 | 0.177670 | 0.736626 | 0.031157 |
| player_round_glicko_rookie+none | tier3 | 6291 | 0.552107 | 0.185802 | 0.713241 | 0.020957 |
| player_round_glicko_rookie+none | unknown | 0 | — | — | — | — |
| player_round_glicko_rookie+none | international=1 | 274 | 0.583029 | 0.198492 | 0.689781 | 0.038599 |
| player_round_glicko_rookie+none | international=0 | 6675 | 0.550816 | 0.185395 | 0.714906 | 0.019138 |

player_round_glicko_rookie+none − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6949 | 0.552086 | 0.693147 | -0.141061 | [-0.152614, -0.129700] | yes |
| tier1 | 172 | 0.626719 | 0.693147 | -0.066428 | [-0.133890, 0.012246] | no |
| tier2 | 486 | 0.525397 | 0.693147 | -0.167750 | [-0.206376, -0.127725] | yes |
| tier3 | 6291 | 0.552107 | 0.693147 | -0.141040 | [-0.152816, -0.129302] | yes |
| international=1 | 274 | 0.583029 | 0.693147 | -0.110118 | [-0.168157, -0.050738] | yes |
| international=0 | 6675 | 0.550816 | 0.693147 | -0.142331 | [-0.153298, -0.130611] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko_rookie+calibration | all | 6949 | 0.551487 | 0.185930 | 0.713916 | 0.022003 |
| player_round_glicko_rookie+calibration | tier1 | 172 | 0.624287 | 0.214427 | 0.674419 | 0.060975 |
| player_round_glicko_rookie+calibration | tier2 | 486 | 0.524600 | 0.177411 | 0.736626 | 0.044566 |
| player_round_glicko_rookie+calibration | tier3 | 6291 | 0.551574 | 0.185809 | 0.713241 | 0.023092 |
| player_round_glicko_rookie+calibration | unknown | 0 | — | — | — | — |
| player_round_glicko_rookie+calibration | international=1 | 274 | 0.581790 | 0.199391 | 0.689781 | 0.042516 |
| player_round_glicko_rookie+calibration | international=0 | 6675 | 0.550243 | 0.185378 | 0.714906 | 0.022125 |

player_round_glicko_rookie+calibration − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie+calibration log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6949 | 0.551487 | 0.693147 | -0.141660 | [-0.152818, -0.130797] | yes |
| tier1 | 172 | 0.624287 | 0.693147 | -0.068860 | [-0.121627, -0.007758] | yes |
| tier2 | 486 | 0.524600 | 0.693147 | -0.168547 | [-0.206456, -0.128548] | yes |
| tier3 | 6291 | 0.551574 | 0.693147 | -0.141573 | [-0.152963, -0.130196] | yes |
| international=1 | 274 | 0.581790 | 0.693147 | -0.111357 | [-0.161910, -0.060249] | yes |
| international=0 | 6675 | 0.550243 | 0.693147 | -0.142904 | [-0.153673, -0.131670] | yes |

player_round_glicko − team_elo (paired log loss):

| Section | Rows | player_round_glicko log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6949 | 0.563146 | 0.630108 | -0.066962 | [-0.075284, -0.058376] | yes |

player_round_glicko_rookie − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6949 | 0.552086 | 0.630108 | -0.078022 | [-0.087580, -0.068567] | yes |

team_elo+none − team_elo (paired log loss):

| Section | Rows | team_elo+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6949 | 0.630108 | 0.630108 | 0.000000 | [0.000000, 0.000000] | no |

team_elo+calibration − team_elo (paired log loss):

| Section | Rows | team_elo+calibration log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6949 | 0.628573 | 0.630108 | -0.001535 | [-0.002698, -0.000349] | yes |

player_round_glicko+none − team_elo (paired log loss):

| Section | Rows | player_round_glicko+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6949 | 0.563146 | 0.630108 | -0.066962 | [-0.075284, -0.058376] | yes |

player_round_glicko+calibration − team_elo (paired log loss):

| Section | Rows | player_round_glicko+calibration log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6949 | 0.562958 | 0.630108 | -0.067149 | [-0.075560, -0.058431] | yes |

player_round_glicko_rookie+none − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6949 | 0.552086 | 0.630108 | -0.078022 | [-0.087580, -0.068567] | yes |

player_round_glicko_rookie+calibration − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie+calibration log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6949 | 0.551487 | 0.630108 | -0.078621 | [-0.087723, -0.069357] | yes |

player_round_glicko − player_round_glicko_rookie (paired log loss):

| Section | Rows | player_round_glicko log loss | player_round_glicko_rookie log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6949 | 0.563146 | 0.552086 | 0.011060 | [0.007499, 0.014673] | yes |
| tier1 | 172 | 0.622423 | 0.626719 | -0.004295 | [-0.018245, 0.005292] | no |
| tier2 | 486 | 0.534850 | 0.525397 | 0.009454 | [0.003564, 0.015233] | yes |
| tier3 | 6291 | 0.563711 | 0.552107 | 0.011604 | [0.007724, 0.015370] | yes |
| international=1 | 274 | 0.592051 | 0.583029 | 0.009022 | [-0.003602, 0.020802] | no |
| international=0 | 6675 | 0.561959 | 0.550816 | 0.011143 | [0.007474, 0.014827] | yes |

team_elo+none − player_round_glicko_rookie (paired log loss):

| Section | Rows | team_elo+none log loss | player_round_glicko_rookie log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6949 | 0.630108 | 0.552086 | 0.078022 | [0.068567, 0.087580] | yes |
| tier1 | 172 | 0.687887 | 0.626719 | 0.061168 | [0.002309, 0.118304] | yes |
| tier2 | 486 | 0.619725 | 0.525397 | 0.094328 | [0.052612, 0.135172] | yes |
| tier3 | 6291 | 0.629330 | 0.552107 | 0.077223 | [0.067352, 0.086728] | yes |
| international=1 | 274 | 0.638133 | 0.583029 | 0.055104 | [0.011150, 0.098780] | yes |
| international=0 | 6675 | 0.629778 | 0.550816 | 0.078962 | [0.068665, 0.088252] | yes |

team_elo+calibration − player_round_glicko_rookie (paired log loss):

| Section | Rows | team_elo+calibration log loss | player_round_glicko_rookie log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6949 | 0.628573 | 0.552086 | 0.076487 | [0.066986, 0.086168] | yes |
| tier1 | 172 | 0.670458 | 0.626719 | 0.043739 | [-0.012237, 0.094764] | no |
| tier2 | 486 | 0.610598 | 0.525397 | 0.085201 | [0.046842, 0.121415] | yes |
| tier3 | 6291 | 0.628816 | 0.552107 | 0.076709 | [0.066880, 0.086154] | yes |
| international=1 | 274 | 0.626821 | 0.583029 | 0.043793 | [0.002034, 0.084639] | yes |
| international=0 | 6675 | 0.628645 | 0.550816 | 0.077829 | [0.067654, 0.087050] | yes |

player_round_glicko+none − player_round_glicko_rookie (paired log loss):

| Section | Rows | player_round_glicko+none log loss | player_round_glicko_rookie log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6949 | 0.563146 | 0.552086 | 0.011060 | [0.007499, 0.014673] | yes |
| tier1 | 172 | 0.622423 | 0.626719 | -0.004295 | [-0.018245, 0.005292] | no |
| tier2 | 486 | 0.534850 | 0.525397 | 0.009454 | [0.003564, 0.015233] | yes |
| tier3 | 6291 | 0.563711 | 0.552107 | 0.011604 | [0.007724, 0.015370] | yes |
| international=1 | 274 | 0.592051 | 0.583029 | 0.009022 | [-0.003602, 0.020802] | no |
| international=0 | 6675 | 0.561959 | 0.550816 | 0.011143 | [0.007474, 0.014827] | yes |

player_round_glicko+calibration − player_round_glicko_rookie (paired log loss):

| Section | Rows | player_round_glicko+calibration log loss | player_round_glicko_rookie log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6949 | 0.562958 | 0.552086 | 0.010872 | [0.007305, 0.014413] | yes |
| tier1 | 172 | 0.620598 | 0.626719 | -0.006121 | [-0.031263, 0.012938] | no |
| tier2 | 486 | 0.535130 | 0.525397 | 0.009733 | [0.004017, 0.015372] | yes |
| tier3 | 6291 | 0.563532 | 0.552107 | 0.011425 | [0.007541, 0.015096] | yes |
| international=1 | 274 | 0.590842 | 0.583029 | 0.007813 | [-0.010245, 0.023439] | no |
| international=0 | 6675 | 0.561814 | 0.550816 | 0.010998 | [0.007331, 0.014610] | yes |

player_round_glicko_rookie+none − player_round_glicko_rookie (paired log loss):

| Section | Rows | player_round_glicko_rookie+none log loss | player_round_glicko_rookie log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6949 | 0.552086 | 0.552086 | 0.000000 | [0.000000, 0.000000] | no |
| tier1 | 172 | 0.626719 | 0.626719 | 0.000000 | [0.000000, 0.000000] | no |
| tier2 | 486 | 0.525397 | 0.525397 | 0.000000 | [0.000000, 0.000000] | no |
| tier3 | 6291 | 0.552107 | 0.552107 | 0.000000 | [0.000000, 0.000000] | no |
| international=1 | 274 | 0.583029 | 0.583029 | 0.000000 | [0.000000, 0.000000] | no |
| international=0 | 6675 | 0.550816 | 0.550816 | 0.000000 | [0.000000, 0.000000] | no |

player_round_glicko_rookie+calibration − player_round_glicko_rookie (paired log loss):

| Section | Rows | player_round_glicko_rookie+calibration log loss | player_round_glicko_rookie log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6949 | 0.551487 | 0.552086 | -0.000599 | [-0.001300, 0.000076] | no |
| tier1 | 172 | 0.624287 | 0.626719 | -0.002431 | [-0.021260, 0.012953] | no |
| tier2 | 486 | 0.524600 | 0.525397 | -0.000796 | [-0.002201, 0.000553] | no |
| tier3 | 6291 | 0.551574 | 0.552107 | -0.000534 | [-0.001123, 0.000053] | no |
| international=1 | 274 | 0.581790 | 0.583029 | -0.001239 | [-0.012641, 0.008643] | no |
| international=0 | 6675 | 0.550243 | 0.550816 | -0.000573 | [-0.001206, -0.000000] | yes |

## Stage 2 — validation vs Kalshi

### team_elo: Kalshi comparison and returns



#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 244 | 0.684225 | 0.590569 | 0.093656 [0.037375, 0.152259] | yes |
| series | tier1 | 101 | 0.722236 | 0.622685 | 0.099551 [0.015488, 0.187749] | yes |
| series | tier2 | 143 | 0.657378 | 0.567886 | 0.089492 [0.016344, 0.175118] | yes |
| series | tier3 | 0 | — | — | — | — |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 101 | 0.722236 | 0.622685 | 0.099551 [0.015488, 0.187749] | yes |
| series | international=0 | 143 | 0.657378 | 0.567886 | 0.089492 [0.016344, 0.175118] | yes |
| map | all | 109 | 0.784133 | 0.699578 | 0.084554 [0.031742, 0.145359] | yes |
| map | tier1 | 102 | 0.745519 | 0.670407 | 0.075112 [0.017849, 0.133182] | yes |
| map | tier2 | 7 | 1.346790 | 1.124640 | 0.222150 [-0.012787, 0.531904] | no |
| map | tier3 | 0 | — | — | — | — |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 102 | 0.745519 | 0.670407 | 0.075112 [0.017849, 0.133182] | yes |
| map | international=0 | 7 | 1.346790 | 1.124640 | 0.222150 [-0.012787, 0.531904] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 190 | 190 | 0.1258 | -5.55% [-22.83%, 11.94%] | $4.18 | 0.084× | 94.59% | $5.03 | 113 (77 unfilled) | -12.28% [-30.68%, 7.07%] | $9.91 |
| series | tier1 | 81 | 81 | 0.1445 | 1.34% [-30.99%, 36.05%] | $14.79 | 0.296× | 71.70% | $5.03 | 46 (35 unfilled) | -13.21% [-46.03%, 19.04%] | $27.47 |
| series | tier2 | 109 | 109 | 0.1119 | -10.73% [-28.16%, 8.09%] | $14.84 | 0.297× | 86.95% | $7.39 | 67 (42 unfilled) | -11.64% [-32.30%, 9.44%] | $21.81 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 81 | 81 | 0.1445 | 1.34% [-30.99%, 36.05%] | $14.79 | 0.296× | 71.70% | $5.03 | 46 (35 unfilled) | -13.21% [-46.03%, 19.04%] | $27.47 |
| series | international=0 | 109 | 109 | 0.1119 | -10.73% [-28.16%, 8.09%] | $14.84 | 0.297× | 86.95% | $7.39 | 67 (42 unfilled) | -11.64% [-32.30%, 9.44%] | $21.81 |
| map | all | 96 | 50 | 0.1009 | -6.88% [-26.72%, 12.90%] | $19.85 | 0.397× | 61.04% | $4.73 | 8 (88 unfilled) | -33.74% [-81.30%, -3.79%] | $42.98 |
| map | tier1 | 91 | 46 | 0.0997 | -4.03% [-24.17%, 17.50%] | $27.10 | 0.542× | 46.81% | $2.49 | 5 (86 unfilled) | -34.77% [-100.00%, 9.64%] | $47.77 |
| map | tier2 | 5 | 4 | 0.1227 | -58.93% [-100.00%, -12.20%] | $36.69 | 0.734× | 26.62% | $4.91 | 3 (2 unfilled) | -32.02% [-100.00%, 2.29%] | $44.99 |
| map | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 91 | 46 | 0.0997 | -4.03% [-24.17%, 17.50%] | $27.10 | 0.542× | 46.81% | $2.49 | 5 (86 unfilled) | -34.77% [-100.00%, 9.64%] | $47.77 |
| map | international=0 | 5 | 4 | 0.1227 | -58.93% [-100.00%, -12.20%] | $36.69 | 0.734× | 26.62% | $4.91 | 3 (2 unfilled) | -32.02% [-100.00%, 2.29%] | $44.99 |
| series+map | all | 286 | 201 | 0.1174 | -6.00% [-20.60%, 8.78%] | $2.29 | 0.046× | 96.92% | $5.03 | 121 (165 unfilled) | -13.70% [-31.75%, 4.23%] | $8.91 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 217 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-01 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 16 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | map | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-03 | series | 65 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | series | 67 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | map | 62 | 1.000000 | 0.000000 | unfitted |
| 2026-05 | series | 108 | 0.881396 | -0.054852 | fitted |
| 2026-05 | map | 69 | 1.000000 | 0.000000 | unfitted |
| 2026-06 | series | 144 | 0.800928 | -0.127974 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 136 | 0.593501 | 0.588044 | 0.005457 [-0.011242, 0.019861] | no |
| series | tier1 | 36 | 0.656825 | 0.664138 | -0.007313 [-0.021027, 0.005847] | no |
| series | tier2 | 100 | 0.570705 | 0.560650 | 0.010055 [-0.011796, 0.028857] | no |
| series | tier3 | 0 | — | — | — | — |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 36 | 0.656825 | 0.664138 | -0.007313 [-0.021027, 0.005847] | no |
| series | international=0 | 100 | 0.570705 | 0.560650 | 0.010055 [-0.011796, 0.028857] | no |
| map | all | 0 | — | — | — | — |
| map | tier1 | 0 | — | — | — | — |
| map | tier2 | 0 | — | — | — | — |
| map | tier3 | 0 | — | — | — | — |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 0 | — | — | — | — |
| map | international=0 | 0 | — | — | — | — |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 59 | 59 | 0.0213 | -21.40% [-58.13%, 20.38%] | $44.38 | 0.888× | 29.62% | $5.47 | 32 (27 unfilled) | -2.60% [-51.02%, 56.24%] | $63.42 |
| series | tier1 | 1 | 1 | 0.0061 | -100.00% [-100.00%, -100.00%] | $49.63 | 0.993× | 0.74% | $0.35 | 0 (1 unfilled) | — | $49.63 |
| series | tier2 | 58 | 58 | 0.0215 | -20.04% [-55.58%, 19.62%] | $44.72 | 0.894× | 29.63% | $5.51 | 32 (26 unfilled) | -2.60% [-51.02%, 56.24%] | $63.89 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 1 | 1 | 0.0061 | -100.00% [-100.00%, -100.00%] | $49.63 | 0.993× | 0.74% | $0.35 | 0 (1 unfilled) | — | $49.63 |
| series | international=0 | 58 | 58 | 0.0215 | -20.04% [-55.58%, 19.62%] | $44.72 | 0.894× | 29.63% | $5.51 | 32 (26 unfilled) | -2.60% [-51.02%, 56.24%] | $63.89 |
| map | all | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier2 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=0 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series+map | all | 59 | 59 | 0.0213 | -21.40% [-58.13%, 20.38%] | $44.38 | 0.888× | 29.62% | $5.47 | 32 (27 unfilled) | -2.60% [-51.02%, 56.24%] | $63.42 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-02 | 62 | 0.713120 | — | 0.656833 | 10.39% (58), $48.17 | — | 4 (54 unfilled) | -18.10% [-100.00%, 15.34%] | $49.27 | — | — | — |
| map | 2026-04 | 7 | 1.346790 | — | 1.124640 | -58.93% (5), $36.69 | — | 3 (2 unfilled) | -32.02% [-100.00%, 2.29%] | $44.99 | — | — | — |
| map | 2026-05 | 40 | 0.795738 | — | 0.691447 | -29.36% (33), $28.15 | — | 1 (32 unfilled) | -100.00% [-100.00%, -100.00%] | $48.48 | — | — | — |
| series | 2026-01 | 16 | 0.819716 | — | 0.612205 | -3.24% (15), $38.75 | — | 10 (5 unfilled) | 20.71% [-53.50%, 98.54%] | $59.66 | — | — | — |
| series | 2026-02 | 49 | 0.679152 | — | 0.595651 | 15.69% (39), $34.91 | — | 18 (21 unfilled) | -32.00% [-74.14%, 15.22%] | $29.41 | — | — | — |
| series | 2026-03 | 2 | 1.488339 | — | 1.445686 | -100.00% (1), $47.64 | — | 0 (1 unfilled) | — | $50.00 | — | — | — |
| series | 2026-04 | 41 | 0.676297 | — | 0.542714 | -3.22% (33), $36.08 | — | 20 (13 unfilled) | -17.46% [-58.95%, 28.49%] | $36.27 | — | — | — |
| series | 2026-05 | 36 | 0.737553 | 0.656825 | 0.664138 | -16.85% (27), $27.35 | -100.00% (1), $49.63 | 18 (9 unfilled) | -13.32% [-65.67%, 48.93%] | $38.45 | 0 (1 unfilled) | — | $49.63 |
| series | 2026-06 | 100 | 0.633001 | 0.570705 | 0.560650 | -12.89% (75), $21.61 | -20.04% (58), $44.72 | 47 (28 unfilled) | -9.14% [-32.99%, 14.33%] | $31.19 | 32 (26 unfilled) | -2.60% [-51.02%, 56.24%] | $63.89 |

### player_round_glicko: Kalshi comparison and returns



#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 244 | 0.615834 | 0.590569 | 0.025265 [-0.013262, 0.061695] | no |
| series | tier1 | 101 | 0.631553 | 0.622685 | 0.008868 [-0.055777, 0.076522] | no |
| series | tier2 | 143 | 0.604732 | 0.567886 | 0.036846 [-0.004699, 0.079842] | no |
| series | tier3 | 0 | — | — | — | — |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 101 | 0.631553 | 0.622685 | 0.008868 [-0.055777, 0.076522] | no |
| series | international=0 | 143 | 0.604732 | 0.567886 | 0.036846 [-0.004699, 0.079842] | no |
| map | all | 109 | 0.700893 | 0.699578 | 0.001314 [-0.077334, 0.061827] | no |
| map | tier1 | 102 | 0.694104 | 0.670407 | 0.023697 [-0.018296, 0.070541] | no |
| map | tier2 | 7 | 0.799813 | 1.124640 | -0.324828 [-1.398870, 0.218825] | no |
| map | tier3 | 0 | — | — | — | — |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 102 | 0.694104 | 0.670407 | 0.023697 [-0.018296, 0.070541] | no |
| map | international=0 | 7 | 0.799813 | 1.124640 | -0.324828 [-1.398870, 0.218825] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 182 | 182 | 0.0954 | -0.12% [-19.52%, 21.93%] | $5.00 | 0.100× | 94.25% | $8.23 | 105 (77 unfilled) | -9.14% [-30.48%, 13.01%] | $17.86 |
| series | tier1 | 84 | 84 | 0.1086 | 10.82% [-21.62%, 44.97%] | $27.43 | 0.549× | 68.90% | $8.23 | 49 (35 unfilled) | -0.87% [-33.45%, 33.42%] | $35.11 |
| series | tier2 | 98 | 98 | 0.0841 | -9.52% [-34.69%, 16.98%] | $9.23 | 0.185× | 89.82% | $8.62 | 56 (42 unfilled) | -16.36% [-43.80%, 12.35%] | $27.15 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 84 | 84 | 0.1086 | 10.82% [-21.62%, 44.97%] | $27.43 | 0.549× | 68.90% | $8.23 | 49 (35 unfilled) | -0.87% [-33.45%, 33.42%] | $35.11 |
| series | international=0 | 98 | 98 | 0.0841 | -9.52% [-34.69%, 16.98%] | $9.23 | 0.185× | 89.82% | $8.62 | 56 (42 unfilled) | -16.36% [-43.80%, 12.35%] | $27.15 |
| map | all | 78 | 42 | 0.0897 | 19.86% [-16.47%, 65.33%] | $103.21 | 2.064× | 30.75% | $13.07 | 5 (73 unfilled) | -40.74% [-100.00%, -0.47%] | $45.96 |
| map | tier1 | 72 | 37 | 0.0813 | 3.94% [-23.06%, 31.04%] | $54.21 | 1.084× | 30.77% | $6.18 | 2 (70 unfilled) | -34.72% [-100.00%, 32.49%] | $47.86 |
| map | tier2 | 6 | 5 | 0.1903 | 210.34% [-72.41%, 710.15%] | $95.14 | 1.903× | 11.92% | $10.37 | 3 (3 unfilled) | -44.74% [-100.00%, -16.71%] | $47.81 |
| map | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 72 | 37 | 0.0813 | 3.94% [-23.06%, 31.04%] | $54.21 | 1.084× | 30.77% | $6.18 | 2 (70 unfilled) | -34.72% [-100.00%, 32.49%] | $47.86 |
| map | international=0 | 6 | 5 | 0.1903 | 210.34% [-72.41%, 710.15%] | $95.14 | 1.903× | 11.92% | $10.37 | 3 (3 unfilled) | -44.74% [-100.00%, -16.71%] | $47.81 |
| series+map | all | 260 | 183 | 0.0937 | 5.86% [-13.88%, 26.63%] | $9.14 | 0.183× | 88.06% | $7.06 | 110 (150 unfilled) | -10.57% [-29.71%, 10.72%] | $20.37 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 217 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-01 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 16 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | map | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-03 | series | 65 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | series | 67 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | map | 62 | 1.000000 | 0.000000 | unfitted |
| 2026-05 | series | 108 | 1.158089 | 0.494527 | fitted |
| 2026-05 | map | 69 | 1.000000 | 0.000000 | unfitted |
| 2026-06 | series | 144 | 1.013746 | 0.396973 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 136 | 0.597529 | 0.588044 | 0.009485 [-0.006557, 0.025070] | no |
| series | tier1 | 36 | 0.670642 | 0.664138 | 0.006504 [-0.037326, 0.052026] | no |
| series | tier2 | 100 | 0.571208 | 0.560650 | 0.010558 [-0.003851, 0.024425] | no |
| series | tier3 | 0 | — | — | — | — |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 36 | 0.670642 | 0.664138 | 0.006504 [-0.037326, 0.052026] | no |
| series | international=0 | 100 | 0.571208 | 0.560650 | 0.010558 [-0.003851, 0.024425] | no |
| map | all | 0 | — | — | — | — |
| map | tier1 | 0 | — | — | — | — |
| map | tier2 | 0 | — | — | — | — |
| map | tier3 | 0 | — | — | — | — |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 0 | — | — | — | — |
| map | international=0 | 0 | — | — | — | — |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 43 | 43 | 0.0293 | -24.24% [-51.83%, 7.01%] | $31.19 | 0.624× | 49.31% | $5.81 | 25 (18 unfilled) | -17.18% [-48.76%, 16.40%] | $40.35 |
| series | tier1 | 17 | 17 | 0.0414 | -16.16% [-56.46%, 27.63%] | $40.08 | 0.802× | 32.63% | $5.81 | 14 (3 unfilled) | -29.15% [-68.09%, 8.85%] | $38.21 |
| series | tier2 | 26 | 26 | 0.0214 | -29.49% [-66.01%, 13.13%] | $38.90 | 0.778× | 34.22% | $5.09 | 11 (15 unfilled) | -2.10% [-57.83%, 54.30%] | $53.45 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 17 | 17 | 0.0414 | -16.16% [-56.46%, 27.63%] | $40.08 | 0.802× | 32.63% | $5.81 | 14 (3 unfilled) | -29.15% [-68.09%, 8.85%] | $38.21 |
| series | international=0 | 26 | 26 | 0.0214 | -29.49% [-66.01%, 13.13%] | $38.90 | 0.778× | 34.22% | $5.09 | 11 (15 unfilled) | -2.10% [-57.83%, 54.30%] | $53.45 |
| map | all | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier2 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=0 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series+map | all | 43 | 43 | 0.0293 | -24.24% [-51.83%, 7.01%] | $31.19 | 0.624× | 49.31% | $5.81 | 25 (18 unfilled) | -17.18% [-48.76%, 16.40%] | $40.35 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-02 | 62 | 0.667047 | — | 0.656833 | 10.38% (44), $62.99 | — | 1 (43 unfilled) | -100.00% [-100.00%, -100.00%] | $47.50 | — | — | — |
| map | 2026-04 | 7 | 0.799813 | — | 1.124640 | 210.34% (6), $95.14 | — | 3 (3 unfilled) | -44.74% [-100.00%, -16.71%] | $47.81 | — | — | — |
| map | 2026-05 | 40 | 0.736043 | — | 0.691447 | -6.30% (28), $43.01 | — | 1 (27 unfilled) | 32.49% [32.49%, 32.49%] | $50.36 | — | — | — |
| series | 2026-01 | 16 | 0.669652 | — | 0.612205 | 18.04% (10), $53.65 | — | 6 (4 unfilled) | 56.20% [-32.52%, 142.11%] | $65.97 | — | — | — |
| series | 2026-02 | 49 | 0.588486 | — | 0.595651 | 11.64% (45), $28.25 | — | 20 (25 unfilled) | -24.35% [-69.08%, 25.66%] | $36.26 | — | — | — |
| series | 2026-03 | 2 | 0.854873 | — | 1.445686 | 396.52% (1), $69.89 | — | 0 (1 unfilled) | — | $50.00 | — | — | — |
| series | 2026-04 | 41 | 0.602815 | — | 0.542714 | -9.76% (30), $31.72 | — | 20 (10 unfilled) | -9.45% [-52.93%, 36.65%] | $41.76 | — | — | — |
| series | 2026-05 | 36 | 0.673238 | 0.670642 | 0.664138 | 7.02% (29), $45.25 | -16.16% (17), $40.08 | 23 (6 unfilled) | 4.79% [-42.19%, 57.07%] | $35.57 | 14 (3 unfilled) | -29.15% [-68.09%, 8.85%] | $38.21 |
| series | 2026-06 | 100 | 0.600515 | 0.571208 | 0.560650 | -15.59% (67), $10.42 | -29.49% (26), $38.90 | 36 (31 unfilled) | -20.23% [-53.11%, 13.76%] | $34.17 | 11 (15 unfilled) | -2.10% [-57.83%, 54.30%] | $53.45 |

### player_round_glicko_rookie: Kalshi comparison and returns



#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 244 | 0.610734 | 0.590569 | 0.020165 [-0.016807, 0.054495] | no |
| series | tier1 | 101 | 0.628997 | 0.622685 | 0.006312 [-0.056735, 0.071966] | no |
| series | tier2 | 143 | 0.597835 | 0.567886 | 0.029949 [-0.009164, 0.070879] | no |
| series | tier3 | 0 | — | — | — | — |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 101 | 0.628997 | 0.622685 | 0.006312 [-0.056735, 0.071966] | no |
| series | international=0 | 143 | 0.597835 | 0.567886 | 0.029949 [-0.009164, 0.070879] | no |
| map | all | 109 | 0.696002 | 0.699578 | -0.003576 [-0.081092, 0.055619] | no |
| map | tier1 | 102 | 0.688062 | 0.670407 | 0.017655 [-0.024516, 0.062717] | no |
| map | tier2 | 7 | 0.811698 | 1.124640 | -0.312943 [-1.387120, 0.206737] | no |
| map | tier3 | 0 | — | — | — | — |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 102 | 0.688062 | 0.670407 | 0.017655 [-0.024516, 0.062717] | no |
| map | international=0 | 7 | 0.811698 | 1.124640 | -0.312943 [-1.387120, 0.206737] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 176 | 176 | 0.0930 | -1.51% [-21.55%, 21.32%] | $7.66 | 0.153× | 89.10% | $6.64 | 103 (73 unfilled) | -6.82% [-26.51%, 14.84%] | $21.48 |
| series | tier1 | 80 | 80 | 0.1085 | 9.26% [-23.14%, 48.67%] | $28.27 | 0.565× | 63.83% | $6.64 | 48 (32 unfilled) | -1.92% [-33.33%, 31.42%] | $34.59 |
| series | tier2 | 96 | 96 | 0.0800 | -10.53% [-33.90%, 14.90%] | $13.72 | 0.274× | 83.73% | $8.02 | 55 (41 unfilled) | -11.09% [-38.21%, 17.60%] | $34.27 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 80 | 80 | 0.1085 | 9.26% [-23.14%, 48.67%] | $28.27 | 0.565× | 63.83% | $6.64 | 48 (32 unfilled) | -1.92% [-33.33%, 31.42%] | $34.59 |
| series | international=0 | 96 | 96 | 0.0800 | -10.53% [-33.90%, 14.90%] | $13.72 | 0.274× | 83.73% | $8.02 | 55 (41 unfilled) | -11.09% [-38.21%, 17.60%] | $34.27 |
| map | all | 81 | 43 | 0.0836 | 19.44% [-17.02%, 62.77%] | $98.96 | 1.979× | 31.10% | $12.33 | 5 (76 unfilled) | -40.74% [-100.00%, -0.47%] | $45.94 |
| map | tier1 | 76 | 39 | 0.0754 | 7.10% [-19.55%, 33.32%] | $55.72 | 1.114× | 31.14% | $6.25 | 2 (74 unfilled) | -34.72% [-100.00%, 32.49%] | $47.86 |
| map | tier2 | 5 | 4 | 0.2091 | 206.70% [-100.00%, 906.04%] | $88.72 | 1.774× | 11.97% | $9.68 | 3 (2 unfilled) | -44.74% [-100.00%, -16.71%] | $47.78 |
| map | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 76 | 39 | 0.0754 | 7.10% [-19.55%, 33.32%] | $55.72 | 1.114× | 31.14% | $6.25 | 2 (74 unfilled) | -34.72% [-100.00%, 32.49%] | $47.86 |
| map | international=0 | 5 | 4 | 0.2091 | 206.70% [-100.00%, 906.04%] | $88.72 | 1.774× | 11.97% | $9.68 | 3 (2 unfilled) | -44.74% [-100.00%, -16.71%] | $47.78 |
| series+map | all | 257 | 181 | 0.0900 | 5.08% [-14.62%, 26.68%] | $12.29 | 0.246× | 83.33% | $6.04 | 108 (149 unfilled) | -8.38% [-27.62%, 12.07%] | $21.95 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 217 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-01 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 16 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | map | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-03 | series | 65 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | series | 67 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | map | 62 | 1.000000 | 0.000000 | unfitted |
| 2026-05 | series | 108 | 1.140959 | 0.482882 | fitted |
| 2026-05 | map | 69 | 1.000000 | 0.000000 | unfitted |
| 2026-06 | series | 144 | 1.016536 | 0.421528 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 136 | 0.594718 | 0.588044 | 0.006674 [-0.009039, 0.021713] | no |
| series | tier1 | 36 | 0.663225 | 0.664138 | -0.000913 [-0.038786, 0.038588] | no |
| series | tier2 | 100 | 0.570056 | 0.560650 | 0.009406 [-0.006083, 0.024120] | no |
| series | tier3 | 0 | — | — | — | — |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 36 | 0.663225 | 0.664138 | -0.000913 [-0.038786, 0.038588] | no |
| series | international=0 | 100 | 0.570056 | 0.560650 | 0.009406 [-0.006083, 0.024120] | no |
| map | all | 0 | — | — | — | — |
| map | tier1 | 0 | — | — | — | — |
| map | tier2 | 0 | — | — | — | — |
| map | tier3 | 0 | — | — | — | — |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 0 | — | — | — | — |
| map | international=0 | 0 | — | — | — | — |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 49 | 49 | 0.0249 | -15.65% [-43.79%, 15.24%] | $35.50 | 0.710× | 44.27% | $5.94 | 30 (19 unfilled) | -12.09% [-45.35%, 24.16%] | $45.86 |
| series | tier1 | 17 | 17 | 0.0336 | -14.09% [-54.11%, 29.87%] | $43.83 | 0.877× | 27.92% | $5.94 | 14 (3 unfilled) | -26.63% [-64.89%, 11.50%] | $42.37 |
| series | tier2 | 32 | 32 | 0.0203 | -16.47% [-51.17%, 25.10%] | $40.45 | 0.809× | 31.05% | $5.37 | 16 (16 unfilled) | 0.54% [-54.31%, 61.63%] | $54.46 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 17 | 17 | 0.0336 | -14.09% [-54.11%, 29.87%] | $43.83 | 0.877× | 27.92% | $5.94 | 14 (3 unfilled) | -26.63% [-64.89%, 11.50%] | $42.37 |
| series | international=0 | 32 | 32 | 0.0203 | -16.47% [-51.17%, 25.10%] | $40.45 | 0.809× | 31.05% | $5.37 | 16 (16 unfilled) | 0.54% [-54.31%, 61.63%] | $54.46 |
| map | all | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier2 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=0 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series+map | all | 49 | 49 | 0.0249 | -15.65% [-43.79%, 15.24%] | $35.50 | 0.710× | 44.27% | $5.94 | 30 (19 unfilled) | -12.09% [-45.35%, 24.16%] | $45.86 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-02 | 62 | 0.663027 | — | 0.656833 | 14.83% (48), $63.70 | — | 1 (47 unfilled) | -100.00% [-100.00%, -100.00%] | $47.50 | — | — | — |
| map | 2026-04 | 7 | 0.811698 | — | 1.124640 | 206.70% (5), $88.72 | — | 3 (2 unfilled) | -44.74% [-100.00%, -16.71%] | $47.78 | — | — | — |
| map | 2026-05 | 40 | 0.726865 | — | 0.691447 | -6.30% (28), $43.72 | — | 1 (27 unfilled) | 32.49% [32.49%, 32.49%] | $50.36 | — | — | — |
| series | 2026-01 | 16 | 0.692581 | — | 0.612205 | -1.56% (12), $45.83 | — | 8 (4 unfilled) | 17.05% [-72.05%, 104.69%] | $58.52 | — | — | — |
| series | 2026-02 | 49 | 0.586653 | — | 0.595651 | 9.66% (42), $30.42 | — | 20 (22 unfilled) | -24.35% [-69.08%, 25.66%] | $37.87 | — | — | — |
| series | 2026-03 | 2 | 0.947654 | — | 1.445686 | 396.52% (1), $69.89 | — | 0 (1 unfilled) | — | $50.00 | — | — | — |
| series | 2026-04 | 41 | 0.586744 | — | 0.542714 | -5.70% (29), $33.86 | — | 19 (10 unfilled) | -3.24% [-50.21%, 46.11%] | $44.41 | — | — | — |
| series | 2026-05 | 36 | 0.658372 | 0.663225 | 0.664138 | 13.65% (26), $50.73 | -14.09% (17), $43.83 | 20 (6 unfilled) | 13.09% [-39.87%, 75.38%] | $38.37 | 14 (3 unfilled) | -26.63% [-64.89%, 11.50%] | $42.37 |
| series | 2026-06 | 100 | 0.595386 | 0.570056 | 0.560650 | -18.97% (66), $14.44 | -16.47% (32), $40.45 | 36 (30 unfilled) | -15.29% [-46.60%, 20.53%] | $39.66 | 16 (16 unfilled) | 0.54% [-54.31%, 61.63%] | $54.46 |

### team_elo+none: Kalshi comparison and returns

none

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 244 | 0.684225 | 0.590569 | 0.093656 [0.037375, 0.152259] | yes |
| series | tier1 | 101 | 0.722236 | 0.622685 | 0.099551 [0.015488, 0.187749] | yes |
| series | tier2 | 143 | 0.657378 | 0.567886 | 0.089492 [0.016344, 0.175118] | yes |
| series | tier3 | 0 | — | — | — | — |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 101 | 0.722236 | 0.622685 | 0.099551 [0.015488, 0.187749] | yes |
| series | international=0 | 143 | 0.657378 | 0.567886 | 0.089492 [0.016344, 0.175118] | yes |
| map | all | 109 | 0.784133 | 0.699578 | 0.084554 [0.031742, 0.145359] | yes |
| map | tier1 | 102 | 0.745519 | 0.670407 | 0.075112 [0.017849, 0.133182] | yes |
| map | tier2 | 7 | 1.346790 | 1.124640 | 0.222150 [-0.012787, 0.531904] | no |
| map | tier3 | 0 | — | — | — | — |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 102 | 0.745519 | 0.670407 | 0.075112 [0.017849, 0.133182] | yes |
| map | international=0 | 7 | 1.346790 | 1.124640 | 0.222150 [-0.012787, 0.531904] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 190 | 190 | 0.1258 | -5.55% [-22.83%, 11.94%] | $4.18 | 0.084× | 94.59% | $5.03 | 113 (77 unfilled) | -12.28% [-30.68%, 7.07%] | $9.91 |
| series | tier1 | 81 | 81 | 0.1445 | 1.34% [-30.99%, 36.05%] | $14.79 | 0.296× | 71.70% | $5.03 | 46 (35 unfilled) | -13.21% [-46.03%, 19.04%] | $27.47 |
| series | tier2 | 109 | 109 | 0.1119 | -10.73% [-28.16%, 8.09%] | $14.84 | 0.297× | 86.95% | $7.39 | 67 (42 unfilled) | -11.64% [-32.30%, 9.44%] | $21.81 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 81 | 81 | 0.1445 | 1.34% [-30.99%, 36.05%] | $14.79 | 0.296× | 71.70% | $5.03 | 46 (35 unfilled) | -13.21% [-46.03%, 19.04%] | $27.47 |
| series | international=0 | 109 | 109 | 0.1119 | -10.73% [-28.16%, 8.09%] | $14.84 | 0.297× | 86.95% | $7.39 | 67 (42 unfilled) | -11.64% [-32.30%, 9.44%] | $21.81 |
| map | all | 96 | 50 | 0.1009 | -6.88% [-26.72%, 12.90%] | $19.85 | 0.397× | 61.04% | $4.73 | 8 (88 unfilled) | -33.74% [-81.30%, -3.79%] | $42.98 |
| map | tier1 | 91 | 46 | 0.0997 | -4.03% [-24.17%, 17.50%] | $27.10 | 0.542× | 46.81% | $2.49 | 5 (86 unfilled) | -34.77% [-100.00%, 9.64%] | $47.77 |
| map | tier2 | 5 | 4 | 0.1227 | -58.93% [-100.00%, -12.20%] | $36.69 | 0.734× | 26.62% | $4.91 | 3 (2 unfilled) | -32.02% [-100.00%, 2.29%] | $44.99 |
| map | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 91 | 46 | 0.0997 | -4.03% [-24.17%, 17.50%] | $27.10 | 0.542× | 46.81% | $2.49 | 5 (86 unfilled) | -34.77% [-100.00%, 9.64%] | $47.77 |
| map | international=0 | 5 | 4 | 0.1227 | -58.93% [-100.00%, -12.20%] | $36.69 | 0.734× | 26.62% | $4.91 | 3 (2 unfilled) | -32.02% [-100.00%, 2.29%] | $44.99 |
| series+map | all | 286 | 201 | 0.1174 | -6.00% [-20.60%, 8.78%] | $2.29 | 0.046× | 96.92% | $5.03 | 121 (165 unfilled) | -13.70% [-31.75%, 4.23%] | $8.91 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 217 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-01 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 16 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | map | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-03 | series | 65 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | series | 67 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | map | 62 | 1.000000 | 0.000000 | unfitted |
| 2026-05 | series | 108 | 0.881396 | -0.054852 | fitted |
| 2026-05 | map | 69 | 1.000000 | 0.000000 | unfitted |
| 2026-06 | series | 144 | 0.800928 | -0.127974 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 136 | 0.593501 | 0.588044 | 0.005457 [-0.011242, 0.019861] | no |
| series | tier1 | 36 | 0.656825 | 0.664138 | -0.007313 [-0.021027, 0.005847] | no |
| series | tier2 | 100 | 0.570705 | 0.560650 | 0.010055 [-0.011796, 0.028857] | no |
| series | tier3 | 0 | — | — | — | — |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 36 | 0.656825 | 0.664138 | -0.007313 [-0.021027, 0.005847] | no |
| series | international=0 | 100 | 0.570705 | 0.560650 | 0.010055 [-0.011796, 0.028857] | no |
| map | all | 0 | — | — | — | — |
| map | tier1 | 0 | — | — | — | — |
| map | tier2 | 0 | — | — | — | — |
| map | tier3 | 0 | — | — | — | — |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 0 | — | — | — | — |
| map | international=0 | 0 | — | — | — | — |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 59 | 59 | 0.0213 | -21.40% [-58.13%, 20.38%] | $44.38 | 0.888× | 29.62% | $5.47 | 32 (27 unfilled) | -2.60% [-51.02%, 56.24%] | $63.42 |
| series | tier1 | 1 | 1 | 0.0061 | -100.00% [-100.00%, -100.00%] | $49.63 | 0.993× | 0.74% | $0.35 | 0 (1 unfilled) | — | $49.63 |
| series | tier2 | 58 | 58 | 0.0215 | -20.04% [-55.58%, 19.62%] | $44.72 | 0.894× | 29.63% | $5.51 | 32 (26 unfilled) | -2.60% [-51.02%, 56.24%] | $63.89 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 1 | 1 | 0.0061 | -100.00% [-100.00%, -100.00%] | $49.63 | 0.993× | 0.74% | $0.35 | 0 (1 unfilled) | — | $49.63 |
| series | international=0 | 58 | 58 | 0.0215 | -20.04% [-55.58%, 19.62%] | $44.72 | 0.894× | 29.63% | $5.51 | 32 (26 unfilled) | -2.60% [-51.02%, 56.24%] | $63.89 |
| map | all | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier2 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=0 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series+map | all | 59 | 59 | 0.0213 | -21.40% [-58.13%, 20.38%] | $44.38 | 0.888× | 29.62% | $5.47 | 32 (27 unfilled) | -2.60% [-51.02%, 56.24%] | $63.42 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-02 | 62 | 0.713120 | — | 0.656833 | 10.39% (58), $48.17 | — | 4 (54 unfilled) | -18.10% [-100.00%, 15.34%] | $49.27 | — | — | — |
| map | 2026-04 | 7 | 1.346790 | — | 1.124640 | -58.93% (5), $36.69 | — | 3 (2 unfilled) | -32.02% [-100.00%, 2.29%] | $44.99 | — | — | — |
| map | 2026-05 | 40 | 0.795738 | — | 0.691447 | -29.36% (33), $28.15 | — | 1 (32 unfilled) | -100.00% [-100.00%, -100.00%] | $48.48 | — | — | — |
| series | 2026-01 | 16 | 0.819716 | — | 0.612205 | -3.24% (15), $38.75 | — | 10 (5 unfilled) | 20.71% [-53.50%, 98.54%] | $59.66 | — | — | — |
| series | 2026-02 | 49 | 0.679152 | — | 0.595651 | 15.69% (39), $34.91 | — | 18 (21 unfilled) | -32.00% [-74.14%, 15.22%] | $29.41 | — | — | — |
| series | 2026-03 | 2 | 1.488339 | — | 1.445686 | -100.00% (1), $47.64 | — | 0 (1 unfilled) | — | $50.00 | — | — | — |
| series | 2026-04 | 41 | 0.676297 | — | 0.542714 | -3.22% (33), $36.08 | — | 20 (13 unfilled) | -17.46% [-58.95%, 28.49%] | $36.27 | — | — | — |
| series | 2026-05 | 36 | 0.737553 | 0.656825 | 0.664138 | -16.85% (27), $27.35 | -100.00% (1), $49.63 | 18 (9 unfilled) | -13.32% [-65.67%, 48.93%] | $38.45 | 0 (1 unfilled) | — | $49.63 |
| series | 2026-06 | 100 | 0.633001 | 0.570705 | 0.560650 | -12.89% (75), $21.61 | -20.04% (58), $44.72 | 47 (28 unfilled) | -9.14% [-32.99%, 14.33%] | $31.19 | 32 (26 unfilled) | -2.60% [-51.02%, 56.24%] | $63.89 |

### team_elo+calibration: Kalshi comparison and returns

calibration: ridge=4; tier1/online=0: rows=1092, T=0.3468; tier1/online=1: rows=567, T=0.7962; tier2/online=0: rows=253, T=1.0000; tier2/online=1: rows=4454, T=0.7831; tier3/online=0: rows=3215, T=0.9227; tier3/online=1: rows=40549, T=0.9141; unknown/online=0: rows=23, T=1.0000

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 244 | 0.659458 | 0.590569 | 0.068889 [0.022816, 0.118475] | yes |
| series | tier1 | 101 | 0.689326 | 0.622685 | 0.066641 [-0.013239, 0.142449] | no |
| series | tier2 | 143 | 0.638362 | 0.567886 | 0.070476 [0.012430, 0.137790] | yes |
| series | tier3 | 0 | — | — | — | — |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 101 | 0.689326 | 0.622685 | 0.066641 [-0.013239, 0.142449] | no |
| series | international=0 | 143 | 0.638362 | 0.567886 | 0.070476 [0.012430, 0.137790] | yes |
| map | all | 109 | 0.711744 | 0.699578 | 0.012166 [-0.031433, 0.055427] | no |
| map | tier1 | 102 | 0.679892 | 0.670407 | 0.009485 [-0.032052, 0.052818] | no |
| map | tier2 | 7 | 1.175879 | 1.124640 | 0.051239 [-0.286197, 0.322909] | no |
| map | tier3 | 0 | — | — | — | — |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 102 | 0.679892 | 0.670407 | 0.009485 [-0.032052, 0.052818] | no |
| map | international=0 | 7 | 1.175879 | 1.124640 | 0.051239 [-0.286197, 0.322909] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 189 | 189 | 0.1222 | 0.86% [-20.16%, 22.47%] | $5.29 | 0.106× | 93.54% | $4.95 | 116 (73 unfilled) | -4.72% [-25.93%, 17.93%] | $22.35 |
| series | tier1 | 87 | 87 | 0.1452 | -0.85% [-32.37%, 35.90%] | $17.88 | 0.358× | 74.84% | $4.95 | 52 (35 unfilled) | 0.08% [-33.93%, 35.42%] | $53.85 |
| series | tier2 | 102 | 102 | 0.1025 | 2.32% [-23.39%, 29.28%] | $15.47 | 0.309× | 87.40% | $7.30 | 64 (38 unfilled) | -8.64% [-36.00%, 21.74%] | $19.26 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 87 | 87 | 0.1452 | -0.85% [-32.37%, 35.90%] | $17.88 | 0.358× | 74.84% | $4.95 | 52 (35 unfilled) | 0.08% [-33.93%, 35.42%] | $53.85 |
| series | international=0 | 102 | 102 | 0.1025 | 2.32% [-23.39%, 29.28%] | $15.47 | 0.309× | 87.40% | $7.30 | 64 (38 unfilled) | -8.64% [-36.00%, 21.74%] | $19.26 |
| map | all | 83 | 44 | 0.0799 | 18.77% [-18.10%, 65.73%] | $47.87 | 0.957× | 42.69% | $6.23 | 8 (75 unfilled) | -48.09% [-100.00%, -15.60%] | $41.34 |
| map | tier1 | 77 | 39 | 0.0801 | 7.64% [-20.68%, 37.78%] | $54.56 | 1.091× | 34.64% | $6.03 | 5 (72 unfilled) | -57.67% [-100.00%, -8.68%] | $41.72 |
| map | tier2 | 6 | 5 | 0.0775 | 162.61% [-100.00%, 710.15%] | $43.82 | 0.876× | 19.00% | $4.91 | 3 (3 unfilled) | -32.02% [-100.00%, 2.29%] | $49.24 |
| map | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 77 | 39 | 0.0801 | 7.64% [-20.68%, 37.78%] | $54.56 | 1.091× | 34.64% | $6.03 | 5 (72 unfilled) | -57.67% [-100.00%, -8.68%] | $41.72 |
| map | international=0 | 6 | 5 | 0.0775 | 162.61% [-100.00%, 710.15%] | $43.82 | 0.876× | 19.00% | $4.91 | 3 (3 unfilled) | -32.02% [-100.00%, 2.29%] | $49.24 |
| series+map | all | 272 | 191 | 0.1093 | 6.32% [-14.53%, 27.42%] | $3.52 | 0.070× | 95.66% | $4.95 | 124 (148 unfilled) | -7.52% [-27.87%, 14.93%] | $14.44 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 217 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-01 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 16 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | map | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-03 | series | 65 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | series | 67 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | map | 62 | 1.000000 | 0.000000 | unfitted |
| 2026-05 | series | 108 | 0.831747 | -0.110293 | fitted |
| 2026-05 | map | 69 | 1.000000 | 0.000000 | unfitted |
| 2026-06 | series | 144 | 0.741750 | -0.159693 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 136 | 0.595099 | 0.588044 | 0.007054 [-0.010700, 0.022311] | no |
| series | tier1 | 36 | 0.657993 | 0.664138 | -0.006145 [-0.017590, 0.004813] | no |
| series | tier2 | 100 | 0.572457 | 0.560650 | 0.011806 [-0.011673, 0.031814] | no |
| series | tier3 | 0 | — | — | — | — |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 36 | 0.657993 | 0.664138 | -0.006145 [-0.017590, 0.004813] | no |
| series | international=0 | 100 | 0.572457 | 0.560650 | 0.011806 [-0.011673, 0.031814] | no |
| map | all | 0 | — | — | — | — |
| map | tier1 | 0 | — | — | — | — |
| map | tier2 | 0 | — | — | — | — |
| map | tier3 | 0 | — | — | — | — |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 0 | — | — | — | — |
| map | international=0 | 0 | — | — | — | — |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 61 | 61 | 0.0254 | -23.99% [-60.05%, 12.64%] | $38.15 | 0.763× | 35.90% | $5.01 | 34 (27 unfilled) | -8.35% [-56.90%, 48.18%] | $59.71 |
| series | tier1 | 1 | 1 | 0.0033 | -100.00% [-100.00%, -100.00%] | $49.79 | 0.996× | 0.41% | $0.19 | 0 (1 unfilled) | — | $49.79 |
| series | tier2 | 60 | 60 | 0.0258 | -22.72% [-57.80%, 16.01%] | $38.30 | 0.766× | 35.92% | $5.03 | 34 (26 unfilled) | -8.35% [-56.90%, 48.18%] | $59.94 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 1 | 1 | 0.0033 | -100.00% [-100.00%, -100.00%] | $49.79 | 0.996× | 0.41% | $0.19 | 0 (1 unfilled) | — | $49.79 |
| series | international=0 | 60 | 60 | 0.0258 | -22.72% [-57.80%, 16.01%] | $38.30 | 0.766× | 35.92% | $5.03 | 34 (26 unfilled) | -8.35% [-56.90%, 48.18%] | $59.94 |
| map | all | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier2 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=0 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series+map | all | 61 | 61 | 0.0254 | -23.99% [-60.05%, 12.64%] | $38.15 | 0.763× | 35.90% | $5.01 | 34 (27 unfilled) | -8.35% [-56.90%, 48.18%] | $59.71 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-02 | 62 | 0.658334 | — | 0.656833 | 13.39% (50), $63.39 | — | 4 (46 unfilled) | -46.96% [-100.00%, 6.84%] | $46.35 | — | — | — |
| map | 2026-04 | 7 | 1.175879 | — | 1.124640 | 162.61% (6), $43.82 | — | 3 (3 unfilled) | -32.02% [-100.00%, 2.29%] | $49.24 | — | — | — |
| map | 2026-05 | 40 | 0.713307 | — | 0.691447 | -3.06% (27), $43.05 | — | 1 (26 unfilled) | -100.00% [-100.00%, -100.00%] | $45.00 | — | — | — |
| series | 2026-01 | 16 | 0.802707 | — | 0.612205 | -3.24% (15), $39.03 | — | 10 (5 unfilled) | 20.71% [-53.50%, 98.54%] | $59.52 | — | — | — |
| series | 2026-02 | 49 | 0.650199 | — | 0.595651 | 2.56% (42), $26.33 | — | 20 (22 unfilled) | -15.18% [-64.00%, 36.23%] | $42.89 | — | — | — |
| series | 2026-03 | 2 | 1.287350 | — | 1.445686 | 293.06% (2), $54.85 | — | 1 (1 unfilled) | 188.60% [188.60%, 188.60%] | $51.02 | — | — | — |
| series | 2026-04 | 41 | 0.663231 | — | 0.542714 | -23.26% (35), $26.69 | — | 22 (13 unfilled) | -42.32% [-79.37%, -2.15%] | $27.49 | — | — | — |
| series | 2026-05 | 36 | 0.692191 | 0.657993 | 0.664138 | -4.43% (30), $43.65 | -100.00% (1), $49.79 | 22 (8 unfilled) | 4.64% [-51.77%, 67.63%] | $48.75 | 0 (1 unfilled) | — | $49.79 |
| series | 2026-06 | 100 | 0.615186 | 0.572457 | 0.560650 | 7.14% (65), $26.47 | -22.72% (60), $38.30 | 41 (24 unfilled) | 4.72% [-30.49%, 47.04%] | $36.54 | 34 (26 unfilled) | -8.35% [-56.90%, 48.18%] | $59.94 |

### player_round_glicko+none: Kalshi comparison and returns

none

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 244 | 0.615834 | 0.590569 | 0.025265 [-0.013262, 0.061695] | no |
| series | tier1 | 101 | 0.631553 | 0.622685 | 0.008868 [-0.055777, 0.076522] | no |
| series | tier2 | 143 | 0.604732 | 0.567886 | 0.036846 [-0.004699, 0.079842] | no |
| series | tier3 | 0 | — | — | — | — |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 101 | 0.631553 | 0.622685 | 0.008868 [-0.055777, 0.076522] | no |
| series | international=0 | 143 | 0.604732 | 0.567886 | 0.036846 [-0.004699, 0.079842] | no |
| map | all | 109 | 0.700893 | 0.699578 | 0.001314 [-0.077334, 0.061827] | no |
| map | tier1 | 102 | 0.694104 | 0.670407 | 0.023697 [-0.018296, 0.070541] | no |
| map | tier2 | 7 | 0.799813 | 1.124640 | -0.324828 [-1.398870, 0.218825] | no |
| map | tier3 | 0 | — | — | — | — |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 102 | 0.694104 | 0.670407 | 0.023697 [-0.018296, 0.070541] | no |
| map | international=0 | 7 | 0.799813 | 1.124640 | -0.324828 [-1.398870, 0.218825] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 182 | 182 | 0.0954 | -0.12% [-19.52%, 21.93%] | $5.00 | 0.100× | 94.25% | $8.23 | 105 (77 unfilled) | -9.14% [-30.48%, 13.01%] | $17.86 |
| series | tier1 | 84 | 84 | 0.1086 | 10.82% [-21.62%, 44.97%] | $27.43 | 0.549× | 68.90% | $8.23 | 49 (35 unfilled) | -0.87% [-33.45%, 33.42%] | $35.11 |
| series | tier2 | 98 | 98 | 0.0841 | -9.52% [-34.69%, 16.98%] | $9.23 | 0.185× | 89.82% | $8.62 | 56 (42 unfilled) | -16.36% [-43.80%, 12.35%] | $27.15 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 84 | 84 | 0.1086 | 10.82% [-21.62%, 44.97%] | $27.43 | 0.549× | 68.90% | $8.23 | 49 (35 unfilled) | -0.87% [-33.45%, 33.42%] | $35.11 |
| series | international=0 | 98 | 98 | 0.0841 | -9.52% [-34.69%, 16.98%] | $9.23 | 0.185× | 89.82% | $8.62 | 56 (42 unfilled) | -16.36% [-43.80%, 12.35%] | $27.15 |
| map | all | 78 | 42 | 0.0897 | 19.86% [-16.47%, 65.33%] | $103.21 | 2.064× | 30.75% | $13.07 | 5 (73 unfilled) | -40.74% [-100.00%, -0.47%] | $45.96 |
| map | tier1 | 72 | 37 | 0.0813 | 3.94% [-23.06%, 31.04%] | $54.21 | 1.084× | 30.77% | $6.18 | 2 (70 unfilled) | -34.72% [-100.00%, 32.49%] | $47.86 |
| map | tier2 | 6 | 5 | 0.1903 | 210.34% [-72.41%, 710.15%] | $95.14 | 1.903× | 11.92% | $10.37 | 3 (3 unfilled) | -44.74% [-100.00%, -16.71%] | $47.81 |
| map | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 72 | 37 | 0.0813 | 3.94% [-23.06%, 31.04%] | $54.21 | 1.084× | 30.77% | $6.18 | 2 (70 unfilled) | -34.72% [-100.00%, 32.49%] | $47.86 |
| map | international=0 | 6 | 5 | 0.1903 | 210.34% [-72.41%, 710.15%] | $95.14 | 1.903× | 11.92% | $10.37 | 3 (3 unfilled) | -44.74% [-100.00%, -16.71%] | $47.81 |
| series+map | all | 260 | 183 | 0.0937 | 5.86% [-13.88%, 26.63%] | $9.14 | 0.183× | 88.06% | $7.06 | 110 (150 unfilled) | -10.57% [-29.71%, 10.72%] | $20.37 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 217 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-01 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 16 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | map | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-03 | series | 65 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | series | 67 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | map | 62 | 1.000000 | 0.000000 | unfitted |
| 2026-05 | series | 108 | 1.158089 | 0.494527 | fitted |
| 2026-05 | map | 69 | 1.000000 | 0.000000 | unfitted |
| 2026-06 | series | 144 | 1.013746 | 0.396973 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 136 | 0.597529 | 0.588044 | 0.009485 [-0.006557, 0.025070] | no |
| series | tier1 | 36 | 0.670642 | 0.664138 | 0.006504 [-0.037326, 0.052026] | no |
| series | tier2 | 100 | 0.571208 | 0.560650 | 0.010558 [-0.003851, 0.024425] | no |
| series | tier3 | 0 | — | — | — | — |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 36 | 0.670642 | 0.664138 | 0.006504 [-0.037326, 0.052026] | no |
| series | international=0 | 100 | 0.571208 | 0.560650 | 0.010558 [-0.003851, 0.024425] | no |
| map | all | 0 | — | — | — | — |
| map | tier1 | 0 | — | — | — | — |
| map | tier2 | 0 | — | — | — | — |
| map | tier3 | 0 | — | — | — | — |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 0 | — | — | — | — |
| map | international=0 | 0 | — | — | — | — |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 43 | 43 | 0.0293 | -24.24% [-51.83%, 7.01%] | $31.19 | 0.624× | 49.31% | $5.81 | 25 (18 unfilled) | -17.18% [-48.76%, 16.40%] | $40.35 |
| series | tier1 | 17 | 17 | 0.0414 | -16.16% [-56.46%, 27.63%] | $40.08 | 0.802× | 32.63% | $5.81 | 14 (3 unfilled) | -29.15% [-68.09%, 8.85%] | $38.21 |
| series | tier2 | 26 | 26 | 0.0214 | -29.49% [-66.01%, 13.13%] | $38.90 | 0.778× | 34.22% | $5.09 | 11 (15 unfilled) | -2.10% [-57.83%, 54.30%] | $53.45 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 17 | 17 | 0.0414 | -16.16% [-56.46%, 27.63%] | $40.08 | 0.802× | 32.63% | $5.81 | 14 (3 unfilled) | -29.15% [-68.09%, 8.85%] | $38.21 |
| series | international=0 | 26 | 26 | 0.0214 | -29.49% [-66.01%, 13.13%] | $38.90 | 0.778× | 34.22% | $5.09 | 11 (15 unfilled) | -2.10% [-57.83%, 54.30%] | $53.45 |
| map | all | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier2 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=0 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series+map | all | 43 | 43 | 0.0293 | -24.24% [-51.83%, 7.01%] | $31.19 | 0.624× | 49.31% | $5.81 | 25 (18 unfilled) | -17.18% [-48.76%, 16.40%] | $40.35 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-02 | 62 | 0.667047 | — | 0.656833 | 10.38% (44), $62.99 | — | 1 (43 unfilled) | -100.00% [-100.00%, -100.00%] | $47.50 | — | — | — |
| map | 2026-04 | 7 | 0.799813 | — | 1.124640 | 210.34% (6), $95.14 | — | 3 (3 unfilled) | -44.74% [-100.00%, -16.71%] | $47.81 | — | — | — |
| map | 2026-05 | 40 | 0.736043 | — | 0.691447 | -6.30% (28), $43.01 | — | 1 (27 unfilled) | 32.49% [32.49%, 32.49%] | $50.36 | — | — | — |
| series | 2026-01 | 16 | 0.669652 | — | 0.612205 | 18.04% (10), $53.65 | — | 6 (4 unfilled) | 56.20% [-32.52%, 142.11%] | $65.97 | — | — | — |
| series | 2026-02 | 49 | 0.588486 | — | 0.595651 | 11.64% (45), $28.25 | — | 20 (25 unfilled) | -24.35% [-69.08%, 25.66%] | $36.26 | — | — | — |
| series | 2026-03 | 2 | 0.854873 | — | 1.445686 | 396.52% (1), $69.89 | — | 0 (1 unfilled) | — | $50.00 | — | — | — |
| series | 2026-04 | 41 | 0.602815 | — | 0.542714 | -9.76% (30), $31.72 | — | 20 (10 unfilled) | -9.45% [-52.93%, 36.65%] | $41.76 | — | — | — |
| series | 2026-05 | 36 | 0.673238 | 0.670642 | 0.664138 | 7.02% (29), $45.25 | -16.16% (17), $40.08 | 23 (6 unfilled) | 4.79% [-42.19%, 57.07%] | $35.57 | 14 (3 unfilled) | -29.15% [-68.09%, 8.85%] | $38.21 |
| series | 2026-06 | 100 | 0.600515 | 0.571208 | 0.560650 | -15.59% (67), $10.42 | -29.49% (26), $38.90 | 36 (31 unfilled) | -20.23% [-53.11%, 13.76%] | $34.17 | 11 (15 unfilled) | -2.10% [-57.83%, 54.30%] | $53.45 |

### player_round_glicko+calibration: Kalshi comparison and returns

calibration: ridge=4; tier1/online=0: rows=1092, T=0.7576; tier1/online=1: rows=567, T=0.8450; tier2/online=0: rows=253, T=1.0000; tier2/online=1: rows=4454, T=1.0273; tier3/online=0: rows=3215, T=1.0701; tier3/online=1: rows=40549, T=1.0250; unknown/online=0: rows=23, T=1.0000

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 244 | 0.614857 | 0.590569 | 0.024288 [-0.013450, 0.059362] | no |
| series | tier1 | 101 | 0.628836 | 0.622685 | 0.006152 [-0.057419, 0.071442] | no |
| series | tier2 | 143 | 0.604984 | 0.567886 | 0.037098 [-0.005120, 0.081220] | no |
| series | tier3 | 0 | — | — | — | — |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 101 | 0.628836 | 0.622685 | 0.006152 [-0.057419, 0.071442] | no |
| series | international=0 | 143 | 0.604984 | 0.567886 | 0.037098 [-0.005120, 0.081220] | no |
| map | all | 109 | 0.689817 | 0.699578 | -0.009761 [-0.084258, 0.048162] | no |
| map | tier1 | 102 | 0.681931 | 0.670407 | 0.011524 [-0.027703, 0.051236] | no |
| map | tier2 | 7 | 0.804725 | 1.124640 | -0.319916 [-1.398085, 0.226065] | no |
| map | tier3 | 0 | — | — | — | — |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 102 | 0.681931 | 0.670407 | 0.011524 [-0.027703, 0.051236] | no |
| map | international=0 | 7 | 0.804725 | 1.124640 | -0.319916 [-1.398085, 0.226065] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 182 | 182 | 0.0955 | -5.26% [-26.59%, 16.34%] | $6.41 | 0.128× | 91.97% | $7.75 | 104 (78 unfilled) | -9.80% [-31.71%, 13.11%] | $21.51 |
| series | tier1 | 82 | 82 | 0.1102 | 3.28% [-30.06%, 39.06%] | $35.62 | 0.712× | 60.38% | $7.75 | 47 (35 unfilled) | -2.70% [-39.19%, 35.12%] | $43.01 |
| series | tier2 | 100 | 100 | 0.0834 | -12.32% [-35.54%, 13.29%] | $9.06 | 0.181× | 90.06% | $8.66 | 57 (43 unfilled) | -15.68% [-41.59%, 11.45%] | $25.44 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 82 | 82 | 0.1102 | 3.28% [-30.06%, 39.06%] | $35.62 | 0.712× | 60.38% | $7.75 | 47 (35 unfilled) | -2.70% [-39.19%, 35.12%] | $43.01 |
| series | international=0 | 100 | 100 | 0.0834 | -12.32% [-35.54%, 13.29%] | $9.06 | 0.181× | 90.06% | $8.66 | 57 (43 unfilled) | -15.68% [-41.59%, 11.45%] | $25.44 |
| map | all | 83 | 44 | 0.0764 | 17.93% [-18.64%, 65.14%] | $97.30 | 1.946× | 26.41% | $11.86 | 6 (77 unfilled) | -50.79% [-100.00%, -11.31%] | $44.11 |
| map | tier1 | 77 | 39 | 0.0673 | 2.95% [-25.38%, 32.93%] | $51.75 | 1.035× | 26.42% | $5.69 | 3 (74 unfilled) | -56.83% [-100.00%, 32.49%] | $45.73 |
| map | tier2 | 6 | 5 | 0.1933 | 210.34% [-72.41%, 710.15%] | $93.87 | 1.877× | 11.91% | $10.23 | 3 (3 unfilled) | -44.74% [-100.00%, -16.71%] | $47.82 |
| map | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 77 | 39 | 0.0673 | 2.95% [-25.38%, 32.93%] | $51.75 | 1.035× | 26.42% | $5.69 | 3 (74 unfilled) | -56.83% [-100.00%, 32.49%] | $45.73 |
| map | international=0 | 6 | 5 | 0.1933 | 210.34% [-72.41%, 710.15%] | $93.87 | 1.877× | 11.91% | $10.23 | 3 (3 unfilled) | -44.74% [-100.00%, -16.71%] | $47.82 |
| series+map | all | 265 | 186 | 0.0895 | 2.00% [-17.67%, 23.76%] | $11.57 | 0.231× | 88.30% | $8.26 | 110 (155 unfilled) | -12.03% [-31.97%, 8.98%] | $22.21 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 217 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-01 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 16 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | map | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-03 | series | 65 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | series | 67 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | map | 62 | 1.000000 | 0.000000 | unfitted |
| 2026-05 | series | 108 | 1.228582 | 0.556488 | fitted |
| 2026-05 | map | 69 | 1.000000 | 0.000000 | unfitted |
| 2026-06 | series | 144 | 1.102447 | 0.487138 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 136 | 0.596803 | 0.588044 | 0.008759 [-0.008158, 0.026330] | no |
| series | tier1 | 36 | 0.664936 | 0.664138 | 0.000797 [-0.034235, 0.037464] | no |
| series | tier2 | 100 | 0.572275 | 0.560650 | 0.011625 [-0.007279, 0.030754] | no |
| series | tier3 | 0 | — | — | — | — |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 36 | 0.664936 | 0.664138 | 0.000797 [-0.034235, 0.037464] | no |
| series | international=0 | 100 | 0.572275 | 0.560650 | 0.011625 [-0.007279, 0.030754] | no |
| map | all | 0 | — | — | — | — |
| map | tier1 | 0 | — | — | — | — |
| map | tier2 | 0 | — | — | — | — |
| map | tier3 | 0 | — | — | — | — |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 0 | — | — | — | — |
| map | international=0 | 0 | — | — | — | — |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 56 | 56 | 0.0269 | -21.76% [-45.64%, 3.05%] | $27.64 | 0.553× | 52.27% | $5.65 | 34 (22 unfilled) | -29.69% [-55.82%, -2.58%] | $37.39 |
| series | tier1 | 14 | 14 | 0.0320 | -19.10% [-63.47%, 31.77%] | $42.47 | 0.849× | 26.67% | $5.65 | 11 (3 unfilled) | -36.42% [-76.16%, 5.89%] | $41.04 |
| series | tier2 | 42 | 42 | 0.0251 | -22.65% [-48.27%, 5.46%] | $32.62 | 0.652× | 46.35% | $5.83 | 23 (19 unfilled) | -26.48% [-61.84%, 8.42%] | $45.76 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 14 | 14 | 0.0320 | -19.10% [-63.47%, 31.77%] | $42.47 | 0.849× | 26.67% | $5.65 | 11 (3 unfilled) | -36.42% [-76.16%, 5.89%] | $41.04 |
| series | international=0 | 42 | 42 | 0.0251 | -22.65% [-48.27%, 5.46%] | $32.62 | 0.652× | 46.35% | $5.83 | 23 (19 unfilled) | -26.48% [-61.84%, 8.42%] | $45.76 |
| map | all | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier2 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=0 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series+map | all | 56 | 56 | 0.0269 | -21.76% [-45.64%, 3.05%] | $27.64 | 0.553× | 52.27% | $5.65 | 34 (22 unfilled) | -29.69% [-55.82%, -2.58%] | $37.39 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-02 | 62 | 0.661195 | — | 0.656833 | 10.10% (52), $57.96 | — | 2 (50 unfilled) | -100.00% [-100.00%, -100.00%] | $45.37 | — | — | — |
| map | 2026-04 | 7 | 0.804725 | — | 1.124640 | 210.34% (6), $93.87 | — | 3 (3 unfilled) | -44.74% [-100.00%, -16.71%] | $47.82 | — | — | — |
| map | 2026-05 | 40 | 0.714072 | — | 0.691447 | -12.07% (25), $44.68 | — | 1 (24 unfilled) | 32.49% [32.49%, 32.49%] | $50.36 | — | — | — |
| series | 2026-01 | 16 | 0.657040 | — | 0.612205 | -1.79% (12), $51.00 | — | 7 (5 unfilled) | 33.55% [-43.16%, 121.47%] | $63.31 | — | — | — |
| series | 2026-02 | 49 | 0.599378 | — | 0.595651 | 7.01% (44), $41.40 | — | 22 (22 unfilled) | -20.50% [-64.95%, 26.94%] | $39.60 | — | — | — |
| series | 2026-03 | 2 | 0.861120 | — | 1.445686 | 396.52% (1), $69.89 | — | 0 (1 unfilled) | — | $50.00 | — | — | — |
| series | 2026-04 | 41 | 0.602616 | — | 0.542714 | -8.79% (31), $32.65 | — | 20 (11 unfilled) | -9.45% [-52.93%, 36.65%] | $42.10 | — | — | — |
| series | 2026-05 | 36 | 0.656397 | 0.664936 | 0.664138 | -0.72% (26), $42.18 | -19.10% (14), $42.47 | 18 (8 unfilled) | 5.07% [-56.48%, 71.30%] | $40.78 | 11 (3 unfilled) | -36.42% [-76.16%, 5.89%] | $41.04 |
| series | 2026-06 | 100 | 0.600832 | 0.572275 | 0.560650 | -20.08% (68), $9.94 | -22.65% (42), $32.62 | 37 (31 unfilled) | -19.07% [-51.52%, 17.36%] | $31.42 | 23 (19 unfilled) | -26.48% [-61.84%, 8.42%] | $45.76 |

### player_round_glicko_rookie+none: Kalshi comparison and returns

none

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 244 | 0.610734 | 0.590569 | 0.020165 [-0.016807, 0.054495] | no |
| series | tier1 | 101 | 0.628997 | 0.622685 | 0.006312 [-0.056735, 0.071966] | no |
| series | tier2 | 143 | 0.597835 | 0.567886 | 0.029949 [-0.009164, 0.070879] | no |
| series | tier3 | 0 | — | — | — | — |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 101 | 0.628997 | 0.622685 | 0.006312 [-0.056735, 0.071966] | no |
| series | international=0 | 143 | 0.597835 | 0.567886 | 0.029949 [-0.009164, 0.070879] | no |
| map | all | 109 | 0.696002 | 0.699578 | -0.003576 [-0.081092, 0.055619] | no |
| map | tier1 | 102 | 0.688062 | 0.670407 | 0.017655 [-0.024516, 0.062717] | no |
| map | tier2 | 7 | 0.811698 | 1.124640 | -0.312943 [-1.387120, 0.206737] | no |
| map | tier3 | 0 | — | — | — | — |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 102 | 0.688062 | 0.670407 | 0.017655 [-0.024516, 0.062717] | no |
| map | international=0 | 7 | 0.811698 | 1.124640 | -0.312943 [-1.387120, 0.206737] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 176 | 176 | 0.0930 | -1.51% [-21.55%, 21.32%] | $7.66 | 0.153× | 89.10% | $6.64 | 103 (73 unfilled) | -6.82% [-26.51%, 14.84%] | $21.48 |
| series | tier1 | 80 | 80 | 0.1085 | 9.26% [-23.14%, 48.67%] | $28.27 | 0.565× | 63.83% | $6.64 | 48 (32 unfilled) | -1.92% [-33.33%, 31.42%] | $34.59 |
| series | tier2 | 96 | 96 | 0.0800 | -10.53% [-33.90%, 14.90%] | $13.72 | 0.274× | 83.73% | $8.02 | 55 (41 unfilled) | -11.09% [-38.21%, 17.60%] | $34.27 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 80 | 80 | 0.1085 | 9.26% [-23.14%, 48.67%] | $28.27 | 0.565× | 63.83% | $6.64 | 48 (32 unfilled) | -1.92% [-33.33%, 31.42%] | $34.59 |
| series | international=0 | 96 | 96 | 0.0800 | -10.53% [-33.90%, 14.90%] | $13.72 | 0.274× | 83.73% | $8.02 | 55 (41 unfilled) | -11.09% [-38.21%, 17.60%] | $34.27 |
| map | all | 81 | 43 | 0.0836 | 19.44% [-17.02%, 62.77%] | $98.96 | 1.979× | 31.10% | $12.33 | 5 (76 unfilled) | -40.74% [-100.00%, -0.47%] | $45.94 |
| map | tier1 | 76 | 39 | 0.0754 | 7.10% [-19.55%, 33.32%] | $55.72 | 1.114× | 31.14% | $6.25 | 2 (74 unfilled) | -34.72% [-100.00%, 32.49%] | $47.86 |
| map | tier2 | 5 | 4 | 0.2091 | 206.70% [-100.00%, 906.04%] | $88.72 | 1.774× | 11.97% | $9.68 | 3 (2 unfilled) | -44.74% [-100.00%, -16.71%] | $47.78 |
| map | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 76 | 39 | 0.0754 | 7.10% [-19.55%, 33.32%] | $55.72 | 1.114× | 31.14% | $6.25 | 2 (74 unfilled) | -34.72% [-100.00%, 32.49%] | $47.86 |
| map | international=0 | 5 | 4 | 0.2091 | 206.70% [-100.00%, 906.04%] | $88.72 | 1.774× | 11.97% | $9.68 | 3 (2 unfilled) | -44.74% [-100.00%, -16.71%] | $47.78 |
| series+map | all | 257 | 181 | 0.0900 | 5.08% [-14.62%, 26.68%] | $12.29 | 0.246× | 83.33% | $6.04 | 108 (149 unfilled) | -8.38% [-27.62%, 12.07%] | $21.95 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 217 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-01 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 16 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | map | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-03 | series | 65 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | series | 67 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | map | 62 | 1.000000 | 0.000000 | unfitted |
| 2026-05 | series | 108 | 1.140959 | 0.482882 | fitted |
| 2026-05 | map | 69 | 1.000000 | 0.000000 | unfitted |
| 2026-06 | series | 144 | 1.016536 | 0.421528 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 136 | 0.594718 | 0.588044 | 0.006674 [-0.009039, 0.021713] | no |
| series | tier1 | 36 | 0.663225 | 0.664138 | -0.000913 [-0.038786, 0.038588] | no |
| series | tier2 | 100 | 0.570056 | 0.560650 | 0.009406 [-0.006083, 0.024120] | no |
| series | tier3 | 0 | — | — | — | — |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 36 | 0.663225 | 0.664138 | -0.000913 [-0.038786, 0.038588] | no |
| series | international=0 | 100 | 0.570056 | 0.560650 | 0.009406 [-0.006083, 0.024120] | no |
| map | all | 0 | — | — | — | — |
| map | tier1 | 0 | — | — | — | — |
| map | tier2 | 0 | — | — | — | — |
| map | tier3 | 0 | — | — | — | — |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 0 | — | — | — | — |
| map | international=0 | 0 | — | — | — | — |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 49 | 49 | 0.0249 | -15.65% [-43.79%, 15.24%] | $35.50 | 0.710× | 44.27% | $5.94 | 30 (19 unfilled) | -12.09% [-45.35%, 24.16%] | $45.86 |
| series | tier1 | 17 | 17 | 0.0336 | -14.09% [-54.11%, 29.87%] | $43.83 | 0.877× | 27.92% | $5.94 | 14 (3 unfilled) | -26.63% [-64.89%, 11.50%] | $42.37 |
| series | tier2 | 32 | 32 | 0.0203 | -16.47% [-51.17%, 25.10%] | $40.45 | 0.809× | 31.05% | $5.37 | 16 (16 unfilled) | 0.54% [-54.31%, 61.63%] | $54.46 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 17 | 17 | 0.0336 | -14.09% [-54.11%, 29.87%] | $43.83 | 0.877× | 27.92% | $5.94 | 14 (3 unfilled) | -26.63% [-64.89%, 11.50%] | $42.37 |
| series | international=0 | 32 | 32 | 0.0203 | -16.47% [-51.17%, 25.10%] | $40.45 | 0.809× | 31.05% | $5.37 | 16 (16 unfilled) | 0.54% [-54.31%, 61.63%] | $54.46 |
| map | all | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier2 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=0 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series+map | all | 49 | 49 | 0.0249 | -15.65% [-43.79%, 15.24%] | $35.50 | 0.710× | 44.27% | $5.94 | 30 (19 unfilled) | -12.09% [-45.35%, 24.16%] | $45.86 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-02 | 62 | 0.663027 | — | 0.656833 | 14.83% (48), $63.70 | — | 1 (47 unfilled) | -100.00% [-100.00%, -100.00%] | $47.50 | — | — | — |
| map | 2026-04 | 7 | 0.811698 | — | 1.124640 | 206.70% (5), $88.72 | — | 3 (2 unfilled) | -44.74% [-100.00%, -16.71%] | $47.78 | — | — | — |
| map | 2026-05 | 40 | 0.726865 | — | 0.691447 | -6.30% (28), $43.72 | — | 1 (27 unfilled) | 32.49% [32.49%, 32.49%] | $50.36 | — | — | — |
| series | 2026-01 | 16 | 0.692581 | — | 0.612205 | -1.56% (12), $45.83 | — | 8 (4 unfilled) | 17.05% [-72.05%, 104.69%] | $58.52 | — | — | — |
| series | 2026-02 | 49 | 0.586653 | — | 0.595651 | 9.66% (42), $30.42 | — | 20 (22 unfilled) | -24.35% [-69.08%, 25.66%] | $37.87 | — | — | — |
| series | 2026-03 | 2 | 0.947654 | — | 1.445686 | 396.52% (1), $69.89 | — | 0 (1 unfilled) | — | $50.00 | — | — | — |
| series | 2026-04 | 41 | 0.586744 | — | 0.542714 | -5.70% (29), $33.86 | — | 19 (10 unfilled) | -3.24% [-50.21%, 46.11%] | $44.41 | — | — | — |
| series | 2026-05 | 36 | 0.658372 | 0.663225 | 0.664138 | 13.65% (26), $50.73 | -14.09% (17), $43.83 | 20 (6 unfilled) | 13.09% [-39.87%, 75.38%] | $38.37 | 14 (3 unfilled) | -26.63% [-64.89%, 11.50%] | $42.37 |
| series | 2026-06 | 100 | 0.595386 | 0.570056 | 0.560650 | -18.97% (66), $14.44 | -16.47% (32), $40.45 | 36 (30 unfilled) | -15.29% [-46.60%, 20.53%] | $39.66 | 16 (16 unfilled) | 0.54% [-54.31%, 61.63%] | $54.46 |

### player_round_glicko_rookie+calibration: Kalshi comparison and returns

calibration: ridge=4; tier1/online=0: rows=1092, T=0.7067; tier1/online=1: rows=567, T=0.7637; tier2/online=0: rows=253, T=1.0000; tier2/online=1: rows=4454, T=0.9685; tier3/online=0: rows=3215, T=1.0226; tier3/online=1: rows=40549, T=0.9383; unknown/online=0: rows=23, T=1.0000

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 244 | 0.610163 | 0.590569 | 0.019594 [-0.015928, 0.052964] | no |
| series | tier1 | 101 | 0.627950 | 0.622685 | 0.005265 [-0.058549, 0.069826] | no |
| series | tier2 | 143 | 0.597600 | 0.567886 | 0.029714 [-0.009397, 0.069780] | no |
| series | tier3 | 0 | — | — | — | — |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 101 | 0.627950 | 0.622685 | 0.005265 [-0.058549, 0.069826] | no |
| series | international=0 | 143 | 0.597600 | 0.567886 | 0.029714 [-0.009397, 0.069780] | no |
| map | all | 109 | 0.683833 | 0.699578 | -0.015746 [-0.088499, 0.040519] | no |
| map | tier1 | 102 | 0.675460 | 0.670407 | 0.005052 [-0.033234, 0.043210] | no |
| map | tier2 | 7 | 0.805836 | 1.124640 | -0.318804 [-1.383113, 0.201506] | no |
| map | tier3 | 0 | — | — | — | — |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 102 | 0.675460 | 0.670407 | 0.005052 [-0.033234, 0.043210] | no |
| map | international=0 | 7 | 0.805836 | 1.124640 | -0.318804 [-1.383113, 0.201506] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 184 | 184 | 0.0889 | -5.16% [-23.23%, 16.02%] | $10.61 | 0.212× | 85.54% | $7.12 | 108 (76 unfilled) | -8.77% [-30.55%, 13.19%] | $31.66 |
| series | tier1 | 85 | 85 | 0.1031 | 5.52% [-27.25%, 40.88%] | $38.73 | 0.775× | 56.39% | $7.14 | 50 (35 unfilled) | 1.49% [-32.75%, 36.80%] | $45.19 |
| series | tier2 | 99 | 99 | 0.0766 | -14.39% [-38.06%, 10.36%] | $13.74 | 0.275× | 84.13% | $8.22 | 58 (41 unfilled) | -17.65% [-43.25%, 7.90%] | $35.88 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 85 | 85 | 0.1031 | 5.52% [-27.25%, 40.88%] | $38.73 | 0.775× | 56.39% | $7.14 | 50 (35 unfilled) | 1.49% [-32.75%, 36.80%] | $45.19 |
| series | international=0 | 99 | 99 | 0.0766 | -14.39% [-38.06%, 10.36%] | $13.74 | 0.275× | 84.13% | $8.22 | 58 (41 unfilled) | -17.65% [-43.25%, 7.90%] | $35.88 |
| map | all | 79 | 42 | 0.0753 | 19.70% [-17.75%, 68.41%] | $107.80 | 2.156× | 21.97% | $11.63 | 6 (73 unfilled) | -50.79% [-100.00%, -11.31%] | $44.27 |
| map | tier1 | 74 | 38 | 0.0666 | 7.08% [-21.78%, 37.11%] | $60.72 | 1.214× | 17.81% | $5.90 | 3 (71 unfilled) | -56.83% [-100.00%, 32.49%] | $45.97 |
| map | tier2 | 5 | 4 | 0.2042 | 206.70% [-100.00%, 906.04%] | $88.69 | 1.774× | 12.00% | $9.68 | 3 (2 unfilled) | -44.74% [-100.00%, -16.71%] | $47.77 |
| map | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 74 | 38 | 0.0666 | 7.08% [-21.78%, 37.11%] | $60.72 | 1.214× | 17.81% | $5.90 | 3 (71 unfilled) | -56.83% [-100.00%, 32.49%] | $45.97 |
| map | international=0 | 5 | 4 | 0.2042 | 206.70% [-100.00%, 906.04%] | $88.69 | 1.774× | 12.00% | $9.68 | 3 (2 unfilled) | -44.74% [-100.00%, -16.71%] | $47.77 |
| series+map | all | 263 | 188 | 0.0848 | 2.31% [-18.48%, 23.95%] | $17.20 | 0.344× | 81.89% | $8.16 | 114 (149 unfilled) | -10.98% [-30.16%, 8.90%] | $29.13 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 217 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-01 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 16 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | map | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-03 | series | 65 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | series | 67 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | map | 62 | 1.000000 | 0.000000 | unfitted |
| 2026-05 | series | 108 | 1.210254 | 0.543616 | fitted |
| 2026-05 | map | 69 | 1.000000 | 0.000000 | unfitted |
| 2026-06 | series | 144 | 1.108442 | 0.510374 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 136 | 0.594111 | 0.588044 | 0.006067 [-0.010337, 0.022868] | no |
| series | tier1 | 36 | 0.659574 | 0.664138 | -0.004564 [-0.035922, 0.027379] | no |
| series | tier2 | 100 | 0.570544 | 0.560650 | 0.009894 [-0.009235, 0.028877] | no |
| series | tier3 | 0 | — | — | — | — |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 36 | 0.659574 | 0.664138 | -0.004564 [-0.035922, 0.027379] | no |
| series | international=0 | 100 | 0.570544 | 0.560650 | 0.009894 [-0.009235, 0.028877] | no |
| map | all | 0 | — | — | — | — |
| map | tier1 | 0 | — | — | — | — |
| map | tier2 | 0 | — | — | — | — |
| map | tier3 | 0 | — | — | — | — |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 0 | — | — | — | — |
| map | international=0 | 0 | — | — | — | — |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 52 | 52 | 0.0266 | -18.44% [-42.50%, 7.39%] | $32.47 | 0.649× | 47.32% | $5.53 | 31 (21 unfilled) | -22.82% [-51.69%, 5.55%] | $40.68 |
| series | tier1 | 13 | 13 | 0.0266 | -12.83% [-59.88%, 40.52%] | $48.26 | 0.965× | 21.71% | $5.52 | 10 (3 unfilled) | -30.02% [-73.45%, 15.25%] | $44.57 |
| series | tier2 | 39 | 39 | 0.0267 | -20.31% [-48.70%, 11.40%] | $33.63 | 0.673× | 43.40% | $5.72 | 21 (18 unfilled) | -19.39% [-53.96%, 15.61%] | $45.82 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 13 | 13 | 0.0266 | -12.83% [-59.88%, 40.52%] | $48.26 | 0.965× | 21.71% | $5.52 | 10 (3 unfilled) | -30.02% [-73.45%, 15.25%] | $44.57 |
| series | international=0 | 39 | 39 | 0.0267 | -20.31% [-48.70%, 11.40%] | $33.63 | 0.673× | 43.40% | $5.72 | 21 (18 unfilled) | -19.39% [-53.96%, 15.61%] | $45.82 |
| map | all | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier2 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=0 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series+map | all | 52 | 52 | 0.0266 | -18.44% [-42.50%, 7.39%] | $32.47 | 0.649× | 47.32% | $5.53 | 31 (21 unfilled) | -22.82% [-51.69%, 5.55%] | $40.68 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-02 | 62 | 0.657457 | — | 0.656833 | 10.10% (52), $60.14 | — | 2 (50 unfilled) | -100.00% [-100.00%, -100.00%] | $45.61 | — | — | — |
| map | 2026-04 | 7 | 0.805836 | — | 1.124640 | 206.70% (5), $88.69 | — | 3 (2 unfilled) | -44.74% [-100.00%, -16.71%] | $47.77 | — | — | — |
| map | 2026-05 | 40 | 0.703364 | — | 0.691447 | -0.11% (22), $50.53 | — | 1 (21 unfilled) | 32.49% [32.49%, 32.49%] | $50.36 | — | — | — |
| series | 2026-01 | 16 | 0.673138 | — | 0.612205 | 9.42% (13), $46.39 | — | 8 (5 unfilled) | 47.45% [-36.57%, 124.67%] | $60.63 | — | — | — |
| series | 2026-02 | 49 | 0.598700 | — | 0.595651 | 10.34% (45), $43.62 | — | 23 (22 unfilled) | -12.76% [-57.77%, 32.62%] | $41.27 | — | — | — |
| series | 2026-03 | 2 | 0.937668 | — | 1.445686 | 396.52% (1), $69.89 | — | 0 (1 unfilled) | — | $50.00 | — | — | — |
| series | 2026-04 | 41 | 0.587118 | — | 0.542714 | -5.70% (29), $33.80 | — | 19 (10 unfilled) | -3.24% [-50.21%, 46.11%] | $44.68 | — | — | — |
| series | 2026-05 | 36 | 0.647678 | 0.659574 | 0.664138 | -4.45% (27), $47.77 | -12.83% (13), $48.26 | 19 (8 unfilled) | -0.55% [-61.73%, 69.66%] | $43.33 | 10 (3 unfilled) | -30.02% [-73.45%, 15.25%] | $44.57 |
| series | 2026-06 | 100 | 0.595097 | 0.570544 | 0.560650 | -24.15% (69), $14.53 | -20.31% (39), $33.63 | 39 (30 unfilled) | -24.73% [-55.18%, 7.72%] | $41.16 | 21 (18 unfilled) | -19.39% [-53.96%, 15.61%] | $45.82 |

## Holdout

### Leaderboard (frozen stage-1 parameters)

| Model | Best params | Map log loss | Series log loss | Rows |
|---|---|---:|---:|---:|
| player_round_glicko_rookie+calibration | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 280, "rookie_maps": 3200, "rookie_penalty": 225, "tau": 0.75} | 0.556776 | 0.533684 | 6005 |
| player_round_glicko_rookie | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 280, "rookie_maps": 3200, "rookie_penalty": 225, "tau": 0.75} | 0.557527 | 0.534081 | 6005 |
| player_round_glicko_rookie+none | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 280, "rookie_maps": 3200, "rookie_penalty": 225, "tau": 0.75} | 0.557527 | 0.534081 | 6005 |
| player_round_glicko+calibration | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 280, "tau": 0.75} | 0.564525 | 0.544761 | 6005 |
| player_round_glicko | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 280, "tau": 0.75} | 0.564710 | 0.544875 | 6005 |
| player_round_glicko+none | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 280, "tau": 0.75} | 0.564710 | 0.544875 | 6005 |
| team_elo+calibration | {"k": 64} | 0.619389 | 0.612743 | 6005 |
| team_elo | {"k": 64} | 0.621147 | 0.613538 | 6005 |
| team_elo+none | {"k": 64} | 0.621147 | 0.613538 | 6005 |

### Maps

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| coin | all | 6005 | 0.693147 | 0.250000 | 0.500000 | 0.048543 |
| coin | tier1 | 85 | 0.693147 | 0.250000 | 0.500000 | 0.041176 |
| coin | tier2 | 679 | 0.693147 | 0.250000 | 0.500000 | 0.064065 |
| coin | tier3 | 5241 | 0.693147 | 0.250000 | 0.500000 | 0.046651 |
| coin | unknown | 0 | — | — | — | — |
| coin | international=1 | 175 | 0.693147 | 0.250000 | 0.500000 | 0.105714 |
| coin | international=0 | 5830 | 0.693147 | 0.250000 | 0.500000 | 0.046827 |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| team_elo | all | 6005 | 0.621147 | 0.216370 | 0.641549 | 0.027592 |
| team_elo | tier1 | 85 | 0.670086 | 0.238838 | 0.588235 | 0.101725 |
| team_elo | tier2 | 679 | 0.645077 | 0.223874 | 0.638439 | 0.065524 |
| team_elo | tier3 | 5241 | 0.617254 | 0.215034 | 0.642816 | 0.027663 |
| team_elo | unknown | 0 | — | — | — | — |
| team_elo | international=1 | 175 | 0.620329 | 0.218030 | 0.622857 | 0.079068 |
| team_elo | international=0 | 5830 | 0.621172 | 0.216321 | 0.642110 | 0.026534 |

team_elo − coin (paired log loss):

| Section | Rows | team_elo log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6005 | 0.621147 | 0.693147 | -0.072000 | [-0.082773, -0.060778] | yes |
| tier1 | 85 | 0.670086 | 0.693147 | -0.023062 | [-0.095434, 0.045858] | no |
| tier2 | 679 | 0.645077 | 0.693147 | -0.048070 | [-0.090938, -0.006010] | yes |
| tier3 | 5241 | 0.617254 | 0.693147 | -0.075894 | [-0.087390, -0.064664] | yes |
| international=1 | 175 | 0.620329 | 0.693147 | -0.072818 | [-0.127425, -0.019028] | yes |
| international=0 | 5830 | 0.621172 | 0.693147 | -0.071975 | [-0.083482, -0.061027] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko | all | 6005 | 0.564710 | 0.193238 | 0.697585 | 0.014188 |
| player_round_glicko | tier1 | 85 | 0.672948 | 0.239407 | 0.576471 | 0.067541 |
| player_round_glicko | tier2 | 679 | 0.606057 | 0.210535 | 0.673785 | 0.066143 |
| player_round_glicko | tier3 | 5241 | 0.557598 | 0.190249 | 0.702633 | 0.013340 |
| player_round_glicko | unknown | 0 | — | — | — | — |
| player_round_glicko | international=1 | 175 | 0.602150 | 0.209359 | 0.662857 | 0.061332 |
| player_round_glicko | international=0 | 5830 | 0.563586 | 0.192754 | 0.698628 | 0.013904 |

player_round_glicko − coin (paired log loss):

| Section | Rows | player_round_glicko log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6005 | 0.564710 | 0.693147 | -0.128437 | [-0.140175, -0.116891] | yes |
| tier1 | 85 | 0.672948 | 0.693147 | -0.020199 | [-0.102599, 0.059475] | no |
| tier2 | 679 | 0.606057 | 0.693147 | -0.087090 | [-0.123840, -0.051818] | yes |
| tier3 | 5241 | 0.557598 | 0.693147 | -0.135549 | [-0.147972, -0.123114] | yes |
| international=1 | 175 | 0.602150 | 0.693147 | -0.090997 | [-0.152339, -0.026487] | yes |
| international=0 | 5830 | 0.563586 | 0.693147 | -0.129561 | [-0.142158, -0.117686] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko_rookie | all | 6005 | 0.557527 | 0.189756 | 0.709409 | 0.021566 |
| player_round_glicko_rookie | tier1 | 85 | 0.672937 | 0.239750 | 0.576471 | 0.077792 |
| player_round_glicko_rookie | tier2 | 679 | 0.610455 | 0.211368 | 0.673049 | 0.073604 |
| player_round_glicko_rookie | tier3 | 5241 | 0.548798 | 0.186146 | 0.716276 | 0.022242 |
| player_round_glicko_rookie | unknown | 0 | — | — | — | — |
| player_round_glicko_rookie | international=1 | 175 | 0.600345 | 0.208531 | 0.662857 | 0.058232 |
| player_round_glicko_rookie | international=0 | 5830 | 0.556242 | 0.189193 | 0.710806 | 0.021981 |

player_round_glicko_rookie − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6005 | 0.557527 | 0.693147 | -0.135620 | [-0.148497, -0.123023] | yes |
| tier1 | 85 | 0.672937 | 0.693147 | -0.020210 | [-0.104359, 0.059006] | no |
| tier2 | 679 | 0.610455 | 0.693147 | -0.082693 | [-0.122191, -0.043836] | yes |
| tier3 | 5241 | 0.548798 | 0.693147 | -0.144349 | [-0.157731, -0.130479] | yes |
| international=1 | 175 | 0.600345 | 0.693147 | -0.092802 | [-0.158740, -0.024036] | yes |
| international=0 | 5830 | 0.556242 | 0.693147 | -0.136905 | [-0.151095, -0.123813] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| team_elo+none | all | 6005 | 0.621147 | 0.216370 | 0.641549 | 0.027592 |
| team_elo+none | tier1 | 85 | 0.670086 | 0.238838 | 0.588235 | 0.101725 |
| team_elo+none | tier2 | 679 | 0.645077 | 0.223874 | 0.638439 | 0.065524 |
| team_elo+none | tier3 | 5241 | 0.617254 | 0.215034 | 0.642816 | 0.027663 |
| team_elo+none | unknown | 0 | — | — | — | — |
| team_elo+none | international=1 | 175 | 0.620329 | 0.218030 | 0.622857 | 0.079068 |
| team_elo+none | international=0 | 5830 | 0.621172 | 0.216321 | 0.642110 | 0.026534 |

team_elo+none − coin (paired log loss):

| Section | Rows | team_elo+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6005 | 0.621147 | 0.693147 | -0.072000 | [-0.082773, -0.060778] | yes |
| tier1 | 85 | 0.670086 | 0.693147 | -0.023062 | [-0.095434, 0.045858] | no |
| tier2 | 679 | 0.645077 | 0.693147 | -0.048070 | [-0.090938, -0.006010] | yes |
| tier3 | 5241 | 0.617254 | 0.693147 | -0.075894 | [-0.087390, -0.064664] | yes |
| international=1 | 175 | 0.620329 | 0.693147 | -0.072818 | [-0.127425, -0.019028] | yes |
| international=0 | 5830 | 0.621172 | 0.693147 | -0.071975 | [-0.083482, -0.061027] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| team_elo+calibration | all | 6005 | 0.619389 | 0.215859 | 0.641549 | 0.024502 |
| team_elo+calibration | tier1 | 85 | 0.672596 | 0.239853 | 0.588235 | 0.040880 |
| team_elo+calibration | tier2 | 679 | 0.632066 | 0.220468 | 0.638439 | 0.061559 |
| team_elo+calibration | tier3 | 5241 | 0.616884 | 0.214873 | 0.642816 | 0.026493 |
| team_elo+calibration | unknown | 0 | — | — | — | — |
| team_elo+calibration | international=1 | 175 | 0.622880 | 0.218690 | 0.622857 | 0.091600 |
| team_elo+calibration | international=0 | 5830 | 0.619285 | 0.215775 | 0.642110 | 0.022891 |

team_elo+calibration − coin (paired log loss):

| Section | Rows | team_elo+calibration log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6005 | 0.619389 | 0.693147 | -0.073758 | [-0.083404, -0.063696] | yes |
| tier1 | 85 | 0.672596 | 0.693147 | -0.020551 | [-0.048418, 0.004231] | no |
| tier2 | 679 | 0.632066 | 0.693147 | -0.061082 | [-0.097592, -0.024019] | yes |
| tier3 | 5241 | 0.616884 | 0.693147 | -0.076263 | [-0.086906, -0.065894] | yes |
| international=1 | 175 | 0.622880 | 0.693147 | -0.070267 | [-0.114686, -0.027129] | yes |
| international=0 | 5830 | 0.619285 | 0.693147 | -0.073862 | [-0.084330, -0.063638] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko+none | all | 6005 | 0.564710 | 0.193238 | 0.697585 | 0.014188 |
| player_round_glicko+none | tier1 | 85 | 0.672948 | 0.239407 | 0.576471 | 0.067541 |
| player_round_glicko+none | tier2 | 679 | 0.606057 | 0.210535 | 0.673785 | 0.066143 |
| player_round_glicko+none | tier3 | 5241 | 0.557598 | 0.190249 | 0.702633 | 0.013340 |
| player_round_glicko+none | unknown | 0 | — | — | — | — |
| player_round_glicko+none | international=1 | 175 | 0.602150 | 0.209359 | 0.662857 | 0.061332 |
| player_round_glicko+none | international=0 | 5830 | 0.563586 | 0.192754 | 0.698628 | 0.013904 |

player_round_glicko+none − coin (paired log loss):

| Section | Rows | player_round_glicko+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6005 | 0.564710 | 0.693147 | -0.128437 | [-0.140175, -0.116891] | yes |
| tier1 | 85 | 0.672948 | 0.693147 | -0.020199 | [-0.102599, 0.059475] | no |
| tier2 | 679 | 0.606057 | 0.693147 | -0.087090 | [-0.123840, -0.051818] | yes |
| tier3 | 5241 | 0.557598 | 0.693147 | -0.135549 | [-0.147972, -0.123114] | yes |
| international=1 | 175 | 0.602150 | 0.693147 | -0.090997 | [-0.152339, -0.026487] | yes |
| international=0 | 5830 | 0.563586 | 0.693147 | -0.129561 | [-0.142158, -0.117686] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko+calibration | all | 6005 | 0.564525 | 0.193173 | 0.697585 | 0.012643 |
| player_round_glicko+calibration | tier1 | 85 | 0.663078 | 0.235913 | 0.576471 | 0.044327 |
| player_round_glicko+calibration | tier2 | 679 | 0.606835 | 0.210780 | 0.673785 | 0.064274 |
| player_round_glicko+calibration | tier3 | 5241 | 0.557445 | 0.190199 | 0.702633 | 0.011462 |
| player_round_glicko+calibration | unknown | 0 | — | — | — | — |
| player_round_glicko+calibration | international=1 | 175 | 0.597344 | 0.207667 | 0.662857 | 0.062321 |
| player_round_glicko+calibration | international=0 | 5830 | 0.563540 | 0.192738 | 0.698628 | 0.012455 |

player_round_glicko+calibration − coin (paired log loss):

| Section | Rows | player_round_glicko+calibration log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6005 | 0.564525 | 0.693147 | -0.128622 | [-0.140557, -0.116768] | yes |
| tier1 | 85 | 0.663078 | 0.693147 | -0.030069 | [-0.095586, 0.031258] | no |
| tier2 | 679 | 0.606835 | 0.693147 | -0.086312 | [-0.123533, -0.050518] | yes |
| tier3 | 5241 | 0.557445 | 0.693147 | -0.135702 | [-0.148388, -0.122923] | yes |
| international=1 | 175 | 0.597344 | 0.693147 | -0.095803 | [-0.155658, -0.036021] | yes |
| international=0 | 5830 | 0.563540 | 0.693147 | -0.129607 | [-0.142555, -0.117496] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko_rookie+none | all | 6005 | 0.557527 | 0.189756 | 0.709409 | 0.021566 |
| player_round_glicko_rookie+none | tier1 | 85 | 0.672937 | 0.239750 | 0.576471 | 0.077792 |
| player_round_glicko_rookie+none | tier2 | 679 | 0.610455 | 0.211368 | 0.673049 | 0.073604 |
| player_round_glicko_rookie+none | tier3 | 5241 | 0.548798 | 0.186146 | 0.716276 | 0.022242 |
| player_round_glicko_rookie+none | unknown | 0 | — | — | — | — |
| player_round_glicko_rookie+none | international=1 | 175 | 0.600345 | 0.208531 | 0.662857 | 0.058232 |
| player_round_glicko_rookie+none | international=0 | 5830 | 0.556242 | 0.189193 | 0.710806 | 0.021981 |

player_round_glicko_rookie+none − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6005 | 0.557527 | 0.693147 | -0.135620 | [-0.148497, -0.123023] | yes |
| tier1 | 85 | 0.672937 | 0.693147 | -0.020210 | [-0.104359, 0.059006] | no |
| tier2 | 679 | 0.610455 | 0.693147 | -0.082693 | [-0.122191, -0.043836] | yes |
| tier3 | 5241 | 0.548798 | 0.693147 | -0.144349 | [-0.157731, -0.130479] | yes |
| international=1 | 175 | 0.600345 | 0.693147 | -0.092802 | [-0.158740, -0.024036] | yes |
| international=0 | 5830 | 0.556242 | 0.693147 | -0.136905 | [-0.151095, -0.123813] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko_rookie+calibration | all | 6005 | 0.556776 | 0.189569 | 0.709409 | 0.016616 |
| player_round_glicko_rookie+calibration | tier1 | 85 | 0.661469 | 0.235394 | 0.576471 | 0.052442 |
| player_round_glicko_rookie+calibration | tier2 | 679 | 0.609464 | 0.211083 | 0.673049 | 0.073764 |
| player_round_glicko_rookie+calibration | tier3 | 5241 | 0.548252 | 0.186038 | 0.716276 | 0.018089 |
| player_round_glicko_rookie+calibration | unknown | 0 | — | — | — | — |
| player_round_glicko_rookie+calibration | international=1 | 175 | 0.594440 | 0.206361 | 0.662857 | 0.064576 |
| player_round_glicko_rookie+calibration | international=0 | 5830 | 0.555645 | 0.189065 | 0.710806 | 0.017297 |

player_round_glicko_rookie+calibration − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie+calibration log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6005 | 0.556776 | 0.693147 | -0.136371 | [-0.148791, -0.124357] | yes |
| tier1 | 85 | 0.661469 | 0.693147 | -0.031678 | [-0.094246, 0.027022] | no |
| tier2 | 679 | 0.609464 | 0.693147 | -0.083683 | [-0.122267, -0.045575] | yes |
| tier3 | 5241 | 0.548252 | 0.693147 | -0.144895 | [-0.157674, -0.131833] | yes |
| international=1 | 175 | 0.594440 | 0.693147 | -0.098708 | [-0.158986, -0.038323] | yes |
| international=0 | 5830 | 0.555645 | 0.693147 | -0.137502 | [-0.151076, -0.124827] | yes |

player_round_glicko − team_elo (paired log loss):

| Section | Rows | player_round_glicko log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6005 | 0.564710 | 0.621147 | -0.056438 | [-0.064754, -0.048179] | yes |

player_round_glicko_rookie − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6005 | 0.557527 | 0.621147 | -0.063620 | [-0.073224, -0.054020] | yes |

team_elo+none − team_elo (paired log loss):

| Section | Rows | team_elo+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6005 | 0.621147 | 0.621147 | 0.000000 | [0.000000, 0.000000] | no |

team_elo+calibration − team_elo (paired log loss):

| Section | Rows | team_elo+calibration log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6005 | 0.619389 | 0.621147 | -0.001758 | [-0.003081, -0.000557] | yes |

player_round_glicko+none − team_elo (paired log loss):

| Section | Rows | player_round_glicko+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6005 | 0.564710 | 0.621147 | -0.056438 | [-0.064754, -0.048179] | yes |

player_round_glicko+calibration − team_elo (paired log loss):

| Section | Rows | player_round_glicko+calibration log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6005 | 0.564525 | 0.621147 | -0.056623 | [-0.065055, -0.048012] | yes |

player_round_glicko_rookie+none − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6005 | 0.557527 | 0.621147 | -0.063620 | [-0.073224, -0.054020] | yes |

player_round_glicko_rookie+calibration − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie+calibration log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6005 | 0.556776 | 0.621147 | -0.064371 | [-0.073701, -0.055005] | yes |

player_round_glicko − player_round_glicko_rookie (paired log loss):

| Section | Rows | player_round_glicko log loss | player_round_glicko_rookie log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6005 | 0.564710 | 0.557527 | 0.007183 | [0.003726, 0.010495] | yes |
| tier1 | 85 | 0.672948 | 0.672937 | 0.000010 | [-0.003421, 0.003854] | no |
| tier2 | 679 | 0.606057 | 0.610455 | -0.004398 | [-0.011072, 0.000840] | no |
| tier3 | 5241 | 0.557598 | 0.548798 | 0.008799 | [0.005084, 0.012192] | yes |
| international=1 | 175 | 0.602150 | 0.600345 | 0.001805 | [-0.007290, 0.012191] | no |
| international=0 | 5830 | 0.563586 | 0.556242 | 0.007344 | [0.003856, 0.010556] | yes |

team_elo+none − player_round_glicko_rookie (paired log loss):

| Section | Rows | team_elo+none log loss | player_round_glicko_rookie log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6005 | 0.621147 | 0.557527 | 0.063620 | [0.054020, 0.073224] | yes |
| tier1 | 85 | 0.670086 | 0.672937 | -0.002852 | [-0.053356, 0.042570] | no |
| tier2 | 679 | 0.645077 | 0.610455 | 0.034622 | [0.006975, 0.064454] | yes |
| tier3 | 5241 | 0.617254 | 0.548798 | 0.068455 | [0.057922, 0.078637] | yes |
| international=1 | 175 | 0.620329 | 0.600345 | 0.019984 | [-0.019675, 0.058270] | no |
| international=0 | 5830 | 0.621172 | 0.556242 | 0.064930 | [0.054824, 0.074860] | yes |

team_elo+calibration − player_round_glicko_rookie (paired log loss):

| Section | Rows | team_elo+calibration log loss | player_round_glicko_rookie log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6005 | 0.619389 | 0.557527 | 0.061862 | [0.052188, 0.071211] | yes |
| tier1 | 85 | 0.672596 | 0.672937 | -0.000341 | [-0.062399, 0.061454] | no |
| tier2 | 679 | 0.632066 | 0.610455 | 0.021611 | [-0.003197, 0.048229] | no |
| tier3 | 5241 | 0.616884 | 0.548798 | 0.068086 | [0.057533, 0.077980] | yes |
| international=1 | 175 | 0.622880 | 0.600345 | 0.022535 | [-0.021738, 0.066019] | no |
| international=0 | 5830 | 0.619285 | 0.556242 | 0.063043 | [0.053219, 0.072897] | yes |

player_round_glicko+none − player_round_glicko_rookie (paired log loss):

| Section | Rows | player_round_glicko+none log loss | player_round_glicko_rookie log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6005 | 0.564710 | 0.557527 | 0.007183 | [0.003726, 0.010495] | yes |
| tier1 | 85 | 0.672948 | 0.672937 | 0.000010 | [-0.003421, 0.003854] | no |
| tier2 | 679 | 0.606057 | 0.610455 | -0.004398 | [-0.011072, 0.000840] | no |
| tier3 | 5241 | 0.557598 | 0.548798 | 0.008799 | [0.005084, 0.012192] | yes |
| international=1 | 175 | 0.602150 | 0.600345 | 0.001805 | [-0.007290, 0.012191] | no |
| international=0 | 5830 | 0.563586 | 0.556242 | 0.007344 | [0.003856, 0.010556] | yes |

player_round_glicko+calibration − player_round_glicko_rookie (paired log loss):

| Section | Rows | player_round_glicko+calibration log loss | player_round_glicko_rookie log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6005 | 0.564525 | 0.557527 | 0.006998 | [0.003613, 0.010280] | yes |
| tier1 | 85 | 0.663078 | 0.672937 | -0.009859 | [-0.030258, 0.008860] | no |
| tier2 | 679 | 0.606835 | 0.610455 | -0.003620 | [-0.010231, 0.001445] | no |
| tier3 | 5241 | 0.557445 | 0.548798 | 0.008647 | [0.004967, 0.012063] | yes |
| international=1 | 175 | 0.597344 | 0.600345 | -0.003001 | [-0.016150, 0.010083] | no |
| international=0 | 5830 | 0.563540 | 0.556242 | 0.007298 | [0.003854, 0.010460] | yes |

player_round_glicko_rookie+none − player_round_glicko_rookie (paired log loss):

| Section | Rows | player_round_glicko_rookie+none log loss | player_round_glicko_rookie log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6005 | 0.557527 | 0.557527 | 0.000000 | [0.000000, 0.000000] | no |
| tier1 | 85 | 0.672937 | 0.672937 | 0.000000 | [0.000000, 0.000000] | no |
| tier2 | 679 | 0.610455 | 0.610455 | 0.000000 | [0.000000, 0.000000] | no |
| tier3 | 5241 | 0.548798 | 0.548798 | 0.000000 | [0.000000, 0.000000] | no |
| international=1 | 175 | 0.600345 | 0.600345 | 0.000000 | [0.000000, 0.000000] | no |
| international=0 | 5830 | 0.556242 | 0.556242 | 0.000000 | [0.000000, 0.000000] | no |

player_round_glicko_rookie+calibration − player_round_glicko_rookie (paired log loss):

| Section | Rows | player_round_glicko_rookie+calibration log loss | player_round_glicko_rookie log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6005 | 0.556776 | 0.557527 | -0.000751 | [-0.001500, -0.000018] | yes |
| tier1 | 85 | 0.661469 | 0.672937 | -0.011468 | [-0.035266, 0.010554] | no |
| tier2 | 679 | 0.609464 | 0.610455 | -0.000991 | [-0.001873, -0.000159] | yes |
| tier3 | 5241 | 0.548252 | 0.548798 | -0.000546 | [-0.001289, 0.000165] | no |
| international=1 | 175 | 0.594440 | 0.600345 | -0.005905 | [-0.017967, 0.004362] | no |
| international=0 | 5830 | 0.555645 | 0.556242 | -0.000596 | [-0.001278, 0.000066] | no |

### Series

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| coin | all | 4076 | 0.693147 | 0.250000 | 0.500000 | 0.048577 |
| coin | tier1 | 40 | 0.693147 | 0.250000 | 0.500000 | 0.100000 |
| coin | tier2 | 438 | 0.693147 | 0.250000 | 0.500000 | 0.061644 |
| coin | tier3 | 3598 | 0.693147 | 0.250000 | 0.500000 | 0.046415 |
| coin | unknown | 0 | — | — | — | — |
| coin | international=1 | 81 | 0.693147 | 0.250000 | 0.500000 | 0.154321 |
| coin | international=0 | 3995 | 0.693147 | 0.250000 | 0.500000 | 0.046433 |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| team_elo | all | 4076 | 0.613538 | 0.213060 | 0.645363 | 0.027632 |
| team_elo | tier1 | 40 | 0.601920 | 0.206311 | 0.625000 | 0.162277 |
| team_elo | tier2 | 438 | 0.646846 | 0.222475 | 0.635845 | 0.094342 |
| team_elo | tier3 | 3598 | 0.609613 | 0.211989 | 0.646748 | 0.026256 |
| team_elo | unknown | 0 | — | — | — | — |
| team_elo | international=1 | 81 | 0.571789 | 0.195384 | 0.654321 | 0.110870 |
| team_elo | international=0 | 3995 | 0.614385 | 0.213418 | 0.645181 | 0.026616 |

team_elo − coin (paired log loss):

| Section | Rows | team_elo log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4076 | 0.613538 | 0.693147 | -0.079609 | [-0.091439, -0.066774] | yes |
| tier1 | 40 | 0.601920 | 0.693147 | -0.091227 | [-0.185427, 0.012465] | no |
| tier2 | 438 | 0.646846 | 0.693147 | -0.046301 | [-0.099441, 0.007905] | no |
| tier3 | 3598 | 0.609613 | 0.693147 | -0.083534 | [-0.095534, -0.071651] | yes |
| international=1 | 81 | 0.571789 | 0.693147 | -0.121358 | [-0.187354, -0.049655] | yes |
| international=0 | 3995 | 0.614385 | 0.693147 | -0.078762 | [-0.091040, -0.066858] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko | all | 4076 | 0.544875 | 0.184988 | 0.714917 | 0.015559 |
| player_round_glicko | tier1 | 40 | 0.591610 | 0.205202 | 0.650000 | 0.134710 |
| player_round_glicko | tier2 | 438 | 0.591393 | 0.203388 | 0.689498 | 0.072477 |
| player_round_glicko | tier3 | 3598 | 0.538692 | 0.182524 | 0.718733 | 0.018392 |
| player_round_glicko | unknown | 0 | — | — | — | — |
| player_round_glicko | international=1 | 81 | 0.523929 | 0.177455 | 0.728395 | 0.105587 |
| player_round_glicko | international=0 | 3995 | 0.545299 | 0.185141 | 0.714643 | 0.014982 |

player_round_glicko − coin (paired log loss):

| Section | Rows | player_round_glicko log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4076 | 0.544875 | 0.693147 | -0.148272 | [-0.161679, -0.134282] | yes |
| tier1 | 40 | 0.591610 | 0.693147 | -0.101537 | [-0.216616, 0.022731] | no |
| tier2 | 438 | 0.591393 | 0.693147 | -0.101754 | [-0.146426, -0.054551] | yes |
| tier3 | 3598 | 0.538692 | 0.693147 | -0.154455 | [-0.168707, -0.139871] | yes |
| international=1 | 81 | 0.523929 | 0.693147 | -0.169218 | [-0.259849, -0.071342] | yes |
| international=0 | 3995 | 0.545299 | 0.693147 | -0.147848 | [-0.161992, -0.133984] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko_rookie | all | 4076 | 0.534081 | 0.179720 | 0.732090 | 0.024656 |
| player_round_glicko_rookie | tier1 | 40 | 0.590019 | 0.205000 | 0.625000 | 0.162573 |
| player_round_glicko_rookie | tier2 | 438 | 0.597910 | 0.204353 | 0.689498 | 0.068044 |
| player_round_glicko_rookie | tier3 | 3598 | 0.525689 | 0.176440 | 0.738466 | 0.028266 |
| player_round_glicko_rookie | unknown | 0 | — | — | — | — |
| player_round_glicko_rookie | international=1 | 81 | 0.523688 | 0.177145 | 0.716049 | 0.144984 |
| player_round_glicko_rookie | international=0 | 3995 | 0.534292 | 0.179772 | 0.732416 | 0.024779 |

player_round_glicko_rookie − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4076 | 0.534081 | 0.693147 | -0.159066 | [-0.173850, -0.143495] | yes |
| tier1 | 40 | 0.590019 | 0.693147 | -0.103128 | [-0.215229, 0.014996] | no |
| tier2 | 438 | 0.597910 | 0.693147 | -0.095237 | [-0.140976, -0.046125] | yes |
| tier3 | 3598 | 0.525689 | 0.693147 | -0.167458 | [-0.182625, -0.151613] | yes |
| international=1 | 81 | 0.523688 | 0.693147 | -0.169460 | [-0.264517, -0.067666] | yes |
| international=0 | 3995 | 0.534292 | 0.693147 | -0.158855 | [-0.174183, -0.143418] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| team_elo+none | all | 4076 | 0.613538 | 0.213060 | 0.645363 | 0.027632 |
| team_elo+none | tier1 | 40 | 0.601920 | 0.206311 | 0.625000 | 0.162277 |
| team_elo+none | tier2 | 438 | 0.646846 | 0.222475 | 0.635845 | 0.094342 |
| team_elo+none | tier3 | 3598 | 0.609613 | 0.211989 | 0.646748 | 0.026256 |
| team_elo+none | unknown | 0 | — | — | — | — |
| team_elo+none | international=1 | 81 | 0.571789 | 0.195384 | 0.654321 | 0.110870 |
| team_elo+none | international=0 | 3995 | 0.614385 | 0.213418 | 0.645181 | 0.026616 |

team_elo+none − coin (paired log loss):

| Section | Rows | team_elo+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4076 | 0.613538 | 0.693147 | -0.079609 | [-0.091439, -0.066774] | yes |
| tier1 | 40 | 0.601920 | 0.693147 | -0.091227 | [-0.185427, 0.012465] | no |
| tier2 | 438 | 0.646846 | 0.693147 | -0.046301 | [-0.099441, 0.007905] | no |
| tier3 | 3598 | 0.609613 | 0.693147 | -0.083534 | [-0.095534, -0.071651] | yes |
| international=1 | 81 | 0.571789 | 0.693147 | -0.121358 | [-0.187354, -0.049655] | yes |
| international=0 | 3995 | 0.614385 | 0.693147 | -0.078762 | [-0.091040, -0.066858] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| team_elo+calibration | all | 4076 | 0.612743 | 0.213002 | 0.645363 | 0.028472 |
| team_elo+calibration | tier1 | 40 | 0.645344 | 0.226332 | 0.625000 | 0.084726 |
| team_elo+calibration | tier2 | 438 | 0.629720 | 0.218395 | 0.635845 | 0.077231 |
| team_elo+calibration | tier3 | 3598 | 0.610314 | 0.212198 | 0.646748 | 0.026642 |
| team_elo+calibration | unknown | 0 | — | — | — | — |
| team_elo+calibration | international=1 | 81 | 0.592065 | 0.205072 | 0.654321 | 0.124752 |
| team_elo+calibration | international=0 | 3995 | 0.613162 | 0.213163 | 0.645181 | 0.026616 |

team_elo+calibration − coin (paired log loss):

| Section | Rows | team_elo+calibration log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4076 | 0.612743 | 0.693147 | -0.080404 | [-0.091431, -0.068257] | yes |
| tier1 | 40 | 0.645344 | 0.693147 | -0.047804 | [-0.084462, -0.008485] | yes |
| tier2 | 438 | 0.629720 | 0.693147 | -0.063428 | [-0.109322, -0.016383] | yes |
| tier3 | 3598 | 0.610314 | 0.693147 | -0.082833 | [-0.094526, -0.071304] | yes |
| international=1 | 81 | 0.592065 | 0.693147 | -0.101082 | [-0.156877, -0.044035] | yes |
| international=0 | 3995 | 0.613162 | 0.693147 | -0.079985 | [-0.091464, -0.068450] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko+none | all | 4076 | 0.544875 | 0.184988 | 0.714917 | 0.015559 |
| player_round_glicko+none | tier1 | 40 | 0.591610 | 0.205202 | 0.650000 | 0.134710 |
| player_round_glicko+none | tier2 | 438 | 0.591393 | 0.203388 | 0.689498 | 0.072477 |
| player_round_glicko+none | tier3 | 3598 | 0.538692 | 0.182524 | 0.718733 | 0.018392 |
| player_round_glicko+none | unknown | 0 | — | — | — | — |
| player_round_glicko+none | international=1 | 81 | 0.523929 | 0.177455 | 0.728395 | 0.105587 |
| player_round_glicko+none | international=0 | 3995 | 0.545299 | 0.185141 | 0.714643 | 0.014982 |

player_round_glicko+none − coin (paired log loss):

| Section | Rows | player_round_glicko+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4076 | 0.544875 | 0.693147 | -0.148272 | [-0.161679, -0.134282] | yes |
| tier1 | 40 | 0.591610 | 0.693147 | -0.101537 | [-0.216616, 0.022731] | no |
| tier2 | 438 | 0.591393 | 0.693147 | -0.101754 | [-0.146426, -0.054551] | yes |
| tier3 | 3598 | 0.538692 | 0.693147 | -0.154455 | [-0.168707, -0.139871] | yes |
| international=1 | 81 | 0.523929 | 0.693147 | -0.169218 | [-0.259849, -0.071342] | yes |
| international=0 | 3995 | 0.545299 | 0.693147 | -0.147848 | [-0.161992, -0.133984] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko+calibration | all | 4076 | 0.544761 | 0.184921 | 0.714917 | 0.014281 |
| player_round_glicko+calibration | tier1 | 40 | 0.595392 | 0.206159 | 0.650000 | 0.088323 |
| player_round_glicko+calibration | tier2 | 438 | 0.592249 | 0.203647 | 0.689498 | 0.071794 |
| player_round_glicko+calibration | tier3 | 3598 | 0.538417 | 0.182406 | 0.718733 | 0.015551 |
| player_round_glicko+calibration | unknown | 0 | — | — | — | — |
| player_round_glicko+calibration | international=1 | 81 | 0.525803 | 0.177932 | 0.728395 | 0.091517 |
| player_round_glicko+calibration | international=0 | 3995 | 0.545145 | 0.185063 | 0.714643 | 0.013557 |

player_round_glicko+calibration − coin (paired log loss):

| Section | Rows | player_round_glicko+calibration log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4076 | 0.544761 | 0.693147 | -0.148387 | [-0.162002, -0.134290] | yes |
| tier1 | 40 | 0.595392 | 0.693147 | -0.097756 | [-0.190733, -0.001633] | yes |
| tier2 | 438 | 0.592249 | 0.693147 | -0.100898 | [-0.146133, -0.053388] | yes |
| tier3 | 3598 | 0.538417 | 0.693147 | -0.154730 | [-0.169280, -0.139761] | yes |
| international=1 | 81 | 0.525803 | 0.693147 | -0.167344 | [-0.250391, -0.076785] | yes |
| international=0 | 3995 | 0.545145 | 0.693147 | -0.148002 | [-0.162398, -0.133826] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko_rookie+none | all | 4076 | 0.534081 | 0.179720 | 0.732090 | 0.024656 |
| player_round_glicko_rookie+none | tier1 | 40 | 0.590019 | 0.205000 | 0.625000 | 0.162573 |
| player_round_glicko_rookie+none | tier2 | 438 | 0.597910 | 0.204353 | 0.689498 | 0.068044 |
| player_round_glicko_rookie+none | tier3 | 3598 | 0.525689 | 0.176440 | 0.738466 | 0.028266 |
| player_round_glicko_rookie+none | unknown | 0 | — | — | — | — |
| player_round_glicko_rookie+none | international=1 | 81 | 0.523688 | 0.177145 | 0.716049 | 0.144984 |
| player_round_glicko_rookie+none | international=0 | 3995 | 0.534292 | 0.179772 | 0.732416 | 0.024779 |

player_round_glicko_rookie+none − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4076 | 0.534081 | 0.693147 | -0.159066 | [-0.173850, -0.143495] | yes |
| tier1 | 40 | 0.590019 | 0.693147 | -0.103128 | [-0.215229, 0.014996] | no |
| tier2 | 438 | 0.597910 | 0.693147 | -0.095237 | [-0.140976, -0.046125] | yes |
| tier3 | 3598 | 0.525689 | 0.693147 | -0.167458 | [-0.182625, -0.151613] | yes |
| international=1 | 81 | 0.523688 | 0.693147 | -0.169460 | [-0.264517, -0.067666] | yes |
| international=0 | 3995 | 0.534292 | 0.693147 | -0.158855 | [-0.174183, -0.143418] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko_rookie+calibration | all | 4076 | 0.533684 | 0.179673 | 0.732090 | 0.023646 |
| player_round_glicko_rookie+calibration | tier1 | 40 | 0.595580 | 0.206233 | 0.625000 | 0.123246 |
| player_round_glicko_rookie+calibration | tier2 | 438 | 0.597059 | 0.203995 | 0.689498 | 0.078308 |
| player_round_glicko_rookie+calibration | tier3 | 3598 | 0.525281 | 0.176416 | 0.738466 | 0.028186 |
| player_round_glicko_rookie+calibration | unknown | 0 | — | — | — | — |
| player_round_glicko_rookie+calibration | international=1 | 81 | 0.526388 | 0.177729 | 0.716049 | 0.145340 |
| player_round_glicko_rookie+calibration | international=0 | 3995 | 0.533832 | 0.179712 | 0.732416 | 0.023886 |

player_round_glicko_rookie+calibration − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie+calibration log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4076 | 0.533684 | 0.693147 | -0.159463 | [-0.173795, -0.144486] | yes |
| tier1 | 40 | 0.595580 | 0.693147 | -0.097567 | [-0.186918, -0.006974] | yes |
| tier2 | 438 | 0.597059 | 0.693147 | -0.096088 | [-0.142635, -0.046486] | yes |
| tier3 | 3598 | 0.525281 | 0.693147 | -0.167866 | [-0.182597, -0.152454] | yes |
| international=1 | 81 | 0.526388 | 0.693147 | -0.166760 | [-0.254646, -0.072038] | yes |
| international=0 | 3995 | 0.533832 | 0.693147 | -0.159315 | [-0.174351, -0.144319] | yes |

player_round_glicko − team_elo (paired log loss):

| Section | Rows | player_round_glicko log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4076 | 0.544875 | 0.613538 | -0.068664 | [-0.079304, -0.058273] | yes |

player_round_glicko_rookie − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4076 | 0.534081 | 0.613538 | -0.079457 | [-0.091320, -0.067522] | yes |

team_elo+none − team_elo (paired log loss):

| Section | Rows | team_elo+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4076 | 0.613538 | 0.613538 | 0.000000 | [0.000000, 0.000000] | no |

team_elo+calibration − team_elo (paired log loss):

| Section | Rows | team_elo+calibration log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4076 | 0.612743 | 0.613538 | -0.000795 | [-0.002355, 0.000683] | no |

player_round_glicko+none − team_elo (paired log loss):

| Section | Rows | player_round_glicko+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4076 | 0.544875 | 0.613538 | -0.068664 | [-0.079304, -0.058273] | yes |

player_round_glicko+calibration − team_elo (paired log loss):

| Section | Rows | player_round_glicko+calibration log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4076 | 0.544761 | 0.613538 | -0.068778 | [-0.079508, -0.058173] | yes |

player_round_glicko_rookie+none − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4076 | 0.534081 | 0.613538 | -0.079457 | [-0.091320, -0.067522] | yes |

player_round_glicko_rookie+calibration − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie+calibration log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4076 | 0.533684 | 0.613538 | -0.079854 | [-0.091396, -0.068190] | yes |

player_round_glicko − player_round_glicko_rookie (paired log loss):

| Section | Rows | player_round_glicko log loss | player_round_glicko_rookie log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4076 | 0.544875 | 0.534081 | 0.010793 | [0.005984, 0.015083] | yes |
| tier1 | 40 | 0.591610 | 0.590019 | 0.001592 | [-0.006079, 0.010522] | no |
| tier2 | 438 | 0.591393 | 0.597910 | -0.006517 | [-0.015139, 0.000362] | no |
| tier3 | 3598 | 0.538692 | 0.525689 | 0.013003 | [0.008019, 0.017931] | yes |
| international=1 | 81 | 0.523929 | 0.523688 | 0.000242 | [-0.018043, 0.017419] | no |
| international=0 | 3995 | 0.545299 | 0.534292 | 0.011007 | [0.006535, 0.015898] | yes |

team_elo+none − player_round_glicko_rookie (paired log loss):

| Section | Rows | team_elo+none log loss | player_round_glicko_rookie log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4076 | 0.613538 | 0.534081 | 0.079457 | [0.067522, 0.091320] | yes |
| tier1 | 40 | 0.601920 | 0.590019 | 0.011901 | [-0.075829, 0.095085] | no |
| tier2 | 438 | 0.646846 | 0.597910 | 0.048936 | [0.013487, 0.085773] | yes |
| tier3 | 3598 | 0.609613 | 0.525689 | 0.083923 | [0.070593, 0.097059] | yes |
| international=1 | 81 | 0.571789 | 0.523688 | 0.048101 | [-0.025978, 0.116352] | no |
| international=0 | 3995 | 0.614385 | 0.534292 | 0.080093 | [0.068301, 0.092911] | yes |

team_elo+calibration − player_round_glicko_rookie (paired log loss):

| Section | Rows | team_elo+calibration log loss | player_round_glicko_rookie log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4076 | 0.612743 | 0.534081 | 0.078661 | [0.066840, 0.090367] | yes |
| tier1 | 40 | 0.645344 | 0.590019 | 0.055325 | [-0.041272, 0.147569] | no |
| tier2 | 438 | 0.629720 | 0.597910 | 0.031809 | [-0.000825, 0.066012] | no |
| tier3 | 3598 | 0.610314 | 0.525689 | 0.084624 | [0.071413, 0.097815] | yes |
| international=1 | 81 | 0.592065 | 0.523688 | 0.068377 | [-0.010137, 0.142448] | no |
| international=0 | 3995 | 0.613162 | 0.534292 | 0.078870 | [0.067005, 0.091663] | yes |

player_round_glicko+none − player_round_glicko_rookie (paired log loss):

| Section | Rows | player_round_glicko+none log loss | player_round_glicko_rookie log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4076 | 0.544875 | 0.534081 | 0.010793 | [0.005984, 0.015083] | yes |
| tier1 | 40 | 0.591610 | 0.590019 | 0.001592 | [-0.006079, 0.010522] | no |
| tier2 | 438 | 0.591393 | 0.597910 | -0.006517 | [-0.015139, 0.000362] | no |
| tier3 | 3598 | 0.538692 | 0.525689 | 0.013003 | [0.008019, 0.017931] | yes |
| international=1 | 81 | 0.523929 | 0.523688 | 0.000242 | [-0.018043, 0.017419] | no |
| international=0 | 3995 | 0.545299 | 0.534292 | 0.011007 | [0.006535, 0.015898] | yes |

player_round_glicko+calibration − player_round_glicko_rookie (paired log loss):

| Section | Rows | player_round_glicko+calibration log loss | player_round_glicko_rookie log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4076 | 0.544761 | 0.534081 | 0.010679 | [0.005996, 0.015068] | yes |
| tier1 | 40 | 0.595392 | 0.590019 | 0.005373 | [-0.020358, 0.028764] | no |
| tier2 | 438 | 0.592249 | 0.597910 | -0.005661 | [-0.014186, 0.001106] | no |
| tier3 | 3598 | 0.538417 | 0.525689 | 0.012727 | [0.007749, 0.017652] | yes |
| international=1 | 81 | 0.525803 | 0.523688 | 0.002115 | [-0.019693, 0.022656] | no |
| international=0 | 3995 | 0.545145 | 0.534292 | 0.010853 | [0.006508, 0.015691] | yes |

player_round_glicko_rookie+none − player_round_glicko_rookie (paired log loss):

| Section | Rows | player_round_glicko_rookie+none log loss | player_round_glicko_rookie log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4076 | 0.534081 | 0.534081 | 0.000000 | [0.000000, 0.000000] | no |
| tier1 | 40 | 0.590019 | 0.590019 | 0.000000 | [0.000000, 0.000000] | no |
| tier2 | 438 | 0.597910 | 0.597910 | 0.000000 | [0.000000, 0.000000] | no |
| tier3 | 3598 | 0.525689 | 0.525689 | 0.000000 | [0.000000, 0.000000] | no |
| international=1 | 81 | 0.523688 | 0.523688 | 0.000000 | [0.000000, 0.000000] | no |
| international=0 | 3995 | 0.534292 | 0.534292 | 0.000000 | [0.000000, 0.000000] | no |

player_round_glicko_rookie+calibration − player_round_glicko_rookie (paired log loss):

| Section | Rows | player_round_glicko_rookie+calibration log loss | player_round_glicko_rookie log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4076 | 0.533684 | 0.534081 | -0.000397 | [-0.001171, 0.000366] | no |
| tier1 | 40 | 0.595580 | 0.590019 | 0.005561 | [-0.024720, 0.033469] | no |
| tier2 | 438 | 0.597059 | 0.597910 | -0.000851 | [-0.002869, 0.001374] | no |
| tier3 | 3598 | 0.525281 | 0.525689 | -0.000409 | [-0.001151, 0.000337] | no |
| international=1 | 81 | 0.526388 | 0.523688 | 0.002700 | [-0.013425, 0.015992] | no |
| international=0 | 3995 | 0.533832 | 0.534292 | -0.000460 | [-0.001184, 0.000278] | no |

## Holdout vs Kalshi

### team_elo: Kalshi comparison and returns



#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 324 | 0.662044 | 0.582065 | 0.079979 [0.043015, 0.119700] | yes |
| series | tier1 | 33 | 0.612331 | 0.584463 | 0.027867 [-0.054989, 0.107649] | no |
| series | tier2 | 284 | 0.669892 | 0.584967 | 0.084925 [0.042541, 0.127505] | yes |
| series | tier3 | 7 | 0.578023 | 0.453037 | 0.124986 [-0.016154, 0.256621] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 33 | 0.612331 | 0.584463 | 0.027867 [-0.054989, 0.107649] | no |
| series | international=0 | 291 | 0.667682 | 0.581793 | 0.085889 [0.043771, 0.128943] | yes |
| map | all | 81 | 0.677740 | 0.712390 | -0.034649 [-0.078626, 0.008810] | no |
| map | tier1 | 40 | 0.749962 | 0.763024 | -0.013062 [-0.071348, 0.046940] | no |
| map | tier2 | 39 | 0.633857 | 0.682577 | -0.048720 [-0.111817, 0.007999] | no |
| map | tier3 | 2 | 0.089025 | 0.281038 | -0.192012 [-0.192012, -0.192012] | yes |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 40 | 0.749962 | 0.763024 | -0.013062 [-0.071348, 0.046940] | no |
| map | international=0 | 41 | 0.607280 | 0.662990 | -0.055710 [-0.115125, 0.003638] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 262 | 262 | 0.0972 | -19.23% [-31.73%, -6.36%] | $0.09 | 0.002× | 99.82% | $4.84 | 138 (124 unfilled) | -17.68% [-33.79%, -1.07%] | $1.98 |
| series | tier1 | 27 | 27 | 0.1024 | -20.98% [-54.95%, 16.64%] | $32.70 | 0.654× | 42.81% | $5.46 | 21 (6 unfilled) | -14.52% [-53.38%, 26.02%] | $42.87 |
| series | tier2 | 229 | 229 | 0.0970 | -18.14% [-31.41%, -5.36%] | $0.34 | 0.007× | 99.32% | $4.84 | 116 (113 unfilled) | -18.57% [-35.19%, -0.33%] | $2.95 |
| series | tier3 | 6 | 6 | 0.0819 | -52.83% [-100.00%, 7.00%] | $33.88 | 0.678× | 33.33% | $5.01 | 1 (5 unfilled) | 19.56% [19.56%, 19.56%] | $50.47 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 27 | 27 | 0.1024 | -20.98% [-54.95%, 16.64%] | $32.70 | 0.654× | 42.81% | $5.46 | 21 (6 unfilled) | -14.52% [-53.38%, 26.02%] | $42.87 |
| series | international=0 | 235 | 235 | 0.0966 | -19.03% [-31.27%, -5.42%] | $0.22 | 0.004× | 99.57% | $4.84 | 117 (118 unfilled) | -18.25% [-34.17%, 0.52%] | $2.52 |
| map | all | 59 | 32 | 0.1097 | 21.73% [1.69%, 43.05%] | $87.41 | 1.748× | 11.11% | $7.27 | 9 (50 unfilled) | 8.57% [-58.27%, 86.43%] | $51.54 |
| map | tier1 | 28 | 14 | 0.0866 | 6.68% [-25.44%, 37.54%] | $57.40 | 1.148× | 10.00% | $3.05 | 8 (20 unfilled) | 6.07% [-69.75%, 89.71%] | $50.59 |
| map | tier2 | 29 | 17 | 0.1298 | 35.78% [9.83%, 65.70%] | $73.93 | 1.479× | 3.15% | $7.27 | 0 (29 unfilled) | — | $50.00 |
| map | tier3 | 2 | 1 | 0.1421 | 29.00% [29.00%, 29.00%] | $51.45 | 1.029× | 0.00% | $2.45 | 1 (1 unfilled) | 29.00% [29.00%, 29.00%] | $50.94 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 28 | 14 | 0.0866 | 6.68% [-25.44%, 37.54%] | $57.40 | 1.148× | 10.00% | $3.05 | 8 (20 unfilled) | 6.07% [-69.75%, 89.71%] | $50.59 |
| map | international=0 | 31 | 18 | 0.1306 | 35.35% [10.79%, 65.95%] | $76.09 | 1.522× | 3.15% | $7.27 | 1 (30 unfilled) | 29.00% [29.00%, 29.00%] | $50.94 |
| series+map | all | 321 | 264 | 0.0995 | -11.68% [-22.60%, -0.35%] | $0.40 | 0.008× | 99.20% | $4.84 | 147 (174 unfilled) | -16.07% [-31.34%, -0.93%] | $2.52 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 0 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-07 | series | 244 | 0.969949 | -0.072315 | fitted |
| 2026-07 | map | 109 | 0.440147 | -0.086052 | fitted |
| 2026-08 | series | 244 | 0.969949 | -0.072315 | fitted |
| 2026-08 | map | 109 | 0.440147 | -0.086052 | fitted |
| 2026-09 | series | 244 | 0.969949 | -0.072315 | fitted |
| 2026-10 | series | 244 | 0.969949 | -0.072315 | fitted |
| 2026-10 | map | 109 | 0.440147 | -0.086052 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 324 | 0.580992 | 0.582065 | -0.001073 [-0.004225, 0.001952] | no |
| series | tier1 | 33 | 0.586890 | 0.584463 | 0.002427 [-0.003097, 0.008382] | no |
| series | tier2 | 284 | 0.583504 | 0.584967 | -0.001463 [-0.005024, 0.002061] | no |
| series | tier3 | 7 | 0.451258 | 0.453037 | -0.001778 [-0.014086, 0.009840] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 33 | 0.586890 | 0.584463 | 0.002427 [-0.003097, 0.008382] | no |
| series | international=0 | 291 | 0.580323 | 0.581793 | -0.001470 [-0.005023, 0.001890] | no |
| map | all | 81 | 0.698023 | 0.712390 | -0.014366 [-0.061070, 0.026603] | no |
| map | tier1 | 40 | 0.718442 | 0.763024 | -0.044583 [-0.123601, 0.010774] | no |
| map | tier2 | 39 | 0.686319 | 0.682577 | 0.003742 [-0.049496, 0.054366] | no |
| map | tier3 | 2 | 0.517877 | 0.281038 | 0.236839 [0.236839, 0.236839] | yes |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 40 | 0.718442 | 0.763024 | -0.044583 [-0.123601, 0.010774] | no |
| map | international=0 | 41 | 0.678102 | 0.662990 | 0.015113 [-0.037669, 0.069983] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 5 | 5 | 0.0077 | 18.26% [-100.00%, 141.59%] | $49.84 | 0.997× | 3.62% | $1.61 | 2 (3 unfilled) | 52.16% [-100.00%, 207.22%] | $50.75 |
| series | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier2 | 5 | 5 | 0.0077 | 18.26% [-100.00%, 141.59%] | $49.84 | 0.997× | 3.62% | $1.61 | 2 (3 unfilled) | 52.16% [-100.00%, 207.22%] | $50.75 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=0 | 5 | 5 | 0.0077 | 18.26% [-100.00%, 141.59%] | $49.84 | 0.997× | 3.62% | $1.61 | 2 (3 unfilled) | 52.16% [-100.00%, 207.22%] | $50.75 |
| map | all | 61 | 33 | 0.0404 | 20.32% [-12.99%, 57.27%] | $80.84 | 1.617× | 20.76% | $4.37 | 10 (51 unfilled) | -5.86% [-80.80%, 110.78%] | $50.29 |
| map | tier1 | 27 | 14 | 0.0291 | 54.13% [1.08%, 119.96%] | $83.05 | 1.661× | 6.43% | $4.04 | 7 (20 unfilled) | 34.93% [-71.22%, 185.69%] | $58.91 |
| map | tier2 | 32 | 18 | 0.0437 | -0.54% [-44.13%, 42.75%] | $54.09 | 1.082× | 20.76% | $4.08 | 1 (31 unfilled) | -100.00% [-100.00%, -100.00%] | $47.45 |
| map | tier3 | 2 | 1 | 0.1411 | -100.00% [-100.00%, -100.00%] | $45.00 | 0.900× | 10.00% | $2.37 | 2 (0 unfilled) | -100.00% [-100.00%, -100.00%] | $45.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 27 | 14 | 0.0291 | 54.13% [1.08%, 119.96%] | $83.05 | 1.661× | 6.43% | $4.04 | 7 (20 unfilled) | 34.93% [-71.22%, 185.69%] | $58.91 |
| map | international=0 | 34 | 19 | 0.0494 | -6.45% [-49.46%, 34.63%] | $48.68 | 0.974× | 20.76% | $4.08 | 3 (31 unfilled) | -100.00% [-100.00%, -100.00%] | $42.71 |
| series+map | all | 66 | 38 | 0.0379 | 20.17% [-15.70%, 55.30%] | $80.58 | 1.612× | 20.76% | $4.37 | 12 (54 unfilled) | 3.87% [-78.01%, 107.51%] | $51.02 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-07 | 39 | 0.633857 | 0.686319 | 0.682577 | 35.78% (29), $73.93 | -0.54% (32), $54.09 | 0 (29 unfilled) | — | $50.00 | 1 (31 unfilled) | -100.00% [-100.00%, -100.00%] | $47.45 |
| map | 2026-08 | 40 | 0.749962 | 0.718442 | 0.763024 | 6.68% (28), $57.40 | 54.13% (27), $83.05 | 8 (20 unfilled) | 6.07% [-69.75%, 89.71%] | $50.59 | 7 (20 unfilled) | 34.93% [-71.22%, 185.69%] | $58.91 |
| map | 2026-10 | 2 | 0.089025 | 0.517877 | 0.281038 | 29.00% (2), $51.45 | -100.00% (2), $45.00 | 1 (1 unfilled) | 29.00% [29.00%, 29.00%] | $50.94 | 2 (0 unfilled) | -100.00% [-100.00%, -100.00%] | $45.00 |
| series | 2026-07 | 48 | 0.769251 | 0.598508 | 0.605402 | -29.54% (40), $14.72 | — (0), $50.00 | 23 (17 unfilled) | -30.68% [-74.76%, 23.27%] | $26.71 | 0 (0 unfilled) | — | $50.00 |
| series | 2026-08 | 33 | 0.612331 | 0.586890 | 0.584463 | -20.98% (27), $32.70 | — (0), $50.00 | 21 (6 unfilled) | -14.52% [-53.38%, 26.02%] | $42.87 | 0 (0 unfilled) | — | $50.00 |
| series | 2026-09 | 192 | 0.633187 | 0.569206 | 0.568687 | -15.35% (159), $2.76 | -23.92% (4), $48.99 | 81 (78 unfilled) | -17.19% [-36.95%, 2.86%] | $8.03 | 2 (2 unfilled) | 52.16% [-100.00%, 207.22%] | $50.75 |
| series | 2026-10 | 51 | 0.701947 | 0.605059 | 0.608911 | -23.50% (36), $23.14 | 188.60% (1), $50.84 | 13 (23 unfilled) | -2.84% [-55.87%, 55.94%] | $42.16 | 0 (1 unfilled) | — | $50.00 |

### player_round_glicko: Kalshi comparison and returns



#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 324 | 0.597459 | 0.582065 | 0.015395 [-0.008073, 0.038488] | no |
| series | tier1 | 33 | 0.621289 | 0.584463 | 0.036826 [-0.052932, 0.128460] | no |
| series | tier2 | 284 | 0.593866 | 0.584967 | 0.008900 [-0.014027, 0.033898] | no |
| series | tier3 | 7 | 0.630899 | 0.453037 | 0.177862 [0.024913, 0.334549] | yes |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 33 | 0.621289 | 0.584463 | 0.036826 [-0.052932, 0.128460] | no |
| series | international=0 | 291 | 0.594757 | 0.581793 | 0.012964 [-0.010517, 0.038379] | no |
| map | all | 81 | 0.688352 | 0.712390 | -0.024037 [-0.061335, 0.012439] | no |
| map | tier1 | 40 | 0.713073 | 0.763024 | -0.049951 [-0.114817, 0.011929] | no |
| map | tier2 | 39 | 0.688649 | 0.682577 | 0.006072 [-0.032422, 0.043353] | no |
| map | tier3 | 2 | 0.188159 | 0.281038 | -0.092878 [-0.092878, -0.092878] | yes |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 40 | 0.713073 | 0.763024 | -0.049951 [-0.114817, 0.011929] | no |
| map | international=0 | 41 | 0.664234 | 0.662990 | 0.001245 [-0.034782, 0.035819] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 216 | 216 | 0.0742 | -14.31% [-27.90%, -0.81%] | $4.63 | 0.093× | 92.13% | $5.72 | 105 (111 unfilled) | -11.22% [-28.66%, 8.09%] | $25.06 |
| series | tier1 | 26 | 26 | 0.1059 | -27.13% [-59.60%, 10.04%] | $30.83 | 0.617× | 38.35% | $4.92 | 20 (6 unfilled) | -18.47% [-57.27%, 23.65%] | $39.28 |
| series | tier2 | 185 | 185 | 0.0690 | -10.81% [-25.25%, 5.16%] | $11.61 | 0.232× | 86.86% | $5.72 | 84 (101 unfilled) | -9.84% [-31.32%, 11.85%] | $33.22 |
| series | tier3 | 5 | 5 | 0.1027 | -76.59% [-100.00%, -28.96%] | $33.13 | 0.663× | 33.73% | $4.93 | 1 (4 unfilled) | 19.56% [19.56%, 19.56%] | $50.47 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 26 | 26 | 0.1059 | -27.13% [-59.60%, 10.04%] | $30.83 | 0.617× | 38.35% | $4.92 | 20 (6 unfilled) | -18.47% [-57.27%, 23.65%] | $39.28 |
| series | international=0 | 190 | 190 | 0.0699 | -12.55% [-27.10%, 2.12%] | $7.64 | 0.153× | 87.01% | $5.72 | 85 (105 unfilled) | -9.50% [-29.99%, 10.79%] | $33.37 |
| map | all | 54 | 29 | 0.0703 | 13.75% [-12.60%, 39.13%] | $60.33 | 1.207× | 16.96% | $4.41 | 6 (48 unfilled) | 17.78% [-54.56%, 82.18%] | $51.22 |
| map | tier1 | 27 | 14 | 0.0877 | 19.15% [-16.26%, 55.66%] | $63.13 | 1.263× | 9.77% | $4.31 | 5 (22 unfilled) | 15.58% [-70.92%, 102.41%] | $50.27 |
| map | tier2 | 25 | 14 | 0.0527 | 6.73% [-31.67%, 48.90%] | $46.46 | 0.929× | 16.96% | $4.41 | 0 (25 unfilled) | — | $50.00 |
| map | tier3 | 2 | 1 | 0.0557 | 29.00% [29.00%, 29.00%] | $51.45 | 1.029× | 0.00% | $2.45 | 1 (1 unfilled) | 29.00% [29.00%, 29.00%] | $50.94 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 27 | 14 | 0.0877 | 19.15% [-16.26%, 55.66%] | $63.13 | 1.263× | 9.77% | $4.31 | 5 (22 unfilled) | 15.58% [-70.92%, 102.41%] | $50.27 |
| map | international=0 | 27 | 15 | 0.0529 | 8.35% [-27.04%, 49.07%] | $47.82 | 0.956× | 16.96% | $4.41 | 1 (26 unfilled) | 29.00% [29.00%, 29.00%] | $50.94 |
| series+map | all | 270 | 218 | 0.0735 | -8.69% [-21.75%, 4.76%] | $7.34 | 0.147× | 87.52% | $5.72 | 111 (159 unfilled) | -9.65% [-27.47%, 7.20%] | $28.52 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 0 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-07 | series | 244 | 1.056071 | 0.276239 | fitted |
| 2026-07 | map | 109 | 0.522513 | 0.249933 | fitted |
| 2026-08 | series | 244 | 1.056071 | 0.276239 | fitted |
| 2026-08 | map | 109 | 0.522513 | 0.249933 | fitted |
| 2026-09 | series | 244 | 1.056071 | 0.276239 | fitted |
| 2026-10 | series | 244 | 1.056071 | 0.276239 | fitted |
| 2026-10 | map | 109 | 0.522513 | 0.249933 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 324 | 0.579335 | 0.582065 | -0.002730 [-0.010283, 0.004265] | no |
| series | tier1 | 33 | 0.582210 | 0.584463 | -0.002254 [-0.029240, 0.023239] | no |
| series | tier2 | 284 | 0.581292 | 0.584967 | -0.003675 [-0.010830, 0.004250] | no |
| series | tier3 | 7 | 0.486399 | 0.453037 | 0.033362 [-0.008901, 0.081342] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 33 | 0.582210 | 0.584463 | -0.002254 [-0.029240, 0.023239] | no |
| series | international=0 | 291 | 0.579009 | 0.581793 | -0.002784 [-0.010393, 0.005163] | no |
| map | all | 81 | 0.683085 | 0.712390 | -0.029305 [-0.070024, 0.006062] | no |
| map | tier1 | 40 | 0.704864 | 0.763024 | -0.058160 [-0.129056, -0.007708] | yes |
| map | tier2 | 39 | 0.675107 | 0.682577 | -0.007470 [-0.055749, 0.035064] | no |
| map | tier3 | 2 | 0.403053 | 0.281038 | 0.122016 [0.122016, 0.122016] | yes |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 40 | 0.704864 | 0.763024 | -0.058160 [-0.129056, -0.007708] | yes |
| map | international=0 | 41 | 0.661836 | 0.662990 | -0.001153 [-0.047678, 0.041608] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 85 | 85 | 0.0212 | 4.64% [-13.55%, 24.93%] | $65.55 | 1.311× | 12.67% | $6.87 | 41 (44 unfilled) | -0.03% [-23.54%, 24.43%] | $51.18 |
| series | tier1 | 15 | 15 | 0.0198 | 6.74% [-41.79%, 54.84%] | $55.44 | 1.109× | 2.92% | $4.99 | 12 (3 unfilled) | 22.69% [-29.82%, 76.13%] | $55.98 |
| series | tier2 | 67 | 67 | 0.0219 | 7.11% [-14.14%, 31.44%] | $62.37 | 1.247× | 12.66% | $6.19 | 28 (39 unfilled) | -10.59% [-36.94%, 14.44%] | $45.80 |
| series | tier3 | 3 | 3 | 0.0113 | -60.66% [-100.00%, 19.56%] | $47.33 | 0.947× | 6.37% | $2.71 | 1 (2 unfilled) | 19.56% [19.56%, 19.56%] | $50.02 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 15 | 15 | 0.0198 | 6.74% [-41.79%, 54.84%] | $55.44 | 1.109× | 2.92% | $4.99 | 12 (3 unfilled) | 22.69% [-29.82%, 76.13%] | $55.98 |
| series | international=0 | 70 | 70 | 0.0215 | 4.18% [-15.80%, 26.99%] | $59.05 | 1.181× | 12.66% | $6.19 | 29 (41 unfilled) | -9.56% [-34.95%, 14.85%] | $45.77 |
| map | all | 54 | 29 | 0.0442 | 25.66% [-10.52%, 66.37%] | $97.93 | 1.959× | 19.31% | $5.37 | 10 (44 unfilled) | 36.87% [-55.26%, 149.31%] | $57.20 |
| map | tier1 | 26 | 14 | 0.0424 | 64.22% [14.87%, 125.15%] | $92.35 | 1.847× | 8.56% | $4.56 | 7 (19 unfilled) | 96.17% [-5.40%, 200.01%] | $66.80 |
| map | tier2 | 26 | 14 | 0.0440 | -2.99% [-50.32%, 47.10%] | $58.89 | 1.178× | 19.31% | $4.45 | 1 (25 unfilled) | -100.00% [-100.00%, -100.00%] | $47.47 |
| map | tier3 | 2 | 1 | 0.0686 | -100.00% [-100.00%, -100.00%] | $45.00 | 0.900× | 10.00% | $2.37 | 2 (0 unfilled) | -100.00% [-100.00%, -100.00%] | $45.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 26 | 14 | 0.0424 | 64.22% [14.87%, 125.15%] | $92.35 | 1.847× | 8.56% | $4.56 | 7 (19 unfilled) | 96.17% [-5.40%, 200.01%] | $66.80 |
| map | international=0 | 28 | 15 | 0.0458 | -9.97% [-56.53%, 39.54%] | $53.00 | 1.060× | 19.31% | $4.45 | 3 (25 unfilled) | -100.00% [-100.00%, -100.00%] | $42.72 |
| series+map | all | 139 | 104 | 0.0301 | 12.91% [-6.08%, 33.01%] | $122.79 | 2.456× | 19.31% | $14.05 | 51 (88 unfilled) | 7.33% [-17.54%, 35.89%] | $55.97 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-07 | 39 | 0.688649 | 0.675107 | 0.682577 | 6.73% (25), $46.46 | -2.99% (26), $58.89 | 0 (25 unfilled) | — | $50.00 | 1 (25 unfilled) | -100.00% [-100.00%, -100.00%] | $47.47 |
| map | 2026-08 | 40 | 0.713073 | 0.704864 | 0.763024 | 19.15% (27), $63.13 | 64.22% (26), $92.35 | 5 (22 unfilled) | 15.58% [-70.92%, 102.41%] | $50.27 | 7 (19 unfilled) | 96.17% [-5.40%, 200.01%] | $66.80 |
| map | 2026-10 | 2 | 0.188159 | 0.403053 | 0.281038 | 29.00% (2), $51.45 | -100.00% (2), $45.00 | 1 (1 unfilled) | 29.00% [29.00%, 29.00%] | $50.94 | 2 (0 unfilled) | -100.00% [-100.00%, -100.00%] | $45.00 |
| series | 2026-07 | 48 | 0.629244 | 0.608785 | 0.605402 | -24.10% (30), $33.71 | -4.29% (6), $50.63 | 16 (14 unfilled) | -18.71% [-64.35%, 29.54%] | $46.41 | 2 (4 unfilled) | -34.64% [-100.00%, 30.72%] | $49.11 |
| series | 2026-08 | 33 | 0.621289 | 0.582210 | 0.584463 | -27.13% (26), $30.83 | 6.74% (15), $55.44 | 20 (6 unfilled) | -18.47% [-57.27%, 23.65%] | $39.28 | 12 (3 unfilled) | 22.69% [-29.82%, 76.13%] | $55.98 |
| series | 2026-09 | 192 | 0.579519 | 0.563802 | 0.568687 | -12.19% (131), $16.18 | -1.25% (57), $54.97 | 58 (73 unfilled) | -8.19% [-31.44%, 15.40%] | $35.80 | 25 (32 unfilled) | -11.70% [-38.89%, 14.47%] | $45.83 |
| series | 2026-10 | 51 | 0.619666 | 0.608235 | 0.608911 | -2.20% (29), $35.63 | 55.14% (7), $53.01 | 11 (18 unfilled) | -2.98% [-59.55%, 55.23%] | $50.01 | 2 (5 unfilled) | 42.17% [19.56%, 64.55%] | $50.82 |

### player_round_glicko_rookie: Kalshi comparison and returns



#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 324 | 0.601977 | 0.582065 | 0.019912 [-0.005205, 0.047373] | no |
| series | tier1 | 33 | 0.616452 | 0.584463 | 0.031988 [-0.054906, 0.119875] | no |
| series | tier2 | 284 | 0.599410 | 0.584967 | 0.014444 [-0.011476, 0.044649] | no |
| series | tier3 | 7 | 0.637883 | 0.453037 | 0.184846 [0.037386, 0.333931] | yes |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 33 | 0.616452 | 0.584463 | 0.031988 [-0.054906, 0.119875] | no |
| series | international=0 | 291 | 0.600336 | 0.581793 | 0.018543 [-0.008084, 0.047327] | no |
| map | all | 81 | 0.689164 | 0.712390 | -0.023225 [-0.060198, 0.013340] | no |
| map | tier1 | 40 | 0.716619 | 0.763024 | -0.046406 [-0.110603, 0.015433] | no |
| map | tier2 | 39 | 0.686509 | 0.682577 | 0.003933 [-0.033978, 0.041372] | no |
| map | tier3 | 2 | 0.191849 | 0.281038 | -0.089188 [-0.089188, -0.089188] | yes |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 40 | 0.716619 | 0.763024 | -0.046406 [-0.110603, 0.015433] | no |
| map | international=0 | 41 | 0.662380 | 0.662990 | -0.000610 [-0.036324, 0.034473] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 217 | 217 | 0.0755 | -14.83% [-28.18%, 0.30%] | $5.19 | 0.104× | 91.44% | $5.89 | 105 (112 unfilled) | -11.25% [-28.73%, 6.60%] | $28.42 |
| series | tier1 | 25 | 25 | 0.1036 | -24.16% [-57.95%, 12.83%] | $33.63 | 0.673× | 32.73% | $4.92 | 20 (5 unfilled) | -18.47% [-57.20%, 23.20%] | $41.32 |
| series | tier2 | 186 | 186 | 0.0714 | -11.43% [-25.97%, 4.66%] | $12.30 | 0.246× | 86.68% | $5.89 | 83 (103 unfilled) | -8.78% [-28.38%, 11.54%] | $36.73 |
| series | tier3 | 6 | 6 | 0.0854 | -80.55% [-100.00%, -40.99%] | $31.94 | 0.639× | 36.12% | $4.76 | 2 (4 unfilled) | -41.37% [-100.00%, 19.56%] | $48.99 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 25 | 25 | 0.1036 | -24.16% [-57.95%, 12.83%] | $33.63 | 0.673× | 32.73% | $4.92 | 20 (5 unfilled) | -18.47% [-57.20%, 23.20%] | $41.32 |
| series | international=0 | 192 | 192 | 0.0719 | -13.61% [-27.42%, 0.96%] | $7.81 | 0.156× | 87.11% | $5.89 | 85 (107 unfilled) | -9.55% [-28.77%, 10.31%] | $35.86 |
| map | all | 56 | 30 | 0.0664 | 14.29% [-9.77%, 39.45%] | $61.62 | 1.232× | 15.90% | $4.55 | 6 (50 unfilled) | 17.78% [-54.56%, 82.18%] | $50.86 |
| map | tier1 | 27 | 14 | 0.0859 | 19.15% [-16.26%, 55.66%] | $62.46 | 1.249× | 10.49% | $3.45 | 5 (22 unfilled) | 15.58% [-70.92%, 102.41%] | $49.92 |
| map | tier2 | 27 | 15 | 0.0479 | 8.35% [-27.68%, 48.95%] | $47.92 | 0.958× | 15.90% | $4.55 | 0 (27 unfilled) | — | $50.00 |
| map | tier3 | 2 | 1 | 0.0527 | 29.00% [29.00%, 29.00%] | $51.45 | 1.029× | 0.00% | $2.45 | 1 (1 unfilled) | 29.00% [29.00%, 29.00%] | $50.94 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 27 | 14 | 0.0859 | 19.15% [-16.26%, 55.66%] | $62.46 | 1.249× | 10.49% | $3.45 | 5 (22 unfilled) | 15.58% [-70.92%, 102.41%] | $49.92 |
| map | international=0 | 29 | 16 | 0.0482 | 9.75% [-24.13%, 47.08%] | $49.32 | 0.986× | 15.90% | $4.55 | 1 (28 unfilled) | 29.00% [29.00%, 29.00%] | $50.94 |
| series+map | all | 273 | 219 | 0.0736 | -8.85% [-21.42%, 3.73%] | $7.18 | 0.144× | 88.16% | $5.89 | 111 (162 unfilled) | -9.69% [-26.74%, 7.00%] | $30.49 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 0 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-07 | series | 244 | 1.055422 | 0.304545 | fitted |
| 2026-07 | map | 109 | 0.536883 | 0.317132 | fitted |
| 2026-08 | series | 244 | 1.055422 | 0.304545 | fitted |
| 2026-08 | map | 109 | 0.536883 | 0.317132 | fitted |
| 2026-09 | series | 244 | 1.055422 | 0.304545 | fitted |
| 2026-10 | series | 244 | 1.055422 | 0.304545 | fitted |
| 2026-10 | map | 109 | 0.536883 | 0.317132 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 324 | 0.580287 | 0.582065 | -0.001778 [-0.010414, 0.006621] | no |
| series | tier1 | 33 | 0.581943 | 0.584463 | -0.002520 [-0.029836, 0.023669] | no |
| series | tier2 | 284 | 0.582243 | 0.584967 | -0.002724 [-0.011260, 0.006808] | no |
| series | tier3 | 7 | 0.493129 | 0.453037 | 0.040092 [-0.003766, 0.089868] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 33 | 0.581943 | 0.584463 | -0.002520 [-0.029836, 0.023669] | no |
| series | international=0 | 291 | 0.580099 | 0.581793 | -0.001694 [-0.010445, 0.007400] | no |
| map | all | 81 | 0.681500 | 0.712390 | -0.030889 [-0.071789, 0.004496] | no |
| map | tier1 | 40 | 0.703133 | 0.763024 | -0.059891 [-0.132308, -0.009060] | yes |
| map | tier2 | 39 | 0.674256 | 0.682577 | -0.008321 [-0.056637, 0.033779] | no |
| map | tier3 | 2 | 0.390086 | 0.281038 | 0.109048 [0.109048, 0.109048] | yes |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 40 | 0.703133 | 0.763024 | -0.059891 [-0.132308, -0.009060] | yes |
| map | international=0 | 41 | 0.660394 | 0.662990 | -0.002595 [-0.047794, 0.040075] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 94 | 94 | 0.0257 | 4.71% [-12.76%, 23.32%] | $58.61 | 1.172× | 17.77% | $6.47 | 44 (50 unfilled) | 3.18% [-19.57%, 25.65%] | $46.36 |
| series | tier1 | 14 | 14 | 0.0249 | 2.31% [-46.98%, 51.84%] | $55.22 | 1.104× | 2.37% | $4.93 | 11 (3 unfilled) | 18.46% [-37.16%, 76.08%] | $56.54 |
| series | tier2 | 77 | 77 | 0.0264 | 7.71% [-11.65%, 29.78%] | $57.27 | 1.145× | 17.79% | $5.86 | 32 (45 unfilled) | -2.66% [-26.66%, 21.22%] | $41.04 |
| series | tier3 | 3 | 3 | 0.0111 | -60.66% [-100.00%, 19.56%] | $46.25 | 0.925× | 7.79% | $3.09 | 1 (2 unfilled) | 19.56% [19.56%, 19.56%] | $49.62 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 14 | 14 | 0.0249 | 2.31% [-46.98%, 51.84%] | $55.22 | 1.104× | 2.37% | $4.93 | 11 (3 unfilled) | 18.46% [-37.16%, 76.08%] | $56.54 |
| series | international=0 | 80 | 80 | 0.0258 | 5.13% [-12.78%, 24.91%] | $52.97 | 1.059× | 17.79% | $5.86 | 33 (47 unfilled) | -1.99% [-26.75%, 19.76%] | $40.64 |
| map | all | 52 | 28 | 0.0467 | 25.67% [-12.40%, 66.85%] | $105.03 | 2.101× | 19.58% | $5.74 | 9 (43 unfilled) | 52.04% [-37.96%, 170.18%] | $57.10 |
| map | tier1 | 24 | 13 | 0.0504 | 67.47% [13.27%, 133.62%] | $96.58 | 1.932× | 3.55% | $4.75 | 6 (18 unfilled) | 128.91% [17.07%, 238.39%] | $66.65 |
| map | tier2 | 26 | 14 | 0.0423 | -2.99% [-50.32%, 47.10%] | $60.41 | 1.208× | 19.58% | $4.49 | 1 (25 unfilled) | -100.00% [-100.00%, -100.00%] | $47.47 |
| map | tier3 | 2 | 1 | 0.0599 | -100.00% [-100.00%, -100.00%] | $45.00 | 0.900× | 10.00% | $2.37 | 2 (0 unfilled) | -100.00% [-100.00%, -100.00%] | $45.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 24 | 13 | 0.0504 | 67.47% [13.27%, 133.62%] | $96.58 | 1.932× | 3.55% | $4.75 | 6 (18 unfilled) | 128.91% [17.07%, 238.39%] | $66.65 |
| map | international=0 | 28 | 15 | 0.0436 | -9.97% [-56.53%, 39.54%] | $54.37 | 1.087× | 19.58% | $4.49 | 3 (25 unfilled) | -100.00% [-100.00%, -100.00%] | $42.72 |
| series+map | all | 146 | 111 | 0.0331 | 12.27% [-6.57%, 30.96%] | $110.53 | 2.211× | 21.69% | $13.45 | 53 (93 unfilled) | 11.63% [-11.27%, 39.77%] | $49.09 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-07 | 39 | 0.686509 | 0.674256 | 0.682577 | 8.35% (27), $47.92 | -2.99% (26), $60.41 | 0 (27 unfilled) | — | $50.00 | 1 (25 unfilled) | -100.00% [-100.00%, -100.00%] | $47.47 |
| map | 2026-08 | 40 | 0.716619 | 0.703133 | 0.763024 | 19.15% (27), $62.46 | 67.47% (24), $96.58 | 5 (22 unfilled) | 15.58% [-70.92%, 102.41%] | $49.92 | 6 (18 unfilled) | 128.91% [17.07%, 238.39%] | $66.65 |
| map | 2026-10 | 2 | 0.191849 | 0.390086 | 0.281038 | 29.00% (2), $51.45 | -100.00% (2), $45.00 | 1 (1 unfilled) | 29.00% [29.00%, 29.00%] | $50.94 | 2 (0 unfilled) | -100.00% [-100.00%, -100.00%] | $45.00 |
| series | 2026-07 | 48 | 0.635337 | 0.611126 | 0.605402 | -27.96% (32), $32.51 | -4.29% (6), $48.42 | 16 (16 unfilled) | -26.33% [-74.57%, 24.32%] | $43.16 | 2 (4 unfilled) | -34.64% [-100.00%, 30.72%] | $46.87 |
| series | 2026-08 | 33 | 0.616452 | 0.581943 | 0.584463 | -24.16% (25), $33.63 | 2.31% (14), $55.22 | 20 (5 unfilled) | -18.47% [-57.20%, 23.20%] | $41.32 | 11 (3 unfilled) | 18.46% [-37.16%, 76.08%] | $56.54 |
| series | 2026-09 | 192 | 0.585999 | 0.564705 | 0.568687 | -10.86% (132), $17.49 | 0.70% (67), $51.17 | 58 (74 unfilled) | -3.69% [-27.35%, 17.61%] | $43.13 | 29 (38 unfilled) | -2.80% [-28.13%, 21.44%] | $43.34 |
| series | 2026-10 | 51 | 0.621364 | 0.608853 | 0.608911 | -10.05% (28), $34.98 | 55.14% (7), $53.47 | 11 (17 unfilled) | -15.66% [-72.15%, 43.72%] | $48.48 | 2 (5 unfilled) | 42.17% [19.56%, 64.55%] | $50.26 |

### team_elo+none: Kalshi comparison and returns

none

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 324 | 0.662044 | 0.582065 | 0.079979 [0.043015, 0.119700] | yes |
| series | tier1 | 33 | 0.612331 | 0.584463 | 0.027867 [-0.054989, 0.107649] | no |
| series | tier2 | 284 | 0.669892 | 0.584967 | 0.084925 [0.042541, 0.127505] | yes |
| series | tier3 | 7 | 0.578023 | 0.453037 | 0.124986 [-0.016154, 0.256621] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 33 | 0.612331 | 0.584463 | 0.027867 [-0.054989, 0.107649] | no |
| series | international=0 | 291 | 0.667682 | 0.581793 | 0.085889 [0.043771, 0.128943] | yes |
| map | all | 81 | 0.677740 | 0.712390 | -0.034649 [-0.078626, 0.008810] | no |
| map | tier1 | 40 | 0.749962 | 0.763024 | -0.013062 [-0.071348, 0.046940] | no |
| map | tier2 | 39 | 0.633857 | 0.682577 | -0.048720 [-0.111817, 0.007999] | no |
| map | tier3 | 2 | 0.089025 | 0.281038 | -0.192012 [-0.192012, -0.192012] | yes |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 40 | 0.749962 | 0.763024 | -0.013062 [-0.071348, 0.046940] | no |
| map | international=0 | 41 | 0.607280 | 0.662990 | -0.055710 [-0.115125, 0.003638] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 262 | 262 | 0.0972 | -19.23% [-31.73%, -6.36%] | $0.09 | 0.002× | 99.82% | $4.84 | 138 (124 unfilled) | -17.68% [-33.79%, -1.07%] | $1.98 |
| series | tier1 | 27 | 27 | 0.1024 | -20.98% [-54.95%, 16.64%] | $32.70 | 0.654× | 42.81% | $5.46 | 21 (6 unfilled) | -14.52% [-53.38%, 26.02%] | $42.87 |
| series | tier2 | 229 | 229 | 0.0970 | -18.14% [-31.41%, -5.36%] | $0.34 | 0.007× | 99.32% | $4.84 | 116 (113 unfilled) | -18.57% [-35.19%, -0.33%] | $2.95 |
| series | tier3 | 6 | 6 | 0.0819 | -52.83% [-100.00%, 7.00%] | $33.88 | 0.678× | 33.33% | $5.01 | 1 (5 unfilled) | 19.56% [19.56%, 19.56%] | $50.47 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 27 | 27 | 0.1024 | -20.98% [-54.95%, 16.64%] | $32.70 | 0.654× | 42.81% | $5.46 | 21 (6 unfilled) | -14.52% [-53.38%, 26.02%] | $42.87 |
| series | international=0 | 235 | 235 | 0.0966 | -19.03% [-31.27%, -5.42%] | $0.22 | 0.004× | 99.57% | $4.84 | 117 (118 unfilled) | -18.25% [-34.17%, 0.52%] | $2.52 |
| map | all | 59 | 32 | 0.1097 | 21.73% [1.69%, 43.05%] | $87.41 | 1.748× | 11.11% | $7.27 | 9 (50 unfilled) | 8.57% [-58.27%, 86.43%] | $51.54 |
| map | tier1 | 28 | 14 | 0.0866 | 6.68% [-25.44%, 37.54%] | $57.40 | 1.148× | 10.00% | $3.05 | 8 (20 unfilled) | 6.07% [-69.75%, 89.71%] | $50.59 |
| map | tier2 | 29 | 17 | 0.1298 | 35.78% [9.83%, 65.70%] | $73.93 | 1.479× | 3.15% | $7.27 | 0 (29 unfilled) | — | $50.00 |
| map | tier3 | 2 | 1 | 0.1421 | 29.00% [29.00%, 29.00%] | $51.45 | 1.029× | 0.00% | $2.45 | 1 (1 unfilled) | 29.00% [29.00%, 29.00%] | $50.94 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 28 | 14 | 0.0866 | 6.68% [-25.44%, 37.54%] | $57.40 | 1.148× | 10.00% | $3.05 | 8 (20 unfilled) | 6.07% [-69.75%, 89.71%] | $50.59 |
| map | international=0 | 31 | 18 | 0.1306 | 35.35% [10.79%, 65.95%] | $76.09 | 1.522× | 3.15% | $7.27 | 1 (30 unfilled) | 29.00% [29.00%, 29.00%] | $50.94 |
| series+map | all | 321 | 264 | 0.0995 | -11.68% [-22.60%, -0.35%] | $0.40 | 0.008× | 99.20% | $4.84 | 147 (174 unfilled) | -16.07% [-31.34%, -0.93%] | $2.52 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 0 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-07 | series | 244 | 0.969949 | -0.072315 | fitted |
| 2026-07 | map | 109 | 0.440147 | -0.086052 | fitted |
| 2026-08 | series | 244 | 0.969949 | -0.072315 | fitted |
| 2026-08 | map | 109 | 0.440147 | -0.086052 | fitted |
| 2026-09 | series | 244 | 0.969949 | -0.072315 | fitted |
| 2026-10 | series | 244 | 0.969949 | -0.072315 | fitted |
| 2026-10 | map | 109 | 0.440147 | -0.086052 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 324 | 0.580992 | 0.582065 | -0.001073 [-0.004225, 0.001952] | no |
| series | tier1 | 33 | 0.586890 | 0.584463 | 0.002427 [-0.003097, 0.008382] | no |
| series | tier2 | 284 | 0.583504 | 0.584967 | -0.001463 [-0.005024, 0.002061] | no |
| series | tier3 | 7 | 0.451258 | 0.453037 | -0.001778 [-0.014086, 0.009840] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 33 | 0.586890 | 0.584463 | 0.002427 [-0.003097, 0.008382] | no |
| series | international=0 | 291 | 0.580323 | 0.581793 | -0.001470 [-0.005023, 0.001890] | no |
| map | all | 81 | 0.698023 | 0.712390 | -0.014366 [-0.061070, 0.026603] | no |
| map | tier1 | 40 | 0.718442 | 0.763024 | -0.044583 [-0.123601, 0.010774] | no |
| map | tier2 | 39 | 0.686319 | 0.682577 | 0.003742 [-0.049496, 0.054366] | no |
| map | tier3 | 2 | 0.517877 | 0.281038 | 0.236839 [0.236839, 0.236839] | yes |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 40 | 0.718442 | 0.763024 | -0.044583 [-0.123601, 0.010774] | no |
| map | international=0 | 41 | 0.678102 | 0.662990 | 0.015113 [-0.037669, 0.069983] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 5 | 5 | 0.0077 | 18.26% [-100.00%, 141.59%] | $49.84 | 0.997× | 3.62% | $1.61 | 2 (3 unfilled) | 52.16% [-100.00%, 207.22%] | $50.75 |
| series | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier2 | 5 | 5 | 0.0077 | 18.26% [-100.00%, 141.59%] | $49.84 | 0.997× | 3.62% | $1.61 | 2 (3 unfilled) | 52.16% [-100.00%, 207.22%] | $50.75 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=0 | 5 | 5 | 0.0077 | 18.26% [-100.00%, 141.59%] | $49.84 | 0.997× | 3.62% | $1.61 | 2 (3 unfilled) | 52.16% [-100.00%, 207.22%] | $50.75 |
| map | all | 61 | 33 | 0.0404 | 20.32% [-12.99%, 57.27%] | $80.84 | 1.617× | 20.76% | $4.37 | 10 (51 unfilled) | -5.86% [-80.80%, 110.78%] | $50.29 |
| map | tier1 | 27 | 14 | 0.0291 | 54.13% [1.08%, 119.96%] | $83.05 | 1.661× | 6.43% | $4.04 | 7 (20 unfilled) | 34.93% [-71.22%, 185.69%] | $58.91 |
| map | tier2 | 32 | 18 | 0.0437 | -0.54% [-44.13%, 42.75%] | $54.09 | 1.082× | 20.76% | $4.08 | 1 (31 unfilled) | -100.00% [-100.00%, -100.00%] | $47.45 |
| map | tier3 | 2 | 1 | 0.1411 | -100.00% [-100.00%, -100.00%] | $45.00 | 0.900× | 10.00% | $2.37 | 2 (0 unfilled) | -100.00% [-100.00%, -100.00%] | $45.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 27 | 14 | 0.0291 | 54.13% [1.08%, 119.96%] | $83.05 | 1.661× | 6.43% | $4.04 | 7 (20 unfilled) | 34.93% [-71.22%, 185.69%] | $58.91 |
| map | international=0 | 34 | 19 | 0.0494 | -6.45% [-49.46%, 34.63%] | $48.68 | 0.974× | 20.76% | $4.08 | 3 (31 unfilled) | -100.00% [-100.00%, -100.00%] | $42.71 |
| series+map | all | 66 | 38 | 0.0379 | 20.17% [-15.70%, 55.30%] | $80.58 | 1.612× | 20.76% | $4.37 | 12 (54 unfilled) | 3.87% [-78.01%, 107.51%] | $51.02 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-07 | 39 | 0.633857 | 0.686319 | 0.682577 | 35.78% (29), $73.93 | -0.54% (32), $54.09 | 0 (29 unfilled) | — | $50.00 | 1 (31 unfilled) | -100.00% [-100.00%, -100.00%] | $47.45 |
| map | 2026-08 | 40 | 0.749962 | 0.718442 | 0.763024 | 6.68% (28), $57.40 | 54.13% (27), $83.05 | 8 (20 unfilled) | 6.07% [-69.75%, 89.71%] | $50.59 | 7 (20 unfilled) | 34.93% [-71.22%, 185.69%] | $58.91 |
| map | 2026-10 | 2 | 0.089025 | 0.517877 | 0.281038 | 29.00% (2), $51.45 | -100.00% (2), $45.00 | 1 (1 unfilled) | 29.00% [29.00%, 29.00%] | $50.94 | 2 (0 unfilled) | -100.00% [-100.00%, -100.00%] | $45.00 |
| series | 2026-07 | 48 | 0.769251 | 0.598508 | 0.605402 | -29.54% (40), $14.72 | — (0), $50.00 | 23 (17 unfilled) | -30.68% [-74.76%, 23.27%] | $26.71 | 0 (0 unfilled) | — | $50.00 |
| series | 2026-08 | 33 | 0.612331 | 0.586890 | 0.584463 | -20.98% (27), $32.70 | — (0), $50.00 | 21 (6 unfilled) | -14.52% [-53.38%, 26.02%] | $42.87 | 0 (0 unfilled) | — | $50.00 |
| series | 2026-09 | 192 | 0.633187 | 0.569206 | 0.568687 | -15.35% (159), $2.76 | -23.92% (4), $48.99 | 81 (78 unfilled) | -17.19% [-36.95%, 2.86%] | $8.03 | 2 (2 unfilled) | 52.16% [-100.00%, 207.22%] | $50.75 |
| series | 2026-10 | 51 | 0.701947 | 0.605059 | 0.608911 | -23.50% (36), $23.14 | 188.60% (1), $50.84 | 13 (23 unfilled) | -2.84% [-55.87%, 55.94%] | $42.16 | 0 (1 unfilled) | — | $50.00 |

### team_elo+calibration: Kalshi comparison and returns

calibration: ridge=4; tier1/online=0: rows=1092, T=0.3468; tier1/online=1: rows=567, T=0.7962; tier2/online=0: rows=253, T=1.0000; tier2/online=1: rows=4454, T=0.7831; tier3/online=0: rows=3215, T=0.9227; tier3/online=1: rows=40549, T=0.9141; unknown/online=0: rows=23, T=1.0000

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 324 | 0.645518 | 0.582065 | 0.063453 [0.033110, 0.095261] | yes |
| series | tier1 | 33 | 0.650928 | 0.584463 | 0.066465 [-0.025646, 0.154302] | no |
| series | tier2 | 284 | 0.646945 | 0.584967 | 0.061978 [0.028713, 0.095882] | yes |
| series | tier3 | 7 | 0.562154 | 0.453037 | 0.109117 [-0.027719, 0.239457] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 33 | 0.650928 | 0.584463 | 0.066465 [-0.025646, 0.154302] | no |
| series | international=0 | 291 | 0.644905 | 0.581793 | 0.063112 [0.030774, 0.097170] | yes |
| map | all | 81 | 0.655248 | 0.712390 | -0.057142 [-0.106126, -0.015965] | yes |
| map | tier1 | 40 | 0.703664 | 0.763024 | -0.059360 [-0.145597, 0.004936] | no |
| map | tier2 | 39 | 0.633647 | 0.682577 | -0.048929 [-0.105525, 0.002804] | no |
| map | tier3 | 2 | 0.108116 | 0.281038 | -0.172922 [-0.172922, -0.172922] | yes |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 40 | 0.703664 | 0.763024 | -0.059360 [-0.145597, 0.004936] | no |
| map | international=0 | 41 | 0.608012 | 0.662990 | -0.054978 [-0.107045, -0.000723] | yes |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 248 | 248 | 0.0894 | -16.99% [-31.29%, -2.59%] | $0.09 | 0.002× | 99.81% | $4.84 | 132 (116 unfilled) | -16.33% [-34.72%, 2.80%] | $1.62 |
| series | tier1 | 25 | 25 | 0.1162 | -15.34% [-63.63%, 41.68%] | $24.60 | 0.492× | 57.43% | $5.53 | 22 (3 unfilled) | -3.72% [-55.16%, 60.37%] | $30.34 |
| series | tier2 | 217 | 217 | 0.0866 | -16.19% [-31.28%, -0.74%] | $0.54 | 0.011× | 98.97% | $4.84 | 109 (108 unfilled) | -19.22% [-38.36%, 1.65%] | $3.36 |
| series | tier3 | 6 | 6 | 0.0798 | -52.83% [-100.00%, 7.00%] | $34.69 | 0.694× | 32.41% | $5.06 | 1 (5 unfilled) | 19.56% [19.56%, 19.56%] | $50.47 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 25 | 25 | 0.1162 | -15.34% [-63.63%, 41.68%] | $24.60 | 0.492× | 57.43% | $5.53 | 22 (3 unfilled) | -3.72% [-55.16%, 60.37%] | $30.34 |
| series | international=0 | 223 | 223 | 0.0864 | -17.18% [-31.49%, -1.47%] | $0.35 | 0.007× | 99.30% | $4.84 | 110 (113 unfilled) | -18.88% [-37.85%, 1.15%] | $2.89 |
| map | all | 61 | 33 | 0.0920 | 38.45% [12.29%, 70.06%] | $164.17 | 3.283× | 7.41% | $7.84 | 11 (50 unfilled) | 36.65% [-46.89%, 133.44%] | $59.72 |
| map | tier1 | 26 | 13 | 0.0821 | 48.77% [0.57%, 111.78%] | $89.78 | 1.796× | 7.40% | $4.35 | 9 (17 unfilled) | 52.85% [-43.86%, 165.13%] | $61.00 |
| map | tier2 | 33 | 19 | 0.0978 | 30.85% [2.03%, 63.58%] | $88.75 | 1.775× | 0.00% | $7.40 | 1 (32 unfilled) | -100.00% [-100.00%, -100.00%] | $48.01 |
| map | tier3 | 2 | 1 | 0.1248 | 29.00% [29.00%, 29.00%] | $51.45 | 1.029× | 0.00% | $2.45 | 1 (1 unfilled) | 29.00% [29.00%, 29.00%] | $50.94 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 26 | 13 | 0.0821 | 48.77% [0.57%, 111.78%] | $89.78 | 1.796× | 7.40% | $4.35 | 9 (17 unfilled) | 52.85% [-43.86%, 165.13%] | $61.00 |
| map | international=0 | 35 | 20 | 0.0993 | 30.75% [1.50%, 59.15%] | $91.34 | 1.827× | 0.00% | $7.40 | 2 (33 unfilled) | -36.74% [-100.00%, 29.00%] | $48.94 |
| series+map | all | 309 | 248 | 0.0899 | -6.01% [-20.94%, 9.13%] | $0.48 | 0.010× | 99.04% | $4.84 | 143 (166 unfilled) | -12.24% [-32.56%, 8.08%] | $1.62 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 0 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-07 | series | 244 | 0.959058 | -0.047414 | fitted |
| 2026-07 | map | 109 | -0.049076 | -0.879877 | fitted |
| 2026-08 | series | 244 | 0.959058 | -0.047414 | fitted |
| 2026-08 | map | 109 | -0.049076 | -0.879877 | fitted |
| 2026-09 | series | 244 | 0.959058 | -0.047414 | fitted |
| 2026-10 | series | 244 | 0.959058 | -0.047414 | fitted |
| 2026-10 | map | 109 | -0.049076 | -0.879877 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 324 | 0.581762 | 0.582065 | -0.000303 [-0.002481, 0.001696] | no |
| series | tier1 | 33 | 0.585117 | 0.584463 | 0.000654 [-0.000936, 0.002213] | no |
| series | tier2 | 284 | 0.584474 | 0.584967 | -0.000493 [-0.003012, 0.001829] | no |
| series | tier3 | 7 | 0.455912 | 0.453037 | 0.002875 [-0.007693, 0.012371] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 33 | 0.585117 | 0.584463 | 0.000654 [-0.000936, 0.002213] | no |
| series | international=0 | 291 | 0.581381 | 0.581793 | -0.000412 [-0.002811, 0.001861] | no |
| map | all | 81 | 0.775383 | 0.712390 | 0.062993 [-0.014722, 0.149071] | no |
| map | tier1 | 40 | 0.734280 | 0.763024 | -0.028744 [-0.101867, 0.026606] | no |
| map | tier2 | 39 | 0.790915 | 0.682577 | 0.108338 [-0.000861, 0.223108] | no |
| map | tier3 | 2 | 1.294543 | 0.281038 | 1.013506 [1.013506, 1.013506] | yes |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 40 | 0.734280 | 0.763024 | -0.028744 [-0.101867, 0.026606] | no |
| map | international=0 | 41 | 0.815483 | 0.662990 | 0.152493 [0.027337, 0.291303] | yes |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier2 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=0 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | all | 50 | 28 | 0.1176 | 8.12% [-35.05%, 54.23%] | $54.05 | 1.081× | 37.99% | $3.84 | 5 (45 unfilled) | 41.11% [-100.00%, 253.77%] | $55.63 |
| map | tier1 | 16 | 9 | 0.0379 | 54.16% [-34.58%, 161.13%] | $72.15 | 1.443× | 12.00% | $3.87 | 2 (14 unfilled) | 253.77% [157.40%, 349.24%] | $65.07 |
| map | tier2 | 32 | 18 | 0.1358 | -8.03% [-48.50%, 36.41%] | $41.57 | 0.831× | 37.99% | $3.84 | 1 (31 unfilled) | -100.00% [-100.00%, -100.00%] | $47.45 |
| map | tier3 | 2 | 1 | 0.4629 | -100.00% [-100.00%, -100.00%] | $45.00 | 0.900× | 10.00% | $2.37 | 2 (0 unfilled) | -100.00% [-100.00%, -100.00%] | $45.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 16 | 9 | 0.0379 | 54.16% [-34.58%, 161.13%] | $72.15 | 1.443× | 12.00% | $3.87 | 2 (14 unfilled) | 253.77% [157.40%, 349.24%] | $65.07 |
| map | international=0 | 34 | 19 | 0.1550 | -13.50% [-51.93%, 30.77%] | $37.41 | 0.748× | 37.99% | $3.84 | 3 (31 unfilled) | -100.00% [-100.00%, -100.00%] | $42.71 |
| series+map | all | 50 | 28 | 0.1176 | 8.12% [-35.05%, 54.23%] | $54.05 | 1.081× | 37.99% | $3.84 | 5 (45 unfilled) | 41.11% [-100.00%, 253.77%] | $55.63 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-07 | 39 | 0.633647 | 0.790915 | 0.682577 | 30.85% (33), $88.75 | -8.03% (32), $41.57 | 1 (32 unfilled) | -100.00% [-100.00%, -100.00%] | $48.01 | 1 (31 unfilled) | -100.00% [-100.00%, -100.00%] | $47.45 |
| map | 2026-08 | 40 | 0.703664 | 0.734280 | 0.763024 | 48.77% (26), $89.78 | 54.16% (16), $72.15 | 9 (17 unfilled) | 52.85% [-43.86%, 165.13%] | $61.00 | 2 (14 unfilled) | 253.77% [157.40%, 349.24%] | $65.07 |
| map | 2026-10 | 2 | 0.108116 | 1.294543 | 0.281038 | 29.00% (2), $51.45 | -100.00% (2), $45.00 | 1 (1 unfilled) | 29.00% [29.00%, 29.00%] | $50.94 | 2 (0 unfilled) | -100.00% [-100.00%, -100.00%] | $45.00 |
| series | 2026-07 | 48 | 0.733000 | 0.602058 | 0.605402 | -28.81% (39), $14.33 | — (0), $50.00 | 21 (18 unfilled) | -36.92% [-81.48%, 20.76%] | $25.15 | 0 (0 unfilled) | — | $50.00 |
| series | 2026-08 | 33 | 0.650928 | 0.585117 | 0.584463 | -15.34% (25), $24.60 | — (0), $50.00 | 22 (3 unfilled) | -3.72% [-55.16%, 60.37%] | $30.34 | 0 (0 unfilled) | — | $50.00 |
| series | 2026-09 | 192 | 0.615359 | 0.569289 | 0.568687 | -13.77% (152), $3.64 | — (0), $50.00 | 77 (75 unfilled) | -15.57% [-37.53%, 6.72%] | $9.99 | 0 (0 unfilled) | — | $50.00 |
| series | 2026-10 | 51 | 0.673223 | 0.607442 | 0.608911 | -19.13% (32), $24.91 | — (0), $50.00 | 12 (20 unfilled) | -8.39% [-64.87%, 50.10%] | $39.06 | 0 (0 unfilled) | — | $50.00 |

### player_round_glicko+none: Kalshi comparison and returns

none

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 324 | 0.597459 | 0.582065 | 0.015395 [-0.008073, 0.038488] | no |
| series | tier1 | 33 | 0.621289 | 0.584463 | 0.036826 [-0.052932, 0.128460] | no |
| series | tier2 | 284 | 0.593866 | 0.584967 | 0.008900 [-0.014027, 0.033898] | no |
| series | tier3 | 7 | 0.630899 | 0.453037 | 0.177862 [0.024913, 0.334549] | yes |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 33 | 0.621289 | 0.584463 | 0.036826 [-0.052932, 0.128460] | no |
| series | international=0 | 291 | 0.594757 | 0.581793 | 0.012964 [-0.010517, 0.038379] | no |
| map | all | 81 | 0.688352 | 0.712390 | -0.024037 [-0.061335, 0.012439] | no |
| map | tier1 | 40 | 0.713073 | 0.763024 | -0.049951 [-0.114817, 0.011929] | no |
| map | tier2 | 39 | 0.688649 | 0.682577 | 0.006072 [-0.032422, 0.043353] | no |
| map | tier3 | 2 | 0.188159 | 0.281038 | -0.092878 [-0.092878, -0.092878] | yes |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 40 | 0.713073 | 0.763024 | -0.049951 [-0.114817, 0.011929] | no |
| map | international=0 | 41 | 0.664234 | 0.662990 | 0.001245 [-0.034782, 0.035819] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 216 | 216 | 0.0742 | -14.31% [-27.90%, -0.81%] | $4.63 | 0.093× | 92.13% | $5.72 | 105 (111 unfilled) | -11.22% [-28.66%, 8.09%] | $25.06 |
| series | tier1 | 26 | 26 | 0.1059 | -27.13% [-59.60%, 10.04%] | $30.83 | 0.617× | 38.35% | $4.92 | 20 (6 unfilled) | -18.47% [-57.27%, 23.65%] | $39.28 |
| series | tier2 | 185 | 185 | 0.0690 | -10.81% [-25.25%, 5.16%] | $11.61 | 0.232× | 86.86% | $5.72 | 84 (101 unfilled) | -9.84% [-31.32%, 11.85%] | $33.22 |
| series | tier3 | 5 | 5 | 0.1027 | -76.59% [-100.00%, -28.96%] | $33.13 | 0.663× | 33.73% | $4.93 | 1 (4 unfilled) | 19.56% [19.56%, 19.56%] | $50.47 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 26 | 26 | 0.1059 | -27.13% [-59.60%, 10.04%] | $30.83 | 0.617× | 38.35% | $4.92 | 20 (6 unfilled) | -18.47% [-57.27%, 23.65%] | $39.28 |
| series | international=0 | 190 | 190 | 0.0699 | -12.55% [-27.10%, 2.12%] | $7.64 | 0.153× | 87.01% | $5.72 | 85 (105 unfilled) | -9.50% [-29.99%, 10.79%] | $33.37 |
| map | all | 54 | 29 | 0.0703 | 13.75% [-12.60%, 39.13%] | $60.33 | 1.207× | 16.96% | $4.41 | 6 (48 unfilled) | 17.78% [-54.56%, 82.18%] | $51.22 |
| map | tier1 | 27 | 14 | 0.0877 | 19.15% [-16.26%, 55.66%] | $63.13 | 1.263× | 9.77% | $4.31 | 5 (22 unfilled) | 15.58% [-70.92%, 102.41%] | $50.27 |
| map | tier2 | 25 | 14 | 0.0527 | 6.73% [-31.67%, 48.90%] | $46.46 | 0.929× | 16.96% | $4.41 | 0 (25 unfilled) | — | $50.00 |
| map | tier3 | 2 | 1 | 0.0557 | 29.00% [29.00%, 29.00%] | $51.45 | 1.029× | 0.00% | $2.45 | 1 (1 unfilled) | 29.00% [29.00%, 29.00%] | $50.94 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 27 | 14 | 0.0877 | 19.15% [-16.26%, 55.66%] | $63.13 | 1.263× | 9.77% | $4.31 | 5 (22 unfilled) | 15.58% [-70.92%, 102.41%] | $50.27 |
| map | international=0 | 27 | 15 | 0.0529 | 8.35% [-27.04%, 49.07%] | $47.82 | 0.956× | 16.96% | $4.41 | 1 (26 unfilled) | 29.00% [29.00%, 29.00%] | $50.94 |
| series+map | all | 270 | 218 | 0.0735 | -8.69% [-21.75%, 4.76%] | $7.34 | 0.147× | 87.52% | $5.72 | 111 (159 unfilled) | -9.65% [-27.47%, 7.20%] | $28.52 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 0 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-07 | series | 244 | 1.056071 | 0.276239 | fitted |
| 2026-07 | map | 109 | 0.522513 | 0.249933 | fitted |
| 2026-08 | series | 244 | 1.056071 | 0.276239 | fitted |
| 2026-08 | map | 109 | 0.522513 | 0.249933 | fitted |
| 2026-09 | series | 244 | 1.056071 | 0.276239 | fitted |
| 2026-10 | series | 244 | 1.056071 | 0.276239 | fitted |
| 2026-10 | map | 109 | 0.522513 | 0.249933 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 324 | 0.579335 | 0.582065 | -0.002730 [-0.010283, 0.004265] | no |
| series | tier1 | 33 | 0.582210 | 0.584463 | -0.002254 [-0.029240, 0.023239] | no |
| series | tier2 | 284 | 0.581292 | 0.584967 | -0.003675 [-0.010830, 0.004250] | no |
| series | tier3 | 7 | 0.486399 | 0.453037 | 0.033362 [-0.008901, 0.081342] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 33 | 0.582210 | 0.584463 | -0.002254 [-0.029240, 0.023239] | no |
| series | international=0 | 291 | 0.579009 | 0.581793 | -0.002784 [-0.010393, 0.005163] | no |
| map | all | 81 | 0.683085 | 0.712390 | -0.029305 [-0.070024, 0.006062] | no |
| map | tier1 | 40 | 0.704864 | 0.763024 | -0.058160 [-0.129056, -0.007708] | yes |
| map | tier2 | 39 | 0.675107 | 0.682577 | -0.007470 [-0.055749, 0.035064] | no |
| map | tier3 | 2 | 0.403053 | 0.281038 | 0.122016 [0.122016, 0.122016] | yes |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 40 | 0.704864 | 0.763024 | -0.058160 [-0.129056, -0.007708] | yes |
| map | international=0 | 41 | 0.661836 | 0.662990 | -0.001153 [-0.047678, 0.041608] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 85 | 85 | 0.0212 | 4.64% [-13.55%, 24.93%] | $65.55 | 1.311× | 12.67% | $6.87 | 41 (44 unfilled) | -0.03% [-23.54%, 24.43%] | $51.18 |
| series | tier1 | 15 | 15 | 0.0198 | 6.74% [-41.79%, 54.84%] | $55.44 | 1.109× | 2.92% | $4.99 | 12 (3 unfilled) | 22.69% [-29.82%, 76.13%] | $55.98 |
| series | tier2 | 67 | 67 | 0.0219 | 7.11% [-14.14%, 31.44%] | $62.37 | 1.247× | 12.66% | $6.19 | 28 (39 unfilled) | -10.59% [-36.94%, 14.44%] | $45.80 |
| series | tier3 | 3 | 3 | 0.0113 | -60.66% [-100.00%, 19.56%] | $47.33 | 0.947× | 6.37% | $2.71 | 1 (2 unfilled) | 19.56% [19.56%, 19.56%] | $50.02 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 15 | 15 | 0.0198 | 6.74% [-41.79%, 54.84%] | $55.44 | 1.109× | 2.92% | $4.99 | 12 (3 unfilled) | 22.69% [-29.82%, 76.13%] | $55.98 |
| series | international=0 | 70 | 70 | 0.0215 | 4.18% [-15.80%, 26.99%] | $59.05 | 1.181× | 12.66% | $6.19 | 29 (41 unfilled) | -9.56% [-34.95%, 14.85%] | $45.77 |
| map | all | 54 | 29 | 0.0442 | 25.66% [-10.52%, 66.37%] | $97.93 | 1.959× | 19.31% | $5.37 | 10 (44 unfilled) | 36.87% [-55.26%, 149.31%] | $57.20 |
| map | tier1 | 26 | 14 | 0.0424 | 64.22% [14.87%, 125.15%] | $92.35 | 1.847× | 8.56% | $4.56 | 7 (19 unfilled) | 96.17% [-5.40%, 200.01%] | $66.80 |
| map | tier2 | 26 | 14 | 0.0440 | -2.99% [-50.32%, 47.10%] | $58.89 | 1.178× | 19.31% | $4.45 | 1 (25 unfilled) | -100.00% [-100.00%, -100.00%] | $47.47 |
| map | tier3 | 2 | 1 | 0.0686 | -100.00% [-100.00%, -100.00%] | $45.00 | 0.900× | 10.00% | $2.37 | 2 (0 unfilled) | -100.00% [-100.00%, -100.00%] | $45.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 26 | 14 | 0.0424 | 64.22% [14.87%, 125.15%] | $92.35 | 1.847× | 8.56% | $4.56 | 7 (19 unfilled) | 96.17% [-5.40%, 200.01%] | $66.80 |
| map | international=0 | 28 | 15 | 0.0458 | -9.97% [-56.53%, 39.54%] | $53.00 | 1.060× | 19.31% | $4.45 | 3 (25 unfilled) | -100.00% [-100.00%, -100.00%] | $42.72 |
| series+map | all | 139 | 104 | 0.0301 | 12.91% [-6.08%, 33.01%] | $122.79 | 2.456× | 19.31% | $14.05 | 51 (88 unfilled) | 7.33% [-17.54%, 35.89%] | $55.97 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-07 | 39 | 0.688649 | 0.675107 | 0.682577 | 6.73% (25), $46.46 | -2.99% (26), $58.89 | 0 (25 unfilled) | — | $50.00 | 1 (25 unfilled) | -100.00% [-100.00%, -100.00%] | $47.47 |
| map | 2026-08 | 40 | 0.713073 | 0.704864 | 0.763024 | 19.15% (27), $63.13 | 64.22% (26), $92.35 | 5 (22 unfilled) | 15.58% [-70.92%, 102.41%] | $50.27 | 7 (19 unfilled) | 96.17% [-5.40%, 200.01%] | $66.80 |
| map | 2026-10 | 2 | 0.188159 | 0.403053 | 0.281038 | 29.00% (2), $51.45 | -100.00% (2), $45.00 | 1 (1 unfilled) | 29.00% [29.00%, 29.00%] | $50.94 | 2 (0 unfilled) | -100.00% [-100.00%, -100.00%] | $45.00 |
| series | 2026-07 | 48 | 0.629244 | 0.608785 | 0.605402 | -24.10% (30), $33.71 | -4.29% (6), $50.63 | 16 (14 unfilled) | -18.71% [-64.35%, 29.54%] | $46.41 | 2 (4 unfilled) | -34.64% [-100.00%, 30.72%] | $49.11 |
| series | 2026-08 | 33 | 0.621289 | 0.582210 | 0.584463 | -27.13% (26), $30.83 | 6.74% (15), $55.44 | 20 (6 unfilled) | -18.47% [-57.27%, 23.65%] | $39.28 | 12 (3 unfilled) | 22.69% [-29.82%, 76.13%] | $55.98 |
| series | 2026-09 | 192 | 0.579519 | 0.563802 | 0.568687 | -12.19% (131), $16.18 | -1.25% (57), $54.97 | 58 (73 unfilled) | -8.19% [-31.44%, 15.40%] | $35.80 | 25 (32 unfilled) | -11.70% [-38.89%, 14.47%] | $45.83 |
| series | 2026-10 | 51 | 0.619666 | 0.608235 | 0.608911 | -2.20% (29), $35.63 | 55.14% (7), $53.01 | 11 (18 unfilled) | -2.98% [-59.55%, 55.23%] | $50.01 | 2 (5 unfilled) | 42.17% [19.56%, 64.55%] | $50.82 |

### player_round_glicko+calibration: Kalshi comparison and returns

calibration: ridge=4; tier1/online=0: rows=1092, T=0.7576; tier1/online=1: rows=567, T=0.8450; tier2/online=0: rows=253, T=1.0000; tier2/online=1: rows=4454, T=1.0273; tier3/online=0: rows=3215, T=1.0701; tier3/online=1: rows=40549, T=1.0250; unknown/online=0: rows=23, T=1.0000

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 324 | 0.598519 | 0.582065 | 0.016454 [-0.007463, 0.039401] | no |
| series | tier1 | 33 | 0.621413 | 0.584463 | 0.036950 [-0.043744, 0.113816] | no |
| series | tier2 | 284 | 0.595021 | 0.584967 | 0.010055 [-0.013676, 0.036211] | no |
| series | tier3 | 7 | 0.632496 | 0.453037 | 0.179459 [0.025079, 0.339082] | yes |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 33 | 0.621413 | 0.584463 | 0.036950 [-0.043744, 0.113816] | no |
| series | international=0 | 291 | 0.595923 | 0.581793 | 0.014130 [-0.009705, 0.040241] | no |
| map | all | 81 | 0.682106 | 0.712390 | -0.030283 [-0.068275, 0.005491] | no |
| map | tier1 | 40 | 0.699597 | 0.763024 | -0.063427 [-0.131911, -0.005080] | yes |
| map | tier2 | 39 | 0.689838 | 0.682577 | 0.007261 [-0.031546, 0.044852] | no |
| map | tier3 | 2 | 0.181525 | 0.281038 | -0.099513 [-0.099513, -0.099513] | yes |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 40 | 0.699597 | 0.763024 | -0.063427 [-0.131911, -0.005080] | yes |
| map | international=0 | 41 | 0.665042 | 0.662990 | 0.002053 [-0.034737, 0.037486] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 217 | 217 | 0.0734 | -12.64% [-26.59%, 2.25%] | $5.63 | 0.113× | 90.31% | $5.66 | 108 (109 unfilled) | -8.27% [-27.24%, 11.54%] | $34.74 |
| series | tier1 | 25 | 25 | 0.0941 | -16.23% [-58.81%, 36.88%] | $37.36 | 0.747× | 25.29% | $4.91 | 21 (4 unfilled) | -6.40% [-55.78%, 50.33%] | $52.26 |
| series | tier2 | 187 | 187 | 0.0698 | -10.43% [-25.12%, 4.95%] | $11.57 | 0.231× | 86.62% | $5.66 | 86 (101 unfilled) | -9.05% [-29.35%, 12.06%] | $33.33 |
| series | tier3 | 5 | 5 | 0.1032 | -76.59% [-100.00%, -28.96%] | $33.13 | 0.663× | 33.73% | $4.93 | 1 (4 unfilled) | 19.56% [19.56%, 19.56%] | $50.47 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 25 | 25 | 0.0941 | -16.23% [-58.81%, 36.88%] | $37.36 | 0.747× | 25.29% | $4.91 | 21 (4 unfilled) | -6.40% [-55.78%, 50.33%] | $52.26 |
| series | international=0 | 192 | 192 | 0.0707 | -12.17% [-26.48%, 2.41%] | $7.61 | 0.152× | 86.90% | $5.66 | 87 (105 unfilled) | -8.73% [-27.77%, 10.80%] | $33.49 |
| map | all | 56 | 31 | 0.0608 | 32.85% [3.11%, 67.90%] | $85.54 | 1.711× | 17.30% | $4.39 | 8 (48 unfilled) | 106.59% [28.29%, 187.90%] | $63.73 |
| map | tier1 | 29 | 16 | 0.0673 | 55.57% [9.62%, 112.05%] | $92.56 | 1.851× | 9.94% | $4.90 | 7 (22 unfilled) | 117.40% [27.87%, 213.35%] | $62.60 |
| map | tier2 | 25 | 14 | 0.0532 | 6.73% [-31.67%, 48.90%] | $44.89 | 0.898× | 17.30% | $4.34 | 0 (25 unfilled) | — | $50.00 |
| map | tier3 | 2 | 1 | 0.0612 | 29.00% [29.00%, 29.00%] | $51.45 | 1.029× | 0.00% | $2.45 | 1 (1 unfilled) | 29.00% [29.00%, 29.00%] | $50.94 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 29 | 16 | 0.0673 | 55.57% [9.62%, 112.05%] | $92.56 | 1.851× | 9.94% | $4.90 | 7 (22 unfilled) | 117.40% [27.87%, 213.35%] | $62.60 |
| map | international=0 | 27 | 15 | 0.0538 | 8.35% [-27.04%, 49.07%] | $46.20 | 0.924× | 17.30% | $4.34 | 1 (26 unfilled) | 29.00% [29.00%, 29.00%] | $50.94 |
| series+map | all | 273 | 220 | 0.0708 | -3.28% [-17.76%, 12.84%] | $9.26 | 0.185× | 84.07% | $5.66 | 116 (157 unfilled) | -0.32% [-20.09%, 23.10%] | $37.28 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 0 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-07 | series | 244 | 1.081103 | 0.305976 | fitted |
| 2026-07 | map | 109 | 0.585438 | 0.293760 | fitted |
| 2026-08 | series | 244 | 1.081103 | 0.305976 | fitted |
| 2026-08 | map | 109 | 0.585438 | 0.293760 | fitted |
| 2026-09 | series | 244 | 1.081103 | 0.305976 | fitted |
| 2026-10 | series | 244 | 1.081103 | 0.305976 | fitted |
| 2026-10 | map | 109 | 0.585438 | 0.293760 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 324 | 0.579770 | 0.582065 | -0.002295 [-0.011110, 0.005993] | no |
| series | tier1 | 33 | 0.583965 | 0.584463 | -0.000499 [-0.022323, 0.020316] | no |
| series | tier2 | 284 | 0.581548 | 0.584967 | -0.003419 [-0.012137, 0.005933] | no |
| series | tier3 | 7 | 0.487884 | 0.453037 | 0.034848 [-0.013703, 0.091757] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 33 | 0.583965 | 0.584463 | -0.000499 [-0.022323, 0.020316] | no |
| series | international=0 | 291 | 0.579295 | 0.581793 | -0.002499 [-0.011487, 0.006845] | no |
| map | all | 81 | 0.682667 | 0.712390 | -0.029723 [-0.068501, 0.003284] | no |
| map | tier1 | 40 | 0.705902 | 0.763024 | -0.057123 [-0.129030, -0.006733] | yes |
| map | tier2 | 39 | 0.674852 | 0.682577 | -0.007724 [-0.051106, 0.029771] | no |
| map | tier3 | 2 | 0.370336 | 0.281038 | 0.089299 [0.089299, 0.089299] | yes |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 40 | 0.705902 | 0.763024 | -0.057123 [-0.129030, -0.006733] | yes |
| map | international=0 | 41 | 0.659998 | 0.662990 | -0.002992 [-0.043464, 0.034711] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 95 | 95 | 0.0249 | 5.01% [-11.79%, 24.90%] | $56.68 | 1.134× | 16.12% | $6.52 | 46 (49 unfilled) | 2.60% [-19.36%, 23.90%] | $44.82 |
| series | tier1 | 11 | 11 | 0.0182 | 2.70% [-56.09%, 62.67%] | $52.31 | 1.046× | 5.94% | $4.83 | 9 (2 unfilled) | 25.83% [-38.26%, 85.46%] | $53.39 |
| series | tier2 | 81 | 81 | 0.0260 | 7.78% [-9.55%, 27.67%] | $58.61 | 1.172× | 16.12% | $6.22 | 36 (45 unfilled) | -3.77% [-26.79%, 18.20%] | $41.48 |
| series | tier3 | 3 | 3 | 0.0174 | -60.66% [-100.00%, 19.56%] | $46.21 | 0.924× | 9.31% | $4.63 | 1 (2 unfilled) | 19.56% [19.56%, 19.56%] | $50.42 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 11 | 11 | 0.0182 | 2.70% [-56.09%, 62.67%] | $52.31 | 1.046× | 5.94% | $4.83 | 9 (2 unfilled) | 25.83% [-38.26%, 85.46%] | $53.39 |
| series | international=0 | 84 | 84 | 0.0257 | 5.31% [-12.78%, 25.62%] | $54.17 | 1.083× | 16.12% | $6.22 | 37 (47 unfilled) | -3.14% [-25.39%, 18.25%] | $41.74 |
| map | all | 51 | 28 | 0.0401 | 26.63% [-11.36%, 69.46%] | $102.87 | 2.057× | 16.28% | $5.68 | 10 (41 unfilled) | 36.87% [-55.26%, 149.31%] | $56.82 |
| map | tier1 | 24 | 13 | 0.0447 | 64.19% [10.48%, 130.60%] | $92.12 | 1.842× | 8.74% | $4.58 | 7 (17 unfilled) | 96.17% [-5.40%, 200.01%] | $66.38 |
| map | tier2 | 25 | 14 | 0.0352 | 0.89% [-46.83%, 50.68%] | $62.00 | 1.240× | 16.28% | $4.60 | 1 (24 unfilled) | -100.00% [-100.00%, -100.00%] | $47.45 |
| map | tier3 | 2 | 1 | 0.0464 | -100.00% [-100.00%, -100.00%] | $45.00 | 0.900× | 10.00% | $2.37 | 2 (0 unfilled) | -100.00% [-100.00%, -100.00%] | $45.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 24 | 13 | 0.0447 | 64.19% [10.48%, 130.60%] | $92.12 | 1.842× | 8.74% | $4.58 | 7 (17 unfilled) | 96.17% [-5.40%, 200.01%] | $66.38 |
| map | international=0 | 27 | 15 | 0.0360 | -6.64% [-53.65%, 41.08%] | $55.80 | 1.116× | 16.28% | $4.60 | 3 (24 unfilled) | -100.00% [-100.00%, -100.00%] | $42.71 |
| series+map | all | 146 | 114 | 0.0302 | 12.66% [-6.15%, 32.90%] | $118.68 | 2.374× | 19.75% | $14.60 | 56 (90 unfilled) | 8.84% [-14.27%, 34.18%] | $50.94 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-07 | 39 | 0.689838 | 0.674852 | 0.682577 | 6.73% (25), $44.89 | 0.89% (25), $62.00 | 0 (25 unfilled) | — | $50.00 | 1 (24 unfilled) | -100.00% [-100.00%, -100.00%] | $47.45 |
| map | 2026-08 | 40 | 0.699597 | 0.705902 | 0.763024 | 55.57% (29), $92.56 | 64.19% (24), $92.12 | 7 (22 unfilled) | 117.40% [27.87%, 213.35%] | $62.60 | 7 (17 unfilled) | 96.17% [-5.40%, 200.01%] | $66.38 |
| map | 2026-10 | 2 | 0.181525 | 0.370336 | 0.281038 | 29.00% (2), $51.45 | -100.00% (2), $45.00 | 1 (1 unfilled) | 29.00% [29.00%, 29.00%] | $50.94 | 2 (0 unfilled) | -100.00% [-100.00%, -100.00%] | $45.00 |
| series | 2026-07 | 48 | 0.630698 | 0.609779 | 0.605402 | -24.02% (30), $33.35 | -4.29% (6), $48.73 | 16 (14 unfilled) | -18.56% [-64.83%, 26.07%] | $46.16 | 2 (4 unfilled) | -34.64% [-100.00%, 30.72%] | $46.51 |
| series | 2026-08 | 33 | 0.621413 | 0.583965 | 0.584463 | -16.23% (25), $37.36 | 2.70% (11), $52.31 | 21 (4 unfilled) | -6.40% [-55.78%, 50.33%] | $52.26 | 9 (2 unfilled) | 25.83% [-38.26%, 85.46%] | $53.39 |
| series | 2026-09 | 192 | 0.580626 | 0.563878 | 0.568687 | -11.66% (133), $16.80 | 1.16% (71), $54.99 | 60 (73 unfilled) | -7.14% [-30.63%, 16.75%] | $35.97 | 33 (38 unfilled) | -3.99% [-27.45%, 19.50%] | $43.62 |
| series | 2026-10 | 51 | 0.620780 | 0.608643 | 0.608911 | -2.20% (29), $34.71 | 55.14% (7), $50.57 | 11 (18 unfilled) | -2.98% [-59.55%, 55.23%] | $50.01 | 2 (5 unfilled) | 42.17% [19.56%, 64.55%] | $51.71 |

### player_round_glicko_rookie+none: Kalshi comparison and returns

none

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 324 | 0.601977 | 0.582065 | 0.019912 [-0.005205, 0.047373] | no |
| series | tier1 | 33 | 0.616452 | 0.584463 | 0.031988 [-0.054906, 0.119875] | no |
| series | tier2 | 284 | 0.599410 | 0.584967 | 0.014444 [-0.011476, 0.044649] | no |
| series | tier3 | 7 | 0.637883 | 0.453037 | 0.184846 [0.037386, 0.333931] | yes |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 33 | 0.616452 | 0.584463 | 0.031988 [-0.054906, 0.119875] | no |
| series | international=0 | 291 | 0.600336 | 0.581793 | 0.018543 [-0.008084, 0.047327] | no |
| map | all | 81 | 0.689164 | 0.712390 | -0.023225 [-0.060198, 0.013340] | no |
| map | tier1 | 40 | 0.716619 | 0.763024 | -0.046406 [-0.110603, 0.015433] | no |
| map | tier2 | 39 | 0.686509 | 0.682577 | 0.003933 [-0.033978, 0.041372] | no |
| map | tier3 | 2 | 0.191849 | 0.281038 | -0.089188 [-0.089188, -0.089188] | yes |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 40 | 0.716619 | 0.763024 | -0.046406 [-0.110603, 0.015433] | no |
| map | international=0 | 41 | 0.662380 | 0.662990 | -0.000610 [-0.036324, 0.034473] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 217 | 217 | 0.0755 | -14.83% [-28.18%, 0.30%] | $5.19 | 0.104× | 91.44% | $5.89 | 105 (112 unfilled) | -11.25% [-28.73%, 6.60%] | $28.42 |
| series | tier1 | 25 | 25 | 0.1036 | -24.16% [-57.95%, 12.83%] | $33.63 | 0.673× | 32.73% | $4.92 | 20 (5 unfilled) | -18.47% [-57.20%, 23.20%] | $41.32 |
| series | tier2 | 186 | 186 | 0.0714 | -11.43% [-25.97%, 4.66%] | $12.30 | 0.246× | 86.68% | $5.89 | 83 (103 unfilled) | -8.78% [-28.38%, 11.54%] | $36.73 |
| series | tier3 | 6 | 6 | 0.0854 | -80.55% [-100.00%, -40.99%] | $31.94 | 0.639× | 36.12% | $4.76 | 2 (4 unfilled) | -41.37% [-100.00%, 19.56%] | $48.99 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 25 | 25 | 0.1036 | -24.16% [-57.95%, 12.83%] | $33.63 | 0.673× | 32.73% | $4.92 | 20 (5 unfilled) | -18.47% [-57.20%, 23.20%] | $41.32 |
| series | international=0 | 192 | 192 | 0.0719 | -13.61% [-27.42%, 0.96%] | $7.81 | 0.156× | 87.11% | $5.89 | 85 (107 unfilled) | -9.55% [-28.77%, 10.31%] | $35.86 |
| map | all | 56 | 30 | 0.0664 | 14.29% [-9.77%, 39.45%] | $61.62 | 1.232× | 15.90% | $4.55 | 6 (50 unfilled) | 17.78% [-54.56%, 82.18%] | $50.86 |
| map | tier1 | 27 | 14 | 0.0859 | 19.15% [-16.26%, 55.66%] | $62.46 | 1.249× | 10.49% | $3.45 | 5 (22 unfilled) | 15.58% [-70.92%, 102.41%] | $49.92 |
| map | tier2 | 27 | 15 | 0.0479 | 8.35% [-27.68%, 48.95%] | $47.92 | 0.958× | 15.90% | $4.55 | 0 (27 unfilled) | — | $50.00 |
| map | tier3 | 2 | 1 | 0.0527 | 29.00% [29.00%, 29.00%] | $51.45 | 1.029× | 0.00% | $2.45 | 1 (1 unfilled) | 29.00% [29.00%, 29.00%] | $50.94 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 27 | 14 | 0.0859 | 19.15% [-16.26%, 55.66%] | $62.46 | 1.249× | 10.49% | $3.45 | 5 (22 unfilled) | 15.58% [-70.92%, 102.41%] | $49.92 |
| map | international=0 | 29 | 16 | 0.0482 | 9.75% [-24.13%, 47.08%] | $49.32 | 0.986× | 15.90% | $4.55 | 1 (28 unfilled) | 29.00% [29.00%, 29.00%] | $50.94 |
| series+map | all | 273 | 219 | 0.0736 | -8.85% [-21.42%, 3.73%] | $7.18 | 0.144× | 88.16% | $5.89 | 111 (162 unfilled) | -9.69% [-26.74%, 7.00%] | $30.49 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 0 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-07 | series | 244 | 1.055422 | 0.304545 | fitted |
| 2026-07 | map | 109 | 0.536883 | 0.317132 | fitted |
| 2026-08 | series | 244 | 1.055422 | 0.304545 | fitted |
| 2026-08 | map | 109 | 0.536883 | 0.317132 | fitted |
| 2026-09 | series | 244 | 1.055422 | 0.304545 | fitted |
| 2026-10 | series | 244 | 1.055422 | 0.304545 | fitted |
| 2026-10 | map | 109 | 0.536883 | 0.317132 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 324 | 0.580287 | 0.582065 | -0.001778 [-0.010414, 0.006621] | no |
| series | tier1 | 33 | 0.581943 | 0.584463 | -0.002520 [-0.029836, 0.023669] | no |
| series | tier2 | 284 | 0.582243 | 0.584967 | -0.002724 [-0.011260, 0.006808] | no |
| series | tier3 | 7 | 0.493129 | 0.453037 | 0.040092 [-0.003766, 0.089868] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 33 | 0.581943 | 0.584463 | -0.002520 [-0.029836, 0.023669] | no |
| series | international=0 | 291 | 0.580099 | 0.581793 | -0.001694 [-0.010445, 0.007400] | no |
| map | all | 81 | 0.681500 | 0.712390 | -0.030889 [-0.071789, 0.004496] | no |
| map | tier1 | 40 | 0.703133 | 0.763024 | -0.059891 [-0.132308, -0.009060] | yes |
| map | tier2 | 39 | 0.674256 | 0.682577 | -0.008321 [-0.056637, 0.033779] | no |
| map | tier3 | 2 | 0.390086 | 0.281038 | 0.109048 [0.109048, 0.109048] | yes |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 40 | 0.703133 | 0.763024 | -0.059891 [-0.132308, -0.009060] | yes |
| map | international=0 | 41 | 0.660394 | 0.662990 | -0.002595 [-0.047794, 0.040075] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 94 | 94 | 0.0257 | 4.71% [-12.76%, 23.32%] | $58.61 | 1.172× | 17.77% | $6.47 | 44 (50 unfilled) | 3.18% [-19.57%, 25.65%] | $46.36 |
| series | tier1 | 14 | 14 | 0.0249 | 2.31% [-46.98%, 51.84%] | $55.22 | 1.104× | 2.37% | $4.93 | 11 (3 unfilled) | 18.46% [-37.16%, 76.08%] | $56.54 |
| series | tier2 | 77 | 77 | 0.0264 | 7.71% [-11.65%, 29.78%] | $57.27 | 1.145× | 17.79% | $5.86 | 32 (45 unfilled) | -2.66% [-26.66%, 21.22%] | $41.04 |
| series | tier3 | 3 | 3 | 0.0111 | -60.66% [-100.00%, 19.56%] | $46.25 | 0.925× | 7.79% | $3.09 | 1 (2 unfilled) | 19.56% [19.56%, 19.56%] | $49.62 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 14 | 14 | 0.0249 | 2.31% [-46.98%, 51.84%] | $55.22 | 1.104× | 2.37% | $4.93 | 11 (3 unfilled) | 18.46% [-37.16%, 76.08%] | $56.54 |
| series | international=0 | 80 | 80 | 0.0258 | 5.13% [-12.78%, 24.91%] | $52.97 | 1.059× | 17.79% | $5.86 | 33 (47 unfilled) | -1.99% [-26.75%, 19.76%] | $40.64 |
| map | all | 52 | 28 | 0.0467 | 25.67% [-12.40%, 66.85%] | $105.03 | 2.101× | 19.58% | $5.74 | 9 (43 unfilled) | 52.04% [-37.96%, 170.18%] | $57.10 |
| map | tier1 | 24 | 13 | 0.0504 | 67.47% [13.27%, 133.62%] | $96.58 | 1.932× | 3.55% | $4.75 | 6 (18 unfilled) | 128.91% [17.07%, 238.39%] | $66.65 |
| map | tier2 | 26 | 14 | 0.0423 | -2.99% [-50.32%, 47.10%] | $60.41 | 1.208× | 19.58% | $4.49 | 1 (25 unfilled) | -100.00% [-100.00%, -100.00%] | $47.47 |
| map | tier3 | 2 | 1 | 0.0599 | -100.00% [-100.00%, -100.00%] | $45.00 | 0.900× | 10.00% | $2.37 | 2 (0 unfilled) | -100.00% [-100.00%, -100.00%] | $45.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 24 | 13 | 0.0504 | 67.47% [13.27%, 133.62%] | $96.58 | 1.932× | 3.55% | $4.75 | 6 (18 unfilled) | 128.91% [17.07%, 238.39%] | $66.65 |
| map | international=0 | 28 | 15 | 0.0436 | -9.97% [-56.53%, 39.54%] | $54.37 | 1.087× | 19.58% | $4.49 | 3 (25 unfilled) | -100.00% [-100.00%, -100.00%] | $42.72 |
| series+map | all | 146 | 111 | 0.0331 | 12.27% [-6.57%, 30.96%] | $110.53 | 2.211× | 21.69% | $13.45 | 53 (93 unfilled) | 11.63% [-11.27%, 39.77%] | $49.09 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-07 | 39 | 0.686509 | 0.674256 | 0.682577 | 8.35% (27), $47.92 | -2.99% (26), $60.41 | 0 (27 unfilled) | — | $50.00 | 1 (25 unfilled) | -100.00% [-100.00%, -100.00%] | $47.47 |
| map | 2026-08 | 40 | 0.716619 | 0.703133 | 0.763024 | 19.15% (27), $62.46 | 67.47% (24), $96.58 | 5 (22 unfilled) | 15.58% [-70.92%, 102.41%] | $49.92 | 6 (18 unfilled) | 128.91% [17.07%, 238.39%] | $66.65 |
| map | 2026-10 | 2 | 0.191849 | 0.390086 | 0.281038 | 29.00% (2), $51.45 | -100.00% (2), $45.00 | 1 (1 unfilled) | 29.00% [29.00%, 29.00%] | $50.94 | 2 (0 unfilled) | -100.00% [-100.00%, -100.00%] | $45.00 |
| series | 2026-07 | 48 | 0.635337 | 0.611126 | 0.605402 | -27.96% (32), $32.51 | -4.29% (6), $48.42 | 16 (16 unfilled) | -26.33% [-74.57%, 24.32%] | $43.16 | 2 (4 unfilled) | -34.64% [-100.00%, 30.72%] | $46.87 |
| series | 2026-08 | 33 | 0.616452 | 0.581943 | 0.584463 | -24.16% (25), $33.63 | 2.31% (14), $55.22 | 20 (5 unfilled) | -18.47% [-57.20%, 23.20%] | $41.32 | 11 (3 unfilled) | 18.46% [-37.16%, 76.08%] | $56.54 |
| series | 2026-09 | 192 | 0.585999 | 0.564705 | 0.568687 | -10.86% (132), $17.49 | 0.70% (67), $51.17 | 58 (74 unfilled) | -3.69% [-27.35%, 17.61%] | $43.13 | 29 (38 unfilled) | -2.80% [-28.13%, 21.44%] | $43.34 |
| series | 2026-10 | 51 | 0.621364 | 0.608853 | 0.608911 | -10.05% (28), $34.98 | 55.14% (7), $53.47 | 11 (17 unfilled) | -15.66% [-72.15%, 43.72%] | $48.48 | 2 (5 unfilled) | 42.17% [19.56%, 64.55%] | $50.26 |

### player_round_glicko_rookie+calibration: Kalshi comparison and returns

calibration: ridge=4; tier1/online=0: rows=1092, T=0.7067; tier1/online=1: rows=567, T=0.7637; tier2/online=0: rows=253, T=1.0000; tier2/online=1: rows=4454, T=0.9685; tier3/online=0: rows=3215, T=1.0226; tier3/online=1: rows=40549, T=0.9383; unknown/online=0: rows=23, T=1.0000

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 324 | 0.600650 | 0.582065 | 0.018585 [-0.006467, 0.044760] | no |
| series | tier1 | 33 | 0.619186 | 0.584463 | 0.034723 [-0.042312, 0.109231] | no |
| series | tier2 | 284 | 0.597610 | 0.584967 | 0.012643 [-0.012627, 0.041419] | no |
| series | tier3 | 7 | 0.636605 | 0.453037 | 0.183568 [0.036541, 0.330942] | yes |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 33 | 0.619186 | 0.584463 | 0.034723 [-0.042312, 0.109231] | no |
| series | international=0 | 291 | 0.598548 | 0.581793 | 0.016755 [-0.009227, 0.044851] | no |
| map | all | 81 | 0.680614 | 0.712390 | -0.031775 [-0.069231, 0.003450] | no |
| map | tier1 | 40 | 0.699748 | 0.763024 | -0.063277 [-0.133048, -0.005750] | yes |
| map | tier2 | 39 | 0.685162 | 0.682577 | 0.002585 [-0.035170, 0.039133] | no |
| map | tier3 | 2 | 0.209268 | 0.281038 | -0.071769 [-0.071769, -0.071769] | yes |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 40 | 0.699748 | 0.763024 | -0.063277 [-0.133048, -0.005750] | yes |
| map | international=0 | 41 | 0.661948 | 0.662990 | -0.001042 [-0.036275, 0.032979] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 214 | 214 | 0.0733 | -12.61% [-27.31%, 3.63%] | $6.77 | 0.135× | 88.99% | $5.94 | 105 (109 unfilled) | -5.55% [-25.48%, 16.06%] | $42.40 |
| series | tier1 | 24 | 24 | 0.0930 | -18.21% [-62.08%, 34.47%] | $37.86 | 0.757× | 24.28% | $4.91 | 21 (3 unfilled) | -6.40% [-55.78%, 50.33%] | $52.53 |
| series | tier2 | 184 | 184 | 0.0703 | -9.64% [-25.72%, 6.62%] | $14.16 | 0.283× | 85.29% | $5.94 | 82 (102 unfilled) | -4.45% [-26.59%, 19.30%] | $41.66 |
| series | tier3 | 6 | 6 | 0.0850 | -80.55% [-100.00%, -40.99%] | $31.99 | 0.640× | 36.02% | $4.76 | 2 (4 unfilled) | -41.37% [-100.00%, 19.56%] | $49.05 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 24 | 24 | 0.0930 | -18.21% [-62.08%, 34.47%] | $37.86 | 0.757× | 24.28% | $4.91 | 21 (3 unfilled) | -6.40% [-55.78%, 50.33%] | $52.53 |
| series | international=0 | 190 | 190 | 0.0708 | -11.90% [-27.39%, 4.45%] | $9.01 | 0.180× | 85.29% | $5.94 | 84 (106 unfilled) | -5.33% [-26.76%, 18.93%] | $40.80 |
| map | all | 56 | 31 | 0.0569 | 30.63% [-1.92%, 66.73%] | $95.87 | 1.917× | 15.54% | $4.58 | 6 (50 unfilled) | 112.07% [6.33%, 227.14%] | $63.51 |
| map | tier1 | 27 | 15 | 0.0683 | 52.92% [-2.08%, 114.59%] | $93.20 | 1.864× | 9.04% | $4.46 | 5 (22 unfilled) | 128.24% [-6.01%, 257.05%] | $62.39 |
| map | tier2 | 27 | 15 | 0.0468 | 8.35% [-27.68%, 48.95%] | $49.96 | 0.999× | 15.54% | $4.55 | 0 (27 unfilled) | — | $50.00 |
| map | tier3 | 2 | 1 | 0.0384 | 29.00% [29.00%, 29.00%] | $51.45 | 1.029× | 0.00% | $2.45 | 1 (1 unfilled) | 29.00% [29.00%, 29.00%] | $50.94 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 27 | 15 | 0.0683 | 52.92% [-2.08%, 114.59%] | $93.20 | 1.864× | 9.04% | $4.46 | 5 (22 unfilled) | 128.24% [-6.01%, 257.05%] | $62.39 |
| map | international=0 | 29 | 16 | 0.0462 | 9.75% [-24.13%, 47.08%] | $51.41 | 1.028× | 15.54% | $4.55 | 1 (28 unfilled) | 29.00% [29.00%, 29.00%] | $50.94 |
| series+map | all | 270 | 216 | 0.0699 | -3.63% [-18.82%, 11.80%] | $10.95 | 0.219× | 82.31% | $5.94 | 111 (159 unfilled) | 0.84% [-20.65%, 25.35%] | $43.71 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 0 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-07 | series | 244 | 1.093983 | 0.346627 | fitted |
| 2026-07 | map | 109 | 0.639421 | 0.391277 | fitted |
| 2026-08 | series | 244 | 1.093983 | 0.346627 | fitted |
| 2026-08 | map | 109 | 0.639421 | 0.391277 | fitted |
| 2026-09 | series | 244 | 1.093983 | 0.346627 | fitted |
| 2026-10 | series | 244 | 1.093983 | 0.346627 | fitted |
| 2026-10 | map | 109 | 0.639421 | 0.391277 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 324 | 0.580634 | 0.582065 | -0.001431 [-0.011120, 0.008187] | no |
| series | tier1 | 33 | 0.584048 | 0.584463 | -0.000415 [-0.023096, 0.021304] | no |
| series | tier2 | 284 | 0.582372 | 0.584967 | -0.002594 [-0.012542, 0.008528] | no |
| series | tier3 | 7 | 0.493991 | 0.453037 | 0.040954 [-0.011024, 0.101861] | no |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 33 | 0.584048 | 0.584463 | -0.000415 [-0.023096, 0.021304] | no |
| series | international=0 | 291 | 0.580246 | 0.581793 | -0.001547 [-0.011831, 0.009070] | no |
| map | all | 81 | 0.681141 | 0.712390 | -0.031248 [-0.069107, 0.001212] | no |
| map | tier1 | 40 | 0.704397 | 0.763024 | -0.058627 [-0.130473, -0.007975] | yes |
| map | tier2 | 39 | 0.673964 | 0.682577 | -0.008613 [-0.050529, 0.027617] | no |
| map | tier3 | 2 | 0.355975 | 0.281038 | 0.074938 [0.074938, 0.074938] | yes |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 40 | 0.704397 | 0.763024 | -0.058627 [-0.130473, -0.007975] | yes |
| map | international=0 | 41 | 0.658452 | 0.662990 | -0.004537 [-0.043460, 0.030043] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 104 | 104 | 0.0287 | 1.48% [-15.05%, 19.36%] | $59.17 | 1.183× | 16.99% | $6.86 | 48 (56 unfilled) | -1.72% [-23.83%, 19.35%] | $45.88 |
| series | tier1 | 12 | 12 | 0.0200 | -5.90% [-60.52%, 50.14%] | $52.17 | 1.043× | 5.98% | $4.91 | 10 (2 unfilled) | 13.15% [-46.07%, 74.65%] | $53.82 |
| series | tier2 | 89 | 89 | 0.0302 | 4.60% [-12.35%, 24.92%] | $63.11 | 1.262× | 16.99% | $6.58 | 37 (52 unfilled) | -6.38% [-28.84%, 15.35%] | $42.43 |
| series | tier3 | 3 | 3 | 0.0188 | -60.66% [-100.00%, 19.56%] | $44.96 | 0.899× | 11.32% | $4.55 | 1 (2 unfilled) | 19.56% [19.56%, 19.56%] | $50.16 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 12 | 12 | 0.0200 | -5.90% [-60.52%, 50.14%] | $52.17 | 1.043× | 5.98% | $4.91 | 10 (2 unfilled) | 13.15% [-46.07%, 74.65%] | $53.82 |
| series | international=0 | 92 | 92 | 0.0298 | 2.46% [-14.68%, 20.60%] | $56.76 | 1.135× | 16.99% | $6.58 | 38 (54 unfilled) | -5.70% [-27.99%, 16.62%] | $42.49 |
| map | all | 54 | 29 | 0.0373 | 28.81% [-5.78%, 67.44%] | $106.82 | 2.136× | 13.60% | $5.86 | 10 (44 unfilled) | 36.87% [-55.26%, 149.31%] | $57.60 |
| map | tier1 | 26 | 14 | 0.0438 | 64.22% [14.87%, 125.15%] | $94.87 | 1.897× | 5.34% | $4.69 | 7 (19 unfilled) | 96.17% [-5.40%, 200.01%] | $66.69 |
| map | tier2 | 26 | 14 | 0.0309 | 3.51% [-42.15%, 51.62%] | $62.46 | 1.249× | 13.60% | $4.65 | 1 (25 unfilled) | -100.00% [-100.00%, -100.00%] | $47.80 |
| map | tier3 | 2 | 1 | 0.0364 | -100.00% [-100.00%, -100.00%] | $45.06 | 0.901× | 9.88% | $2.34 | 2 (0 unfilled) | -100.00% [-100.00%, -100.00%] | $45.06 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 26 | 14 | 0.0438 | 64.22% [14.87%, 125.15%] | $94.87 | 1.897× | 5.34% | $4.69 | 7 (19 unfilled) | 96.17% [-5.40%, 200.01%] | $66.69 |
| map | international=0 | 28 | 15 | 0.0313 | -3.95% [-47.06%, 41.19%] | $56.29 | 1.126× | 13.60% | $4.65 | 3 (25 unfilled) | -100.00% [-100.00%, -100.00%] | $43.08 |
| series+map | all | 158 | 121 | 0.0316 | 10.94% [-6.66%, 31.35%] | $122.31 | 2.446× | 21.88% | $15.14 | 58 (100 unfilled) | 5.06% [-18.49%, 28.46%] | $50.98 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-07 | 39 | 0.685162 | 0.673964 | 0.682577 | 8.35% (27), $49.96 | 3.51% (26), $62.46 | 0 (27 unfilled) | — | $50.00 | 1 (25 unfilled) | -100.00% [-100.00%, -100.00%] | $47.80 |
| map | 2026-08 | 40 | 0.699748 | 0.704397 | 0.763024 | 52.92% (27), $93.20 | 64.22% (26), $94.87 | 5 (22 unfilled) | 128.24% [-6.01%, 257.05%] | $62.39 | 7 (19 unfilled) | 96.17% [-5.40%, 200.01%] | $66.69 |
| map | 2026-10 | 2 | 0.209268 | 0.355975 | 0.281038 | 29.00% (2), $51.45 | -100.00% (2), $45.06 | 1 (1 unfilled) | 29.00% [29.00%, 29.00%] | $50.94 | 2 (0 unfilled) | -100.00% [-100.00%, -100.00%] | $45.06 |
| series | 2026-07 | 48 | 0.632791 | 0.611302 | 0.605402 | -30.20% (33), $33.82 | -4.29% (6), $49.16 | 17 (16 unfilled) | -30.77% [-73.34%, 16.36%] | $44.69 | 2 (4 unfilled) | -34.64% [-100.00%, 30.72%] | $46.29 |
| series | 2026-08 | 33 | 0.619186 | 0.584048 | 0.584463 | -18.21% (24), $37.86 | -5.90% (12), $52.17 | 21 (3 unfilled) | -6.40% [-55.78%, 50.33%] | $52.53 | 10 (2 unfilled) | 13.15% [-46.07%, 74.65%] | $53.82 |
| series | 2026-09 | 192 | 0.584414 | 0.565002 | 0.568687 | -8.30% (130), $17.99 | -0.73% (77), $58.21 | 57 (73 unfilled) | 2.68% [-23.16%, 30.88%] | $45.99 | 34 (43 unfilled) | -6.82% [-29.45%, 15.97%] | $44.52 |
| series | 2026-10 | 51 | 0.619528 | 0.608410 | 0.608911 | -6.70% (27), $37.65 | 33.93% (9), $49.55 | 10 (17 unfilled) | -7.19% [-69.34%, 56.85%] | $49.95 | 2 (7 unfilled) | 42.17% [19.56%, 64.55%] | $51.64 |

# R6 Elo backtest

## Combined summary (validation, all sections)

| Model | Series Δ log loss | Series flat ROI | Series Kelly (LoL caps) $ | Series flat ROI depth-capped | Series Kelly depth-capped $ | Map Δ log loss | Map flat ROI | Map Kelly (LoL caps) $ | Map flat ROI depth-capped | Map Kelly depth-capped $ | Series blended Δ log loss | Series blended flat ROI | Series blended Kelly (LoL caps) $ | Series blended flat ROI depth-capped | Series blended Kelly depth-capped $ | Map blended Δ log loss | Map blended flat ROI | Map blended Kelly (LoL caps) $ | Map blended flat ROI depth-capped | Map blended Kelly depth-capped $ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| team_elo | 0.093656 | -5.55% | $4.18 | -12.28% | $9.91 | 0.084554 | -6.88% | $19.85 | -33.74% | $42.98 | 0.005457 | -21.40% | $44.38 | -2.60% | $63.42 | — | — | $50.00 | — | $50.00 |
| player_round_glicko | 0.025265 | -0.12% | $5.00 | -9.14% | $17.86 | 0.001314 | 19.86% | $103.21 | -40.74% | $45.96 | 0.009485 | -24.24% | $31.19 | -17.18% | $40.35 | — | — | $50.00 | — | $50.00 |
| player_round_glicko_rookie | 0.020165 | -1.51% | $7.66 | -6.82% | $21.48 | -0.003576 | 19.44% | $98.96 | -40.74% | $45.94 | 0.006674 | -15.65% | $35.50 | -12.09% | $45.86 | — | — | $50.00 | — | $50.00 |
| team_elo+none | 0.093656 | -5.55% | $4.18 | -12.28% | $9.91 | 0.084554 | -6.88% | $19.85 | -33.74% | $42.98 | 0.005457 | -21.40% | $44.38 | -2.60% | $63.42 | — | — | $50.00 | — | $50.00 |
| team_elo+regional | 0.087404 | -4.69% | $8.49 | -8.66% | $17.66 | 0.047226 | 1.85% | $38.48 | -40.58% | $40.62 | 0.004804 | -26.53% | $46.48 | -4.36% | $58.21 | — | — | $50.00 | — | $50.00 |
| team_elo+calibration | 0.068889 | 0.86% | $5.29 | -4.72% | $22.35 | 0.012166 | 18.77% | $47.87 | -48.09% | $41.34 | 0.007054 | -23.99% | $38.15 | -8.35% | $59.71 | — | — | $50.00 | — | $50.00 |
| player_round_glicko+none | 0.025265 | -0.12% | $5.00 | -9.14% | $17.86 | 0.001314 | 19.86% | $103.21 | -40.74% | $45.96 | 0.009485 | -24.24% | $31.19 | -17.18% | $40.35 | — | — | $50.00 | — | $50.00 |
| player_round_glicko+regional | 0.024139 | -4.75% | $4.62 | -9.40% | $17.99 | -0.005069 | 17.42% | $100.25 | -40.74% | $45.96 | 0.009164 | -15.04% | $31.17 | -3.09% | $44.23 | — | — | $50.00 | — | $50.00 |
| player_round_glicko+calibration | 0.024288 | -5.26% | $6.41 | -9.80% | $21.51 | -0.009761 | 17.93% | $97.30 | -50.79% | $44.11 | 0.008759 | -21.76% | $27.64 | -29.69% | $37.39 | — | — | $50.00 | — | $50.00 |
| player_round_glicko_rookie+none | 0.020165 | -1.51% | $7.66 | -6.82% | $21.48 | -0.003576 | 19.44% | $98.96 | -40.74% | $45.94 | 0.006674 | -15.65% | $35.50 | -12.09% | $45.86 | — | — | $50.00 | — | $50.00 |
| player_round_glicko_rookie+regional | 0.020204 | -1.89% | $6.49 | -8.17% | $20.05 | -0.009187 | 17.09% | $93.90 | -40.74% | $45.94 | 0.006905 | -11.61% | $36.95 | -9.17% | $47.16 | — | — | $50.00 | — | $50.00 |
| player_round_glicko_rookie+calibration | 0.019594 | -5.16% | $10.61 | -8.77% | $31.66 | -0.015746 | 19.70% | $107.80 | -50.79% | $44.27 | 0.006067 | -18.44% | $32.47 | -22.82% | $40.68 | — | — | $50.00 | — | $50.00 |

Series temperatures (stage 1; p′ = σ(T·logit p), T < 1 pulls odds toward 50%): team_elo Bo3 0.63, Bo5 0.40; player_round_glicko_rookie Bo3 0.70, Bo5 0.63; player_round_glicko Bo3 0.77, Bo5 0.64; team_elo+none Bo3 0.63, Bo5 0.40; team_elo+regional Bo3 0.64, Bo5 0.40; team_elo+calibration Bo3 0.73, Bo5 0.40; player_round_glicko+none Bo3 0.77, Bo5 0.64; player_round_glicko+regional Bo3 0.77, Bo5 0.64; player_round_glicko+calibration Bo3 0.75, Bo5 0.63; player_round_glicko_rookie+none Bo3 0.70, Bo5 0.63; player_round_glicko_rookie+regional Bo3 0.71, Bo5 0.63; player_round_glicko_rookie+calibration Bo3 0.75, Bo5 0.67

Parameters minimize tuning map log loss across all sections. Replay predicts before update; Replay starts at the first map. Tuning: [2023-01-01, 2026-01-01); validation: [2026-01-01, 2026-07-01). Holdout is scored only with --holdout and never selects parameters. Series use the first map prediction and independent maps in Bo1/Bo3/Bo5; Bo2, unknown/unsupported lengths and unknown results are skipped. Accuracy gives 0.5 predictions half credit; ECE uses 10 equal-width bins. Log loss clips probabilities at 1e-6. Paired bootstrap uses 2,000 resamples, seed 0, clustered by match_id. Differences are the named model minus its comparator; negative favors the model. Significance requires a 95% percentile interval excluding zero. Tuning scores are selection diagnostics, not independent evidence of improvement.

Fit through 2025-12-31. Unknown host-region map rows: 6007 (including missing/un).

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
| tradeable | team_elo+regional | series | 244 | 0.087404 | 0.004804 | -8.66% | -4.36% |
| tradeable | team_elo+regional | map | 109 | 0.047226 | — | -40.58% | — |
| tradeable | team_elo+calibration | series | 244 | 0.068889 | 0.007054 | -4.72% | -8.35% |
| tradeable | team_elo+calibration | map | 109 | 0.012166 | — | -48.09% | — |
| tradeable | player_round_glicko+none | series | 244 | 0.025265 | 0.009485 | -9.14% | -17.18% |
| tradeable | player_round_glicko+none | map | 109 | 0.001314 | — | -40.74% | — |
| tradeable | player_round_glicko+regional | series | 244 | 0.024139 | 0.009164 | -9.40% | -3.09% |
| tradeable | player_round_glicko+regional | map | 109 | -0.005069 | — | -40.74% | — |
| tradeable | player_round_glicko+calibration | series | 244 | 0.024288 | 0.008759 | -9.80% | -29.69% |
| tradeable | player_round_glicko+calibration | map | 109 | -0.009761 | — | -50.79% | — |
| tradeable | player_round_glicko_rookie+none | series | 244 | 0.020165 | 0.006674 | -6.82% | -12.09% |
| tradeable | player_round_glicko_rookie+none | map | 109 | -0.003576 | — | -40.74% | — |
| tradeable | player_round_glicko_rookie+regional | series | 244 | 0.020204 | 0.006905 | -8.17% | -9.17% |
| tradeable | player_round_glicko_rookie+regional | map | 109 | -0.009187 | — | -40.74% | — |
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
| hours24 | team_elo+regional | series | 109 | 0.120114 | — | -31.67% | — |
| hours24 | team_elo+regional | map | 44 | 0.067011 | — | — | — |
| hours24 | team_elo+calibration | series | 109 | 0.093531 | — | -19.61% | — |
| hours24 | team_elo+calibration | map | 44 | -0.003006 | — | -100.00% | — |
| hours24 | player_round_glicko+none | series | 109 | 0.006323 | — | -21.37% | — |
| hours24 | player_round_glicko+none | map | 44 | -0.039777 | — | -100.00% | — |
| hours24 | player_round_glicko+regional | series | 109 | 0.007646 | — | -19.44% | — |
| hours24 | player_round_glicko+regional | map | 44 | -0.035823 | — | -100.00% | — |
| hours24 | player_round_glicko+calibration | series | 109 | 0.013510 | — | -21.38% | — |
| hours24 | player_round_glicko+calibration | map | 44 | -0.056343 | — | -100.00% | — |
| hours24 | player_round_glicko_rookie+none | series | 109 | 0.000483 | — | -14.26% | — |
| hours24 | player_round_glicko_rookie+none | map | 44 | -0.039804 | — | -100.00% | — |
| hours24 | player_round_glicko_rookie+regional | series | 109 | 0.002506 | — | -14.26% | — |
| hours24 | player_round_glicko_rookie+regional | map | 44 | -0.037599 | — | -100.00% | — |
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
| hours6 | team_elo+regional | series | 225 | 0.087110 | 0.008954 | 4.60% | -6.20% |
| hours6 | team_elo+regional | map | 101 | 0.055253 | — | -7.14% | — |
| hours6 | team_elo+calibration | series | 225 | 0.067086 | 0.012754 | -4.94% | -8.73% |
| hours6 | team_elo+calibration | map | 101 | 0.013732 | — | -4.06% | — |
| hours6 | player_round_glicko+none | series | 225 | 0.020227 | 0.014016 | -10.41% | -16.62% |
| hours6 | player_round_glicko+none | map | 101 | 0.000572 | — | -27.07% | — |
| hours6 | player_round_glicko+regional | series | 225 | 0.018846 | 0.015920 | -13.37% | -16.26% |
| hours6 | player_round_glicko+regional | map | 101 | -0.006282 | — | -32.48% | — |
| hours6 | player_round_glicko+calibration | series | 225 | 0.020486 | 0.015613 | -12.24% | -21.61% |
| hours6 | player_round_glicko+calibration | map | 101 | -0.011870 | — | -29.35% | — |
| hours6 | player_round_glicko_rookie+none | series | 225 | 0.014415 | 0.013427 | -8.19% | -17.53% |
| hours6 | player_round_glicko_rookie+none | map | 101 | -0.003735 | — | -17.47% | — |
| hours6 | player_round_glicko_rookie+regional | series | 225 | 0.014062 | 0.014682 | -7.10% | -8.94% |
| hours6 | player_round_glicko_rookie+regional | map | 101 | -0.009933 | — | -23.59% | — |
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
| player_round_glicko_rookie+regional | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 280, "rookie_maps": 3200, "rookie_penalty": 225, "tau": 0.75} | 0.569669 | 0.552075 | 9782 |
| player_round_glicko+calibration | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 280, "tau": 0.75} | 0.577029 | 0.562958 | 9782 |
| player_round_glicko+regional | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 280, "tau": 0.75} | 0.577421 | 0.563130 | 9782 |
| player_round_glicko | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 280, "tau": 0.75} | 0.577429 | 0.563146 | 9782 |
| player_round_glicko+none | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 280, "tau": 0.75} | 0.577429 | 0.563146 | 9782 |
| team_elo+calibration | {"k": 64} | 0.631718 | 0.628573 | 9782 |
| team_elo+regional | {"k": 64} | 0.633476 | 0.629966 | 9782 |
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
| team_elo+regional | all | 9782 | 0.633476 | 0.221170 | 0.640309 | 0.029636 |
| team_elo+regional | tier1 | 393 | 0.703898 | 0.251271 | 0.568702 | 0.076231 |
| team_elo+regional | tier2 | 757 | 0.630648 | 0.217529 | 0.645310 | 0.069367 |
| team_elo+regional | tier3 | 8632 | 0.630518 | 0.220119 | 0.643130 | 0.027549 |
| team_elo+regional | unknown | 0 | — | — | — | — |
| team_elo+regional | international=1 | 593 | 0.659218 | 0.231809 | 0.623946 | 0.035236 |
| team_elo+regional | international=0 | 9189 | 0.631815 | 0.220483 | 0.641365 | 0.029434 |

team_elo+regional − coin (paired log loss):

| Section | Rows | team_elo+regional log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9782 | 0.633476 | 0.693147 | -0.059671 | [-0.067426, -0.051724] | yes |
| tier1 | 393 | 0.703898 | 0.693147 | 0.010751 | [-0.025582, 0.048504] | no |
| tier2 | 757 | 0.630648 | 0.693147 | -0.062499 | [-0.098211, -0.024861] | yes |
| tier3 | 8632 | 0.630518 | 0.693147 | -0.062629 | [-0.070648, -0.054426] | yes |
| international=1 | 593 | 0.659218 | 0.693147 | -0.033929 | [-0.065648, -0.002013] | yes |
| international=0 | 9189 | 0.631815 | 0.693147 | -0.061332 | [-0.069016, -0.053514] | yes |

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
| player_round_glicko+regional | all | 9782 | 0.577421 | 0.197588 | 0.685749 | 0.016908 |
| player_round_glicko+regional | tier1 | 393 | 0.667932 | 0.233264 | 0.625954 | 0.054828 |
| player_round_glicko+regional | tier2 | 757 | 0.547723 | 0.186130 | 0.726552 | 0.027843 |
| player_round_glicko+regional | tier3 | 8632 | 0.575904 | 0.196968 | 0.684893 | 0.019162 |
| player_round_glicko+regional | unknown | 0 | — | — | — | — |
| player_round_glicko+regional | international=1 | 593 | 0.633185 | 0.219080 | 0.649241 | 0.037092 |
| player_round_glicko+regional | international=0 | 9189 | 0.573822 | 0.196201 | 0.688105 | 0.017783 |

player_round_glicko+regional − coin (paired log loss):

| Section | Rows | player_round_glicko+regional log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9782 | 0.577421 | 0.693147 | -0.115727 | [-0.123985, -0.107086] | yes |
| tier1 | 393 | 0.667932 | 0.693147 | -0.025215 | [-0.065192, 0.015078] | no |
| tier2 | 757 | 0.547723 | 0.693147 | -0.145424 | [-0.177851, -0.113379] | yes |
| tier3 | 8632 | 0.575904 | 0.693147 | -0.117243 | [-0.126207, -0.108524] | yes |
| international=1 | 593 | 0.633185 | 0.693147 | -0.059962 | [-0.096300, -0.023699] | yes |
| international=0 | 9189 | 0.573822 | 0.693147 | -0.119325 | [-0.128174, -0.110354] | yes |

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
| player_round_glicko_rookie+regional | all | 9782 | 0.569669 | 0.193672 | 0.695819 | 0.018646 |
| player_round_glicko_rookie+regional | tier1 | 393 | 0.676101 | 0.233549 | 0.618321 | 0.071132 |
| player_round_glicko_rookie+regional | tier2 | 757 | 0.538982 | 0.183421 | 0.727873 | 0.034516 |
| player_round_glicko_rookie+regional | tier3 | 8632 | 0.567514 | 0.192756 | 0.696536 | 0.019867 |
| player_round_glicko_rookie+regional | unknown | 0 | — | — | — | — |
| player_round_glicko_rookie+regional | international=1 | 593 | 0.636186 | 0.218033 | 0.645868 | 0.044941 |
| player_round_glicko_rookie+regional | international=0 | 9189 | 0.565376 | 0.192100 | 0.699042 | 0.017964 |

player_round_glicko_rookie+regional − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie+regional log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9782 | 0.569669 | 0.693147 | -0.123479 | [-0.132579, -0.113660] | yes |
| tier1 | 393 | 0.676101 | 0.693147 | -0.017046 | [-0.061288, 0.032707] | no |
| tier2 | 757 | 0.538982 | 0.693147 | -0.154165 | [-0.187199, -0.120969] | yes |
| tier3 | 8632 | 0.567514 | 0.693147 | -0.125633 | [-0.135450, -0.115727] | yes |
| international=1 | 593 | 0.636186 | 0.693147 | -0.056962 | [-0.096361, -0.015609] | yes |
| international=0 | 9189 | 0.565376 | 0.693147 | -0.127771 | [-0.137860, -0.117733] | yes |

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

team_elo+regional − team_elo (paired log loss):

| Section | Rows | team_elo+regional log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9782 | 0.633476 | 0.633978 | -0.000502 | [-0.000995, -0.000040] | yes |

team_elo+calibration − team_elo (paired log loss):

| Section | Rows | team_elo+calibration log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9782 | 0.631718 | 0.633978 | -0.002261 | [-0.003575, -0.001011] | yes |

player_round_glicko+none − team_elo (paired log loss):

| Section | Rows | player_round_glicko+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9782 | 0.577429 | 0.633978 | -0.056549 | [-0.063107, -0.049410] | yes |

player_round_glicko+regional − team_elo (paired log loss):

| Section | Rows | player_round_glicko+regional log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9782 | 0.577421 | 0.633978 | -0.056558 | [-0.063208, -0.049357] | yes |

player_round_glicko+calibration − team_elo (paired log loss):

| Section | Rows | player_round_glicko+calibration log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9782 | 0.577029 | 0.633978 | -0.056950 | [-0.063572, -0.049760] | yes |

player_round_glicko_rookie+none − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9782 | 0.569667 | 0.633978 | -0.064311 | [-0.071964, -0.056331] | yes |

player_round_glicko_rookie+regional − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie+regional log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9782 | 0.569669 | 0.633978 | -0.064310 | [-0.072011, -0.056417] | yes |

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

team_elo+regional − player_round_glicko_rookie (paired log loss):

| Section | Rows | team_elo+regional log loss | player_round_glicko_rookie log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9782 | 0.633476 | 0.569667 | 0.063809 | [0.055854, 0.071431] | yes |
| tier1 | 393 | 0.703898 | 0.677440 | 0.026459 | [-0.012635, 0.064586] | no |
| tier2 | 757 | 0.630648 | 0.538149 | 0.092499 | [0.059708, 0.123532] | yes |
| tier3 | 8632 | 0.630518 | 0.567525 | 0.062993 | [0.054670, 0.071255] | yes |
| international=1 | 593 | 0.659218 | 0.636911 | 0.022307 | [-0.008247, 0.051360] | no |
| international=0 | 9189 | 0.631815 | 0.565328 | 0.066487 | [0.058614, 0.074812] | yes |

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

player_round_glicko+regional − player_round_glicko_rookie (paired log loss):

| Section | Rows | player_round_glicko+regional log loss | player_round_glicko_rookie log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9782 | 0.577421 | 0.569667 | 0.007753 | [0.004913, 0.010361] | yes |
| tier1 | 393 | 0.667932 | 0.677440 | -0.009508 | [-0.022338, 0.001188] | no |
| tier2 | 757 | 0.547723 | 0.538149 | 0.009575 | [0.005114, 0.013734] | yes |
| tier3 | 8632 | 0.575904 | 0.567525 | 0.008379 | [0.005346, 0.011309] | yes |
| international=1 | 593 | 0.633185 | 0.636911 | -0.003726 | [-0.013519, 0.005145] | no |
| international=0 | 9189 | 0.573822 | 0.565328 | 0.008494 | [0.005493, 0.011252] | yes |

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

player_round_glicko_rookie+regional − player_round_glicko_rookie (paired log loss):

| Section | Rows | player_round_glicko_rookie+regional log loss | player_round_glicko_rookie log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9782 | 0.569669 | 0.569667 | 0.000001 | [-0.000249, 0.000265] | no |
| tier1 | 393 | 0.676101 | 0.677440 | -0.001339 | [-0.006555, 0.003799] | no |
| tier2 | 757 | 0.538982 | 0.538149 | 0.000834 | [-0.000982, 0.002639] | no |
| tier3 | 8632 | 0.567514 | 0.567525 | -0.000011 | [-0.000097, 0.000072] | no |
| international=1 | 593 | 0.636186 | 0.636911 | -0.000726 | [-0.004297, 0.002680] | no |
| international=0 | 9189 | 0.565376 | 0.565328 | 0.000048 | [-0.000122, 0.000210] | no |

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
| team_elo+regional | all | 6949 | 0.629966 | 0.219568 | 0.645848 | 0.029659 |
| team_elo+regional | tier1 | 172 | 0.674015 | 0.238646 | 0.590116 | 0.071695 |
| team_elo+regional | tier2 | 486 | 0.622382 | 0.212093 | 0.663580 | 0.080837 |
| team_elo+regional | tier3 | 6291 | 0.629348 | 0.219624 | 0.646002 | 0.027076 |
| team_elo+regional | unknown | 0 | — | — | — | — |
| team_elo+regional | international=1 | 274 | 0.630084 | 0.220033 | 0.631387 | 0.051749 |
| team_elo+regional | international=0 | 6675 | 0.629962 | 0.219549 | 0.646442 | 0.029848 |

team_elo+regional − coin (paired log loss):

| Section | Rows | team_elo+regional log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6949 | 0.629966 | 0.693147 | -0.063181 | [-0.072329, -0.054925] | yes |
| tier1 | 172 | 0.674015 | 0.693147 | -0.019132 | [-0.077070, 0.039828] | no |
| tier2 | 486 | 0.622382 | 0.693147 | -0.070765 | [-0.115373, -0.025495] | yes |
| tier3 | 6291 | 0.629348 | 0.693147 | -0.063799 | [-0.072370, -0.054499] | yes |
| international=1 | 274 | 0.630084 | 0.693147 | -0.063063 | [-0.105428, -0.014371] | yes |
| international=0 | 6675 | 0.629962 | 0.693147 | -0.063186 | [-0.071794, -0.054434] | yes |

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
| player_round_glicko+regional | all | 6949 | 0.563130 | 0.191438 | 0.702619 | 0.020014 |
| player_round_glicko+regional | tier1 | 172 | 0.621574 | 0.213517 | 0.680233 | 0.062265 |
| player_round_glicko+regional | tier2 | 486 | 0.535101 | 0.180608 | 0.742798 | 0.045140 |
| player_round_glicko+regional | tier3 | 6291 | 0.563698 | 0.191671 | 0.700127 | 0.022681 |
| player_round_glicko+regional | unknown | 0 | — | — | — | — |
| player_round_glicko+regional | international=1 | 274 | 0.591693 | 0.203355 | 0.689781 | 0.061511 |
| player_round_glicko+regional | international=0 | 6675 | 0.561958 | 0.190949 | 0.703146 | 0.020429 |

player_round_glicko+regional − coin (paired log loss):

| Section | Rows | player_round_glicko+regional log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6949 | 0.563130 | 0.693147 | -0.130017 | [-0.139971, -0.119836] | yes |
| tier1 | 172 | 0.621574 | 0.693147 | -0.071574 | [-0.136344, -0.000522] | yes |
| tier2 | 486 | 0.535101 | 0.693147 | -0.158046 | [-0.195593, -0.117752] | yes |
| tier3 | 6291 | 0.563698 | 0.693147 | -0.129449 | [-0.139722, -0.118980] | yes |
| international=1 | 274 | 0.591693 | 0.693147 | -0.101454 | [-0.156783, -0.044088] | yes |
| international=0 | 6675 | 0.561958 | 0.693147 | -0.131189 | [-0.140763, -0.120429] | yes |

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
| player_round_glicko_rookie+regional | all | 6949 | 0.552075 | 0.185911 | 0.713772 | 0.017673 |
| player_round_glicko_rookie+regional | tier1 | 172 | 0.626904 | 0.213496 | 0.674419 | 0.053087 |
| player_round_glicko_rookie+regional | tier2 | 486 | 0.525805 | 0.177786 | 0.736626 | 0.036992 |
| player_round_glicko_rookie+regional | tier3 | 6291 | 0.552058 | 0.185785 | 0.713082 | 0.020098 |
| player_round_glicko_rookie+regional | unknown | 0 | — | — | — | — |
| player_round_glicko_rookie+regional | international=1 | 274 | 0.583514 | 0.198809 | 0.686131 | 0.067450 |
| player_round_glicko_rookie+regional | international=0 | 6675 | 0.550784 | 0.185382 | 0.714906 | 0.018379 |

player_round_glicko_rookie+regional − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie+regional log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6949 | 0.552075 | 0.693147 | -0.141072 | [-0.152690, -0.129703] | yes |
| tier1 | 172 | 0.626904 | 0.693147 | -0.066244 | [-0.134198, 0.012631] | no |
| tier2 | 486 | 0.525805 | 0.693147 | -0.167342 | [-0.205700, -0.126680] | yes |
| tier3 | 6291 | 0.552058 | 0.693147 | -0.141089 | [-0.152886, -0.129314] | yes |
| international=1 | 274 | 0.583514 | 0.693147 | -0.109633 | [-0.167706, -0.050542] | yes |
| international=0 | 6675 | 0.550784 | 0.693147 | -0.142363 | [-0.153351, -0.130543] | yes |

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

team_elo+regional − team_elo (paired log loss):

| Section | Rows | team_elo+regional log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6949 | 0.629966 | 0.630108 | -0.000141 | [-0.000643, 0.000323] | no |

team_elo+calibration − team_elo (paired log loss):

| Section | Rows | team_elo+calibration log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6949 | 0.628573 | 0.630108 | -0.001535 | [-0.002698, -0.000349] | yes |

player_round_glicko+none − team_elo (paired log loss):

| Section | Rows | player_round_glicko+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6949 | 0.563146 | 0.630108 | -0.066962 | [-0.075284, -0.058376] | yes |

player_round_glicko+regional − team_elo (paired log loss):

| Section | Rows | player_round_glicko+regional log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6949 | 0.563130 | 0.630108 | -0.066977 | [-0.075235, -0.058392] | yes |

player_round_glicko+calibration − team_elo (paired log loss):

| Section | Rows | player_round_glicko+calibration log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6949 | 0.562958 | 0.630108 | -0.067149 | [-0.075560, -0.058431] | yes |

player_round_glicko_rookie+none − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6949 | 0.552086 | 0.630108 | -0.078022 | [-0.087580, -0.068567] | yes |

player_round_glicko_rookie+regional − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie+regional log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6949 | 0.552075 | 0.630108 | -0.078033 | [-0.087523, -0.068519] | yes |

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

team_elo+regional − player_round_glicko_rookie (paired log loss):

| Section | Rows | team_elo+regional log loss | player_round_glicko_rookie log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6949 | 0.629966 | 0.552086 | 0.077880 | [0.068438, 0.087399] | yes |
| tier1 | 172 | 0.674015 | 0.626719 | 0.047297 | [-0.008545, 0.102197] | no |
| tier2 | 486 | 0.622382 | 0.525397 | 0.096986 | [0.055037, 0.137933] | yes |
| tier3 | 6291 | 0.629348 | 0.552107 | 0.077240 | [0.067407, 0.086662] | yes |
| international=1 | 274 | 0.630084 | 0.583029 | 0.047056 | [0.003637, 0.088708] | yes |
| international=0 | 6675 | 0.629962 | 0.550816 | 0.079146 | [0.068905, 0.088386] | yes |

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

player_round_glicko+regional − player_round_glicko_rookie (paired log loss):

| Section | Rows | player_round_glicko+regional log loss | player_round_glicko_rookie log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6949 | 0.563130 | 0.552086 | 0.011044 | [0.007575, 0.014651] | yes |
| tier1 | 172 | 0.621574 | 0.626719 | -0.005145 | [-0.021161, 0.007939] | no |
| tier2 | 486 | 0.535101 | 0.525397 | 0.009705 | [0.003727, 0.015646] | yes |
| tier3 | 6291 | 0.563698 | 0.552107 | 0.011590 | [0.007698, 0.015385] | yes |
| international=1 | 274 | 0.591693 | 0.583029 | 0.008664 | [-0.005003, 0.021077] | no |
| international=0 | 6675 | 0.561958 | 0.550816 | 0.011142 | [0.007505, 0.014777] | yes |

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

player_round_glicko_rookie+regional − player_round_glicko_rookie (paired log loss):

| Section | Rows | player_round_glicko_rookie+regional log loss | player_round_glicko_rookie log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6949 | 0.552075 | 0.552086 | -0.000011 | [-0.000283, 0.000260] | no |
| tier1 | 172 | 0.626904 | 0.626719 | 0.000185 | [-0.008644, 0.008852] | no |
| tier2 | 486 | 0.525805 | 0.525397 | 0.000408 | [-0.001563, 0.002209] | no |
| tier3 | 6291 | 0.552058 | 0.552107 | -0.000049 | [-0.000162, 0.000057] | no |
| international=1 | 274 | 0.583514 | 0.583029 | 0.000486 | [-0.005121, 0.005882] | no |
| international=0 | 6675 | 0.550784 | 0.550816 | -0.000032 | [-0.000205, 0.000123] | no |

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

### team_elo+regional: Kalshi comparison and returns

regional: rows=1894, ridge=4, s=0.661877, effects: NA=0.0705541, EU=0.111281, SA=0.0203275, APAC=-0.147067, CN=-0.0550959

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 244 | 0.677973 | 0.590569 | 0.087404 [0.031450, 0.145785] | yes |
| series | tier1 | 101 | 0.700488 | 0.622685 | 0.077804 [-0.005294, 0.163436] | no |
| series | tier2 | 143 | 0.662071 | 0.567886 | 0.094185 [0.020764, 0.179575] | yes |
| series | tier3 | 0 | — | — | — | — |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 101 | 0.700488 | 0.622685 | 0.077804 [-0.005294, 0.163436] | no |
| series | international=0 | 143 | 0.662071 | 0.567886 | 0.094185 [0.020764, 0.179575] | yes |
| map | all | 109 | 0.746805 | 0.699578 | 0.047226 [-0.002497, 0.103424] | no |
| map | tier1 | 102 | 0.705629 | 0.670407 | 0.035222 [-0.015247, 0.089065] | no |
| map | tier2 | 7 | 1.346790 | 1.124640 | 0.222150 [-0.012787, 0.531904] | no |
| map | tier3 | 0 | — | — | — | — |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 102 | 0.705629 | 0.670407 | 0.035222 [-0.015247, 0.089065] | no |
| map | international=0 | 7 | 1.346790 | 1.124640 | 0.222150 [-0.012787, 0.531904] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 190 | 190 | 0.1228 | -4.69% [-22.01%, 13.89%] | $8.49 | 0.170× | 91.38% | $6.35 | 112 (78 unfilled) | -8.66% [-27.62%, 10.70%] | $17.66 |
| series | tier1 | 81 | 81 | 0.1368 | 3.32% [-29.70%, 38.34%] | $31.28 | 0.626× | 64.29% | $6.35 | 45 (36 unfilled) | -4.28% [-40.38%, 32.50%] | $41.39 |
| series | tier2 | 109 | 109 | 0.1124 | -10.73% [-28.16%, 8.09%] | $13.83 | 0.277× | 87.82% | $7.39 | 67 (42 unfilled) | -11.64% [-32.30%, 9.44%] | $22.83 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 81 | 81 | 0.1368 | 3.32% [-29.70%, 38.34%] | $31.28 | 0.626× | 64.29% | $6.35 | 45 (36 unfilled) | -4.28% [-40.38%, 32.50%] | $41.39 |
| series | international=0 | 109 | 109 | 0.1124 | -10.73% [-28.16%, 8.09%] | $13.83 | 0.277× | 87.82% | $7.39 | 67 (42 unfilled) | -11.64% [-32.30%, 9.44%] | $22.83 |
| map | all | 82 | 43 | 0.0866 | 1.85% [-21.19%, 24.92%] | $38.48 | 0.770× | 54.66% | $8.22 | 7 (75 unfilled) | -40.58% [-100.00%, -6.14%] | $40.62 |
| map | tier1 | 77 | 39 | 0.0842 | 5.78% [-18.26%, 30.07%] | $52.45 | 1.049× | 38.19% | $6.10 | 4 (73 unfilled) | -46.96% [-100.00%, 6.84%] | $45.13 |
| map | tier2 | 5 | 4 | 0.1227 | -58.93% [-100.00%, -12.20%] | $36.69 | 0.734× | 26.62% | $4.91 | 3 (2 unfilled) | -32.02% [-100.00%, 2.29%] | $44.99 |
| map | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 77 | 39 | 0.0842 | 5.78% [-18.26%, 30.07%] | $52.45 | 1.049× | 38.19% | $6.10 | 4 (73 unfilled) | -46.96% [-100.00%, 6.84%] | $45.13 |
| map | international=0 | 5 | 4 | 0.1227 | -58.93% [-100.00%, -12.20%] | $36.69 | 0.734× | 26.62% | $4.91 | 3 (2 unfilled) | -32.02% [-100.00%, 2.29%] | $44.99 |
| series+map | all | 272 | 202 | 0.1119 | -2.72% [-17.85%, 12.49%] | $6.15 | 0.123× | 94.59% | $7.41 | 119 (153 unfilled) | -10.55% [-28.92%, 7.58%] | $11.65 |

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
| 2026-05 | series | 108 | 0.884797 | -0.038319 | fitted |
| 2026-05 | map | 69 | 1.000000 | 0.000000 | unfitted |
| 2026-06 | series | 144 | 0.806973 | -0.086760 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 136 | 0.592848 | 0.588044 | 0.004804 [-0.009912, 0.017624] | no |
| series | tier1 | 36 | 0.658498 | 0.664138 | -0.005641 [-0.018445, 0.006226] | no |
| series | tier2 | 100 | 0.569214 | 0.560650 | 0.008564 [-0.010517, 0.024607] | no |
| series | tier3 | 0 | — | — | — | — |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 36 | 0.658498 | 0.664138 | -0.005641 [-0.018445, 0.006226] | no |
| series | international=0 | 100 | 0.569214 | 0.560650 | 0.008564 [-0.010517, 0.024607] | no |
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
| series | all | 52 | 52 | 0.0161 | -26.53% [-63.41%, 16.49%] | $46.48 | 0.930× | 22.60% | $4.73 | 28 (24 unfilled) | -4.36% [-60.07%, 63.89%] | $58.21 |
| series | tier1 | 1 | 1 | 0.0064 | -100.00% [-100.00%, -100.00%] | $49.60 | 0.992× | 0.80% | $0.37 | 0 (1 unfilled) | — | $49.60 |
| series | tier2 | 51 | 51 | 0.0163 | -25.09% [-63.19%, 20.73%] | $46.87 | 0.937× | 22.58% | $4.77 | 28 (23 unfilled) | -4.36% [-60.07%, 63.89%] | $58.69 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 1 | 1 | 0.0064 | -100.00% [-100.00%, -100.00%] | $49.60 | 0.992× | 0.80% | $0.37 | 0 (1 unfilled) | — | $49.60 |
| series | international=0 | 51 | 51 | 0.0163 | -25.09% [-63.19%, 20.73%] | $46.87 | 0.937× | 22.58% | $4.77 | 28 (23 unfilled) | -4.36% [-60.07%, 63.89%] | $58.69 |
| map | all | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier2 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=0 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series+map | all | 52 | 52 | 0.0161 | -26.53% [-63.41%, 16.49%] | $46.48 | 0.930× | 22.60% | $4.73 | 28 (24 unfilled) | -4.36% [-60.07%, 63.89%] | $58.21 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-02 | 62 | 0.677843 | — | 0.656833 | 29.28% (46), $83.72 | — | 3 (43 unfilled) | -29.00% [-100.00%, 6.84%] | $48.88 | — | — | — |
| map | 2026-04 | 7 | 1.346790 | — | 1.124640 | -58.93% (5), $36.69 | — | 3 (2 unfilled) | -32.02% [-100.00%, 2.29%] | $44.99 | — | — | — |
| map | 2026-05 | 40 | 0.748698 | — | 0.691447 | -29.27% (31), $31.29 | — | 1 (30 unfilled) | -100.00% [-100.00%, -100.00%] | $46.17 | — | — | — |
| series | 2026-01 | 16 | 0.801933 | — | 0.612205 | -3.24% (15), $34.71 | — | 10 (5 unfilled) | 20.71% [-53.50%, 98.54%] | $55.03 | — | — | — |
| series | 2026-02 | 49 | 0.670014 | — | 0.595651 | 2.37% (42), $53.98 | — | 18 (24 unfilled) | -41.75% [-80.90%, 5.03%] | $35.44 | — | — | — |
| series | 2026-03 | 2 | 1.488339 | — | 1.445686 | -100.00% (1), $47.64 | — | 0 (1 unfilled) | — | $50.00 | — | — | — |
| series | 2026-04 | 41 | 0.682708 | — | 0.542714 | -3.22% (33), $33.63 | — | 20 (13 unfilled) | -17.46% [-58.95%, 28.49%] | $36.27 | — | — | — |
| series | 2026-05 | 36 | 0.696882 | 0.658498 | 0.664138 | 9.09% (24), $41.90 | -100.00% (1), $49.60 | 17 (7 unfilled) | 20.81% [-42.36%, 94.70%] | $51.32 | 0 (1 unfilled) | — | $49.60 |
| series | 2026-06 | 100 | 0.637085 | 0.569214 | 0.560650 | -12.89% (75), $21.67 | -25.09% (51), $46.87 | 47 (28 unfilled) | -9.14% [-32.99%, 14.33%] | $33.20 | 28 (23 unfilled) | -4.36% [-60.07%, 63.89%] | $58.69 |

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

### player_round_glicko+regional: Kalshi comparison and returns

regional: rows=1894, ridge=4, s=0.945901, effects: NA=0.0609718, EU=0.0306863, SA=0.127254, APAC=-0.164177, CN=-0.0547349

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 244 | 0.614708 | 0.590569 | 0.024139 [-0.012655, 0.059984] | no |
| series | tier1 | 101 | 0.627753 | 0.622685 | 0.005069 [-0.057508, 0.070240] | no |
| series | tier2 | 143 | 0.605494 | 0.567886 | 0.037608 [-0.003942, 0.080993] | no |
| series | tier3 | 0 | — | — | — | — |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 101 | 0.627753 | 0.622685 | 0.005069 [-0.057508, 0.070240] | no |
| series | international=0 | 143 | 0.605494 | 0.567886 | 0.037608 [-0.003942, 0.080993] | no |
| map | all | 109 | 0.694509 | 0.699578 | -0.005069 [-0.082302, 0.054564] | no |
| map | tier1 | 102 | 0.687283 | 0.670407 | 0.016875 [-0.023701, 0.061815] | no |
| map | tier2 | 7 | 0.799813 | 1.124640 | -0.324828 [-1.398870, 0.218825] | no |
| map | tier3 | 0 | — | — | — | — |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 102 | 0.687283 | 0.670407 | 0.016875 [-0.023701, 0.061815] | no |
| map | international=0 | 7 | 0.799813 | 1.124640 | -0.324828 [-1.398870, 0.218825] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 186 | 186 | 0.0910 | -4.75% [-21.81%, 13.69%] | $4.62 | 0.092× | 94.58% | $8.41 | 110 (76 unfilled) | -9.40% [-29.14%, 9.80%] | $17.99 |
| series | tier1 | 86 | 86 | 0.0994 | 0.93% [-25.94%, 28.37%] | $25.88 | 0.518× | 69.65% | $8.41 | 52 (34 unfilled) | -1.67% [-32.18%, 30.02%] | $36.89 |
| series | tier2 | 100 | 100 | 0.0838 | -9.64% [-33.38%, 17.17%] | $9.10 | 0.182× | 89.97% | $8.62 | 58 (42 unfilled) | -16.32% [-43.04%, 11.90%] | $25.25 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 86 | 86 | 0.0994 | 0.93% [-25.94%, 28.37%] | $25.88 | 0.518× | 69.65% | $8.41 | 52 (34 unfilled) | -1.67% [-32.18%, 30.02%] | $36.89 |
| series | international=0 | 100 | 100 | 0.0838 | -9.64% [-33.38%, 17.17%] | $9.10 | 0.182× | 89.97% | $8.62 | 58 (42 unfilled) | -16.32% [-43.04%, 11.90%] | $25.25 |
| map | all | 78 | 42 | 0.0859 | 17.42% [-18.75%, 64.57%] | $100.25 | 2.005× | 32.62% | $12.45 | 5 (73 unfilled) | -40.74% [-100.00%, -0.47%] | $45.96 |
| map | tier1 | 72 | 37 | 0.0772 | 1.28% [-24.37%, 27.60%] | $52.65 | 1.053× | 32.63% | $5.89 | 2 (70 unfilled) | -34.72% [-100.00%, 32.49%] | $47.86 |
| map | tier2 | 6 | 5 | 0.1903 | 210.34% [-72.41%, 710.15%] | $95.14 | 1.903× | 11.92% | $10.37 | 3 (3 unfilled) | -44.74% [-100.00%, -16.71%] | $47.81 |
| map | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 72 | 37 | 0.0772 | 1.28% [-24.37%, 27.60%] | $52.65 | 1.053× | 32.63% | $5.89 | 2 (70 unfilled) | -34.72% [-100.00%, 32.49%] | $47.86 |
| map | international=0 | 6 | 5 | 0.1903 | 210.34% [-72.41%, 710.15%] | $95.14 | 1.903× | 11.92% | $10.37 | 3 (3 unfilled) | -44.74% [-100.00%, -16.71%] | $47.81 |
| series+map | all | 264 | 187 | 0.0895 | 1.79% [-17.19%, 21.92%] | $7.95 | 0.159× | 89.16% | $6.90 | 115 (149 unfilled) | -10.76% [-30.70%, 9.27%] | $19.61 |

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
| 2026-05 | series | 108 | 1.139047 | 0.481863 | fitted |
| 2026-05 | map | 69 | 1.000000 | 0.000000 | unfitted |
| 2026-06 | series | 144 | 1.011191 | 0.412620 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 136 | 0.597208 | 0.588044 | 0.009164 [-0.006152, 0.024343] | no |
| series | tier1 | 36 | 0.665941 | 0.664138 | 0.001802 [-0.036440, 0.040973] | no |
| series | tier2 | 100 | 0.572464 | 0.560650 | 0.011814 [-0.003725, 0.026706] | no |
| series | tier3 | 0 | — | — | — | — |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 36 | 0.665941 | 0.664138 | 0.001802 [-0.036440, 0.040973] | no |
| series | international=0 | 100 | 0.572464 | 0.560650 | 0.011814 [-0.003725, 0.026706] | no |
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
| series | all | 50 | 50 | 0.0240 | -15.04% [-42.20%, 15.02%] | $31.17 | 0.623× | 51.33% | $6.05 | 30 (20 unfilled) | -3.09% [-36.78%, 33.32%] | $44.23 |
| series | tier1 | 18 | 18 | 0.0307 | -3.25% [-44.59%, 38.09%] | $42.23 | 0.845× | 31.78% | $6.05 | 15 (3 unfilled) | -12.80% [-51.52%, 22.99%] | $41.60 |
| series | tier2 | 32 | 32 | 0.0202 | -21.61% [-55.83%, 18.75%] | $36.96 | 0.739× | 38.42% | $5.49 | 15 (17 unfilled) | 6.54% [-52.85%, 68.78%] | $53.82 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 18 | 18 | 0.0307 | -3.25% [-44.59%, 38.09%] | $42.23 | 0.845× | 31.78% | $6.05 | 15 (3 unfilled) | -12.80% [-51.52%, 22.99%] | $41.60 |
| series | international=0 | 32 | 32 | 0.0202 | -21.61% [-55.83%, 18.75%] | $36.96 | 0.739× | 38.42% | $5.49 | 15 (17 unfilled) | 6.54% [-52.85%, 68.78%] | $53.82 |
| map | all | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier2 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=0 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series+map | all | 50 | 50 | 0.0240 | -15.04% [-42.20%, 15.02%] | $31.17 | 0.623× | 51.33% | $6.05 | 30 (20 unfilled) | -3.09% [-36.78%, 33.32%] | $44.23 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-02 | 62 | 0.667108 | — | 0.656833 | 7.58% (42), $59.99 | — | 1 (41 unfilled) | -100.00% [-100.00%, -100.00%] | $47.50 | — | — | — |
| map | 2026-04 | 7 | 0.799813 | — | 1.124640 | 210.34% (6), $95.14 | — | 3 (3 unfilled) | -44.74% [-100.00%, -16.71%] | $47.81 | — | — | — |
| map | 2026-05 | 40 | 0.718554 | — | 0.691447 | -7.63% (30), $43.84 | — | 1 (29 unfilled) | 32.49% [32.49%, 32.49%] | $50.36 | — | — | — |
| series | 2026-01 | 16 | 0.677490 | — | 0.612205 | 7.40% (11), $47.15 | — | 7 (4 unfilled) | 33.91% [-55.75%, 121.81%] | $64.64 | — | — | — |
| series | 2026-02 | 49 | 0.585421 | — | 0.595651 | -5.57% (43), $31.78 | — | 21 (22 unfilled) | -22.31% [-64.97%, 22.85%] | $40.32 | — | — | — |
| series | 2026-03 | 2 | 0.854873 | — | 1.445686 | 396.52% (1), $69.89 | — | 0 (1 unfilled) | — | $50.00 | — | — | — |
| series | 2026-04 | 41 | 0.600473 | — | 0.542714 | -9.76% (30), $33.29 | — | 20 (10 unfilled) | -9.45% [-52.93%, 36.65%] | $41.76 | — | — | — |
| series | 2026-05 | 36 | 0.663267 | 0.665941 | 0.664138 | 7.48% (32), $43.33 | -3.25% (18), $42.23 | 24 (8 unfilled) | 6.11% [-39.16%, 56.58%] | $34.36 | 15 (3 unfilled) | -12.80% [-51.52%, 22.99%] | $41.60 |
| series | 2026-06 | 100 | 0.602565 | 0.572464 | 0.560650 | -15.58% (69), $9.76 | -21.61% (32), $36.96 | 38 (31 unfilled) | -19.97% [-52.51%, 13.24%] | $31.50 | 15 (17 unfilled) | 6.54% [-52.85%, 68.78%] | $53.82 |

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

### player_round_glicko_rookie+regional: Kalshi comparison and returns

regional: rows=1894, ridge=4, s=0.899999, effects: NA=0.0301737, EU=0.03988, SA=0.145406, APAC=-0.163275, CN=-0.0521839

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 244 | 0.610773 | 0.590569 | 0.020204 [-0.015695, 0.054383] | no |
| series | tier1 | 101 | 0.628180 | 0.622685 | 0.005495 [-0.055028, 0.069592] | no |
| series | tier2 | 143 | 0.598479 | 0.567886 | 0.030593 [-0.008434, 0.071928] | no |
| series | tier3 | 0 | — | — | — | — |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 101 | 0.628180 | 0.622685 | 0.005495 [-0.055028, 0.069592] | no |
| series | international=0 | 143 | 0.598479 | 0.567886 | 0.030593 [-0.008434, 0.071928] | no |
| map | all | 109 | 0.690391 | 0.699578 | -0.009187 [-0.085669, 0.048916] | no |
| map | tier1 | 102 | 0.682066 | 0.670407 | 0.011658 [-0.028678, 0.054625] | no |
| map | tier2 | 7 | 0.811698 | 1.124640 | -0.312943 [-1.387120, 0.206737] | no |
| map | tier3 | 0 | — | — | — | — |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 102 | 0.682066 | 0.670407 | 0.011658 [-0.028678, 0.054625] | no |
| map | international=0 | 7 | 0.811698 | 1.124640 | -0.312943 [-1.387120, 0.206737] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 183 | 183 | 0.0867 | -1.89% [-21.29%, 19.13%] | $6.49 | 0.130× | 90.57% | $6.49 | 106 (77 unfilled) | -8.17% [-28.88%, 12.88%] | $20.05 |
| series | tier1 | 85 | 85 | 0.0949 | 8.14% [-22.22%, 43.62%] | $23.89 | 0.478× | 65.97% | $6.49 | 49 (36 unfilled) | -4.61% [-35.95%, 29.58%] | $33.06 |
| series | tier2 | 98 | 98 | 0.0795 | -10.63% [-33.53%, 14.22%] | $13.72 | 0.274× | 83.74% | $8.02 | 57 (41 unfilled) | -11.24% [-36.58%, 15.68%] | $33.48 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 85 | 85 | 0.0949 | 8.14% [-22.22%, 43.62%] | $23.89 | 0.478× | 65.97% | $6.49 | 49 (36 unfilled) | -4.61% [-35.95%, 29.58%] | $33.06 |
| series | international=0 | 98 | 98 | 0.0795 | -10.63% [-33.53%, 14.22%] | $13.72 | 0.274× | 83.74% | $8.02 | 57 (41 unfilled) | -11.24% [-36.58%, 15.68%] | $33.48 |
| map | all | 81 | 43 | 0.0786 | 17.09% [-18.40%, 61.89%] | $93.90 | 1.878× | 32.17% | $11.55 | 5 (76 unfilled) | -40.74% [-100.00%, -0.47%] | $45.94 |
| map | tier1 | 76 | 39 | 0.0700 | 4.58% [-21.99%, 30.68%] | $52.85 | 1.057× | 32.18% | $5.85 | 2 (74 unfilled) | -34.72% [-100.00%, 32.49%] | $47.86 |
| map | tier2 | 5 | 4 | 0.2091 | 206.70% [-100.00%, 906.04%] | $88.72 | 1.774× | 11.97% | $9.68 | 3 (2 unfilled) | -44.74% [-100.00%, -16.71%] | $47.78 |
| map | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 76 | 39 | 0.0700 | 4.58% [-21.99%, 30.68%] | $52.85 | 1.057× | 32.18% | $5.85 | 2 (74 unfilled) | -34.72% [-100.00%, 32.49%] | $47.86 |
| map | international=0 | 5 | 4 | 0.2091 | 206.70% [-100.00%, 906.04%] | $88.72 | 1.774× | 11.97% | $9.68 | 3 (2 unfilled) | -44.74% [-100.00%, -16.71%] | $47.78 |
| series+map | all | 264 | 185 | 0.0842 | 3.92% [-15.21%, 24.33%] | $9.76 | 0.195× | 84.45% | $5.94 | 111 (153 unfilled) | -9.63% [-29.17%, 10.09%] | $19.69 |

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
| 2026-05 | series | 108 | 1.125178 | 0.469148 | fitted |
| 2026-05 | map | 69 | 1.000000 | 0.000000 | unfitted |
| 2026-06 | series | 144 | 1.011525 | 0.420778 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 136 | 0.594949 | 0.588044 | 0.006905 [-0.007775, 0.021323] | no |
| series | tier1 | 36 | 0.662377 | 0.664138 | -0.001761 [-0.033827, 0.030630] | no |
| series | tier2 | 100 | 0.570674 | 0.560650 | 0.010024 [-0.005410, 0.024964] | no |
| series | tier3 | 0 | — | — | — | — |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 36 | 0.662377 | 0.664138 | -0.001761 [-0.033827, 0.030630] | no |
| series | international=0 | 100 | 0.570674 | 0.560650 | 0.010024 [-0.005410, 0.024964] | no |
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
| series | all | 49 | 49 | 0.0218 | -11.61% [-39.72%, 18.87%] | $36.95 | 0.739× | 43.87% | $6.18 | 29 (20 unfilled) | -9.17% [-44.36%, 29.17%] | $47.16 |
| series | tier1 | 17 | 17 | 0.0233 | -2.42% [-46.55%, 43.02%] | $46.91 | 0.938× | 25.88% | $6.18 | 13 (4 unfilled) | -21.20% [-59.83%, 20.46%] | $43.29 |
| series | tier2 | 32 | 32 | 0.0209 | -16.47% [-51.17%, 25.10%] | $39.43 | 0.789× | 32.53% | $5.39 | 16 (16 unfilled) | 0.54% [-54.31%, 61.63%] | $54.84 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 17 | 17 | 0.0233 | -2.42% [-46.55%, 43.02%] | $46.91 | 0.938× | 25.88% | $6.18 | 13 (4 unfilled) | -21.20% [-59.83%, 20.46%] | $43.29 |
| series | international=0 | 32 | 32 | 0.0209 | -16.47% [-51.17%, 25.10%] | $39.43 | 0.789× | 32.53% | $5.39 | 16 (16 unfilled) | 0.54% [-54.31%, 61.63%] | $54.84 |
| map | all | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier2 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=0 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series+map | all | 49 | 49 | 0.0218 | -11.61% [-39.72%, 18.87%] | $36.95 | 0.739× | 43.87% | $6.18 | 29 (20 unfilled) | -9.17% [-44.36%, 29.17%] | $47.16 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-02 | 62 | 0.662991 | — | 0.656833 | 12.47% (46), $59.65 | — | 1 (45 unfilled) | -100.00% [-100.00%, -100.00%] | $47.50 | — | — | — |
| map | 2026-04 | 7 | 0.811698 | — | 1.124640 | 206.70% (5), $88.72 | — | 3 (2 unfilled) | -44.74% [-100.00%, -16.71%] | $47.78 | — | — | — |
| map | 2026-05 | 40 | 0.711632 | — | 0.691447 | -7.63% (30), $44.27 | — | 1 (29 unfilled) | 32.49% [32.49%, 32.49%] | $50.36 | — | — | — |
| series | 2026-01 | 16 | 0.697428 | — | 0.612205 | -1.40% (12), $40.22 | — | 8 (4 unfilled) | 17.34% [-72.08%, 98.34%] | $56.76 | — | — | — |
| series | 2026-02 | 49 | 0.585256 | — | 0.595651 | 11.09% (44), $32.51 | — | 20 (24 unfilled) | -24.42% [-69.44%, 26.61%] | $40.44 | — | — | — |
| series | 2026-03 | 2 | 0.947654 | — | 1.445686 | 396.52% (1), $69.89 | — | 0 (1 unfilled) | — | $50.00 | — | — | — |
| series | 2026-04 | 41 | 0.585229 | — | 0.542714 | -5.70% (29), $34.74 | — | 19 (10 unfilled) | -3.24% [-50.21%, 46.11%] | $44.63 | — | — | — |
| series | 2026-05 | 36 | 0.655827 | 0.662377 | 0.664138 | 7.61% (29), $45.85 | -2.42% (17), $46.91 | 21 (8 unfilled) | 6.09% [-42.75%, 62.70%] | $35.56 | 13 (4 unfilled) | -21.20% [-59.83%, 20.46%] | $43.29 |
| series | 2026-06 | 100 | 0.596928 | 0.570674 | 0.560650 | -18.86% (68), $14.12 | -16.47% (32), $39.43 | 38 (30 unfilled) | -15.29% [-47.12%, 17.88%] | $38.49 | 16 (16 unfilled) | 0.54% [-54.31%, 61.63%] | $54.84 |

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

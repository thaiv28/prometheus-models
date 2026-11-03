# R6 Elo backtest

## Combined summary (validation, all sections)

| Model | Series Δ log loss | Series flat ROI | Series Kelly (LoL caps) $ | Series flat ROI depth-capped | Series Kelly depth-capped $ | Map Δ log loss | Map flat ROI | Map Kelly (LoL caps) $ | Map flat ROI depth-capped | Map Kelly depth-capped $ | Series blended Δ log loss | Series blended flat ROI | Series blended Kelly (LoL caps) $ | Series blended flat ROI depth-capped | Series blended Kelly depth-capped $ | Map blended Δ log loss | Map blended flat ROI | Map blended Kelly (LoL caps) $ | Map blended flat ROI depth-capped | Map blended Kelly depth-capped $ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| team_elo | — | — | $50.00 | — | $50.00 | — | — | $50.00 | — | $50.00 | — | — | $50.00 | — | $50.00 | — | — | $50.00 | — | $50.00 |
| player_glicko | — | — | $50.00 | — | $50.00 | — | — | $50.00 | — | $50.00 | — | — | $50.00 | — | $50.00 | — | — | $50.00 | — | $50.00 |
| player_round_glicko | — | — | $50.00 | — | $50.00 | — | — | $50.00 | — | $50.00 | — | — | $50.00 | — | $50.00 | — | — | $50.00 | — | $50.00 |
| team_elo+none | — | — | $50.00 | — | $50.00 | — | — | $50.00 | — | $50.00 | — | — | $50.00 | — | $50.00 | — | — | $50.00 | — | $50.00 |
| player_glicko+none | — | — | $50.00 | — | $50.00 | — | — | $50.00 | — | $50.00 | — | — | $50.00 | — | $50.00 | — | — | $50.00 | — | $50.00 |
| player_round_glicko+none | — | — | $50.00 | — | $50.00 | — | — | $50.00 | — | $50.00 | — | — | $50.00 | — | $50.00 | — | — | $50.00 | — | $50.00 |

Series temperatures (stage 1; p′ = σ(T·logit p), T < 1 pulls odds toward 50%): team_elo Bo3 0.63, Bo5 0.40; player_round_glicko Bo3 0.77, Bo5 0.64; player_glicko Bo3 0.75, Bo5 0.51; team_elo+none Bo3 0.63, Bo5 0.40; player_glicko+none Bo3 0.75, Bo5 0.51; player_round_glicko+none Bo3 0.77, Bo5 0.64

Parameters minimize tuning map log loss across all sections. Replay predicts before update; Replay starts at the first map. Tuning: [2023-01-01, 2026-01-01); validation: [2026-07-01, 2026-07-01). Holdout is scored only with --holdout and never selects parameters. Series use the first map prediction and independent maps in Bo1/Bo3/Bo5; Bo2, unknown/unsupported lengths and unknown results are skipped. Accuracy gives 0.5 predictions half credit; ECE uses 10 equal-width bins. Log loss clips probabilities at 1e-6. Paired bootstrap uses 2,000 resamples, seed 0, clustered by match_id. Differences are the named model minus its comparator; negative favors the model. Significance requires a 95% percentile interval excluding zero. Tuning scores are selection diagnostics, not independent evidence of improvement.

Fit through 2025-12-31. Unknown host-region map rows: 6007 (including missing/un).

## Stage 1 — tuning (outcomes)

### Leaderboard

| Model | Best params | Map log loss | Series log loss | Rows |
|---|---|---:|---:|---:|
| player_round_glicko | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 280, "tau": 0.75} | 0.589676 | 0.575553 | 50153 |
| player_glicko | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 350} | 0.598164 | 0.584678 | 50153 |
| team_elo | {"k": 64} | 0.635894 | 0.630922 | 50153 |

Kalshi uses the first hourly bid/ask (midpoint for log loss, ask/bid for bets) ending ≥30 min after the market opened and ≥2 h before the scheduled start, with a spread ≤ 0.06: a price a bot could trade before the series. Markets without such a quote are skipped. oriented to team1 using aliases. One contract per event, preferring team1. Compare identical rows; map predictions use the first map's pre-match chance. Missing links, aliases or candles are skipped; unplayed maps are not in the rows. Returns use frozen stage-1 parameters. Each bet buys $1 of contracts, fees extra; order fees ceil to a cent (0.07 × contracts × price × (1−price)). Edge selection uses unrounded per-contract fees. ROI divides profit by stake plus fees; intervals resample matches 2,000 times. Unlimited depth and depth-capped returns are shown together. Depth uses 0.5 of acceptable-price tape volume in the 6 hours after the quote, missing tapes give zero fills. Partial Kelly fills are allowed; flat bets require the full $1 stake. Kelly uses LoL caps and rounded-fee affordability, from a $50 seed. Each slice runs independently. Tape volume is a fill proxy; no slippage is modeled.

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
| player_glicko | all | 50153 | 0.598164 | 0.206616 | 0.669621 | 0.021073 |
| player_glicko | tier1 | 1659 | 0.657249 | 0.232297 | 0.598553 | 0.036024 |
| player_glicko | tier2 | 4707 | 0.599005 | 0.207014 | 0.667304 | 0.027983 |
| player_glicko | tier3 | 43764 | 0.595953 | 0.205650 | 0.672459 | 0.021637 |
| player_glicko | unknown | 23 | 0.370500 | 0.110833 | 0.869565 | 0.131220 |
| player_glicko | international=1 | 1755 | 0.654650 | 0.230796 | 0.605983 | 0.031746 |
| player_glicko | international=0 | 48398 | 0.596115 | 0.205739 | 0.671929 | 0.022303 |

player_glicko − coin (paired log loss):

| Section | Rows | player_glicko log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 50153 | 0.598164 | 0.693147 | -0.094983 | [-0.098605, -0.091370] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko | all | 50153 | 0.589676 | 0.203043 | 0.677527 | 0.020655 |
| player_round_glicko | tier1 | 1659 | 0.658246 | 0.233369 | 0.589210 | 0.039147 |
| player_round_glicko | tier2 | 4707 | 0.592897 | 0.204682 | 0.670491 | 0.028236 |
| player_round_glicko | tier3 | 43764 | 0.586854 | 0.201768 | 0.681553 | 0.020879 |
| player_round_glicko | unknown | 23 | 0.353969 | 0.107215 | 0.826087 | 0.158715 |
| player_round_glicko | international=1 | 1755 | 0.654289 | 0.230742 | 0.597151 | 0.037968 |
| player_round_glicko | international=0 | 48398 | 0.587333 | 0.202039 | 0.680441 | 0.021609 |

player_round_glicko − coin (paired log loss):

| Section | Rows | player_round_glicko log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 50153 | 0.589676 | 0.693147 | -0.103471 | [-0.107049, -0.099893] | yes |

player_round_glicko − team_elo (paired log loss):

| Section | Rows | player_round_glicko log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 50153 | 0.589676 | 0.635894 | -0.046218 | [-0.049145, -0.043310] | yes |

player_glicko − team_elo (paired log loss):

| Section | Rows | player_glicko log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 50153 | 0.598164 | 0.635894 | -0.037730 | [-0.040262, -0.035083] | yes |

player_glicko − player_round_glicko (paired log loss):

| Section | Rows | player_glicko log loss | player_round_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 50153 | 0.598164 | 0.589676 | 0.008488 | [0.006957, 0.010187] | yes |
| tier1 | 1659 | 0.657249 | 0.658246 | -0.000997 | [-0.009493, 0.007223] | no |
| tier2 | 4707 | 0.599005 | 0.592897 | 0.006108 | [0.001172, 0.011016] | yes |
| tier3 | 43764 | 0.595953 | 0.586854 | 0.009099 | [0.007360, 0.010757] | yes |
| unknown | 23 | 0.370500 | 0.353969 | 0.016532 | [-0.031657, 0.053531] | no |
| international=1 | 1755 | 0.654650 | 0.654289 | 0.000362 | [-0.008578, 0.009408] | no |
| international=0 | 48398 | 0.596115 | 0.587333 | 0.008782 | [0.007116, 0.010358] | yes |

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
| player_glicko | all | 35144 | 0.584678 | 0.200928 | 0.681581 | 0.024716 |
| player_glicko | tier1 | 818 | 0.650327 | 0.227571 | 0.625917 | 0.054004 |
| player_glicko | tier2 | 3188 | 0.578338 | 0.198325 | 0.685069 | 0.039566 |
| player_glicko | tier3 | 31128 | 0.583666 | 0.200522 | 0.682617 | 0.025303 |
| player_glicko | unknown | 10 | 0.388037 | 0.115781 | 0.900000 | 0.168969 |
| player_glicko | international=1 | 885 | 0.647275 | 0.225720 | 0.634463 | 0.049238 |
| player_glicko | international=0 | 34259 | 0.583061 | 0.200288 | 0.682799 | 0.025965 |

player_glicko − coin (paired log loss):

| Section | Rows | player_glicko log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 35144 | 0.584678 | 0.693147 | -0.108469 | [-0.112989, -0.104286] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko | all | 35144 | 0.575553 | 0.196985 | 0.689947 | 0.024388 |
| player_round_glicko | tier1 | 818 | 0.650729 | 0.228305 | 0.605134 | 0.046285 |
| player_round_glicko | tier2 | 3188 | 0.572485 | 0.196112 | 0.687578 | 0.033489 |
| player_round_glicko | tier3 | 31128 | 0.573951 | 0.196275 | 0.692383 | 0.024437 |
| player_round_glicko | unknown | 10 | 0.391680 | 0.122269 | 0.800000 | 0.174607 |
| player_round_glicko | international=1 | 885 | 0.644834 | 0.224761 | 0.616384 | 0.041302 |
| player_round_glicko | international=0 | 34259 | 0.573763 | 0.196268 | 0.691847 | 0.025264 |

player_round_glicko − coin (paired log loss):

| Section | Rows | player_round_glicko log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 35144 | 0.575553 | 0.693147 | -0.117594 | [-0.122096, -0.113241] | yes |

player_round_glicko − team_elo (paired log loss):

| Section | Rows | player_round_glicko log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 35144 | 0.575553 | 0.630922 | -0.055369 | [-0.058872, -0.051983] | yes |

player_glicko − team_elo (paired log loss):

| Section | Rows | player_glicko log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 35144 | 0.584678 | 0.630922 | -0.046243 | [-0.049449, -0.043069] | yes |

player_glicko − player_round_glicko (paired log loss):

| Section | Rows | player_glicko log loss | player_round_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 35144 | 0.584678 | 0.575553 | 0.009126 | [0.007065, 0.011053] | yes |
| tier1 | 818 | 0.650327 | 0.650729 | -0.000402 | [-0.013741, 0.012141] | no |
| tier2 | 3188 | 0.578338 | 0.572485 | 0.005854 | [-0.000165, 0.012417] | no |
| tier3 | 31128 | 0.583666 | 0.573951 | 0.009715 | [0.007629, 0.011774] | yes |
| unknown | 10 | 0.388037 | 0.391680 | -0.003642 | [-0.090966, 0.069691] | no |
| international=1 | 885 | 0.647275 | 0.644834 | 0.002441 | [-0.010364, 0.015899] | no |
| international=0 | 34259 | 0.583061 | 0.573763 | 0.009298 | [0.007351, 0.011245] | yes |

## Stage 2 — validation (outcomes)

### Leaderboard (frozen stage-1 parameters)

| Model | Best params | Map log loss | Series log loss | Rows |
|---|---|---:|---:|---:|
| team_elo | {"k": 64} | nan | nan | 0 |
| player_glicko | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 350} | nan | nan | 0 |
| player_round_glicko | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 280, "tau": 0.75} | nan | nan | 0 |
| team_elo+none | {"k": 64} | nan | nan | 0 |
| player_glicko+none | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 350} | nan | nan | 0 |
| player_round_glicko+none | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 280, "tau": 0.75} | nan | nan | 0 |

### Maps

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| coin | all | 0 | — | — | — | — |
| coin | tier1 | 0 | — | — | — | — |
| coin | tier2 | 0 | — | — | — | — |
| coin | tier3 | 0 | — | — | — | — |
| coin | unknown | 0 | — | — | — | — |
| coin | international=1 | 0 | — | — | — | — |
| coin | international=0 | 0 | — | — | — | — |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| team_elo | all | 0 | — | — | — | — |
| team_elo | tier1 | 0 | — | — | — | — |
| team_elo | tier2 | 0 | — | — | — | — |
| team_elo | tier3 | 0 | — | — | — | — |
| team_elo | unknown | 0 | — | — | — | — |
| team_elo | international=1 | 0 | — | — | — | — |
| team_elo | international=0 | 0 | — | — | — | — |

team_elo − coin (paired log loss):

| Section | Rows | team_elo log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko | all | 0 | — | — | — | — |
| player_glicko | tier1 | 0 | — | — | — | — |
| player_glicko | tier2 | 0 | — | — | — | — |
| player_glicko | tier3 | 0 | — | — | — | — |
| player_glicko | unknown | 0 | — | — | — | — |
| player_glicko | international=1 | 0 | — | — | — | — |
| player_glicko | international=0 | 0 | — | — | — | — |

player_glicko − coin (paired log loss):

| Section | Rows | player_glicko log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko | all | 0 | — | — | — | — |
| player_round_glicko | tier1 | 0 | — | — | — | — |
| player_round_glicko | tier2 | 0 | — | — | — | — |
| player_round_glicko | tier3 | 0 | — | — | — | — |
| player_round_glicko | unknown | 0 | — | — | — | — |
| player_round_glicko | international=1 | 0 | — | — | — | — |
| player_round_glicko | international=0 | 0 | — | — | — | — |

player_round_glicko − coin (paired log loss):

| Section | Rows | player_round_glicko log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| team_elo+none | all | 0 | — | — | — | — |
| team_elo+none | tier1 | 0 | — | — | — | — |
| team_elo+none | tier2 | 0 | — | — | — | — |
| team_elo+none | tier3 | 0 | — | — | — | — |
| team_elo+none | unknown | 0 | — | — | — | — |
| team_elo+none | international=1 | 0 | — | — | — | — |
| team_elo+none | international=0 | 0 | — | — | — | — |

team_elo+none − coin (paired log loss):

| Section | Rows | team_elo+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko+none | all | 0 | — | — | — | — |
| player_glicko+none | tier1 | 0 | — | — | — | — |
| player_glicko+none | tier2 | 0 | — | — | — | — |
| player_glicko+none | tier3 | 0 | — | — | — | — |
| player_glicko+none | unknown | 0 | — | — | — | — |
| player_glicko+none | international=1 | 0 | — | — | — | — |
| player_glicko+none | international=0 | 0 | — | — | — | — |

player_glicko+none − coin (paired log loss):

| Section | Rows | player_glicko+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko+none | all | 0 | — | — | — | — |
| player_round_glicko+none | tier1 | 0 | — | — | — | — |
| player_round_glicko+none | tier2 | 0 | — | — | — | — |
| player_round_glicko+none | tier3 | 0 | — | — | — | — |
| player_round_glicko+none | unknown | 0 | — | — | — | — |
| player_round_glicko+none | international=1 | 0 | — | — | — | — |
| player_round_glicko+none | international=0 | 0 | — | — | — | — |

player_round_glicko+none − coin (paired log loss):

| Section | Rows | player_round_glicko+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|

player_glicko − team_elo (paired log loss):

| Section | Rows | player_glicko log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|

player_round_glicko − team_elo (paired log loss):

| Section | Rows | player_round_glicko log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|

team_elo+none − team_elo (paired log loss):

| Section | Rows | team_elo+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|

player_glicko+none − team_elo (paired log loss):

| Section | Rows | player_glicko+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|

player_round_glicko+none − team_elo (paired log loss):

| Section | Rows | player_round_glicko+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|

player_glicko − player_round_glicko (paired log loss):

| Section | Rows | player_glicko log loss | player_round_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|

team_elo+none − player_round_glicko (paired log loss):

| Section | Rows | team_elo+none log loss | player_round_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|

player_glicko+none − player_round_glicko (paired log loss):

| Section | Rows | player_glicko+none log loss | player_round_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|

player_round_glicko+none − player_round_glicko (paired log loss):

| Section | Rows | player_round_glicko+none log loss | player_round_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|

### Series

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| coin | all | 0 | — | — | — | — |
| coin | tier1 | 0 | — | — | — | — |
| coin | tier2 | 0 | — | — | — | — |
| coin | tier3 | 0 | — | — | — | — |
| coin | unknown | 0 | — | — | — | — |
| coin | international=1 | 0 | — | — | — | — |
| coin | international=0 | 0 | — | — | — | — |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| team_elo | all | 0 | — | — | — | — |
| team_elo | tier1 | 0 | — | — | — | — |
| team_elo | tier2 | 0 | — | — | — | — |
| team_elo | tier3 | 0 | — | — | — | — |
| team_elo | unknown | 0 | — | — | — | — |
| team_elo | international=1 | 0 | — | — | — | — |
| team_elo | international=0 | 0 | — | — | — | — |

team_elo − coin (paired log loss):

| Section | Rows | team_elo log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko | all | 0 | — | — | — | — |
| player_glicko | tier1 | 0 | — | — | — | — |
| player_glicko | tier2 | 0 | — | — | — | — |
| player_glicko | tier3 | 0 | — | — | — | — |
| player_glicko | unknown | 0 | — | — | — | — |
| player_glicko | international=1 | 0 | — | — | — | — |
| player_glicko | international=0 | 0 | — | — | — | — |

player_glicko − coin (paired log loss):

| Section | Rows | player_glicko log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko | all | 0 | — | — | — | — |
| player_round_glicko | tier1 | 0 | — | — | — | — |
| player_round_glicko | tier2 | 0 | — | — | — | — |
| player_round_glicko | tier3 | 0 | — | — | — | — |
| player_round_glicko | unknown | 0 | — | — | — | — |
| player_round_glicko | international=1 | 0 | — | — | — | — |
| player_round_glicko | international=0 | 0 | — | — | — | — |

player_round_glicko − coin (paired log loss):

| Section | Rows | player_round_glicko log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| team_elo+none | all | 0 | — | — | — | — |
| team_elo+none | tier1 | 0 | — | — | — | — |
| team_elo+none | tier2 | 0 | — | — | — | — |
| team_elo+none | tier3 | 0 | — | — | — | — |
| team_elo+none | unknown | 0 | — | — | — | — |
| team_elo+none | international=1 | 0 | — | — | — | — |
| team_elo+none | international=0 | 0 | — | — | — | — |

team_elo+none − coin (paired log loss):

| Section | Rows | team_elo+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_glicko+none | all | 0 | — | — | — | — |
| player_glicko+none | tier1 | 0 | — | — | — | — |
| player_glicko+none | tier2 | 0 | — | — | — | — |
| player_glicko+none | tier3 | 0 | — | — | — | — |
| player_glicko+none | unknown | 0 | — | — | — | — |
| player_glicko+none | international=1 | 0 | — | — | — | — |
| player_glicko+none | international=0 | 0 | — | — | — | — |

player_glicko+none − coin (paired log loss):

| Section | Rows | player_glicko+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko+none | all | 0 | — | — | — | — |
| player_round_glicko+none | tier1 | 0 | — | — | — | — |
| player_round_glicko+none | tier2 | 0 | — | — | — | — |
| player_round_glicko+none | tier3 | 0 | — | — | — | — |
| player_round_glicko+none | unknown | 0 | — | — | — | — |
| player_round_glicko+none | international=1 | 0 | — | — | — | — |
| player_round_glicko+none | international=0 | 0 | — | — | — | — |

player_round_glicko+none − coin (paired log loss):

| Section | Rows | player_round_glicko+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|

player_glicko − team_elo (paired log loss):

| Section | Rows | player_glicko log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|

player_round_glicko − team_elo (paired log loss):

| Section | Rows | player_round_glicko log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|

team_elo+none − team_elo (paired log loss):

| Section | Rows | team_elo+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|

player_glicko+none − team_elo (paired log loss):

| Section | Rows | player_glicko+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|

player_round_glicko+none − team_elo (paired log loss):

| Section | Rows | player_round_glicko+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|

player_glicko − player_round_glicko (paired log loss):

| Section | Rows | player_glicko log loss | player_round_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|

team_elo+none − player_round_glicko (paired log loss):

| Section | Rows | team_elo+none log loss | player_round_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|

player_glicko+none − player_round_glicko (paired log loss):

| Section | Rows | player_glicko+none log loss | player_round_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|

player_round_glicko+none − player_round_glicko (paired log loss):

| Section | Rows | player_round_glicko+none log loss | player_round_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|

## Stage 2 — validation vs Kalshi

### team_elo: Kalshi comparison and returns



no linked markets (rows: 0)

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 0 | — | — | — | — |
| series | tier1 | 0 | — | — | — | — |
| series | tier2 | 0 | — | — | — | — |
| series | tier3 | 0 | — | — | — | — |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 0 | — | — | — | — |
| series | international=0 | 0 | — | — | — | — |
| map | all | 0 | — | — | — | — |
| map | tier1 | 0 | — | — | — | — |
| map | tier2 | 0 | — | — | — | — |
| map | tier3 | 0 | — | — | — | — |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 0 | — | — | — | — |
| map | international=0 | 0 | — | — | — | — |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier2 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=0 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | all | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier2 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=0 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 0 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 0 | — | — | — | — |
| series | tier1 | 0 | — | — | — | — |
| series | tier2 | 0 | — | — | — | — |
| series | tier3 | 0 | — | — | — | — |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 0 | — | — | — | — |
| series | international=0 | 0 | — | — | — | — |
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
| series | all | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier2 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=0 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | all | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier2 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=0 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|

### player_glicko: Kalshi comparison and returns



no linked markets (rows: 0)

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 0 | — | — | — | — |
| series | tier1 | 0 | — | — | — | — |
| series | tier2 | 0 | — | — | — | — |
| series | tier3 | 0 | — | — | — | — |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 0 | — | — | — | — |
| series | international=0 | 0 | — | — | — | — |
| map | all | 0 | — | — | — | — |
| map | tier1 | 0 | — | — | — | — |
| map | tier2 | 0 | — | — | — | — |
| map | tier3 | 0 | — | — | — | — |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 0 | — | — | — | — |
| map | international=0 | 0 | — | — | — | — |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier2 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=0 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | all | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier2 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=0 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 0 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 0 | — | — | — | — |
| series | tier1 | 0 | — | — | — | — |
| series | tier2 | 0 | — | — | — | — |
| series | tier3 | 0 | — | — | — | — |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 0 | — | — | — | — |
| series | international=0 | 0 | — | — | — | — |
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
| series | all | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier2 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=0 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | all | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier2 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=0 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|

### player_round_glicko: Kalshi comparison and returns



no linked markets (rows: 0)

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 0 | — | — | — | — |
| series | tier1 | 0 | — | — | — | — |
| series | tier2 | 0 | — | — | — | — |
| series | tier3 | 0 | — | — | — | — |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 0 | — | — | — | — |
| series | international=0 | 0 | — | — | — | — |
| map | all | 0 | — | — | — | — |
| map | tier1 | 0 | — | — | — | — |
| map | tier2 | 0 | — | — | — | — |
| map | tier3 | 0 | — | — | — | — |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 0 | — | — | — | — |
| map | international=0 | 0 | — | — | — | — |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier2 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=0 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | all | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier2 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=0 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 0 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 0 | — | — | — | — |
| series | tier1 | 0 | — | — | — | — |
| series | tier2 | 0 | — | — | — | — |
| series | tier3 | 0 | — | — | — | — |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 0 | — | — | — | — |
| series | international=0 | 0 | — | — | — | — |
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
| series | all | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier2 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=0 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | all | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier2 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=0 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|

### team_elo+none: Kalshi comparison and returns

none

no linked markets (rows: 0)

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 0 | — | — | — | — |
| series | tier1 | 0 | — | — | — | — |
| series | tier2 | 0 | — | — | — | — |
| series | tier3 | 0 | — | — | — | — |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 0 | — | — | — | — |
| series | international=0 | 0 | — | — | — | — |
| map | all | 0 | — | — | — | — |
| map | tier1 | 0 | — | — | — | — |
| map | tier2 | 0 | — | — | — | — |
| map | tier3 | 0 | — | — | — | — |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 0 | — | — | — | — |
| map | international=0 | 0 | — | — | — | — |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier2 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=0 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | all | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier2 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=0 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 0 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 0 | — | — | — | — |
| series | tier1 | 0 | — | — | — | — |
| series | tier2 | 0 | — | — | — | — |
| series | tier3 | 0 | — | — | — | — |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 0 | — | — | — | — |
| series | international=0 | 0 | — | — | — | — |
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
| series | all | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier2 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=0 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | all | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier2 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=0 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|

### player_glicko+none: Kalshi comparison and returns

none

no linked markets (rows: 0)

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 0 | — | — | — | — |
| series | tier1 | 0 | — | — | — | — |
| series | tier2 | 0 | — | — | — | — |
| series | tier3 | 0 | — | — | — | — |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 0 | — | — | — | — |
| series | international=0 | 0 | — | — | — | — |
| map | all | 0 | — | — | — | — |
| map | tier1 | 0 | — | — | — | — |
| map | tier2 | 0 | — | — | — | — |
| map | tier3 | 0 | — | — | — | — |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 0 | — | — | — | — |
| map | international=0 | 0 | — | — | — | — |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier2 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=0 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | all | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier2 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=0 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 0 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 0 | — | — | — | — |
| series | tier1 | 0 | — | — | — | — |
| series | tier2 | 0 | — | — | — | — |
| series | tier3 | 0 | — | — | — | — |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 0 | — | — | — | — |
| series | international=0 | 0 | — | — | — | — |
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
| series | all | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier2 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=0 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | all | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier2 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=0 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|

### player_round_glicko+none: Kalshi comparison and returns

none

no linked markets (rows: 0)

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 0 | — | — | — | — |
| series | tier1 | 0 | — | — | — | — |
| series | tier2 | 0 | — | — | — | — |
| series | tier3 | 0 | — | — | — | — |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 0 | — | — | — | — |
| series | international=0 | 0 | — | — | — | — |
| map | all | 0 | — | — | — | — |
| map | tier1 | 0 | — | — | — | — |
| map | tier2 | 0 | — | — | — | — |
| map | tier3 | 0 | — | — | — | — |
| map | unknown | 0 | — | — | — | — |
| map | international=1 | 0 | — | — | — | — |
| map | international=0 | 0 | — | — | — | — |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier2 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=0 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | all | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier2 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=0 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-11-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 0 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 0 | — | — | — | — |
| series | tier1 | 0 | — | — | — | — |
| series | tier2 | 0 | — | — | — | — |
| series | tier3 | 0 | — | — | — | — |
| series | unknown | 0 | — | — | — | — |
| series | international=1 | 0 | — | — | — | — |
| series | international=0 | 0 | — | — | — | — |
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
| series | all | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier2 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | international=0 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | all | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier2 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | tier3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | unknown | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=1 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | international=0 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|

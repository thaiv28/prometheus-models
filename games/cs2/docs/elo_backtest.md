# Elo variants benchmark

## Combined summary (validation, all sections)

| Model | Series Δ log loss | Series flat ROI | Series Kelly (LoL caps) $ | Series flat ROI depth-capped | Series Kelly depth-capped $ | Map Δ log loss | Map flat ROI | Map Kelly (LoL caps) $ | Map flat ROI depth-capped | Map Kelly depth-capped $ | Series blended Δ log loss | Series blended flat ROI | Series blended Kelly (LoL caps) $ | Series blended flat ROI depth-capped | Series blended Kelly depth-capped $ | Map blended Δ log loss | Map blended flat ROI | Map blended Kelly (LoL caps) $ | Map blended flat ROI depth-capped | Map blended Kelly depth-capped $ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| team_elo | 0.020181 | -6.01% | $0.09 | -5.04% | $0.07 | 0.023144 | -6.49% | $0.09 | -13.47% | $0.09 | -0.001482 | 2.74% | $19.26 | 5.21% | $101.79 | 0.001097 | -2.31% | $27.38 | -5.97% | $28.26 |
| player_round_glicko | -0.000053 | 2.00% | $0.03 | 0.02% | $0.09 | 0.006237 | -5.59% | $0.09 | -13.93% | $0.09 | -0.011511 | 7.71% | $9760.38 | 5.18% | $709.30 | -0.002393 | 1.90% | $283.51 | -6.48% | $16.17 |
| player_round_glicko_rookie_weights | -0.005361 | 2.73% | $0.09 | -0.02% | $0.08 | 0.004293 | -4.83% | $0.09 | -17.08% | $0.09 | -0.014581 | 8.41% | $13532.46 | 5.32% | $769.27 | -0.003210 | 4.36% | $667.99 | -6.80% | $13.69 |
| team_elo+none | 0.020181 | -6.01% | $0.09 | -5.04% | $0.07 | 0.023144 | -6.49% | $0.09 | -13.47% | $0.09 | -0.001482 | 2.74% | $19.26 | 5.21% | $101.79 | 0.001097 | -2.31% | $27.38 | -5.97% | $28.26 |
| player_round_glicko+none | -0.000053 | 2.00% | $0.03 | 0.02% | $0.09 | 0.006237 | -5.59% | $0.09 | -13.93% | $0.09 | -0.011511 | 7.71% | $9760.38 | 5.18% | $709.30 | -0.002393 | 1.90% | $283.51 | -6.48% | $16.17 |
| player_round_glicko_rookie_weights+none | -0.005361 | 2.73% | $0.09 | -0.02% | $0.08 | 0.004293 | -4.83% | $0.09 | -17.08% | $0.09 | -0.014581 | 8.41% | $13532.46 | 5.32% | $769.27 | -0.003210 | 4.36% | $667.99 | -6.80% | $13.69 |

Series temperatures (stage 1; p′ = σ(T·logit p), T < 1 pulls odds toward 50%): team_elo Bo3 0.71, Bo5 0.63; player_round_glicko_rookie_weights Bo3 0.88, Bo5 0.66; player_round_glicko Bo3 0.83, Bo5 0.59; team_elo+none Bo3 0.71, Bo5 0.63; player_round_glicko+none Bo3 0.83, Bo5 0.59; player_round_glicko_rookie_weights+none Bo3 0.88, Bo5 0.66

Parameters minimize tuning map log loss across all sections. Replay predicts before update; Replay starts at the first map. Tuning: [2024-01-01, 2026-01-01); validation: [2026-01-01, 2026-11-01). Holdout is scored only with --holdout and never selects parameters. Series use the first map prediction and independent maps in an odd best-of; missing/even best-of or unknown results are skipped. Accuracy gives 0.5 predictions half credit; ECE uses 10 equal-width bins. Log loss clips probabilities at 1e-6. Paired bootstrap uses 2,000 resamples, seed 0, clustered by match_id. Differences are the named model minus its comparator; negative favors the model. Significance requires a 95% percentile interval excluding zero. Tuning scores are selection diagnostics, not independent evidence of improvement.

Fit through 2025-12-31. Unknown host-region map rows: 911 (including missing/un).

## Stage 1 — tuning (outcomes)

### Leaderboard

| Model | Best params | Map log loss | Series log loss | Rows |
|---|---|---:|---:|---:|
| player_round_glicko_rookie_weights | {"k": 32, "new_player": "teammates", "online_k": 1.0, "rd_info": 0.125, "rd_new": 350, "rookie_maps": 400, "rookie_penalty": 200, "tau": 0.5, "tier3_k": 0.75} | 0.629692 | 0.598834 | 73819 |
| player_round_glicko | {"k": 32, "new_player": "teammates", "rd_info": 0.125, "rd_new": 350, "tau": 0.5} | 0.639856 | 0.618358 | 73819 |
| team_elo | {"k": 32} | 0.660656 | 0.645151 | 73819 |

Kalshi uses the first hourly bid/ask (midpoint for log loss, ask/bid for bets) ending ≥30 min after the market opened and ≥2 h before the scheduled start, with a spread ≤ 0.06: a price a bot could trade before any veto. Markets without such a quote are skipped. oriented to team1 using aliases. One contract per event, preferring team1. Compare identical rows; map predictions use the first map's pre-match chance. Missing links, aliases or candles are skipped; unplayed maps are not in the rows. Returns use frozen stage-1 parameters. Each bet buys $1 of contracts, fees extra; order fees ceil to a cent (0.07 × contracts × price × (1−price)). Edge selection uses unrounded per-contract fees. ROI divides profit by stake plus fees; intervals resample matches 2,000 times. Unlimited depth and depth-capped returns are shown together. Depth uses 0.5 of acceptable-price tape volume in the 6 hours after the quote, missing tapes give zero fills. Partial Kelly fills are allowed; flat bets require the full $1 stake. Kelly uses LoL caps and rounded-fee affordability, from a $50 seed. Each slice runs independently. Tape volume is a fill proxy; no slippage is modeled.

### Maps

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| coin | all | 73819 | 0.693147 | 0.250000 | 0.500000 | 0.047813 |
| coin | tier1 | 4470 | 0.693147 | 0.250000 | 0.500000 | 0.041163 |
| coin | tier2 | 18909 | 0.693147 | 0.250000 | 0.500000 | 0.047464 |
| coin | tier3 | 50234 | 0.693147 | 0.250000 | 0.500000 | 0.048732 |
| coin | unknown | 206 | 0.693147 | 0.250000 | 0.500000 | 0.000000 |
| coin | international=1 | 2557 | 0.693147 | 0.250000 | 0.500000 | 0.029918 |
| coin | international=0 | 71262 | 0.693147 | 0.250000 | 0.500000 | 0.048455 |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| team_elo | all | 73819 | 0.660656 | 0.234159 | 0.602528 | 0.027876 |
| team_elo | tier1 | 4470 | 0.675361 | 0.240596 | 0.593177 | 0.038378 |
| team_elo | tier2 | 18909 | 0.663269 | 0.235239 | 0.602385 | 0.025216 |
| team_elo | tier3 | 50234 | 0.658376 | 0.233184 | 0.603376 | 0.030657 |
| team_elo | unknown | 206 | 0.657627 | 0.232983 | 0.611650 | 0.066165 |
| team_elo | international=1 | 2557 | 0.666122 | 0.236517 | 0.609699 | 0.032560 |
| team_elo | international=0 | 71262 | 0.660460 | 0.234074 | 0.602270 | 0.028070 |

team_elo − coin (paired log loss):

| Section | Rows | team_elo log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 73819 | 0.660656 | 0.693147 | -0.032491 | [-0.034711, -0.030393] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko | all | 73819 | 0.639856 | 0.224858 | 0.627203 | 0.020776 |
| player_round_glicko | tier1 | 4470 | 0.665034 | 0.236102 | 0.596868 | 0.017341 |
| player_round_glicko | tier2 | 18909 | 0.647966 | 0.228640 | 0.614654 | 0.016128 |
| player_round_glicko | tier3 | 50234 | 0.634554 | 0.222423 | 0.634809 | 0.023255 |
| player_round_glicko | unknown | 206 | 0.641926 | 0.227528 | 0.582524 | 0.068982 |
| player_round_glicko | international=1 | 2557 | 0.660852 | 0.234453 | 0.602659 | 0.020152 |
| player_round_glicko | international=0 | 71262 | 0.639102 | 0.224513 | 0.628084 | 0.021255 |

player_round_glicko − coin (paired log loss):

| Section | Rows | player_round_glicko log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 73819 | 0.639856 | 0.693147 | -0.053292 | [-0.055684, -0.050854] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko_rookie_weights | all | 73819 | 0.629692 | 0.220367 | 0.639124 | 0.016500 |
| player_round_glicko_rookie_weights | tier1 | 4470 | 0.662370 | 0.234520 | 0.605593 | 0.020120 |
| player_round_glicko_rookie_weights | tier2 | 18909 | 0.645525 | 0.227406 | 0.619097 | 0.014102 |
| player_round_glicko_rookie_weights | tier3 | 50234 | 0.620837 | 0.216458 | 0.649679 | 0.018351 |
| player_round_glicko_rookie_weights | unknown | 206 | 0.626510 | 0.220413 | 0.631068 | 0.071909 |
| player_round_glicko_rookie_weights | international=1 | 2557 | 0.657558 | 0.232896 | 0.614392 | 0.025462 |
| player_round_glicko_rookie_weights | international=0 | 71262 | 0.628692 | 0.219918 | 0.640012 | 0.016938 |

player_round_glicko_rookie_weights − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie_weights log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 73819 | 0.629692 | 0.693147 | -0.063456 | [-0.066033, -0.060980] | yes |

player_round_glicko_rookie_weights − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie_weights log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 73819 | 0.629692 | 0.660656 | -0.030964 | [-0.032900, -0.029105] | yes |

player_round_glicko − team_elo (paired log loss):

| Section | Rows | player_round_glicko log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 73819 | 0.639856 | 0.660656 | -0.020800 | [-0.022565, -0.019081] | yes |

player_round_glicko − player_round_glicko_rookie_weights (paired log loss):

| Section | Rows | player_round_glicko log loss | player_round_glicko_rookie_weights log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 73819 | 0.639856 | 0.629692 | 0.010164 | [0.009212, 0.011137] | yes |

### Series

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| coin | all | 35914 | 0.693147 | 0.250000 | 0.500000 | 0.062260 |
| coin | tier1 | 2047 | 0.693147 | 0.250000 | 0.500000 | 0.055447 |
| coin | tier2 | 8853 | 0.693147 | 0.250000 | 0.500000 | 0.064328 |
| coin | tier3 | 24957 | 0.693147 | 0.250000 | 0.500000 | 0.062047 |
| coin | unknown | 57 | 0.693147 | 0.250000 | 0.500000 | 0.078947 |
| coin | international=1 | 1101 | 0.693147 | 0.250000 | 0.500000 | 0.038601 |
| coin | international=0 | 34813 | 0.693147 | 0.250000 | 0.500000 | 0.063008 |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| team_elo | all | 35914 | 0.645151 | 0.227103 | 0.620635 | 0.036068 |
| team_elo | tier1 | 2047 | 0.660860 | 0.233880 | 0.605032 | 0.037747 |
| team_elo | tier2 | 8853 | 0.644740 | 0.226790 | 0.626059 | 0.028896 |
| team_elo | tier3 | 24957 | 0.643908 | 0.226610 | 0.620127 | 0.041106 |
| team_elo | unknown | 57 | 0.689249 | 0.248006 | 0.561404 | 0.159128 |
| team_elo | international=1 | 1101 | 0.644312 | 0.226879 | 0.625795 | 0.037687 |
| team_elo | international=0 | 34813 | 0.645178 | 0.227110 | 0.620472 | 0.037106 |

team_elo − coin (paired log loss):

| Section | Rows | team_elo log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 35914 | 0.645151 | 0.693147 | -0.047996 | [-0.051019, -0.044927] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko | all | 35914 | 0.618358 | 0.214857 | 0.655134 | 0.028540 |
| player_round_glicko | tier1 | 2047 | 0.650154 | 0.228637 | 0.624084 | 0.025984 |
| player_round_glicko | tier2 | 8853 | 0.622921 | 0.217361 | 0.645939 | 0.027796 |
| player_round_glicko | tier3 | 24957 | 0.613902 | 0.212731 | 0.661358 | 0.030934 |
| player_round_glicko | unknown | 57 | 0.719010 | 0.261977 | 0.473684 | 0.160496 |
| player_round_glicko | international=1 | 1101 | 0.640461 | 0.225357 | 0.625341 | 0.023509 |
| player_round_glicko | international=0 | 34813 | 0.617659 | 0.214525 | 0.656077 | 0.029184 |

player_round_glicko − coin (paired log loss):

| Section | Rows | player_round_glicko log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 35914 | 0.618358 | 0.693147 | -0.074789 | [-0.078602, -0.070917] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko_rookie_weights | all | 35914 | 0.598834 | 0.206175 | 0.675113 | 0.022633 |
| player_round_glicko_rookie_weights | tier1 | 2047 | 0.648019 | 0.225951 | 0.635564 | 0.024807 |
| player_round_glicko_rookie_weights | tier2 | 8853 | 0.618462 | 0.214924 | 0.649384 | 0.021894 |
| player_round_glicko_rookie_weights | tier3 | 24957 | 0.587650 | 0.201365 | 0.687703 | 0.024203 |
| player_round_glicko_rookie_weights | unknown | 57 | 0.680625 | 0.243377 | 0.578947 | 0.128965 |
| player_round_glicko_rookie_weights | international=1 | 1101 | 0.635993 | 0.222675 | 0.645322 | 0.031294 |
| player_round_glicko_rookie_weights | international=0 | 34813 | 0.597658 | 0.205653 | 0.676055 | 0.023566 |

player_round_glicko_rookie_weights − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie_weights log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 35914 | 0.598834 | 0.693147 | -0.094314 | [-0.098482, -0.089918] | yes |

player_round_glicko_rookie_weights − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie_weights log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 35914 | 0.598834 | 0.645151 | -0.046318 | [-0.049726, -0.042902] | yes |

player_round_glicko − team_elo (paired log loss):

| Section | Rows | player_round_glicko log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 35914 | 0.618358 | 0.645151 | -0.026793 | [-0.029732, -0.023875] | yes |

player_round_glicko − player_round_glicko_rookie_weights (paired log loss):

| Section | Rows | player_round_glicko log loss | player_round_glicko_rookie_weights log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 35914 | 0.618358 | 0.598834 | 0.019525 | [0.017538, 0.021432] | yes |

## Stage 2 — validation (outcomes)

### Leaderboard (frozen stage-1 parameters)

| Model | Best params | Map log loss | Series log loss | Rows |
|---|---|---:|---:|---:|
| player_round_glicko_rookie_weights | {"k": 32, "new_player": "teammates", "online_k": 1.0, "rd_info": 0.125, "rd_new": 350, "rookie_maps": 400, "rookie_penalty": 200, "tau": 0.5, "tier3_k": 0.75} | 0.618139 | 0.578887 | 36077 |
| player_round_glicko_rookie_weights+none | {"k": 32, "new_player": "teammates", "online_k": 1.0, "rd_info": 0.125, "rd_new": 350, "rookie_maps": 400, "rookie_penalty": 200, "tau": 0.5, "tier3_k": 0.75} | 0.618139 | 0.578887 | 36077 |
| player_round_glicko | {"k": 32, "new_player": "teammates", "rd_info": 0.125, "rd_new": 350, "tau": 0.5} | 0.625617 | 0.594345 | 36077 |
| player_round_glicko+none | {"k": 32, "new_player": "teammates", "rd_info": 0.125, "rd_new": 350, "tau": 0.5} | 0.625617 | 0.594345 | 36077 |
| team_elo | {"k": 32} | 0.650234 | 0.626402 | 36077 |
| team_elo+none | {"k": 32} | 0.650234 | 0.626402 | 36077 |

### Maps

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| coin | all | 36077 | 0.693147 | 0.250000 | 0.500000 | 0.053760 |
| coin | tier1 | 2097 | 0.693147 | 0.250000 | 0.500000 | 0.037911 |
| coin | tier2 | 9801 | 0.693147 | 0.250000 | 0.500000 | 0.056984 |
| coin | tier3 | 23489 | 0.693147 | 0.250000 | 0.500000 | 0.053067 |
| coin | unknown | 690 | 0.693147 | 0.250000 | 0.500000 | 0.079710 |
| coin | international=1 | 1194 | 0.693147 | 0.250000 | 0.500000 | 0.030151 |
| coin | international=0 | 34883 | 0.693147 | 0.250000 | 0.500000 | 0.054568 |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| team_elo | all | 36077 | 0.650234 | 0.229436 | 0.615974 | 0.028812 |
| team_elo | tier1 | 2097 | 0.671551 | 0.237404 | 0.608488 | 0.036213 |
| team_elo | tier2 | 9801 | 0.656685 | 0.232323 | 0.610142 | 0.039304 |
| team_elo | tier3 | 23489 | 0.646743 | 0.228000 | 0.618268 | 0.025957 |
| team_elo | unknown | 690 | 0.612645 | 0.213119 | 0.643478 | 0.065640 |
| team_elo | international=1 | 1194 | 0.642206 | 0.225237 | 0.642379 | 0.031870 |
| team_elo | international=0 | 34883 | 0.650508 | 0.229580 | 0.615070 | 0.029358 |

team_elo − coin (paired log loss):

| Section | Rows | team_elo log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 36077 | 0.650234 | 0.693147 | -0.042914 | [-0.046471, -0.039369] | yes |
| tier1 | 2097 | 0.671551 | 0.693147 | -0.021596 | [-0.038037, -0.003738] | yes |
| tier2 | 9801 | 0.656685 | 0.693147 | -0.036463 | [-0.044110, -0.029479] | yes |
| tier3 | 23489 | 0.646743 | 0.693147 | -0.046404 | [-0.050407, -0.042160] | yes |
| unknown | 690 | 0.612645 | 0.693147 | -0.080502 | [-0.108390, -0.053386] | yes |
| international=1 | 1194 | 0.642206 | 0.693147 | -0.050941 | [-0.073387, -0.028520] | yes |
| international=0 | 34883 | 0.650508 | 0.693147 | -0.042639 | [-0.046233, -0.038949] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko | all | 36077 | 0.625617 | 0.218804 | 0.641891 | 0.017991 |
| player_round_glicko | tier1 | 2097 | 0.661497 | 0.234357 | 0.604435 | 0.021142 |
| player_round_glicko | tier2 | 9801 | 0.631168 | 0.221527 | 0.634119 | 0.014267 |
| player_round_glicko | tier3 | 23489 | 0.621076 | 0.216693 | 0.647793 | 0.019824 |
| player_round_glicko | unknown | 690 | 0.592301 | 0.204709 | 0.665217 | 0.056666 |
| player_round_glicko | international=1 | 1194 | 0.642351 | 0.225679 | 0.640704 | 0.038688 |
| player_round_glicko | international=0 | 34883 | 0.625044 | 0.218569 | 0.641932 | 0.018515 |

player_round_glicko − coin (paired log loss):

| Section | Rows | player_round_glicko log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 36077 | 0.625617 | 0.693147 | -0.067530 | [-0.071173, -0.063777] | yes |
| tier1 | 2097 | 0.661497 | 0.693147 | -0.031650 | [-0.043698, -0.019410] | yes |
| tier2 | 9801 | 0.631168 | 0.693147 | -0.061979 | [-0.068398, -0.055804] | yes |
| tier3 | 23489 | 0.621076 | 0.693147 | -0.072071 | [-0.076689, -0.067466] | yes |
| unknown | 690 | 0.592301 | 0.693147 | -0.100846 | [-0.127713, -0.073188] | yes |
| international=1 | 1194 | 0.642351 | 0.693147 | -0.050796 | [-0.066895, -0.035179] | yes |
| international=0 | 34883 | 0.625044 | 0.693147 | -0.068103 | [-0.071894, -0.064246] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko_rookie_weights | all | 36077 | 0.618139 | 0.215549 | 0.650179 | 0.017006 |
| player_round_glicko_rookie_weights | tier1 | 2097 | 0.658988 | 0.233212 | 0.605627 | 0.019746 |
| player_round_glicko_rookie_weights | tier2 | 9801 | 0.630205 | 0.220980 | 0.638965 | 0.023920 |
| player_round_glicko_rookie_weights | tier3 | 23489 | 0.610359 | 0.212083 | 0.658585 | 0.016958 |
| player_round_glicko_rookie_weights | unknown | 690 | 0.587431 | 0.202752 | 0.658696 | 0.070602 |
| player_round_glicko_rookie_weights | international=1 | 1194 | 0.639645 | 0.224305 | 0.641541 | 0.035878 |
| player_round_glicko_rookie_weights | international=0 | 34883 | 0.617402 | 0.215250 | 0.650474 | 0.017659 |

player_round_glicko_rookie_weights − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie_weights log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 36077 | 0.618139 | 0.693147 | -0.075009 | [-0.078810, -0.071011] | yes |
| tier1 | 2097 | 0.658988 | 0.693147 | -0.034159 | [-0.045851, -0.021635] | yes |
| tier2 | 9801 | 0.630205 | 0.693147 | -0.062942 | [-0.069511, -0.056688] | yes |
| tier3 | 23489 | 0.610359 | 0.693147 | -0.082788 | [-0.087761, -0.078029] | yes |
| unknown | 690 | 0.587431 | 0.693147 | -0.105716 | [-0.133868, -0.077545] | yes |
| international=1 | 1194 | 0.639645 | 0.693147 | -0.053502 | [-0.069754, -0.036951] | yes |
| international=0 | 34883 | 0.617402 | 0.693147 | -0.075745 | [-0.079407, -0.071781] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| team_elo+none | all | 36077 | 0.650234 | 0.229436 | 0.615974 | 0.028812 |
| team_elo+none | tier1 | 2097 | 0.671551 | 0.237404 | 0.608488 | 0.036213 |
| team_elo+none | tier2 | 9801 | 0.656685 | 0.232323 | 0.610142 | 0.039304 |
| team_elo+none | tier3 | 23489 | 0.646743 | 0.228000 | 0.618268 | 0.025957 |
| team_elo+none | unknown | 690 | 0.612645 | 0.213119 | 0.643478 | 0.065640 |
| team_elo+none | international=1 | 1194 | 0.642206 | 0.225237 | 0.642379 | 0.031870 |
| team_elo+none | international=0 | 34883 | 0.650508 | 0.229580 | 0.615070 | 0.029358 |

team_elo+none − coin (paired log loss):

| Section | Rows | team_elo+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 36077 | 0.650234 | 0.693147 | -0.042914 | [-0.046471, -0.039369] | yes |
| tier1 | 2097 | 0.671551 | 0.693147 | -0.021596 | [-0.038037, -0.003738] | yes |
| tier2 | 9801 | 0.656685 | 0.693147 | -0.036463 | [-0.044110, -0.029479] | yes |
| tier3 | 23489 | 0.646743 | 0.693147 | -0.046404 | [-0.050407, -0.042160] | yes |
| unknown | 690 | 0.612645 | 0.693147 | -0.080502 | [-0.108390, -0.053386] | yes |
| international=1 | 1194 | 0.642206 | 0.693147 | -0.050941 | [-0.073387, -0.028520] | yes |
| international=0 | 34883 | 0.650508 | 0.693147 | -0.042639 | [-0.046233, -0.038949] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko+none | all | 36077 | 0.625617 | 0.218804 | 0.641891 | 0.017991 |
| player_round_glicko+none | tier1 | 2097 | 0.661497 | 0.234357 | 0.604435 | 0.021142 |
| player_round_glicko+none | tier2 | 9801 | 0.631168 | 0.221527 | 0.634119 | 0.014267 |
| player_round_glicko+none | tier3 | 23489 | 0.621076 | 0.216693 | 0.647793 | 0.019824 |
| player_round_glicko+none | unknown | 690 | 0.592301 | 0.204709 | 0.665217 | 0.056666 |
| player_round_glicko+none | international=1 | 1194 | 0.642351 | 0.225679 | 0.640704 | 0.038688 |
| player_round_glicko+none | international=0 | 34883 | 0.625044 | 0.218569 | 0.641932 | 0.018515 |

player_round_glicko+none − coin (paired log loss):

| Section | Rows | player_round_glicko+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 36077 | 0.625617 | 0.693147 | -0.067530 | [-0.071173, -0.063777] | yes |
| tier1 | 2097 | 0.661497 | 0.693147 | -0.031650 | [-0.043698, -0.019410] | yes |
| tier2 | 9801 | 0.631168 | 0.693147 | -0.061979 | [-0.068398, -0.055804] | yes |
| tier3 | 23489 | 0.621076 | 0.693147 | -0.072071 | [-0.076689, -0.067466] | yes |
| unknown | 690 | 0.592301 | 0.693147 | -0.100846 | [-0.127713, -0.073188] | yes |
| international=1 | 1194 | 0.642351 | 0.693147 | -0.050796 | [-0.066895, -0.035179] | yes |
| international=0 | 34883 | 0.625044 | 0.693147 | -0.068103 | [-0.071894, -0.064246] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko_rookie_weights+none | all | 36077 | 0.618139 | 0.215549 | 0.650179 | 0.017006 |
| player_round_glicko_rookie_weights+none | tier1 | 2097 | 0.658988 | 0.233212 | 0.605627 | 0.019746 |
| player_round_glicko_rookie_weights+none | tier2 | 9801 | 0.630205 | 0.220980 | 0.638965 | 0.023920 |
| player_round_glicko_rookie_weights+none | tier3 | 23489 | 0.610359 | 0.212083 | 0.658585 | 0.016958 |
| player_round_glicko_rookie_weights+none | unknown | 690 | 0.587431 | 0.202752 | 0.658696 | 0.070602 |
| player_round_glicko_rookie_weights+none | international=1 | 1194 | 0.639645 | 0.224305 | 0.641541 | 0.035878 |
| player_round_glicko_rookie_weights+none | international=0 | 34883 | 0.617402 | 0.215250 | 0.650474 | 0.017659 |

player_round_glicko_rookie_weights+none − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie_weights+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 36077 | 0.618139 | 0.693147 | -0.075009 | [-0.078810, -0.071011] | yes |
| tier1 | 2097 | 0.658988 | 0.693147 | -0.034159 | [-0.045851, -0.021635] | yes |
| tier2 | 9801 | 0.630205 | 0.693147 | -0.062942 | [-0.069511, -0.056688] | yes |
| tier3 | 23489 | 0.610359 | 0.693147 | -0.082788 | [-0.087761, -0.078029] | yes |
| unknown | 690 | 0.587431 | 0.693147 | -0.105716 | [-0.133868, -0.077545] | yes |
| international=1 | 1194 | 0.639645 | 0.693147 | -0.053502 | [-0.069754, -0.036951] | yes |
| international=0 | 34883 | 0.617402 | 0.693147 | -0.075745 | [-0.079407, -0.071781] | yes |

player_round_glicko − team_elo (paired log loss):

| Section | Rows | player_round_glicko log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 36077 | 0.625617 | 0.650234 | -0.024617 | [-0.027266, -0.022060] | yes |

player_round_glicko_rookie_weights − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie_weights log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 36077 | 0.618139 | 0.650234 | -0.032095 | [-0.034942, -0.029293] | yes |

team_elo+none − team_elo (paired log loss):

| Section | Rows | team_elo+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 36077 | 0.650234 | 0.650234 | 0.000000 | [0.000000, 0.000000] | no |

player_round_glicko+none − team_elo (paired log loss):

| Section | Rows | player_round_glicko+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 36077 | 0.625617 | 0.650234 | -0.024617 | [-0.027266, -0.022060] | yes |

player_round_glicko_rookie_weights+none − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie_weights+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 36077 | 0.618139 | 0.650234 | -0.032095 | [-0.034942, -0.029293] | yes |

player_round_glicko − player_round_glicko_rookie_weights (paired log loss):

| Section | Rows | player_round_glicko log loss | player_round_glicko_rookie_weights log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 36077 | 0.625617 | 0.618139 | 0.007478 | [0.006128, 0.008773] | yes |
| tier1 | 2097 | 0.661497 | 0.658988 | 0.002509 | [0.000562, 0.004564] | yes |
| tier2 | 9801 | 0.631168 | 0.630205 | 0.000963 | [-0.000576, 0.002314] | no |
| tier3 | 23489 | 0.621076 | 0.610359 | 0.010718 | [0.008760, 0.012585] | yes |
| unknown | 690 | 0.592301 | 0.587431 | 0.004870 | [-0.000403, 0.010745] | no |
| international=1 | 1194 | 0.642351 | 0.639645 | 0.002706 | [-0.000001, 0.005659] | no |
| international=0 | 34883 | 0.625044 | 0.617402 | 0.007642 | [0.006314, 0.008968] | yes |

team_elo+none − player_round_glicko_rookie_weights (paired log loss):

| Section | Rows | team_elo+none log loss | player_round_glicko_rookie_weights log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 36077 | 0.650234 | 0.618139 | 0.032095 | [0.029293, 0.034942] | yes |
| tier1 | 2097 | 0.671551 | 0.658988 | 0.012563 | [0.003205, 0.022627] | yes |
| tier2 | 9801 | 0.656685 | 0.630205 | 0.026479 | [0.021597, 0.031484] | yes |
| tier3 | 23489 | 0.646743 | 0.610359 | 0.036384 | [0.032628, 0.040097] | yes |
| unknown | 690 | 0.612645 | 0.587431 | 0.025214 | [0.007994, 0.042822] | yes |
| international=1 | 1194 | 0.642206 | 0.639645 | 0.002561 | [-0.009300, 0.013969] | no |
| international=0 | 34883 | 0.650508 | 0.617402 | 0.033106 | [0.030119, 0.035958] | yes |

player_round_glicko+none − player_round_glicko_rookie_weights (paired log loss):

| Section | Rows | player_round_glicko+none log loss | player_round_glicko_rookie_weights log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 36077 | 0.625617 | 0.618139 | 0.007478 | [0.006128, 0.008773] | yes |
| tier1 | 2097 | 0.661497 | 0.658988 | 0.002509 | [0.000562, 0.004564] | yes |
| tier2 | 9801 | 0.631168 | 0.630205 | 0.000963 | [-0.000576, 0.002314] | no |
| tier3 | 23489 | 0.621076 | 0.610359 | 0.010718 | [0.008760, 0.012585] | yes |
| unknown | 690 | 0.592301 | 0.587431 | 0.004870 | [-0.000403, 0.010745] | no |
| international=1 | 1194 | 0.642351 | 0.639645 | 0.002706 | [-0.000001, 0.005659] | no |
| international=0 | 34883 | 0.625044 | 0.617402 | 0.007642 | [0.006314, 0.008968] | yes |

player_round_glicko_rookie_weights+none − player_round_glicko_rookie_weights (paired log loss):

| Section | Rows | player_round_glicko_rookie_weights+none log loss | player_round_glicko_rookie_weights log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 36077 | 0.618139 | 0.618139 | 0.000000 | [0.000000, 0.000000] | no |
| tier1 | 2097 | 0.658988 | 0.658988 | 0.000000 | [0.000000, 0.000000] | no |
| tier2 | 9801 | 0.630205 | 0.630205 | 0.000000 | [0.000000, 0.000000] | no |
| tier3 | 23489 | 0.610359 | 0.610359 | 0.000000 | [0.000000, 0.000000] | no |
| unknown | 690 | 0.587431 | 0.587431 | 0.000000 | [0.000000, 0.000000] | no |
| international=1 | 1194 | 0.639645 | 0.639645 | 0.000000 | [0.000000, 0.000000] | no |
| international=0 | 34883 | 0.617402 | 0.617402 | 0.000000 | [0.000000, 0.000000] | no |

### Series

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| coin | all | 16918 | 0.693147 | 0.250000 | 0.500000 | 0.070812 |
| coin | tier1 | 897 | 0.693147 | 0.250000 | 0.500000 | 0.046265 |
| coin | tier2 | 4498 | 0.693147 | 0.250000 | 0.500000 | 0.079813 |
| coin | tier3 | 11240 | 0.693147 | 0.250000 | 0.500000 | 0.067883 |
| coin | unknown | 283 | 0.693147 | 0.250000 | 0.500000 | 0.121908 |
| coin | international=1 | 503 | 0.693147 | 0.250000 | 0.500000 | 0.034791 |
| coin | international=0 | 16415 | 0.693147 | 0.250000 | 0.500000 | 0.071916 |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| team_elo | all | 16918 | 0.626402 | 0.218831 | 0.641802 | 0.032995 |
| team_elo | tier1 | 897 | 0.645834 | 0.225146 | 0.640468 | 0.033051 |
| team_elo | tier2 | 4498 | 0.633288 | 0.221630 | 0.639173 | 0.034607 |
| team_elo | tier3 | 11240 | 0.623778 | 0.217877 | 0.641593 | 0.036605 |
| team_elo | unknown | 283 | 0.559580 | 0.192254 | 0.696113 | 0.084073 |
| team_elo | international=1 | 503 | 0.606870 | 0.209320 | 0.682903 | 0.037080 |
| team_elo | international=0 | 16415 | 0.627000 | 0.219123 | 0.640542 | 0.034226 |

team_elo − coin (paired log loss):

| Section | Rows | team_elo log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 16918 | 0.626402 | 0.693147 | -0.066745 | [-0.071650, -0.061619] | yes |
| tier1 | 897 | 0.645834 | 0.693147 | -0.047314 | [-0.074068, -0.019278] | yes |
| tier2 | 4498 | 0.633288 | 0.693147 | -0.059859 | [-0.071033, -0.048938] | yes |
| tier3 | 11240 | 0.623778 | 0.693147 | -0.069369 | [-0.075112, -0.063371] | yes |
| unknown | 283 | 0.559580 | 0.693147 | -0.133568 | [-0.174459, -0.093804] | yes |
| international=1 | 503 | 0.606870 | 0.693147 | -0.086277 | [-0.121276, -0.050598] | yes |
| international=0 | 16415 | 0.627000 | 0.693147 | -0.066147 | [-0.071613, -0.060866] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko | all | 16918 | 0.594345 | 0.204656 | 0.677621 | 0.025638 |
| player_round_glicko | tier1 | 897 | 0.643332 | 0.225663 | 0.629877 | 0.032790 |
| player_round_glicko | tier2 | 4498 | 0.596977 | 0.206358 | 0.672076 | 0.022926 |
| player_round_glicko | tier3 | 11240 | 0.590857 | 0.202834 | 0.682607 | 0.027825 |
| player_round_glicko | unknown | 283 | 0.535797 | 0.183378 | 0.719081 | 0.072738 |
| player_round_glicko | international=1 | 503 | 0.613594 | 0.212822 | 0.667992 | 0.055328 |
| player_round_glicko | international=0 | 16415 | 0.593755 | 0.204406 | 0.677917 | 0.026457 |

player_round_glicko − coin (paired log loss):

| Section | Rows | player_round_glicko log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 16918 | 0.594345 | 0.693147 | -0.098802 | [-0.104825, -0.092726] | yes |
| tier1 | 897 | 0.643332 | 0.693147 | -0.049815 | [-0.069739, -0.027690] | yes |
| tier2 | 4498 | 0.596977 | 0.693147 | -0.096170 | [-0.106972, -0.085692] | yes |
| tier3 | 11240 | 0.590857 | 0.693147 | -0.102291 | [-0.109809, -0.094583] | yes |
| unknown | 283 | 0.535797 | 0.693147 | -0.157350 | [-0.197578, -0.115163] | yes |
| international=1 | 503 | 0.613594 | 0.693147 | -0.079553 | [-0.107462, -0.051578] | yes |
| international=0 | 16415 | 0.593755 | 0.693147 | -0.099392 | [-0.105432, -0.092906] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko_rookie_weights | all | 16918 | 0.578887 | 0.198120 | 0.694379 | 0.023510 |
| player_round_glicko_rookie_weights | tier1 | 897 | 0.640079 | 0.224276 | 0.636009 | 0.029518 |
| player_round_glicko_rookie_weights | tier2 | 4498 | 0.593395 | 0.204916 | 0.680747 | 0.029785 |
| player_round_glicko_rookie_weights | tier3 | 11240 | 0.569607 | 0.193797 | 0.704226 | 0.021625 |
| player_round_glicko_rookie_weights | unknown | 283 | 0.522908 | 0.178942 | 0.704947 | 0.082707 |
| player_round_glicko_rookie_weights | international=1 | 503 | 0.609161 | 0.210921 | 0.671968 | 0.047260 |
| player_round_glicko_rookie_weights | international=0 | 16415 | 0.577959 | 0.197728 | 0.695065 | 0.023589 |

player_round_glicko_rookie_weights − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie_weights log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 16918 | 0.578887 | 0.693147 | -0.114260 | [-0.120782, -0.107800] | yes |
| tier1 | 897 | 0.640079 | 0.693147 | -0.053068 | [-0.073649, -0.029745] | yes |
| tier2 | 4498 | 0.593395 | 0.693147 | -0.099752 | [-0.110605, -0.088694] | yes |
| tier3 | 11240 | 0.569607 | 0.693147 | -0.123540 | [-0.131524, -0.115063] | yes |
| unknown | 283 | 0.522908 | 0.693147 | -0.170239 | [-0.211716, -0.126429] | yes |
| international=1 | 503 | 0.609161 | 0.693147 | -0.083986 | [-0.113008, -0.053947] | yes |
| international=0 | 16415 | 0.577959 | 0.693147 | -0.115188 | [-0.121840, -0.108290] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| team_elo+none | all | 16918 | 0.626402 | 0.218831 | 0.641802 | 0.032995 |
| team_elo+none | tier1 | 897 | 0.645834 | 0.225146 | 0.640468 | 0.033051 |
| team_elo+none | tier2 | 4498 | 0.633288 | 0.221630 | 0.639173 | 0.034607 |
| team_elo+none | tier3 | 11240 | 0.623778 | 0.217877 | 0.641593 | 0.036605 |
| team_elo+none | unknown | 283 | 0.559580 | 0.192254 | 0.696113 | 0.084073 |
| team_elo+none | international=1 | 503 | 0.606870 | 0.209320 | 0.682903 | 0.037080 |
| team_elo+none | international=0 | 16415 | 0.627000 | 0.219123 | 0.640542 | 0.034226 |

team_elo+none − coin (paired log loss):

| Section | Rows | team_elo+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 16918 | 0.626402 | 0.693147 | -0.066745 | [-0.071650, -0.061619] | yes |
| tier1 | 897 | 0.645834 | 0.693147 | -0.047314 | [-0.074068, -0.019278] | yes |
| tier2 | 4498 | 0.633288 | 0.693147 | -0.059859 | [-0.071033, -0.048938] | yes |
| tier3 | 11240 | 0.623778 | 0.693147 | -0.069369 | [-0.075112, -0.063371] | yes |
| unknown | 283 | 0.559580 | 0.693147 | -0.133568 | [-0.174459, -0.093804] | yes |
| international=1 | 503 | 0.606870 | 0.693147 | -0.086277 | [-0.121276, -0.050598] | yes |
| international=0 | 16415 | 0.627000 | 0.693147 | -0.066147 | [-0.071613, -0.060866] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko+none | all | 16918 | 0.594345 | 0.204656 | 0.677621 | 0.025638 |
| player_round_glicko+none | tier1 | 897 | 0.643332 | 0.225663 | 0.629877 | 0.032790 |
| player_round_glicko+none | tier2 | 4498 | 0.596977 | 0.206358 | 0.672076 | 0.022926 |
| player_round_glicko+none | tier3 | 11240 | 0.590857 | 0.202834 | 0.682607 | 0.027825 |
| player_round_glicko+none | unknown | 283 | 0.535797 | 0.183378 | 0.719081 | 0.072738 |
| player_round_glicko+none | international=1 | 503 | 0.613594 | 0.212822 | 0.667992 | 0.055328 |
| player_round_glicko+none | international=0 | 16415 | 0.593755 | 0.204406 | 0.677917 | 0.026457 |

player_round_glicko+none − coin (paired log loss):

| Section | Rows | player_round_glicko+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 16918 | 0.594345 | 0.693147 | -0.098802 | [-0.104825, -0.092726] | yes |
| tier1 | 897 | 0.643332 | 0.693147 | -0.049815 | [-0.069739, -0.027690] | yes |
| tier2 | 4498 | 0.596977 | 0.693147 | -0.096170 | [-0.106972, -0.085692] | yes |
| tier3 | 11240 | 0.590857 | 0.693147 | -0.102291 | [-0.109809, -0.094583] | yes |
| unknown | 283 | 0.535797 | 0.693147 | -0.157350 | [-0.197578, -0.115163] | yes |
| international=1 | 503 | 0.613594 | 0.693147 | -0.079553 | [-0.107462, -0.051578] | yes |
| international=0 | 16415 | 0.593755 | 0.693147 | -0.099392 | [-0.105432, -0.092906] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko_rookie_weights+none | all | 16918 | 0.578887 | 0.198120 | 0.694379 | 0.023510 |
| player_round_glicko_rookie_weights+none | tier1 | 897 | 0.640079 | 0.224276 | 0.636009 | 0.029518 |
| player_round_glicko_rookie_weights+none | tier2 | 4498 | 0.593395 | 0.204916 | 0.680747 | 0.029785 |
| player_round_glicko_rookie_weights+none | tier3 | 11240 | 0.569607 | 0.193797 | 0.704226 | 0.021625 |
| player_round_glicko_rookie_weights+none | unknown | 283 | 0.522908 | 0.178942 | 0.704947 | 0.082707 |
| player_round_glicko_rookie_weights+none | international=1 | 503 | 0.609161 | 0.210921 | 0.671968 | 0.047260 |
| player_round_glicko_rookie_weights+none | international=0 | 16415 | 0.577959 | 0.197728 | 0.695065 | 0.023589 |

player_round_glicko_rookie_weights+none − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie_weights+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 16918 | 0.578887 | 0.693147 | -0.114260 | [-0.120782, -0.107800] | yes |
| tier1 | 897 | 0.640079 | 0.693147 | -0.053068 | [-0.073649, -0.029745] | yes |
| tier2 | 4498 | 0.593395 | 0.693147 | -0.099752 | [-0.110605, -0.088694] | yes |
| tier3 | 11240 | 0.569607 | 0.693147 | -0.123540 | [-0.131524, -0.115063] | yes |
| unknown | 283 | 0.522908 | 0.693147 | -0.170239 | [-0.211716, -0.126429] | yes |
| international=1 | 503 | 0.609161 | 0.693147 | -0.083986 | [-0.113008, -0.053947] | yes |
| international=0 | 16415 | 0.577959 | 0.693147 | -0.115188 | [-0.121840, -0.108290] | yes |

player_round_glicko − team_elo (paired log loss):

| Section | Rows | player_round_glicko log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 16918 | 0.594345 | 0.626402 | -0.032057 | [-0.036641, -0.027590] | yes |

player_round_glicko_rookie_weights − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie_weights log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 16918 | 0.578887 | 0.626402 | -0.047515 | [-0.052375, -0.042687] | yes |

team_elo+none − team_elo (paired log loss):

| Section | Rows | team_elo+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 16918 | 0.626402 | 0.626402 | 0.000000 | [0.000000, 0.000000] | no |

player_round_glicko+none − team_elo (paired log loss):

| Section | Rows | player_round_glicko+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 16918 | 0.594345 | 0.626402 | -0.032057 | [-0.036641, -0.027590] | yes |

player_round_glicko_rookie_weights+none − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie_weights+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 16918 | 0.578887 | 0.626402 | -0.047515 | [-0.052375, -0.042687] | yes |

player_round_glicko − player_round_glicko_rookie_weights (paired log loss):

| Section | Rows | player_round_glicko log loss | player_round_glicko_rookie_weights log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 16918 | 0.594345 | 0.578887 | 0.015458 | [0.012670, 0.018281] | yes |
| tier1 | 897 | 0.643332 | 0.640079 | 0.003253 | [-0.000256, 0.006580] | no |
| tier2 | 4498 | 0.596977 | 0.593395 | 0.003582 | [0.000690, 0.006415] | yes |
| tier3 | 11240 | 0.590857 | 0.569607 | 0.021249 | [0.017139, 0.025227] | yes |
| unknown | 283 | 0.535797 | 0.522908 | 0.012889 | [0.000712, 0.024956] | yes |
| international=1 | 503 | 0.613594 | 0.609161 | 0.004433 | [-0.000057, 0.008689] | no |
| international=0 | 16415 | 0.593755 | 0.577959 | 0.015796 | [0.012965, 0.018885] | yes |

team_elo+none − player_round_glicko_rookie_weights (paired log loss):

| Section | Rows | team_elo+none log loss | player_round_glicko_rookie_weights log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 16918 | 0.626402 | 0.578887 | 0.047515 | [0.042687, 0.052375] | yes |
| tier1 | 897 | 0.645834 | 0.640079 | 0.005754 | [-0.011366, 0.022747] | no |
| tier2 | 4498 | 0.633288 | 0.593395 | 0.039894 | [0.032039, 0.048575] | yes |
| tier3 | 11240 | 0.623778 | 0.569607 | 0.054171 | [0.047526, 0.060630] | yes |
| unknown | 283 | 0.559580 | 0.522908 | 0.036672 | [0.009233, 0.064805] | yes |
| international=1 | 503 | 0.606870 | 0.609161 | -0.002291 | [-0.020659, 0.015238] | no |
| international=0 | 16415 | 0.627000 | 0.577959 | 0.049041 | [0.043998, 0.054112] | yes |

player_round_glicko+none − player_round_glicko_rookie_weights (paired log loss):

| Section | Rows | player_round_glicko+none log loss | player_round_glicko_rookie_weights log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 16918 | 0.594345 | 0.578887 | 0.015458 | [0.012670, 0.018281] | yes |
| tier1 | 897 | 0.643332 | 0.640079 | 0.003253 | [-0.000256, 0.006580] | no |
| tier2 | 4498 | 0.596977 | 0.593395 | 0.003582 | [0.000690, 0.006415] | yes |
| tier3 | 11240 | 0.590857 | 0.569607 | 0.021249 | [0.017139, 0.025227] | yes |
| unknown | 283 | 0.535797 | 0.522908 | 0.012889 | [0.000712, 0.024956] | yes |
| international=1 | 503 | 0.613594 | 0.609161 | 0.004433 | [-0.000057, 0.008689] | no |
| international=0 | 16415 | 0.593755 | 0.577959 | 0.015796 | [0.012965, 0.018885] | yes |

player_round_glicko_rookie_weights+none − player_round_glicko_rookie_weights (paired log loss):

| Section | Rows | player_round_glicko_rookie_weights+none log loss | player_round_glicko_rookie_weights log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 16918 | 0.578887 | 0.578887 | 0.000000 | [0.000000, 0.000000] | no |
| tier1 | 897 | 0.640079 | 0.640079 | 0.000000 | [0.000000, 0.000000] | no |
| tier2 | 4498 | 0.593395 | 0.593395 | 0.000000 | [0.000000, 0.000000] | no |
| tier3 | 11240 | 0.569607 | 0.569607 | 0.000000 | [0.000000, 0.000000] | no |
| unknown | 283 | 0.522908 | 0.522908 | 0.000000 | [0.000000, 0.000000] | no |
| international=1 | 503 | 0.609161 | 0.609161 | 0.000000 | [0.000000, 0.000000] | no |
| international=0 | 16415 | 0.577959 | 0.577959 | 0.000000 | [0.000000, 0.000000] | no |

## Stage 2 — validation vs Kalshi

### team_elo: Kalshi comparison and returns



#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 4456 | 0.620539 | 0.600358 | 0.020181 [0.012193, 0.027888] | yes |
| series | tier1 | 725 | 0.638064 | 0.616830 | 0.021234 [0.001915, 0.042106] | yes |
| series | tier2 | 1962 | 0.622792 | 0.590722 | 0.032070 [0.021227, 0.043410] | yes |
| series | tier3 | 1727 | 0.612961 | 0.607536 | 0.005425 [-0.008027, 0.018367] | no |
| series | unknown | 42 | 0.524418 | 0.471027 | 0.053390 [-0.019773, 0.132155] | no |
| series | international=1 | 448 | 0.599625 | 0.591446 | 0.008179 [-0.012963, 0.029675] | no |
| series | international=0 | 4008 | 0.622877 | 0.601354 | 0.021522 [0.013213, 0.029830] | yes |
| map | all | 4477 | 0.657933 | 0.634789 | 0.023144 [0.016028, 0.030213] | yes |
| map | tier1 | 1176 | 0.666677 | 0.646419 | 0.020258 [0.006107, 0.035503] | yes |
| map | tier2 | 1968 | 0.658913 | 0.631291 | 0.027622 [0.017419, 0.037958] | yes |
| map | tier3 | 1279 | 0.651000 | 0.632601 | 0.018399 [0.006219, 0.031922] | yes |
| map | unknown | 54 | 0.596005 | 0.560856 | 0.035149 [-0.014130, 0.080307] | no |
| map | international=1 | 788 | 0.629576 | 0.630059 | -0.000484 [-0.016658, 0.016022] | no |
| map | international=0 | 3689 | 0.663990 | 0.635800 | 0.028190 [0.020205, 0.036309] | yes |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 3277 | 3270 | 0.0855 | -6.01% [-10.54%, -1.78%] | $0.09 | 0.002× | 99.92% | $10.94 | 2085 (1192 unfilled) | -5.04% [-10.57%, 0.28%] | $0.07 |
| series | tier1 | 521 | 521 | 0.0784 | -9.16% [-19.73%, 1.80%] | $0.17 | 0.003× | 99.90% | $16.25 | 426 (95 unfilled) | -6.49% [-18.04%, 5.46%] | $3.08 |
| series | tier2 | 1418 | 1415 | 0.0820 | -11.38% [-17.57%, -4.76%] | $0.09 | 0.002× | 99.82% | $4.97 | 888 (530 unfilled) | -13.16% [-20.97%, -5.32%] | $0.10 |
| series | tier3 | 1307 | 1303 | 0.0918 | 1.70% [-5.11%, 9.11%] | $0.05 | 0.001× | 99.95% | $9.37 | 751 (556 unfilled) | 6.01% [-3.31%, 15.31%] | $19.30 |
| series | unknown | 31 | 31 | 0.0983 | -33.27% [-60.31%, -4.25%] | $20.59 | 0.412× | 62.49% | $5.25 | 20 (11 unfilled) | -28.92% [-65.84%, 12.03%] | $28.17 |
| series | international=1 | 319 | 319 | 0.0729 | -5.58% [-20.18%, 10.53%] | $9.48 | 0.190× | 96.24% | $8.24 | 277 (42 unfilled) | -7.06% [-20.99%, 6.88%] | $12.77 |
| series | international=0 | 2958 | 2951 | 0.0868 | -6.06% [-10.55%, -1.53%] | $0.10 | 0.002× | 99.89% | $8.72 | 1808 (1150 unfilled) | -4.73% [-10.38%, 0.95%] | $0.06 |
| map | all | 3086 | 1910 | 0.0715 | -6.49% [-10.49%, -2.60%] | $0.09 | 0.002× | 99.93% | $13.15 | 928 (2158 unfilled) | -13.47% [-20.50%, -6.16%] | $0.09 |
| map | tier1 | 791 | 519 | 0.0733 | -3.24% [-11.32%, 5.37%] | $4.62 | 0.092× | 96.66% | $4.70 | 256 (535 unfilled) | -5.00% [-18.40%, 9.52%] | $18.89 |
| map | tier2 | 1356 | 824 | 0.0699 | -8.25% [-14.12%, -2.50%] | $0.10 | 0.002× | 99.89% | $8.39 | 405 (951 unfilled) | -17.86% [-26.92%, -8.35%] | $0.07 |
| map | tier3 | 905 | 547 | 0.0718 | -5.77% [-13.07%, 1.86%] | $0.31 | 0.006× | 99.84% | $15.86 | 255 (650 unfilled) | -13.93% [-26.52%, -0.20%] | $4.72 |
| map | unknown | 34 | 20 | 0.0861 | -31.25% [-56.01%, -7.09%] | $28.26 | 0.565× | 43.48% | $4.78 | 12 (22 unfilled) | -36.23% [-75.72%, 1.05%] | $37.40 |
| map | international=1 | 524 | 350 | 0.0701 | 2.86% [-8.04%, 13.12%] | $83.84 | 1.677× | 74.81% | $8.59 | 178 (346 unfilled) | 5.16% [-12.13%, 22.84%] | $102.15 |
| map | international=0 | 2562 | 1560 | 0.0718 | -8.40% [-12.66%, -4.26%] | $0.09 | 0.002× | 99.89% | $7.68 | 750 (1812 unfilled) | -17.89% [-25.07%, -10.58%] | $0.09 |
| series+map | all | 6363 | 3679 | 0.0787 | -6.25% [-9.46%, -2.83%] | $0.08 | 0.002× | 99.88% | $6.33 | 3013 (3350 unfilled) | -7.63% [-12.36%, -2.91%] | $0.04 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2026-01-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 371 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-01 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-01 | map | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 51 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | map | 63 | 1.000000 | 0.000000 | unfitted |
| 2026-03 | series | 206 | 1.445963 | 0.701043 | fitted |
| 2026-03 | map | 165 | 1.203008 | -0.223533 | fitted |
| 2026-04 | series | 510 | 1.317039 | 0.381122 | fitted |
| 2026-04 | map | 309 | 1.143422 | -0.015436 | fitted |
| 2026-05 | series | 832 | 1.293329 | 0.451990 | fitted |
| 2026-05 | map | 582 | 1.082493 | 0.402515 | fitted |
| 2026-06 | series | 1192 | 1.283400 | 0.362163 | fitted |
| 2026-06 | map | 1034 | 1.131085 | 0.369016 | fitted |
| 2026-07 | series | 1540 | 1.206917 | 0.329427 | fitted |
| 2026-07 | map | 1448 | 1.118934 | 0.352859 | fitted |
| 2026-08 | series | 2053 | 1.152513 | 0.205875 | fitted |
| 2026-08 | map | 2066 | 1.057427 | 0.114644 | fitted |
| 2026-09 | series | 2770 | 1.168182 | 0.320251 | fitted |
| 2026-09 | map | 2939 | 1.115860 | 0.165299 | fitted |
| 2026-10 | series | 3684 | 1.153622 | 0.279948 | fitted |
| 2026-10 | map | 3818 | 1.114956 | 0.099319 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 4250 | 0.600111 | 0.601593 | -0.001482 [-0.004460, 0.001484] | no |
| series | tier1 | 614 | 0.621096 | 0.616540 | 0.004556 [-0.004246, 0.013878] | no |
| series | tier2 | 1873 | 0.594383 | 0.593752 | 0.000631 [-0.004479, 0.005525] | no |
| series | tier3 | 1721 | 0.602496 | 0.607981 | -0.005485 [-0.009382, -0.001402] | yes |
| series | unknown | 42 | 0.451047 | 0.471027 | -0.019980 [-0.053332, 0.013587] | no |
| series | international=1 | 370 | 0.587866 | 0.589385 | -0.001519 [-0.011232, 0.008713] | no |
| series | international=0 | 3880 | 0.601279 | 0.602757 | -0.001479 [-0.004426, 0.001745] | no |
| map | all | 4312 | 0.636366 | 0.635269 | 0.001097 [-0.000926, 0.003097] | no |
| map | tier1 | 1046 | 0.654215 | 0.649504 | 0.004710 [0.000228, 0.009235] | yes |
| map | tier2 | 1936 | 0.631262 | 0.631140 | 0.000122 [-0.002731, 0.002885] | no |
| map | tier3 | 1276 | 0.633026 | 0.633014 | 0.000012 [-0.003162, 0.003591] | no |
| map | unknown | 54 | 0.552559 | 0.560856 | -0.008297 [-0.020260, 0.002638] | no |
| map | international=1 | 686 | 0.628933 | 0.629473 | -0.000540 [-0.005162, 0.004515] | no |
| map | international=0 | 3626 | 0.637773 | 0.636366 | 0.001407 [-0.000758, 0.003639] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 1638 | 1636 | 0.0253 | 2.74% [-1.45%, 7.12%] | $19.26 | 0.385× | 87.33% | $5.32 | 1083 (555 unfilled) | 5.21% [0.23%, 11.01%] | $101.79 |
| series | tier1 | 239 | 239 | 0.0288 | 1.73% [-8.62%, 12.93%] | $26.30 | 0.526× | 72.81% | $9.11 | 189 (50 unfilled) | 3.13% [-7.78%, 13.69%] | $58.67 |
| series | tier2 | 787 | 785 | 0.0278 | -2.54% [-8.07%, 3.11%] | $8.27 | 0.165× | 86.45% | $4.90 | 519 (268 unfilled) | 0.04% [-7.23%, 7.49%] | $24.14 |
| series | tier3 | 588 | 588 | 0.0200 | 10.64% [3.04%, 18.77%] | $284.46 | 5.689× | 55.43% | $31.13 | 358 (230 unfilled) | 14.78% [4.88%, 26.71%] | $158.57 |
| series | unknown | 24 | 24 | 0.0383 | -8.11% [-36.22%, 21.16%] | $56.74 | 1.135× | 25.81% | $6.70 | 17 (7 unfilled) | -15.01% [-52.27%, 23.73%] | $52.68 |
| series | international=1 | 146 | 146 | 0.0264 | 4.90% [-8.27%, 19.89%] | $45.68 | 0.914× | 47.10% | $8.36 | 124 (22 unfilled) | 2.37% [-10.06%, 15.63%] | $49.87 |
| series | international=0 | 1492 | 1490 | 0.0252 | 2.53% [-2.16%, 7.25%] | $18.26 | 0.365× | 88.82% | $4.90 | 959 (533 unfilled) | 5.58% [-0.07%, 11.73%] | $98.19 |
| map | all | 616 | 393 | 0.0193 | -2.31% [-9.63%, 5.91%] | $27.38 | 0.548× | 84.15% | $12.16 | 189 (427 unfilled) | -5.97% [-16.87%, 4.17%] | $28.26 |
| map | tier1 | 160 | 102 | 0.0251 | -15.02% [-26.38%, -2.65%] | $22.56 | 0.451× | 60.55% | $4.27 | 55 (105 unfilled) | -11.82% [-32.59%, 9.08%] | $42.56 |
| map | tier2 | 289 | 186 | 0.0190 | -1.99% [-13.47%, 13.14%] | $41.29 | 0.826× | 58.40% | $8.24 | 88 (201 unfilled) | -3.48% [-19.03%, 12.24%] | $36.67 |
| map | tier3 | 155 | 96 | 0.0144 | 9.62% [-3.88%, 22.51%] | $76.37 | 1.527× | 24.18% | $5.18 | 40 (115 unfilled) | -6.62% [-28.34%, 16.16%] | $44.82 |
| map | unknown | 12 | 9 | 0.0113 | 5.15% [-23.22%, 33.94%] | $49.98 | 1.000× | 7.06% | $3.69 | 6 (6 unfilled) | 15.58% [-7.91%, 41.56%] | $50.08 |
| map | international=1 | 97 | 62 | 0.0231 | -2.33% [-17.53%, 12.65%] | $50.65 | 1.013× | 24.92% | $4.20 | 42 (55 unfilled) | -8.81% [-34.49%, 17.58%] | $45.91 |
| map | international=0 | 519 | 331 | 0.0185 | -2.31% [-10.77%, 6.49%] | $26.85 | 0.537× | 84.14% | $12.35 | 147 (372 unfilled) | -5.16% [-16.32%, 6.82%] | $30.37 |
| series+map | all | 2254 | 1684 | 0.0237 | 1.36% [-2.47%, 5.64%] | $26.85 | 0.537× | 85.84% | $6.40 | 1272 (982 unfilled) | 3.55% [-1.19%, 8.56%] | $81.11 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-01 | 63 | 0.681679 | — | 0.638920 | -14.41% (45), $38.28 | — | 5 (40 unfilled) | -48.78% [-100.00%, 5.91%] | $46.59 | — | — | — |
| map | 2026-02 | 102 | 0.648781 | — | 0.611955 | -21.41% (68), $16.87 | — | 28 (40 unfilled) | -45.38% [-75.28%, -12.44%] | $21.42 | — | — | — |
| map | 2026-03 | 144 | 0.656391 | 0.647109 | 0.642845 | 1.83% (80), $54.56 | -3.31% (27), $40.17 | 48 (32 unfilled) | 11.15% [-22.17%, 43.96%] | $62.30 | 14 (13 unfilled) | -28.01% [-60.80%, 7.45%] | $36.56 |
| map | 2026-04 | 273 | 0.637080 | 0.650671 | 0.647894 | 15.73% (182), $205.02 | -15.77% (13), $40.95 | 67 (115 unfilled) | -7.97% [-29.09%, 14.44%] | $24.75 | 6 (7 unfilled) | -17.55% [-65.37%, 27.10%] | $45.83 |
| map | 2026-05 | 452 | 0.647192 | 0.634171 | 0.636432 | -2.81% (295), $18.68 | 2.53% (131), $110.80 | 97 (198 unfilled) | -6.30% [-25.52%, 13.46%] | $27.58 | 53 (78 unfilled) | -2.73% [-26.94%, 20.11%] | $54.39 |
| map | 2026-06 | 414 | 0.657774 | 0.647814 | 0.650163 | -0.70% (272), $38.46 | 6.94% (132), $60.86 | 50 (222 unfilled) | 8.73% [-17.74%, 33.93%] | $61.43 | 26 (106 unfilled) | 1.55% [-28.90%, 27.17%] | $49.38 |
| map | 2026-07 | 618 | 0.693682 | 0.658848 | 0.647047 | -18.21% (413), $0.05 | -15.61% (165), $17.46 | 97 (316 unfilled) | -16.40% [-36.75%, 4.00%] | $17.04 | 36 (129 unfilled) | -9.42% [-33.25%, 12.07%] | $40.97 |
| map | 2026-08 | 873 | 0.637753 | 0.621006 | 0.623251 | -3.01% (645), $13.04 | 18.32% (26), $60.67 | 122 (523 unfilled) | -6.93% [-25.31%, 11.31%] | $18.26 | 5 (21 unfilled) | 5.33% [-48.86%, 37.07%] | $50.85 |
| map | 2026-09 | 879 | 0.669080 | 0.632716 | 0.631507 | -12.26% (647), $0.06 | -4.94% (100), $35.33 | 241 (406 unfilled) | -20.49% [-35.94%, -4.43%] | $2.83 | 40 (60 unfilled) | -4.89% [-28.10%, 18.22%] | $46.77 |
| map | 2026-10 | 659 | 0.651862 | 0.626541 | 0.628124 | -5.75% (439), $2.10 | 9.66% (22), $51.45 | 173 (266 unfilled) | -19.82% [-33.76%, -5.77%] | $2.79 | 9 (13 unfilled) | -2.14% [-37.22%, 29.09%] | $50.69 |
| series | 2026-01 | 51 | 0.553145 | — | 0.602759 | 16.48% (43), $92.41 | — | 37 (6 unfilled) | 35.87% [-0.84%, 74.68%] | $99.58 | — | — | — |
| series | 2026-02 | 155 | 0.583441 | — | 0.565710 | -20.57% (111), $6.39 | — | 100 (11 unfilled) | -18.21% [-38.24%, 2.58%] | $9.94 | — | — | — |
| series | 2026-03 | 304 | 0.623567 | 0.596656 | 0.590480 | -14.70% (204), $0.88 | -0.71% (196), $23.74 | 159 (45 unfilled) | -8.13% [-24.78%, 9.10%] | $4.44 | 147 (49 unfilled) | 1.17% [-11.30%, 14.26%] | $54.50 |
| series | 2026-04 | 322 | 0.590015 | 0.572611 | 0.580957 | 2.21% (239), $19.44 | 7.88% (184), $64.01 | 184 (55 unfilled) | -0.97% [-18.37%, 18.03%] | $13.52 | 143 (41 unfilled) | 8.63% [-6.23%, 26.38%] | $44.10 |
| series | 2026-05 | 360 | 0.614746 | 0.584865 | 0.584764 | -17.31% (252), $0.71 | -2.65% (186), $55.88 | 200 (52 unfilled) | -20.60% [-35.49%, -4.49%] | $1.31 | 150 (36 unfilled) | -1.65% [-14.48%, 11.20%] | $65.39 |
| series | 2026-06 | 348 | 0.648179 | 0.637442 | 0.633931 | 0.30% (255), $19.11 | 2.51% (170), $25.93 | 164 (91 unfilled) | 14.70% [-4.41%, 34.93%] | $193.38 | 111 (59 unfilled) | 7.70% [-7.19%, 23.51%] | $33.43 |
| series | 2026-07 | 513 | 0.655255 | 0.620106 | 0.614447 | -16.01% (371), $0.06 | -4.83% (193), $23.72 | 226 (145 unfilled) | -15.35% [-32.07%, 4.87%] | $0.40 | 118 (75 unfilled) | -0.32% [-22.16%, 29.63%] | $40.87 |
| series | 2026-08 | 717 | 0.617572 | 0.608383 | 0.614837 | 2.30% (556), $3.47 | 10.03% (179), $124.28 | 277 (279 unfilled) | 1.55% [-13.84%, 18.80%] | $19.98 | 92 (87 unfilled) | 18.11% [3.47%, 32.49%] | $103.14 |
| series | 2026-09 | 914 | 0.634290 | 0.602148 | 0.602664 | -5.78% (690), $0.03 | 1.44% (311), $33.75 | 389 (301 unfilled) | -5.59% [-17.54%, 5.85%] | $0.02 | 187 (124 unfilled) | 7.36% [-3.77%, 19.28%] | $56.68 |
| series | 2026-10 | 772 | 0.597628 | 0.579842 | 0.585736 | -4.92% (556), $0.07 | 8.84% (219), $95.14 | 349 (207 unfilled) | -4.63% [-16.79%, 7.71%] | $3.60 | 135 (84 unfilled) | 4.68% [-8.53%, 17.31%] | $62.09 |

### player_round_glicko: Kalshi comparison and returns



#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 4456 | 0.600306 | 0.600358 | -0.000053 [-0.008150, 0.007996] | no |
| series | tier1 | 725 | 0.634196 | 0.616830 | 0.017366 [-0.000104, 0.034578] | no |
| series | tier2 | 1962 | 0.597202 | 0.590722 | 0.006480 [-0.003845, 0.017065] | no |
| series | tier3 | 1727 | 0.592254 | 0.607536 | -0.015282 [-0.029514, -0.000721] | yes |
| series | unknown | 42 | 0.491357 | 0.471027 | 0.020329 [-0.038591, 0.078661] | no |
| series | international=1 | 448 | 0.607693 | 0.591446 | 0.016248 [-0.006945, 0.037620] | no |
| series | international=0 | 4008 | 0.599480 | 0.601354 | -0.001875 [-0.010319, 0.006261] | no |
| map | all | 4477 | 0.641027 | 0.634789 | 0.006237 [0.000224, 0.012190] | yes |
| map | tier1 | 1176 | 0.657301 | 0.646419 | 0.010882 [-0.001220, 0.022426] | no |
| map | tier2 | 1968 | 0.637418 | 0.631291 | 0.006126 [-0.002066, 0.014388] | no |
| map | tier3 | 1279 | 0.634187 | 0.632601 | 0.001586 [-0.011520, 0.014496] | no |
| map | unknown | 54 | 0.580145 | 0.560856 | 0.019289 [-0.012097, 0.053023] | no |
| map | international=1 | 788 | 0.636734 | 0.630059 | 0.006675 [-0.007771, 0.020655] | no |
| map | international=0 | 3689 | 0.641944 | 0.635800 | 0.006144 [-0.000259, 0.012618] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 3316 | 3311 | 0.0819 | 2.00% [-2.29%, 6.57%] | $0.03 | 0.001× | 99.97% | $9.61 | 2108 (1208 unfilled) | 0.02% [-5.35%, 5.35%] | $0.09 |
| series | tier1 | 536 | 536 | 0.0780 | 0.03% [-11.36%, 12.19%] | $0.10 | 0.002× | 99.92% | $12.56 | 432 (104 unfilled) | -4.05% [-15.88%, 8.62%] | $0.09 |
| series | tier2 | 1406 | 1403 | 0.0716 | -2.58% [-9.12%, 3.98%] | $0.08 | 0.002× | 99.95% | $16.00 | 884 (522 unfilled) | -3.44% [-10.86%, 4.95%] | $0.05 |
| series | tier3 | 1341 | 1339 | 0.0945 | 8.13% [1.35%, 15.21%] | $5297.53 | 105.951× | 86.78% | $249.12 | 769 (572 unfilled) | 6.65% [-2.33%, 15.58%] | $105.61 |
| series | unknown | 33 | 33 | 0.0729 | -19.63% [-49.59%, 13.36%] | $32.55 | 0.651× | 38.66% | $5.10 | 23 (10 unfilled) | -11.86% [-49.11%, 31.13%] | $37.63 |
| series | international=1 | 338 | 338 | 0.0790 | 0.67% [-15.46%, 17.32%] | $0.72 | 0.014× | 99.50% | $11.49 | 290 (48 unfilled) | -5.45% [-20.57%, 10.36%] | $0.51 |
| series | international=0 | 2978 | 2973 | 0.0822 | 2.15% [-2.29%, 6.54%] | $0.08 | 0.002× | 99.87% | $6.32 | 1818 (1160 unfilled) | 0.89% [-4.89%, 6.71%] | $0.08 |
| map | all | 2876 | 1825 | 0.0593 | -5.59% [-10.02%, -1.07%] | $0.09 | 0.002× | 99.98% | $36.65 | 834 (2042 unfilled) | -13.93% [-21.51%, -6.28%] | $0.09 |
| map | tier1 | 754 | 513 | 0.0603 | -4.58% [-13.26%, 4.66%] | $4.14 | 0.083× | 95.75% | $8.27 | 227 (527 unfilled) | -5.50% [-21.78%, 12.10%] | $11.73 |
| map | tier2 | 1239 | 769 | 0.0528 | -5.94% [-12.33%, 0.75%] | $0.10 | 0.002× | 99.93% | $13.37 | 356 (883 unfilled) | -16.59% [-26.63%, -5.97%] | $0.32 |
| map | tier3 | 851 | 521 | 0.0686 | -5.68% [-13.50%, 2.34%] | $5.59 | 0.112× | 98.41% | $19.13 | 239 (612 unfilled) | -17.99% [-32.50%, -3.35%] | $6.00 |
| map | unknown | 32 | 22 | 0.0441 | -14.08% [-42.90%, 15.39%] | $37.95 | 0.759× | 26.08% | $4.78 | 12 (20 unfilled) | -13.86% [-51.82%, 16.78%] | $46.29 |
| map | international=1 | 500 | 344 | 0.0636 | -4.27% [-15.95%, 7.45%] | $30.11 | 0.602× | 88.18% | $24.78 | 157 (343 unfilled) | -4.70% [-25.35%, 17.56%] | $35.04 |
| map | international=0 | 2376 | 1481 | 0.0585 | -5.88% [-10.57%, -1.18%] | $0.08 | 0.002× | 99.92% | $9.48 | 677 (1699 unfilled) | -16.08% [-23.60%, -8.43%] | $0.10 |
| series+map | all | 6192 | 3642 | 0.0714 | -1.53% [-5.10%, 2.10%] | $0.07 | 0.001× | 99.92% | $6.83 | 2942 (3250 unfilled) | -3.93% [-8.69%, 1.06%] | $0.09 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2026-01-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 371 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-01 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-01 | map | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 51 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | map | 63 | 1.000000 | 0.000000 | unfitted |
| 2026-03 | series | 206 | 1.453867 | 0.659498 | fitted |
| 2026-03 | map | 165 | 1.268993 | 0.229978 | fitted |
| 2026-04 | series | 510 | 1.467817 | 0.856730 | fitted |
| 2026-04 | map | 309 | 1.196905 | 0.201954 | fitted |
| 2026-05 | series | 832 | 1.407610 | 0.781346 | fitted |
| 2026-05 | map | 582 | 1.336306 | 0.806289 | fitted |
| 2026-06 | series | 1192 | 1.399653 | 0.688576 | fitted |
| 2026-06 | map | 1034 | 1.356820 | 0.730843 | fitted |
| 2026-07 | series | 1540 | 1.309316 | 0.674754 | fitted |
| 2026-07 | map | 1448 | 1.301925 | 0.709868 | fitted |
| 2026-08 | series | 2053 | 1.244676 | 0.565525 | fitted |
| 2026-08 | map | 2066 | 1.164405 | 0.515103 | fitted |
| 2026-09 | series | 2770 | 1.237907 | 0.610315 | fitted |
| 2026-09 | map | 2939 | 1.224941 | 0.581191 | fitted |
| 2026-10 | series | 3684 | 1.241803 | 0.635053 | fitted |
| 2026-10 | map | 3818 | 1.204383 | 0.481869 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 4250 | 0.590082 | 0.601593 | -0.011511 [-0.016603, -0.006458] | yes |
| series | tier1 | 614 | 0.620491 | 0.616540 | 0.003951 [-0.006460, 0.014324] | no |
| series | tier2 | 1873 | 0.584326 | 0.593752 | -0.009426 [-0.016237, -0.002622] | yes |
| series | tier3 | 1721 | 0.588975 | 0.607981 | -0.019005 [-0.028643, -0.009594] | yes |
| series | unknown | 42 | 0.447581 | 0.471027 | -0.023446 [-0.054151, 0.009416] | no |
| series | international=1 | 370 | 0.588395 | 0.589385 | -0.000990 [-0.013239, 0.012145] | no |
| series | international=0 | 3880 | 0.590243 | 0.602757 | -0.012514 [-0.017887, -0.007064] | yes |
| map | all | 4312 | 0.632876 | 0.635269 | -0.002393 [-0.005975, 0.001192] | no |
| map | tier1 | 1046 | 0.653502 | 0.649504 | 0.003998 [-0.002805, 0.010258] | no |
| map | tier2 | 1936 | 0.626311 | 0.631140 | -0.004830 [-0.009495, -0.000002] | yes |
| map | tier3 | 1276 | 0.629480 | 0.633014 | -0.003534 [-0.011344, 0.005077] | no |
| map | unknown | 54 | 0.548987 | 0.560856 | -0.011869 [-0.031342, 0.007291] | no |
| map | international=1 | 686 | 0.627847 | 0.629473 | -0.001626 [-0.008455, 0.005624] | no |
| map | international=0 | 3626 | 0.633828 | 0.636366 | -0.002538 [-0.006614, 0.001553] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 2515 | 2511 | 0.0477 | 7.71% [3.75%, 11.73%] | $9760.38 | 195.208× | 85.42% | $249.12 | 1572 (943 unfilled) | 5.18% [0.28%, 10.52%] | $709.30 |
| series | tier1 | 314 | 314 | 0.0363 | -1.69% [-14.05%, 10.65%] | $10.23 | 0.205× | 90.45% | $6.60 | 243 (71 unfilled) | -2.20% [-15.81%, 11.31%] | $22.91 |
| series | tier2 | 1096 | 1095 | 0.0424 | 5.49% [0.06%, 10.76%] | $3909.68 | 78.194× | 62.73% | $249.12 | 669 (427 unfilled) | 2.09% [-4.58%, 9.13%] | $126.07 |
| series | tier3 | 1075 | 1072 | 0.0567 | 12.95% [6.77%, 19.89%] | $11775.79 | 235.516× | 60.73% | $249.12 | 639 (436 unfilled) | 11.46% [2.51%, 20.53%] | $1103.77 |
| series | unknown | 30 | 30 | 0.0392 | -0.48% [-26.76%, 26.08%] | $67.23 | 1.345× | 9.34% | $6.33 | 21 (9 unfilled) | -1.48% [-35.68%, 33.44%] | $57.73 |
| series | international=1 | 188 | 188 | 0.0336 | 2.54% [-14.22%, 20.28%] | $78.92 | 1.578× | 46.01% | $10.83 | 152 (36 unfilled) | 2.17% [-16.14%, 21.90%] | $82.69 |
| series | international=0 | 2327 | 2323 | 0.0488 | 8.13% [3.96%, 12.27%] | $10938.88 | 218.778× | 85.13% | $249.12 | 1420 (907 unfilled) | 5.51% [0.44%, 10.73%] | $594.35 |
| map | all | 1762 | 1092 | 0.0332 | 1.90% [-2.67%, 6.57%] | $283.51 | 5.670× | 79.13% | $41.89 | 510 (1252 unfilled) | -6.48% [-14.87%, 2.23%] | $16.17 |
| map | tier1 | 338 | 218 | 0.0312 | -3.85% [-15.75%, 8.80%] | $22.13 | 0.443× | 80.17% | $7.36 | 108 (230 unfilled) | -6.89% [-29.23%, 18.93%] | $46.98 |
| map | tier2 | 780 | 479 | 0.0288 | 2.29% [-4.74%, 9.55%] | $186.10 | 3.722× | 49.25% | $28.47 | 211 (569 unfilled) | -9.64% [-20.07%, 0.95%] | $20.14 |
| map | tier3 | 624 | 382 | 0.0400 | 4.12% [-3.73%, 11.78%] | $201.42 | 4.028× | 65.83% | $30.09 | 182 (442 unfilled) | -3.99% [-17.51%, 9.51%] | $37.91 |
| map | unknown | 20 | 13 | 0.0262 | 15.16% [-9.30%, 40.33%] | $52.68 | 1.054× | 3.66% | $4.86 | 9 (11 unfilled) | 22.60% [-1.92%, 51.23%] | $54.59 |
| map | international=1 | 223 | 144 | 0.0311 | 4.09% [-11.38%, 20.02%] | $81.47 | 1.629× | 35.84% | $8.39 | 79 (144 unfilled) | 5.06% [-24.53%, 35.46%] | $74.98 |
| map | international=0 | 1539 | 948 | 0.0335 | 1.58% [-3.41%, 6.52%] | $193.06 | 3.861× | 77.51% | $25.05 | 431 (1108 unfilled) | -8.60% [-16.96%, 0.11%] | $10.49 |
| series+map | all | 4277 | 2639 | 0.0417 | 5.32% [1.79%, 8.74%] | $11937.46 | 238.749× | 63.99% | $249.30 | 2082 (2195 unfilled) | 2.33% [-2.39%, 7.03%] | $455.75 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-01 | 63 | 0.634559 | — | 0.638920 | 0.71% (42), $58.19 | — | 5 (37 unfilled) | 11.19% [-66.65%, 89.92%] | $50.98 | — | — | — |
| map | 2026-02 | 102 | 0.642663 | — | 0.611955 | -16.79% (59), $28.27 | — | 18 (41 unfilled) | -48.65% [-83.20%, -10.86%] | $28.60 | — | — | — |
| map | 2026-03 | 144 | 0.656733 | 0.643151 | 0.642845 | -2.78% (81), $47.71 | 12.33% (35), $59.80 | 42 (39 unfilled) | 0.10% [-37.81%, 38.93%] | $45.27 | 15 (20 unfilled) | -0.93% [-36.71%, 24.55%] | $49.44 |
| map | 2026-04 | 273 | 0.624606 | 0.639455 | 0.647894 | 15.90% (166), $252.50 | 35.18% (30), $60.87 | 50 (116 unfilled) | -12.03% [-40.47%, 16.39%] | $30.51 | 9 (21 unfilled) | -27.47% [-80.10%, 8.21%] | $48.34 |
| map | 2026-05 | 452 | 0.643603 | 0.631681 | 0.636432 | -4.81% (280), $31.69 | 6.20% (233), $85.20 | 89 (191 unfilled) | -5.28% [-28.73%, 18.47%] | $30.96 | 89 (144 unfilled) | 1.24% [-19.67%, 20.24%] | $45.53 |
| map | 2026-06 | 414 | 0.643189 | 0.642528 | 0.650163 | 2.08% (246), $80.80 | 4.92% (224), $93.53 | 50 (196 unfilled) | 9.65% [-19.31%, 37.75%] | $61.24 | 46 (178 unfilled) | 3.70% [-23.08%, 31.01%] | $58.17 |
| map | 2026-07 | 618 | 0.658813 | 0.654574 | 0.647047 | -6.68% (396), $6.44 | -5.20% (344), $13.47 | 98 (298 unfilled) | -11.37% [-32.50%, 10.74%] | $28.69 | 75 (269 unfilled) | -7.66% [-26.37%, 12.02%] | $41.40 |
| map | 2026-08 | 873 | 0.620008 | 0.613011 | 0.623251 | -3.47% (604), $6.23 | 8.16% (339), $320.01 | 112 (492 unfilled) | -8.75% [-30.61%, 13.49%] | $33.57 | 69 (270 unfilled) | 0.56% [-22.95%, 25.56%] | $45.16 |
| map | 2026-09 | 879 | 0.648612 | 0.634161 | 0.631507 | -11.74% (605), $0.05 | -5.41% (360), $34.89 | 224 (381 unfilled) | -18.80% [-34.50%, -2.35%] | $2.83 | 143 (217 unfilled) | -9.49% [-26.14%, 10.13%] | $47.32 |
| map | 2026-10 | 659 | 0.642685 | 0.626917 | 0.628124 | -12.25% (397), $0.29 | 1.45% (197), $44.75 | 146 (251 unfilled) | -26.71% [-42.77%, -10.35%] | $3.85 | 64 (133 unfilled) | -22.33% [-42.80%, -1.12%] | $23.69 |
| series | 2026-01 | 51 | 0.581275 | — | 0.602759 | 25.16% (37), $78.76 | — | 31 (6 unfilled) | 38.44% [-8.42%, 87.10%] | $85.01 | — | — | — |
| series | 2026-02 | 155 | 0.584314 | — | 0.565710 | -14.52% (116), $11.90 | — | 104 (12 unfilled) | -15.93% [-35.06%, 3.62%] | $11.80 | — | — | — |
| series | 2026-03 | 304 | 0.583521 | 0.571284 | 0.590480 | -0.71% (225), $33.67 | 11.03% (198), $274.34 | 172 (53 unfilled) | -1.55% [-18.67%, 15.86%] | $52.07 | 148 (50 unfilled) | 6.83% [-5.78%, 19.59%] | $140.60 |
| series | 2026-04 | 322 | 0.584297 | 0.568843 | 0.580957 | -0.07% (240), $12.89 | 7.45% (222), $155.01 | 180 (60 unfilled) | 2.24% [-15.82%, 24.04%] | $37.33 | 162 (60 unfilled) | 12.32% [-3.24%, 28.96%] | $177.09 |
| series | 2026-05 | 360 | 0.603914 | 0.580706 | 0.584764 | -7.39% (261), $2.19 | 0.31% (236), $45.12 | 213 (48 unfilled) | -8.17% [-24.62%, 7.54%] | $2.37 | 185 (51 unfilled) | -1.03% [-13.90%, 12.66%] | $39.59 |
| series | 2026-06 | 348 | 0.619820 | 0.625813 | 0.633931 | 7.32% (248), $193.65 | 7.63% (213), $72.62 | 164 (84 unfilled) | 15.94% [-2.69%, 35.25%] | $420.27 | 140 (73 unfilled) | 7.37% [-6.87%, 21.50%] | $71.51 |
| series | 2026-07 | 513 | 0.627545 | 0.614287 | 0.614447 | 2.06% (386), $0.93 | -1.23% (324), $16.46 | 244 (142 unfilled) | -0.58% [-17.28%, 17.91%] | $19.46 | 198 (126 unfilled) | -3.72% [-19.73%, 15.79%] | $13.23 |
| series | 2026-08 | 717 | 0.604422 | 0.596721 | 0.614837 | 5.93% (562), $32.26 | 12.12% (422), $620.18 | 273 (289 unfilled) | -0.10% [-15.53%, 16.22%] | $21.97 | 206 (216 unfilled) | 15.41% [-1.68%, 33.83%] | $325.04 |
| series | 2026-09 | 914 | 0.596996 | 0.586579 | 0.602664 | 1.57% (690), $10.25 | 12.98% (496), $1432.83 | 386 (304 unfilled) | -4.55% [-16.27%, 7.01%] | $0.81 | 286 (210 unfilled) | 4.14% [-8.04%, 15.83%] | $127.29 |
| series | 2026-10 | 772 | 0.589575 | 0.576507 | 0.585736 | 4.47% (551), $2.94 | 6.67% (404), $137.57 | 341 (210 unfilled) | 4.13% [-8.10%, 17.57%] | $31.19 | 247 (157 unfilled) | 2.76% [-8.16%, 13.70%] | $83.39 |

### player_round_glicko_rookie_weights: Kalshi comparison and returns



#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 4456 | 0.594997 | 0.600358 | -0.005361 [-0.013206, 0.002268] | no |
| series | tier1 | 725 | 0.630703 | 0.616830 | 0.013872 [-0.002584, 0.029938] | no |
| series | tier2 | 1962 | 0.594171 | 0.590722 | 0.003449 [-0.006705, 0.013790] | no |
| series | tier3 | 1727 | 0.583516 | 0.607536 | -0.024020 [-0.038017, -0.010329] | yes |
| series | unknown | 42 | 0.489338 | 0.471027 | 0.018311 [-0.044404, 0.079300] | no |
| series | international=1 | 448 | 0.603206 | 0.591446 | 0.011760 [-0.009762, 0.031669] | no |
| series | international=0 | 4008 | 0.594079 | 0.601354 | -0.007275 [-0.015439, 0.000505] | no |
| map | all | 4477 | 0.639083 | 0.634789 | 0.004293 [-0.001658, 0.009869] | no |
| map | tier1 | 1176 | 0.655445 | 0.646419 | 0.009026 [-0.002478, 0.019755] | no |
| map | tier2 | 1968 | 0.635944 | 0.631291 | 0.004652 [-0.002996, 0.012632] | no |
| map | tier3 | 1279 | 0.631309 | 0.632601 | -0.001292 [-0.013629, 0.011091] | no |
| map | unknown | 54 | 0.581280 | 0.560856 | 0.020423 [-0.010986, 0.054196] | no |
| map | international=1 | 788 | 0.634694 | 0.630059 | 0.004635 [-0.009042, 0.017801] | no |
| map | international=0 | 3689 | 0.640020 | 0.635800 | 0.004220 [-0.001983, 0.010677] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 3270 | 3265 | 0.0825 | 2.73% [-1.63%, 6.92%] | $0.09 | 0.002× | 99.93% | $12.48 | 2077 (1193 unfilled) | -0.02% [-5.21%, 5.71%] | $0.08 |
| series | tier1 | 526 | 526 | 0.0732 | -2.28% [-14.01%, 9.69%] | $0.06 | 0.001× | 99.96% | $16.35 | 426 (100 unfilled) | -4.94% [-17.42%, 7.81%] | $0.36 |
| series | tier2 | 1374 | 1371 | 0.0728 | -1.48% [-7.89%, 4.92%] | $0.02 | 0.000× | 99.99% | $17.25 | 863 (511 unfilled) | -3.72% [-11.00%, 4.24%] | $0.09 |
| series | tier3 | 1337 | 1335 | 0.0964 | 9.52% [2.35%, 16.57%] | $10973.44 | 219.469× | 80.48% | $249.12 | 766 (571 unfilled) | 7.28% [-1.08%, 16.74%] | $316.90 |
| series | unknown | 33 | 33 | 0.0763 | -16.71% [-48.28%, 16.01%] | $41.47 | 0.829× | 32.38% | $5.89 | 22 (11 unfilled) | -13.08% [-54.22%, 30.96%] | $42.04 |
| series | international=1 | 320 | 320 | 0.0746 | -3.38% [-17.98%, 12.76%] | $2.25 | 0.045× | 99.04% | $13.41 | 275 (45 unfilled) | -7.77% [-22.86%, 7.68%] | $1.03 |
| series | international=0 | 2950 | 2945 | 0.0834 | 3.39% [-1.08%, 8.14%] | $0.04 | 0.001× | 99.94% | $5.92 | 1802 (1148 unfilled) | 1.17% [-4.44%, 6.78%] | $21.68 |
| map | all | 2828 | 1810 | 0.0575 | -4.83% [-9.47%, -0.22%] | $0.09 | 0.002× | 99.98% | $46.16 | 821 (2007 unfilled) | -17.08% [-25.31%, -9.25%] | $0.09 |
| map | tier1 | 745 | 510 | 0.0562 | -4.51% [-13.36%, 4.52%] | $4.70 | 0.094× | 95.55% | $9.25 | 225 (520 unfilled) | -8.48% [-24.83%, 9.10%] | $10.26 |
| map | tier2 | 1210 | 759 | 0.0520 | -4.42% [-10.92%, 2.24%] | $0.08 | 0.002× | 99.95% | $14.99 | 345 (865 unfilled) | -18.63% [-28.71%, -7.80%] | $0.28 |
| map | tier3 | 843 | 520 | 0.0667 | -5.29% [-13.05%, 2.37%] | $2.18 | 0.044× | 99.28% | $16.07 | 240 (603 unfilled) | -22.93% [-36.55%, -8.98%] | $2.32 |
| map | unknown | 30 | 21 | 0.0475 | -16.90% [-48.08%, 13.49%] | $36.25 | 0.725× | 31.58% | $4.78 | 11 (19 unfilled) | -16.99% [-56.80%, 17.05%] | $46.36 |
| map | international=1 | 507 | 347 | 0.0575 | -2.93% [-14.78%, 8.76%] | $40.55 | 0.811× | 85.54% | $26.91 | 160 (347 unfilled) | -6.35% [-27.22%, 14.91%] | $32.62 |
| map | international=0 | 2321 | 1463 | 0.0575 | -5.25% [-9.93%, -0.34%] | $0.09 | 0.002× | 99.92% | $11.90 | 661 (1660 unfilled) | -19.69% [-27.21%, -11.83%] | $0.10 |
| series+map | all | 6098 | 3584 | 0.0709 | -0.78% [-4.50%, 2.69%] | $0.05 | 0.001× | 99.97% | $15.97 | 2898 (3200 unfilled) | -4.85% [-9.52%, -0.06%] | $0.03 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2026-01-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 371 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-01 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-01 | map | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 51 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | map | 63 | 1.000000 | 0.000000 | unfitted |
| 2026-03 | series | 206 | 1.429141 | 0.713157 | fitted |
| 2026-03 | map | 165 | 1.243703 | 0.156871 | fitted |
| 2026-04 | series | 510 | 1.427210 | 0.840946 | fitted |
| 2026-04 | map | 309 | 1.195945 | 0.207217 | fitted |
| 2026-05 | series | 832 | 1.380243 | 0.793125 | fitted |
| 2026-05 | map | 582 | 1.324317 | 0.791176 | fitted |
| 2026-06 | series | 1192 | 1.378099 | 0.701722 | fitted |
| 2026-06 | map | 1034 | 1.356969 | 0.749742 | fitted |
| 2026-07 | series | 1540 | 1.298813 | 0.717070 | fitted |
| 2026-07 | map | 1448 | 1.315498 | 0.755874 | fitted |
| 2026-08 | series | 2053 | 1.240421 | 0.626065 | fitted |
| 2026-08 | map | 2066 | 1.179960 | 0.575474 | fitted |
| 2026-09 | series | 2770 | 1.236628 | 0.661569 | fitted |
| 2026-09 | map | 2939 | 1.244118 | 0.635687 | fitted |
| 2026-10 | series | 3684 | 1.235600 | 0.686911 | fitted |
| 2026-10 | map | 3818 | 1.217517 | 0.529179 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 4250 | 0.587012 | 0.601593 | -0.014581 [-0.020078, -0.009170] | yes |
| series | tier1 | 614 | 0.621026 | 0.616540 | 0.004486 [-0.006341, 0.015635] | no |
| series | tier2 | 1873 | 0.583196 | 0.593752 | -0.010556 [-0.017792, -0.003460] | yes |
| series | tier3 | 1721 | 0.582443 | 0.607981 | -0.025537 [-0.035688, -0.015440] | yes |
| series | unknown | 42 | 0.447165 | 0.471027 | -0.023863 [-0.056523, 0.010582] | no |
| series | international=1 | 370 | 0.589094 | 0.589385 | -0.000291 [-0.013554, 0.013705] | no |
| series | international=0 | 3880 | 0.586814 | 0.602757 | -0.015944 [-0.021791, -0.010169] | yes |
| map | all | 4312 | 0.632059 | 0.635269 | -0.003210 [-0.006854, 0.000459] | no |
| map | tier1 | 1046 | 0.654007 | 0.649504 | 0.004502 [-0.002295, 0.011013] | no |
| map | tier2 | 1936 | 0.625447 | 0.631140 | -0.005693 [-0.010448, -0.000835] | yes |
| map | tier3 | 1276 | 0.627602 | 0.633014 | -0.005412 [-0.013322, 0.002855] | no |
| map | unknown | 54 | 0.549293 | 0.560856 | -0.011564 [-0.032919, 0.009334] | no |
| map | international=1 | 686 | 0.627673 | 0.629473 | -0.001800 [-0.008701, 0.005680] | no |
| map | international=0 | 3626 | 0.632889 | 0.636366 | -0.003477 [-0.007571, 0.000746] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 2647 | 2643 | 0.0515 | 8.41% [4.43%, 12.34%] | $13532.46 | 270.649× | 62.37% | $249.12 | 1648 (999 unfilled) | 5.32% [0.45%, 10.45%] | $769.27 |
| series | tier1 | 337 | 337 | 0.0371 | -4.53% [-15.72%, 6.41%] | $11.06 | 0.221× | 92.26% | $8.98 | 261 (76 unfilled) | -4.80% [-17.06%, 7.91%] | $25.10 |
| series | tier2 | 1129 | 1128 | 0.0456 | 5.27% [-0.43%, 10.95%] | $5491.01 | 109.820× | 60.61% | $249.47 | 692 (437 unfilled) | 2.11% [-4.51%, 8.87%] | $75.31 |
| series | tier3 | 1153 | 1150 | 0.0616 | 15.42% [9.09%, 21.76%] | $12442.14 | 248.843× | 69.84% | $249.12 | 677 (476 unfilled) | 12.67% [5.16%, 21.30%] | $1396.11 |
| series | unknown | 28 | 28 | 0.0486 | 2.60% [-24.44%, 29.48%] | $64.58 | 1.292× | 12.16% | $6.45 | 18 (10 unfilled) | -0.20% [-37.94%, 38.62%] | $55.37 |
| series | international=1 | 200 | 200 | 0.0345 | -3.91% [-18.57%, 11.64%] | $67.05 | 1.341× | 52.52% | $9.67 | 165 (35 unfilled) | -5.27% [-21.04%, 10.98%] | $91.56 |
| series | international=0 | 2447 | 2443 | 0.0529 | 9.42% [5.55%, 13.42%] | $13655.86 | 273.117× | 86.84% | $249.12 | 1483 (964 unfilled) | 6.51% [1.40%, 11.63%] | $553.74 |
| map | all | 1832 | 1150 | 0.0338 | 4.36% [-0.67%, 9.49%] | $667.99 | 13.360× | 78.89% | $136.80 | 519 (1313 unfilled) | -6.80% [-14.57%, 1.80%] | $13.69 |
| map | tier1 | 363 | 245 | 0.0298 | -1.32% [-13.08%, 11.77%] | $16.85 | 0.337× | 80.44% | $6.62 | 111 (252 unfilled) | -8.00% [-26.97%, 11.89%] | $33.96 |
| map | tier2 | 798 | 492 | 0.0294 | 3.64% [-3.25%, 10.29%] | $169.23 | 3.385× | 54.44% | $31.74 | 214 (584 unfilled) | -9.02% [-21.01%, 2.11%] | $23.44 |
| map | tier3 | 651 | 400 | 0.0415 | 8.10% [0.54%, 15.94%] | $546.85 | 10.937× | 64.49% | $60.34 | 185 (466 unfilled) | -4.93% [-18.33%, 9.31%] | $33.44 |
| map | unknown | 20 | 13 | 0.0297 | 15.16% [-9.30%, 40.33%] | $56.10 | 1.122× | 6.81% | $4.97 | 9 (11 unfilled) | 22.60% [-1.92%, 51.23%] | $57.13 |
| map | international=1 | 244 | 168 | 0.0284 | 7.82% [-7.43%, 24.55%] | $68.83 | 1.377× | 47.22% | $8.40 | 83 (161 unfilled) | 2.32% [-21.80%, 27.89%] | $54.81 |
| map | international=0 | 1588 | 982 | 0.0346 | 3.83% [-1.12%, 8.84%] | $503.58 | 10.072× | 76.22% | $67.50 | 436 (1152 unfilled) | -8.54% [-16.89%, -0.29%] | $12.13 |
| series+map | all | 4479 | 2770 | 0.0443 | 6.75% [3.51%, 10.30%] | $19834.28 | 396.686× | 42.30% | $249.47 | 2167 (2312 unfilled) | 2.42% [-1.91%, 6.89%] | $402.54 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-01 | 63 | 0.631801 | — | 0.638920 | 14.89% (42), $68.21 | — | 4 (38 unfilled) | -3.09% [-100.00%, 95.23%] | $50.62 | — | — | — |
| map | 2026-02 | 102 | 0.644367 | — | 0.611955 | -26.74% (58), $25.11 | — | 21 (37 unfilled) | -69.47% [-100.00%, -34.77%] | $25.70 | — | — | — |
| map | 2026-03 | 144 | 0.653556 | 0.642727 | 0.642845 | 1.84% (79), $40.38 | 10.13% (28), $53.89 | 40 (39 unfilled) | 14.05% [-26.54%, 58.60%] | $51.95 | 14 (14 unfilled) | -4.23% [-39.90%, 22.32%] | $49.44 |
| map | 2026-04 | 273 | 0.623220 | 0.638026 | 0.647894 | 16.45% (161), $285.53 | 73.35% (32), $89.96 | 50 (111 unfilled) | -15.69% [-43.59%, 13.75%] | $33.86 | 10 (22 unfilled) | -20.41% [-65.20%, 20.35%] | $47.06 |
| map | 2026-05 | 452 | 0.640346 | 0.629637 | 0.636432 | -2.35% (277), $48.46 | 4.17% (231), $107.51 | 94 (183 unfilled) | -4.58% [-28.26%, 18.24%] | $30.28 | 90 (141 unfilled) | -4.26% [-24.61%, 15.33%] | $49.97 |
| map | 2026-06 | 414 | 0.641458 | 0.641087 | 0.650163 | 3.91% (236), $98.54 | 9.56% (215), $113.91 | 49 (187 unfilled) | -2.94% [-31.03%, 30.60%] | $44.36 | 46 (169 unfilled) | 4.40% [-21.35%, 31.35%] | $55.28 |
| map | 2026-07 | 618 | 0.655439 | 0.653475 | 0.647047 | -7.02% (381), $6.57 | -4.52% (347), $16.55 | 86 (295 unfilled) | -9.88% [-31.96%, 13.31%] | $29.45 | 72 (275 unfilled) | -2.33% [-22.60%, 16.21%] | $46.67 |
| map | 2026-08 | 873 | 0.619331 | 0.611896 | 0.623251 | -2.00% (592), $13.90 | 12.02% (388), $306.43 | 116 (476 unfilled) | -8.38% [-28.83%, 13.12%] | $34.38 | 76 (312 unfilled) | 7.81% [-15.64%, 32.66%] | $58.92 |
| map | 2026-09 | 879 | 0.647004 | 0.634692 | 0.631507 | -12.49% (593), $0.07 | -4.76% (379), $25.74 | 207 (386 unfilled) | -26.22% [-42.19%, -10.54%] | $0.66 | 141 (238 unfilled) | -16.86% [-31.68%, -1.14%] | $23.97 |
| map | 2026-10 | 659 | 0.640272 | 0.626361 | 0.628124 | -11.12% (409), $0.42 | 4.96% (212), $51.17 | 154 (255 unfilled) | -29.23% [-44.53%, -13.84%] | $2.58 | 70 (142 unfilled) | -16.21% [-35.48%, 2.96%] | $24.07 |
| series | 2026-01 | 51 | 0.572357 | — | 0.602759 | 22.55% (38), $106.74 | — | 34 (4 unfilled) | 37.27% [-7.13%, 85.27%] | $107.08 | — | — | — |
| series | 2026-02 | 155 | 0.578866 | — | 0.565710 | -13.90% (116), $11.46 | — | 104 (12 unfilled) | -17.00% [-36.36%, 2.19%] | $11.66 | — | — | — |
| series | 2026-03 | 304 | 0.583253 | 0.571458 | 0.590480 | 2.90% (224), $48.26 | 12.07% (197), $292.49 | 174 (50 unfilled) | 1.92% [-14.33%, 19.30%] | $54.45 | 147 (50 unfilled) | 10.54% [-1.33%, 23.53%] | $142.50 |
| series | 2026-04 | 322 | 0.579510 | 0.566600 | 0.580957 | -0.75% (237), $29.17 | 6.76% (223), $127.38 | 170 (67 unfilled) | 4.36% [-14.84%, 26.03%] | $55.34 | 163 (60 unfilled) | 10.67% [-5.08%, 28.47%] | $121.40 |
| series | 2026-05 | 360 | 0.600817 | 0.579972 | 0.584764 | -7.06% (264), $4.36 | 0.94% (247), $68.36 | 213 (51 unfilled) | -9.56% [-24.92%, 5.83%] | $1.97 | 196 (51 unfilled) | -2.27% [-16.29%, 11.35%] | $44.11 |
| series | 2026-06 | 348 | 0.613647 | 0.621359 | 0.633931 | 8.80% (242), $251.80 | 9.18% (215), $133.82 | 157 (85 unfilled) | 18.61% [-1.02%, 38.91%] | $335.07 | 137 (78 unfilled) | 8.87% [-5.58%, 22.97%] | $83.68 |
| series | 2026-07 | 513 | 0.619201 | 0.609705 | 0.614447 | 2.31% (379), $1.37 | 0.73% (342), $19.57 | 241 (138 unfilled) | 1.22% [-15.12%, 20.49%] | $32.27 | 214 (128 unfilled) | -1.67% [-16.10%, 16.17%] | $12.99 |
| series | 2026-08 | 717 | 0.598945 | 0.591806 | 0.614837 | 6.82% (556), $81.61 | 11.63% (449), $638.21 | 272 (284 unfilled) | 2.38% [-12.87%, 18.77%] | $47.37 | 219 (230 unfilled) | 13.25% [-3.09%, 31.47%] | $328.44 |
| series | 2026-09 | 914 | 0.589270 | 0.582209 | 0.602664 | 5.56% (676), $40.70 | 14.89% (535), $2967.71 | 377 (299 unfilled) | -5.18% [-17.19%, 6.83%] | $5.78 | 305 (230 unfilled) | 3.61% [-6.48%, 14.26%] | $160.16 |
| series | 2026-10 | 772 | 0.586725 | 0.575606 | 0.585736 | 0.95% (538), $14.20 | 6.23% (439), $208.24 | 335 (203 unfilled) | -1.48% [-13.61%, 11.03%] | $36.47 | 267 (172 unfilled) | 4.02% [-6.76%, 13.82%] | $80.60 |

### team_elo+none: Kalshi comparison and returns

none

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 4456 | 0.620539 | 0.600358 | 0.020181 [0.012193, 0.027888] | yes |
| series | tier1 | 725 | 0.638064 | 0.616830 | 0.021234 [0.001915, 0.042106] | yes |
| series | tier2 | 1962 | 0.622792 | 0.590722 | 0.032070 [0.021227, 0.043410] | yes |
| series | tier3 | 1727 | 0.612961 | 0.607536 | 0.005425 [-0.008027, 0.018367] | no |
| series | unknown | 42 | 0.524418 | 0.471027 | 0.053390 [-0.019773, 0.132155] | no |
| series | international=1 | 448 | 0.599625 | 0.591446 | 0.008179 [-0.012963, 0.029675] | no |
| series | international=0 | 4008 | 0.622877 | 0.601354 | 0.021522 [0.013213, 0.029830] | yes |
| map | all | 4477 | 0.657933 | 0.634789 | 0.023144 [0.016028, 0.030213] | yes |
| map | tier1 | 1176 | 0.666677 | 0.646419 | 0.020258 [0.006107, 0.035503] | yes |
| map | tier2 | 1968 | 0.658913 | 0.631291 | 0.027622 [0.017419, 0.037958] | yes |
| map | tier3 | 1279 | 0.651000 | 0.632601 | 0.018399 [0.006219, 0.031922] | yes |
| map | unknown | 54 | 0.596005 | 0.560856 | 0.035149 [-0.014130, 0.080307] | no |
| map | international=1 | 788 | 0.629576 | 0.630059 | -0.000484 [-0.016658, 0.016022] | no |
| map | international=0 | 3689 | 0.663990 | 0.635800 | 0.028190 [0.020205, 0.036309] | yes |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 3277 | 3270 | 0.0855 | -6.01% [-10.54%, -1.78%] | $0.09 | 0.002× | 99.92% | $10.94 | 2085 (1192 unfilled) | -5.04% [-10.57%, 0.28%] | $0.07 |
| series | tier1 | 521 | 521 | 0.0784 | -9.16% [-19.73%, 1.80%] | $0.17 | 0.003× | 99.90% | $16.25 | 426 (95 unfilled) | -6.49% [-18.04%, 5.46%] | $3.08 |
| series | tier2 | 1418 | 1415 | 0.0820 | -11.38% [-17.57%, -4.76%] | $0.09 | 0.002× | 99.82% | $4.97 | 888 (530 unfilled) | -13.16% [-20.97%, -5.32%] | $0.10 |
| series | tier3 | 1307 | 1303 | 0.0918 | 1.70% [-5.11%, 9.11%] | $0.05 | 0.001× | 99.95% | $9.37 | 751 (556 unfilled) | 6.01% [-3.31%, 15.31%] | $19.30 |
| series | unknown | 31 | 31 | 0.0983 | -33.27% [-60.31%, -4.25%] | $20.59 | 0.412× | 62.49% | $5.25 | 20 (11 unfilled) | -28.92% [-65.84%, 12.03%] | $28.17 |
| series | international=1 | 319 | 319 | 0.0729 | -5.58% [-20.18%, 10.53%] | $9.48 | 0.190× | 96.24% | $8.24 | 277 (42 unfilled) | -7.06% [-20.99%, 6.88%] | $12.77 |
| series | international=0 | 2958 | 2951 | 0.0868 | -6.06% [-10.55%, -1.53%] | $0.10 | 0.002× | 99.89% | $8.72 | 1808 (1150 unfilled) | -4.73% [-10.38%, 0.95%] | $0.06 |
| map | all | 3086 | 1910 | 0.0715 | -6.49% [-10.49%, -2.60%] | $0.09 | 0.002× | 99.93% | $13.15 | 928 (2158 unfilled) | -13.47% [-20.50%, -6.16%] | $0.09 |
| map | tier1 | 791 | 519 | 0.0733 | -3.24% [-11.32%, 5.37%] | $4.62 | 0.092× | 96.66% | $4.70 | 256 (535 unfilled) | -5.00% [-18.40%, 9.52%] | $18.89 |
| map | tier2 | 1356 | 824 | 0.0699 | -8.25% [-14.12%, -2.50%] | $0.10 | 0.002× | 99.89% | $8.39 | 405 (951 unfilled) | -17.86% [-26.92%, -8.35%] | $0.07 |
| map | tier3 | 905 | 547 | 0.0718 | -5.77% [-13.07%, 1.86%] | $0.31 | 0.006× | 99.84% | $15.86 | 255 (650 unfilled) | -13.93% [-26.52%, -0.20%] | $4.72 |
| map | unknown | 34 | 20 | 0.0861 | -31.25% [-56.01%, -7.09%] | $28.26 | 0.565× | 43.48% | $4.78 | 12 (22 unfilled) | -36.23% [-75.72%, 1.05%] | $37.40 |
| map | international=1 | 524 | 350 | 0.0701 | 2.86% [-8.04%, 13.12%] | $83.84 | 1.677× | 74.81% | $8.59 | 178 (346 unfilled) | 5.16% [-12.13%, 22.84%] | $102.15 |
| map | international=0 | 2562 | 1560 | 0.0718 | -8.40% [-12.66%, -4.26%] | $0.09 | 0.002× | 99.89% | $7.68 | 750 (1812 unfilled) | -17.89% [-25.07%, -10.58%] | $0.09 |
| series+map | all | 6363 | 3679 | 0.0787 | -6.25% [-9.46%, -2.83%] | $0.08 | 0.002× | 99.88% | $6.33 | 3013 (3350 unfilled) | -7.63% [-12.36%, -2.91%] | $0.04 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2026-01-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 371 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-01 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-01 | map | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 51 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | map | 63 | 1.000000 | 0.000000 | unfitted |
| 2026-03 | series | 206 | 1.445963 | 0.701043 | fitted |
| 2026-03 | map | 165 | 1.203008 | -0.223533 | fitted |
| 2026-04 | series | 510 | 1.317039 | 0.381122 | fitted |
| 2026-04 | map | 309 | 1.143422 | -0.015436 | fitted |
| 2026-05 | series | 832 | 1.293329 | 0.451990 | fitted |
| 2026-05 | map | 582 | 1.082493 | 0.402515 | fitted |
| 2026-06 | series | 1192 | 1.283400 | 0.362163 | fitted |
| 2026-06 | map | 1034 | 1.131085 | 0.369016 | fitted |
| 2026-07 | series | 1540 | 1.206917 | 0.329427 | fitted |
| 2026-07 | map | 1448 | 1.118934 | 0.352859 | fitted |
| 2026-08 | series | 2053 | 1.152513 | 0.205875 | fitted |
| 2026-08 | map | 2066 | 1.057427 | 0.114644 | fitted |
| 2026-09 | series | 2770 | 1.168182 | 0.320251 | fitted |
| 2026-09 | map | 2939 | 1.115860 | 0.165299 | fitted |
| 2026-10 | series | 3684 | 1.153622 | 0.279948 | fitted |
| 2026-10 | map | 3818 | 1.114956 | 0.099319 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 4250 | 0.600111 | 0.601593 | -0.001482 [-0.004460, 0.001484] | no |
| series | tier1 | 614 | 0.621096 | 0.616540 | 0.004556 [-0.004246, 0.013878] | no |
| series | tier2 | 1873 | 0.594383 | 0.593752 | 0.000631 [-0.004479, 0.005525] | no |
| series | tier3 | 1721 | 0.602496 | 0.607981 | -0.005485 [-0.009382, -0.001402] | yes |
| series | unknown | 42 | 0.451047 | 0.471027 | -0.019980 [-0.053332, 0.013587] | no |
| series | international=1 | 370 | 0.587866 | 0.589385 | -0.001519 [-0.011232, 0.008713] | no |
| series | international=0 | 3880 | 0.601279 | 0.602757 | -0.001479 [-0.004426, 0.001745] | no |
| map | all | 4312 | 0.636366 | 0.635269 | 0.001097 [-0.000926, 0.003097] | no |
| map | tier1 | 1046 | 0.654215 | 0.649504 | 0.004710 [0.000228, 0.009235] | yes |
| map | tier2 | 1936 | 0.631262 | 0.631140 | 0.000122 [-0.002731, 0.002885] | no |
| map | tier3 | 1276 | 0.633026 | 0.633014 | 0.000012 [-0.003162, 0.003591] | no |
| map | unknown | 54 | 0.552559 | 0.560856 | -0.008297 [-0.020260, 0.002638] | no |
| map | international=1 | 686 | 0.628933 | 0.629473 | -0.000540 [-0.005162, 0.004515] | no |
| map | international=0 | 3626 | 0.637773 | 0.636366 | 0.001407 [-0.000758, 0.003639] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 1638 | 1636 | 0.0253 | 2.74% [-1.45%, 7.12%] | $19.26 | 0.385× | 87.33% | $5.32 | 1083 (555 unfilled) | 5.21% [0.23%, 11.01%] | $101.79 |
| series | tier1 | 239 | 239 | 0.0288 | 1.73% [-8.62%, 12.93%] | $26.30 | 0.526× | 72.81% | $9.11 | 189 (50 unfilled) | 3.13% [-7.78%, 13.69%] | $58.67 |
| series | tier2 | 787 | 785 | 0.0278 | -2.54% [-8.07%, 3.11%] | $8.27 | 0.165× | 86.45% | $4.90 | 519 (268 unfilled) | 0.04% [-7.23%, 7.49%] | $24.14 |
| series | tier3 | 588 | 588 | 0.0200 | 10.64% [3.04%, 18.77%] | $284.46 | 5.689× | 55.43% | $31.13 | 358 (230 unfilled) | 14.78% [4.88%, 26.71%] | $158.57 |
| series | unknown | 24 | 24 | 0.0383 | -8.11% [-36.22%, 21.16%] | $56.74 | 1.135× | 25.81% | $6.70 | 17 (7 unfilled) | -15.01% [-52.27%, 23.73%] | $52.68 |
| series | international=1 | 146 | 146 | 0.0264 | 4.90% [-8.27%, 19.89%] | $45.68 | 0.914× | 47.10% | $8.36 | 124 (22 unfilled) | 2.37% [-10.06%, 15.63%] | $49.87 |
| series | international=0 | 1492 | 1490 | 0.0252 | 2.53% [-2.16%, 7.25%] | $18.26 | 0.365× | 88.82% | $4.90 | 959 (533 unfilled) | 5.58% [-0.07%, 11.73%] | $98.19 |
| map | all | 616 | 393 | 0.0193 | -2.31% [-9.63%, 5.91%] | $27.38 | 0.548× | 84.15% | $12.16 | 189 (427 unfilled) | -5.97% [-16.87%, 4.17%] | $28.26 |
| map | tier1 | 160 | 102 | 0.0251 | -15.02% [-26.38%, -2.65%] | $22.56 | 0.451× | 60.55% | $4.27 | 55 (105 unfilled) | -11.82% [-32.59%, 9.08%] | $42.56 |
| map | tier2 | 289 | 186 | 0.0190 | -1.99% [-13.47%, 13.14%] | $41.29 | 0.826× | 58.40% | $8.24 | 88 (201 unfilled) | -3.48% [-19.03%, 12.24%] | $36.67 |
| map | tier3 | 155 | 96 | 0.0144 | 9.62% [-3.88%, 22.51%] | $76.37 | 1.527× | 24.18% | $5.18 | 40 (115 unfilled) | -6.62% [-28.34%, 16.16%] | $44.82 |
| map | unknown | 12 | 9 | 0.0113 | 5.15% [-23.22%, 33.94%] | $49.98 | 1.000× | 7.06% | $3.69 | 6 (6 unfilled) | 15.58% [-7.91%, 41.56%] | $50.08 |
| map | international=1 | 97 | 62 | 0.0231 | -2.33% [-17.53%, 12.65%] | $50.65 | 1.013× | 24.92% | $4.20 | 42 (55 unfilled) | -8.81% [-34.49%, 17.58%] | $45.91 |
| map | international=0 | 519 | 331 | 0.0185 | -2.31% [-10.77%, 6.49%] | $26.85 | 0.537× | 84.14% | $12.35 | 147 (372 unfilled) | -5.16% [-16.32%, 6.82%] | $30.37 |
| series+map | all | 2254 | 1684 | 0.0237 | 1.36% [-2.47%, 5.64%] | $26.85 | 0.537× | 85.84% | $6.40 | 1272 (982 unfilled) | 3.55% [-1.19%, 8.56%] | $81.11 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-01 | 63 | 0.681679 | — | 0.638920 | -14.41% (45), $38.28 | — | 5 (40 unfilled) | -48.78% [-100.00%, 5.91%] | $46.59 | — | — | — |
| map | 2026-02 | 102 | 0.648781 | — | 0.611955 | -21.41% (68), $16.87 | — | 28 (40 unfilled) | -45.38% [-75.28%, -12.44%] | $21.42 | — | — | — |
| map | 2026-03 | 144 | 0.656391 | 0.647109 | 0.642845 | 1.83% (80), $54.56 | -3.31% (27), $40.17 | 48 (32 unfilled) | 11.15% [-22.17%, 43.96%] | $62.30 | 14 (13 unfilled) | -28.01% [-60.80%, 7.45%] | $36.56 |
| map | 2026-04 | 273 | 0.637080 | 0.650671 | 0.647894 | 15.73% (182), $205.02 | -15.77% (13), $40.95 | 67 (115 unfilled) | -7.97% [-29.09%, 14.44%] | $24.75 | 6 (7 unfilled) | -17.55% [-65.37%, 27.10%] | $45.83 |
| map | 2026-05 | 452 | 0.647192 | 0.634171 | 0.636432 | -2.81% (295), $18.68 | 2.53% (131), $110.80 | 97 (198 unfilled) | -6.30% [-25.52%, 13.46%] | $27.58 | 53 (78 unfilled) | -2.73% [-26.94%, 20.11%] | $54.39 |
| map | 2026-06 | 414 | 0.657774 | 0.647814 | 0.650163 | -0.70% (272), $38.46 | 6.94% (132), $60.86 | 50 (222 unfilled) | 8.73% [-17.74%, 33.93%] | $61.43 | 26 (106 unfilled) | 1.55% [-28.90%, 27.17%] | $49.38 |
| map | 2026-07 | 618 | 0.693682 | 0.658848 | 0.647047 | -18.21% (413), $0.05 | -15.61% (165), $17.46 | 97 (316 unfilled) | -16.40% [-36.75%, 4.00%] | $17.04 | 36 (129 unfilled) | -9.42% [-33.25%, 12.07%] | $40.97 |
| map | 2026-08 | 873 | 0.637753 | 0.621006 | 0.623251 | -3.01% (645), $13.04 | 18.32% (26), $60.67 | 122 (523 unfilled) | -6.93% [-25.31%, 11.31%] | $18.26 | 5 (21 unfilled) | 5.33% [-48.86%, 37.07%] | $50.85 |
| map | 2026-09 | 879 | 0.669080 | 0.632716 | 0.631507 | -12.26% (647), $0.06 | -4.94% (100), $35.33 | 241 (406 unfilled) | -20.49% [-35.94%, -4.43%] | $2.83 | 40 (60 unfilled) | -4.89% [-28.10%, 18.22%] | $46.77 |
| map | 2026-10 | 659 | 0.651862 | 0.626541 | 0.628124 | -5.75% (439), $2.10 | 9.66% (22), $51.45 | 173 (266 unfilled) | -19.82% [-33.76%, -5.77%] | $2.79 | 9 (13 unfilled) | -2.14% [-37.22%, 29.09%] | $50.69 |
| series | 2026-01 | 51 | 0.553145 | — | 0.602759 | 16.48% (43), $92.41 | — | 37 (6 unfilled) | 35.87% [-0.84%, 74.68%] | $99.58 | — | — | — |
| series | 2026-02 | 155 | 0.583441 | — | 0.565710 | -20.57% (111), $6.39 | — | 100 (11 unfilled) | -18.21% [-38.24%, 2.58%] | $9.94 | — | — | — |
| series | 2026-03 | 304 | 0.623567 | 0.596656 | 0.590480 | -14.70% (204), $0.88 | -0.71% (196), $23.74 | 159 (45 unfilled) | -8.13% [-24.78%, 9.10%] | $4.44 | 147 (49 unfilled) | 1.17% [-11.30%, 14.26%] | $54.50 |
| series | 2026-04 | 322 | 0.590015 | 0.572611 | 0.580957 | 2.21% (239), $19.44 | 7.88% (184), $64.01 | 184 (55 unfilled) | -0.97% [-18.37%, 18.03%] | $13.52 | 143 (41 unfilled) | 8.63% [-6.23%, 26.38%] | $44.10 |
| series | 2026-05 | 360 | 0.614746 | 0.584865 | 0.584764 | -17.31% (252), $0.71 | -2.65% (186), $55.88 | 200 (52 unfilled) | -20.60% [-35.49%, -4.49%] | $1.31 | 150 (36 unfilled) | -1.65% [-14.48%, 11.20%] | $65.39 |
| series | 2026-06 | 348 | 0.648179 | 0.637442 | 0.633931 | 0.30% (255), $19.11 | 2.51% (170), $25.93 | 164 (91 unfilled) | 14.70% [-4.41%, 34.93%] | $193.38 | 111 (59 unfilled) | 7.70% [-7.19%, 23.51%] | $33.43 |
| series | 2026-07 | 513 | 0.655255 | 0.620106 | 0.614447 | -16.01% (371), $0.06 | -4.83% (193), $23.72 | 226 (145 unfilled) | -15.35% [-32.07%, 4.87%] | $0.40 | 118 (75 unfilled) | -0.32% [-22.16%, 29.63%] | $40.87 |
| series | 2026-08 | 717 | 0.617572 | 0.608383 | 0.614837 | 2.30% (556), $3.47 | 10.03% (179), $124.28 | 277 (279 unfilled) | 1.55% [-13.84%, 18.80%] | $19.98 | 92 (87 unfilled) | 18.11% [3.47%, 32.49%] | $103.14 |
| series | 2026-09 | 914 | 0.634290 | 0.602148 | 0.602664 | -5.78% (690), $0.03 | 1.44% (311), $33.75 | 389 (301 unfilled) | -5.59% [-17.54%, 5.85%] | $0.02 | 187 (124 unfilled) | 7.36% [-3.77%, 19.28%] | $56.68 |
| series | 2026-10 | 772 | 0.597628 | 0.579842 | 0.585736 | -4.92% (556), $0.07 | 8.84% (219), $95.14 | 349 (207 unfilled) | -4.63% [-16.79%, 7.71%] | $3.60 | 135 (84 unfilled) | 4.68% [-8.53%, 17.31%] | $62.09 |

### player_round_glicko+none: Kalshi comparison and returns

none

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 4456 | 0.600306 | 0.600358 | -0.000053 [-0.008150, 0.007996] | no |
| series | tier1 | 725 | 0.634196 | 0.616830 | 0.017366 [-0.000104, 0.034578] | no |
| series | tier2 | 1962 | 0.597202 | 0.590722 | 0.006480 [-0.003845, 0.017065] | no |
| series | tier3 | 1727 | 0.592254 | 0.607536 | -0.015282 [-0.029514, -0.000721] | yes |
| series | unknown | 42 | 0.491357 | 0.471027 | 0.020329 [-0.038591, 0.078661] | no |
| series | international=1 | 448 | 0.607693 | 0.591446 | 0.016248 [-0.006945, 0.037620] | no |
| series | international=0 | 4008 | 0.599480 | 0.601354 | -0.001875 [-0.010319, 0.006261] | no |
| map | all | 4477 | 0.641027 | 0.634789 | 0.006237 [0.000224, 0.012190] | yes |
| map | tier1 | 1176 | 0.657301 | 0.646419 | 0.010882 [-0.001220, 0.022426] | no |
| map | tier2 | 1968 | 0.637418 | 0.631291 | 0.006126 [-0.002066, 0.014388] | no |
| map | tier3 | 1279 | 0.634187 | 0.632601 | 0.001586 [-0.011520, 0.014496] | no |
| map | unknown | 54 | 0.580145 | 0.560856 | 0.019289 [-0.012097, 0.053023] | no |
| map | international=1 | 788 | 0.636734 | 0.630059 | 0.006675 [-0.007771, 0.020655] | no |
| map | international=0 | 3689 | 0.641944 | 0.635800 | 0.006144 [-0.000259, 0.012618] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 3316 | 3311 | 0.0819 | 2.00% [-2.29%, 6.57%] | $0.03 | 0.001× | 99.97% | $9.61 | 2108 (1208 unfilled) | 0.02% [-5.35%, 5.35%] | $0.09 |
| series | tier1 | 536 | 536 | 0.0780 | 0.03% [-11.36%, 12.19%] | $0.10 | 0.002× | 99.92% | $12.56 | 432 (104 unfilled) | -4.05% [-15.88%, 8.62%] | $0.09 |
| series | tier2 | 1406 | 1403 | 0.0716 | -2.58% [-9.12%, 3.98%] | $0.08 | 0.002× | 99.95% | $16.00 | 884 (522 unfilled) | -3.44% [-10.86%, 4.95%] | $0.05 |
| series | tier3 | 1341 | 1339 | 0.0945 | 8.13% [1.35%, 15.21%] | $5297.53 | 105.951× | 86.78% | $249.12 | 769 (572 unfilled) | 6.65% [-2.33%, 15.58%] | $105.61 |
| series | unknown | 33 | 33 | 0.0729 | -19.63% [-49.59%, 13.36%] | $32.55 | 0.651× | 38.66% | $5.10 | 23 (10 unfilled) | -11.86% [-49.11%, 31.13%] | $37.63 |
| series | international=1 | 338 | 338 | 0.0790 | 0.67% [-15.46%, 17.32%] | $0.72 | 0.014× | 99.50% | $11.49 | 290 (48 unfilled) | -5.45% [-20.57%, 10.36%] | $0.51 |
| series | international=0 | 2978 | 2973 | 0.0822 | 2.15% [-2.29%, 6.54%] | $0.08 | 0.002× | 99.87% | $6.32 | 1818 (1160 unfilled) | 0.89% [-4.89%, 6.71%] | $0.08 |
| map | all | 2876 | 1825 | 0.0593 | -5.59% [-10.02%, -1.07%] | $0.09 | 0.002× | 99.98% | $36.65 | 834 (2042 unfilled) | -13.93% [-21.51%, -6.28%] | $0.09 |
| map | tier1 | 754 | 513 | 0.0603 | -4.58% [-13.26%, 4.66%] | $4.14 | 0.083× | 95.75% | $8.27 | 227 (527 unfilled) | -5.50% [-21.78%, 12.10%] | $11.73 |
| map | tier2 | 1239 | 769 | 0.0528 | -5.94% [-12.33%, 0.75%] | $0.10 | 0.002× | 99.93% | $13.37 | 356 (883 unfilled) | -16.59% [-26.63%, -5.97%] | $0.32 |
| map | tier3 | 851 | 521 | 0.0686 | -5.68% [-13.50%, 2.34%] | $5.59 | 0.112× | 98.41% | $19.13 | 239 (612 unfilled) | -17.99% [-32.50%, -3.35%] | $6.00 |
| map | unknown | 32 | 22 | 0.0441 | -14.08% [-42.90%, 15.39%] | $37.95 | 0.759× | 26.08% | $4.78 | 12 (20 unfilled) | -13.86% [-51.82%, 16.78%] | $46.29 |
| map | international=1 | 500 | 344 | 0.0636 | -4.27% [-15.95%, 7.45%] | $30.11 | 0.602× | 88.18% | $24.78 | 157 (343 unfilled) | -4.70% [-25.35%, 17.56%] | $35.04 |
| map | international=0 | 2376 | 1481 | 0.0585 | -5.88% [-10.57%, -1.18%] | $0.08 | 0.002× | 99.92% | $9.48 | 677 (1699 unfilled) | -16.08% [-23.60%, -8.43%] | $0.10 |
| series+map | all | 6192 | 3642 | 0.0714 | -1.53% [-5.10%, 2.10%] | $0.07 | 0.001× | 99.92% | $6.83 | 2942 (3250 unfilled) | -3.93% [-8.69%, 1.06%] | $0.09 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2026-01-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 371 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-01 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-01 | map | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 51 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | map | 63 | 1.000000 | 0.000000 | unfitted |
| 2026-03 | series | 206 | 1.453867 | 0.659498 | fitted |
| 2026-03 | map | 165 | 1.268993 | 0.229978 | fitted |
| 2026-04 | series | 510 | 1.467817 | 0.856730 | fitted |
| 2026-04 | map | 309 | 1.196905 | 0.201954 | fitted |
| 2026-05 | series | 832 | 1.407610 | 0.781346 | fitted |
| 2026-05 | map | 582 | 1.336306 | 0.806289 | fitted |
| 2026-06 | series | 1192 | 1.399653 | 0.688576 | fitted |
| 2026-06 | map | 1034 | 1.356820 | 0.730843 | fitted |
| 2026-07 | series | 1540 | 1.309316 | 0.674754 | fitted |
| 2026-07 | map | 1448 | 1.301925 | 0.709868 | fitted |
| 2026-08 | series | 2053 | 1.244676 | 0.565525 | fitted |
| 2026-08 | map | 2066 | 1.164405 | 0.515103 | fitted |
| 2026-09 | series | 2770 | 1.237907 | 0.610315 | fitted |
| 2026-09 | map | 2939 | 1.224941 | 0.581191 | fitted |
| 2026-10 | series | 3684 | 1.241803 | 0.635053 | fitted |
| 2026-10 | map | 3818 | 1.204383 | 0.481869 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 4250 | 0.590082 | 0.601593 | -0.011511 [-0.016603, -0.006458] | yes |
| series | tier1 | 614 | 0.620491 | 0.616540 | 0.003951 [-0.006460, 0.014324] | no |
| series | tier2 | 1873 | 0.584326 | 0.593752 | -0.009426 [-0.016237, -0.002622] | yes |
| series | tier3 | 1721 | 0.588975 | 0.607981 | -0.019005 [-0.028643, -0.009594] | yes |
| series | unknown | 42 | 0.447581 | 0.471027 | -0.023446 [-0.054151, 0.009416] | no |
| series | international=1 | 370 | 0.588395 | 0.589385 | -0.000990 [-0.013239, 0.012145] | no |
| series | international=0 | 3880 | 0.590243 | 0.602757 | -0.012514 [-0.017887, -0.007064] | yes |
| map | all | 4312 | 0.632876 | 0.635269 | -0.002393 [-0.005975, 0.001192] | no |
| map | tier1 | 1046 | 0.653502 | 0.649504 | 0.003998 [-0.002805, 0.010258] | no |
| map | tier2 | 1936 | 0.626311 | 0.631140 | -0.004830 [-0.009495, -0.000002] | yes |
| map | tier3 | 1276 | 0.629480 | 0.633014 | -0.003534 [-0.011344, 0.005077] | no |
| map | unknown | 54 | 0.548987 | 0.560856 | -0.011869 [-0.031342, 0.007291] | no |
| map | international=1 | 686 | 0.627847 | 0.629473 | -0.001626 [-0.008455, 0.005624] | no |
| map | international=0 | 3626 | 0.633828 | 0.636366 | -0.002538 [-0.006614, 0.001553] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 2515 | 2511 | 0.0477 | 7.71% [3.75%, 11.73%] | $9760.38 | 195.208× | 85.42% | $249.12 | 1572 (943 unfilled) | 5.18% [0.28%, 10.52%] | $709.30 |
| series | tier1 | 314 | 314 | 0.0363 | -1.69% [-14.05%, 10.65%] | $10.23 | 0.205× | 90.45% | $6.60 | 243 (71 unfilled) | -2.20% [-15.81%, 11.31%] | $22.91 |
| series | tier2 | 1096 | 1095 | 0.0424 | 5.49% [0.06%, 10.76%] | $3909.68 | 78.194× | 62.73% | $249.12 | 669 (427 unfilled) | 2.09% [-4.58%, 9.13%] | $126.07 |
| series | tier3 | 1075 | 1072 | 0.0567 | 12.95% [6.77%, 19.89%] | $11775.79 | 235.516× | 60.73% | $249.12 | 639 (436 unfilled) | 11.46% [2.51%, 20.53%] | $1103.77 |
| series | unknown | 30 | 30 | 0.0392 | -0.48% [-26.76%, 26.08%] | $67.23 | 1.345× | 9.34% | $6.33 | 21 (9 unfilled) | -1.48% [-35.68%, 33.44%] | $57.73 |
| series | international=1 | 188 | 188 | 0.0336 | 2.54% [-14.22%, 20.28%] | $78.92 | 1.578× | 46.01% | $10.83 | 152 (36 unfilled) | 2.17% [-16.14%, 21.90%] | $82.69 |
| series | international=0 | 2327 | 2323 | 0.0488 | 8.13% [3.96%, 12.27%] | $10938.88 | 218.778× | 85.13% | $249.12 | 1420 (907 unfilled) | 5.51% [0.44%, 10.73%] | $594.35 |
| map | all | 1762 | 1092 | 0.0332 | 1.90% [-2.67%, 6.57%] | $283.51 | 5.670× | 79.13% | $41.89 | 510 (1252 unfilled) | -6.48% [-14.87%, 2.23%] | $16.17 |
| map | tier1 | 338 | 218 | 0.0312 | -3.85% [-15.75%, 8.80%] | $22.13 | 0.443× | 80.17% | $7.36 | 108 (230 unfilled) | -6.89% [-29.23%, 18.93%] | $46.98 |
| map | tier2 | 780 | 479 | 0.0288 | 2.29% [-4.74%, 9.55%] | $186.10 | 3.722× | 49.25% | $28.47 | 211 (569 unfilled) | -9.64% [-20.07%, 0.95%] | $20.14 |
| map | tier3 | 624 | 382 | 0.0400 | 4.12% [-3.73%, 11.78%] | $201.42 | 4.028× | 65.83% | $30.09 | 182 (442 unfilled) | -3.99% [-17.51%, 9.51%] | $37.91 |
| map | unknown | 20 | 13 | 0.0262 | 15.16% [-9.30%, 40.33%] | $52.68 | 1.054× | 3.66% | $4.86 | 9 (11 unfilled) | 22.60% [-1.92%, 51.23%] | $54.59 |
| map | international=1 | 223 | 144 | 0.0311 | 4.09% [-11.38%, 20.02%] | $81.47 | 1.629× | 35.84% | $8.39 | 79 (144 unfilled) | 5.06% [-24.53%, 35.46%] | $74.98 |
| map | international=0 | 1539 | 948 | 0.0335 | 1.58% [-3.41%, 6.52%] | $193.06 | 3.861× | 77.51% | $25.05 | 431 (1108 unfilled) | -8.60% [-16.96%, 0.11%] | $10.49 |
| series+map | all | 4277 | 2639 | 0.0417 | 5.32% [1.79%, 8.74%] | $11937.46 | 238.749× | 63.99% | $249.30 | 2082 (2195 unfilled) | 2.33% [-2.39%, 7.03%] | $455.75 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-01 | 63 | 0.634559 | — | 0.638920 | 0.71% (42), $58.19 | — | 5 (37 unfilled) | 11.19% [-66.65%, 89.92%] | $50.98 | — | — | — |
| map | 2026-02 | 102 | 0.642663 | — | 0.611955 | -16.79% (59), $28.27 | — | 18 (41 unfilled) | -48.65% [-83.20%, -10.86%] | $28.60 | — | — | — |
| map | 2026-03 | 144 | 0.656733 | 0.643151 | 0.642845 | -2.78% (81), $47.71 | 12.33% (35), $59.80 | 42 (39 unfilled) | 0.10% [-37.81%, 38.93%] | $45.27 | 15 (20 unfilled) | -0.93% [-36.71%, 24.55%] | $49.44 |
| map | 2026-04 | 273 | 0.624606 | 0.639455 | 0.647894 | 15.90% (166), $252.50 | 35.18% (30), $60.87 | 50 (116 unfilled) | -12.03% [-40.47%, 16.39%] | $30.51 | 9 (21 unfilled) | -27.47% [-80.10%, 8.21%] | $48.34 |
| map | 2026-05 | 452 | 0.643603 | 0.631681 | 0.636432 | -4.81% (280), $31.69 | 6.20% (233), $85.20 | 89 (191 unfilled) | -5.28% [-28.73%, 18.47%] | $30.96 | 89 (144 unfilled) | 1.24% [-19.67%, 20.24%] | $45.53 |
| map | 2026-06 | 414 | 0.643189 | 0.642528 | 0.650163 | 2.08% (246), $80.80 | 4.92% (224), $93.53 | 50 (196 unfilled) | 9.65% [-19.31%, 37.75%] | $61.24 | 46 (178 unfilled) | 3.70% [-23.08%, 31.01%] | $58.17 |
| map | 2026-07 | 618 | 0.658813 | 0.654574 | 0.647047 | -6.68% (396), $6.44 | -5.20% (344), $13.47 | 98 (298 unfilled) | -11.37% [-32.50%, 10.74%] | $28.69 | 75 (269 unfilled) | -7.66% [-26.37%, 12.02%] | $41.40 |
| map | 2026-08 | 873 | 0.620008 | 0.613011 | 0.623251 | -3.47% (604), $6.23 | 8.16% (339), $320.01 | 112 (492 unfilled) | -8.75% [-30.61%, 13.49%] | $33.57 | 69 (270 unfilled) | 0.56% [-22.95%, 25.56%] | $45.16 |
| map | 2026-09 | 879 | 0.648612 | 0.634161 | 0.631507 | -11.74% (605), $0.05 | -5.41% (360), $34.89 | 224 (381 unfilled) | -18.80% [-34.50%, -2.35%] | $2.83 | 143 (217 unfilled) | -9.49% [-26.14%, 10.13%] | $47.32 |
| map | 2026-10 | 659 | 0.642685 | 0.626917 | 0.628124 | -12.25% (397), $0.29 | 1.45% (197), $44.75 | 146 (251 unfilled) | -26.71% [-42.77%, -10.35%] | $3.85 | 64 (133 unfilled) | -22.33% [-42.80%, -1.12%] | $23.69 |
| series | 2026-01 | 51 | 0.581275 | — | 0.602759 | 25.16% (37), $78.76 | — | 31 (6 unfilled) | 38.44% [-8.42%, 87.10%] | $85.01 | — | — | — |
| series | 2026-02 | 155 | 0.584314 | — | 0.565710 | -14.52% (116), $11.90 | — | 104 (12 unfilled) | -15.93% [-35.06%, 3.62%] | $11.80 | — | — | — |
| series | 2026-03 | 304 | 0.583521 | 0.571284 | 0.590480 | -0.71% (225), $33.67 | 11.03% (198), $274.34 | 172 (53 unfilled) | -1.55% [-18.67%, 15.86%] | $52.07 | 148 (50 unfilled) | 6.83% [-5.78%, 19.59%] | $140.60 |
| series | 2026-04 | 322 | 0.584297 | 0.568843 | 0.580957 | -0.07% (240), $12.89 | 7.45% (222), $155.01 | 180 (60 unfilled) | 2.24% [-15.82%, 24.04%] | $37.33 | 162 (60 unfilled) | 12.32% [-3.24%, 28.96%] | $177.09 |
| series | 2026-05 | 360 | 0.603914 | 0.580706 | 0.584764 | -7.39% (261), $2.19 | 0.31% (236), $45.12 | 213 (48 unfilled) | -8.17% [-24.62%, 7.54%] | $2.37 | 185 (51 unfilled) | -1.03% [-13.90%, 12.66%] | $39.59 |
| series | 2026-06 | 348 | 0.619820 | 0.625813 | 0.633931 | 7.32% (248), $193.65 | 7.63% (213), $72.62 | 164 (84 unfilled) | 15.94% [-2.69%, 35.25%] | $420.27 | 140 (73 unfilled) | 7.37% [-6.87%, 21.50%] | $71.51 |
| series | 2026-07 | 513 | 0.627545 | 0.614287 | 0.614447 | 2.06% (386), $0.93 | -1.23% (324), $16.46 | 244 (142 unfilled) | -0.58% [-17.28%, 17.91%] | $19.46 | 198 (126 unfilled) | -3.72% [-19.73%, 15.79%] | $13.23 |
| series | 2026-08 | 717 | 0.604422 | 0.596721 | 0.614837 | 5.93% (562), $32.26 | 12.12% (422), $620.18 | 273 (289 unfilled) | -0.10% [-15.53%, 16.22%] | $21.97 | 206 (216 unfilled) | 15.41% [-1.68%, 33.83%] | $325.04 |
| series | 2026-09 | 914 | 0.596996 | 0.586579 | 0.602664 | 1.57% (690), $10.25 | 12.98% (496), $1432.83 | 386 (304 unfilled) | -4.55% [-16.27%, 7.01%] | $0.81 | 286 (210 unfilled) | 4.14% [-8.04%, 15.83%] | $127.29 |
| series | 2026-10 | 772 | 0.589575 | 0.576507 | 0.585736 | 4.47% (551), $2.94 | 6.67% (404), $137.57 | 341 (210 unfilled) | 4.13% [-8.10%, 17.57%] | $31.19 | 247 (157 unfilled) | 2.76% [-8.16%, 13.70%] | $83.39 |

### player_round_glicko_rookie_weights+none: Kalshi comparison and returns

none

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 4456 | 0.594997 | 0.600358 | -0.005361 [-0.013206, 0.002268] | no |
| series | tier1 | 725 | 0.630703 | 0.616830 | 0.013872 [-0.002584, 0.029938] | no |
| series | tier2 | 1962 | 0.594171 | 0.590722 | 0.003449 [-0.006705, 0.013790] | no |
| series | tier3 | 1727 | 0.583516 | 0.607536 | -0.024020 [-0.038017, -0.010329] | yes |
| series | unknown | 42 | 0.489338 | 0.471027 | 0.018311 [-0.044404, 0.079300] | no |
| series | international=1 | 448 | 0.603206 | 0.591446 | 0.011760 [-0.009762, 0.031669] | no |
| series | international=0 | 4008 | 0.594079 | 0.601354 | -0.007275 [-0.015439, 0.000505] | no |
| map | all | 4477 | 0.639083 | 0.634789 | 0.004293 [-0.001658, 0.009869] | no |
| map | tier1 | 1176 | 0.655445 | 0.646419 | 0.009026 [-0.002478, 0.019755] | no |
| map | tier2 | 1968 | 0.635944 | 0.631291 | 0.004652 [-0.002996, 0.012632] | no |
| map | tier3 | 1279 | 0.631309 | 0.632601 | -0.001292 [-0.013629, 0.011091] | no |
| map | unknown | 54 | 0.581280 | 0.560856 | 0.020423 [-0.010986, 0.054196] | no |
| map | international=1 | 788 | 0.634694 | 0.630059 | 0.004635 [-0.009042, 0.017801] | no |
| map | international=0 | 3689 | 0.640020 | 0.635800 | 0.004220 [-0.001983, 0.010677] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 3270 | 3265 | 0.0825 | 2.73% [-1.63%, 6.92%] | $0.09 | 0.002× | 99.93% | $12.48 | 2077 (1193 unfilled) | -0.02% [-5.21%, 5.71%] | $0.08 |
| series | tier1 | 526 | 526 | 0.0732 | -2.28% [-14.01%, 9.69%] | $0.06 | 0.001× | 99.96% | $16.35 | 426 (100 unfilled) | -4.94% [-17.42%, 7.81%] | $0.36 |
| series | tier2 | 1374 | 1371 | 0.0728 | -1.48% [-7.89%, 4.92%] | $0.02 | 0.000× | 99.99% | $17.25 | 863 (511 unfilled) | -3.72% [-11.00%, 4.24%] | $0.09 |
| series | tier3 | 1337 | 1335 | 0.0964 | 9.52% [2.35%, 16.57%] | $10973.44 | 219.469× | 80.48% | $249.12 | 766 (571 unfilled) | 7.28% [-1.08%, 16.74%] | $316.90 |
| series | unknown | 33 | 33 | 0.0763 | -16.71% [-48.28%, 16.01%] | $41.47 | 0.829× | 32.38% | $5.89 | 22 (11 unfilled) | -13.08% [-54.22%, 30.96%] | $42.04 |
| series | international=1 | 320 | 320 | 0.0746 | -3.38% [-17.98%, 12.76%] | $2.25 | 0.045× | 99.04% | $13.41 | 275 (45 unfilled) | -7.77% [-22.86%, 7.68%] | $1.03 |
| series | international=0 | 2950 | 2945 | 0.0834 | 3.39% [-1.08%, 8.14%] | $0.04 | 0.001× | 99.94% | $5.92 | 1802 (1148 unfilled) | 1.17% [-4.44%, 6.78%] | $21.68 |
| map | all | 2828 | 1810 | 0.0575 | -4.83% [-9.47%, -0.22%] | $0.09 | 0.002× | 99.98% | $46.16 | 821 (2007 unfilled) | -17.08% [-25.31%, -9.25%] | $0.09 |
| map | tier1 | 745 | 510 | 0.0562 | -4.51% [-13.36%, 4.52%] | $4.70 | 0.094× | 95.55% | $9.25 | 225 (520 unfilled) | -8.48% [-24.83%, 9.10%] | $10.26 |
| map | tier2 | 1210 | 759 | 0.0520 | -4.42% [-10.92%, 2.24%] | $0.08 | 0.002× | 99.95% | $14.99 | 345 (865 unfilled) | -18.63% [-28.71%, -7.80%] | $0.28 |
| map | tier3 | 843 | 520 | 0.0667 | -5.29% [-13.05%, 2.37%] | $2.18 | 0.044× | 99.28% | $16.07 | 240 (603 unfilled) | -22.93% [-36.55%, -8.98%] | $2.32 |
| map | unknown | 30 | 21 | 0.0475 | -16.90% [-48.08%, 13.49%] | $36.25 | 0.725× | 31.58% | $4.78 | 11 (19 unfilled) | -16.99% [-56.80%, 17.05%] | $46.36 |
| map | international=1 | 507 | 347 | 0.0575 | -2.93% [-14.78%, 8.76%] | $40.55 | 0.811× | 85.54% | $26.91 | 160 (347 unfilled) | -6.35% [-27.22%, 14.91%] | $32.62 |
| map | international=0 | 2321 | 1463 | 0.0575 | -5.25% [-9.93%, -0.34%] | $0.09 | 0.002× | 99.92% | $11.90 | 661 (1660 unfilled) | -19.69% [-27.21%, -11.83%] | $0.10 |
| series+map | all | 6098 | 3584 | 0.0709 | -0.78% [-4.50%, 2.69%] | $0.05 | 0.001× | 99.97% | $15.97 | 2898 (3200 unfilled) | -4.85% [-9.52%, -0.06%] | $0.03 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2026-01-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 371 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-01 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-01 | map | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 51 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | map | 63 | 1.000000 | 0.000000 | unfitted |
| 2026-03 | series | 206 | 1.429141 | 0.713157 | fitted |
| 2026-03 | map | 165 | 1.243703 | 0.156871 | fitted |
| 2026-04 | series | 510 | 1.427210 | 0.840946 | fitted |
| 2026-04 | map | 309 | 1.195945 | 0.207217 | fitted |
| 2026-05 | series | 832 | 1.380243 | 0.793125 | fitted |
| 2026-05 | map | 582 | 1.324317 | 0.791176 | fitted |
| 2026-06 | series | 1192 | 1.378099 | 0.701722 | fitted |
| 2026-06 | map | 1034 | 1.356969 | 0.749742 | fitted |
| 2026-07 | series | 1540 | 1.298813 | 0.717070 | fitted |
| 2026-07 | map | 1448 | 1.315498 | 0.755874 | fitted |
| 2026-08 | series | 2053 | 1.240421 | 0.626065 | fitted |
| 2026-08 | map | 2066 | 1.179960 | 0.575474 | fitted |
| 2026-09 | series | 2770 | 1.236628 | 0.661569 | fitted |
| 2026-09 | map | 2939 | 1.244118 | 0.635687 | fitted |
| 2026-10 | series | 3684 | 1.235600 | 0.686911 | fitted |
| 2026-10 | map | 3818 | 1.217517 | 0.529179 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 4250 | 0.587012 | 0.601593 | -0.014581 [-0.020078, -0.009170] | yes |
| series | tier1 | 614 | 0.621026 | 0.616540 | 0.004486 [-0.006341, 0.015635] | no |
| series | tier2 | 1873 | 0.583196 | 0.593752 | -0.010556 [-0.017792, -0.003460] | yes |
| series | tier3 | 1721 | 0.582443 | 0.607981 | -0.025537 [-0.035688, -0.015440] | yes |
| series | unknown | 42 | 0.447165 | 0.471027 | -0.023863 [-0.056523, 0.010582] | no |
| series | international=1 | 370 | 0.589094 | 0.589385 | -0.000291 [-0.013554, 0.013705] | no |
| series | international=0 | 3880 | 0.586814 | 0.602757 | -0.015944 [-0.021791, -0.010169] | yes |
| map | all | 4312 | 0.632059 | 0.635269 | -0.003210 [-0.006854, 0.000459] | no |
| map | tier1 | 1046 | 0.654007 | 0.649504 | 0.004502 [-0.002295, 0.011013] | no |
| map | tier2 | 1936 | 0.625447 | 0.631140 | -0.005693 [-0.010448, -0.000835] | yes |
| map | tier3 | 1276 | 0.627602 | 0.633014 | -0.005412 [-0.013322, 0.002855] | no |
| map | unknown | 54 | 0.549293 | 0.560856 | -0.011564 [-0.032919, 0.009334] | no |
| map | international=1 | 686 | 0.627673 | 0.629473 | -0.001800 [-0.008701, 0.005680] | no |
| map | international=0 | 3626 | 0.632889 | 0.636366 | -0.003477 [-0.007571, 0.000746] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 2647 | 2643 | 0.0515 | 8.41% [4.43%, 12.34%] | $13532.46 | 270.649× | 62.37% | $249.12 | 1648 (999 unfilled) | 5.32% [0.45%, 10.45%] | $769.27 |
| series | tier1 | 337 | 337 | 0.0371 | -4.53% [-15.72%, 6.41%] | $11.06 | 0.221× | 92.26% | $8.98 | 261 (76 unfilled) | -4.80% [-17.06%, 7.91%] | $25.10 |
| series | tier2 | 1129 | 1128 | 0.0456 | 5.27% [-0.43%, 10.95%] | $5491.01 | 109.820× | 60.61% | $249.47 | 692 (437 unfilled) | 2.11% [-4.51%, 8.87%] | $75.31 |
| series | tier3 | 1153 | 1150 | 0.0616 | 15.42% [9.09%, 21.76%] | $12442.14 | 248.843× | 69.84% | $249.12 | 677 (476 unfilled) | 12.67% [5.16%, 21.30%] | $1396.11 |
| series | unknown | 28 | 28 | 0.0486 | 2.60% [-24.44%, 29.48%] | $64.58 | 1.292× | 12.16% | $6.45 | 18 (10 unfilled) | -0.20% [-37.94%, 38.62%] | $55.37 |
| series | international=1 | 200 | 200 | 0.0345 | -3.91% [-18.57%, 11.64%] | $67.05 | 1.341× | 52.52% | $9.67 | 165 (35 unfilled) | -5.27% [-21.04%, 10.98%] | $91.56 |
| series | international=0 | 2447 | 2443 | 0.0529 | 9.42% [5.55%, 13.42%] | $13655.86 | 273.117× | 86.84% | $249.12 | 1483 (964 unfilled) | 6.51% [1.40%, 11.63%] | $553.74 |
| map | all | 1832 | 1150 | 0.0338 | 4.36% [-0.67%, 9.49%] | $667.99 | 13.360× | 78.89% | $136.80 | 519 (1313 unfilled) | -6.80% [-14.57%, 1.80%] | $13.69 |
| map | tier1 | 363 | 245 | 0.0298 | -1.32% [-13.08%, 11.77%] | $16.85 | 0.337× | 80.44% | $6.62 | 111 (252 unfilled) | -8.00% [-26.97%, 11.89%] | $33.96 |
| map | tier2 | 798 | 492 | 0.0294 | 3.64% [-3.25%, 10.29%] | $169.23 | 3.385× | 54.44% | $31.74 | 214 (584 unfilled) | -9.02% [-21.01%, 2.11%] | $23.44 |
| map | tier3 | 651 | 400 | 0.0415 | 8.10% [0.54%, 15.94%] | $546.85 | 10.937× | 64.49% | $60.34 | 185 (466 unfilled) | -4.93% [-18.33%, 9.31%] | $33.44 |
| map | unknown | 20 | 13 | 0.0297 | 15.16% [-9.30%, 40.33%] | $56.10 | 1.122× | 6.81% | $4.97 | 9 (11 unfilled) | 22.60% [-1.92%, 51.23%] | $57.13 |
| map | international=1 | 244 | 168 | 0.0284 | 7.82% [-7.43%, 24.55%] | $68.83 | 1.377× | 47.22% | $8.40 | 83 (161 unfilled) | 2.32% [-21.80%, 27.89%] | $54.81 |
| map | international=0 | 1588 | 982 | 0.0346 | 3.83% [-1.12%, 8.84%] | $503.58 | 10.072× | 76.22% | $67.50 | 436 (1152 unfilled) | -8.54% [-16.89%, -0.29%] | $12.13 |
| series+map | all | 4479 | 2770 | 0.0443 | 6.75% [3.51%, 10.30%] | $19834.28 | 396.686× | 42.30% | $249.47 | 2167 (2312 unfilled) | 2.42% [-1.91%, 6.89%] | $402.54 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-01 | 63 | 0.631801 | — | 0.638920 | 14.89% (42), $68.21 | — | 4 (38 unfilled) | -3.09% [-100.00%, 95.23%] | $50.62 | — | — | — |
| map | 2026-02 | 102 | 0.644367 | — | 0.611955 | -26.74% (58), $25.11 | — | 21 (37 unfilled) | -69.47% [-100.00%, -34.77%] | $25.70 | — | — | — |
| map | 2026-03 | 144 | 0.653556 | 0.642727 | 0.642845 | 1.84% (79), $40.38 | 10.13% (28), $53.89 | 40 (39 unfilled) | 14.05% [-26.54%, 58.60%] | $51.95 | 14 (14 unfilled) | -4.23% [-39.90%, 22.32%] | $49.44 |
| map | 2026-04 | 273 | 0.623220 | 0.638026 | 0.647894 | 16.45% (161), $285.53 | 73.35% (32), $89.96 | 50 (111 unfilled) | -15.69% [-43.59%, 13.75%] | $33.86 | 10 (22 unfilled) | -20.41% [-65.20%, 20.35%] | $47.06 |
| map | 2026-05 | 452 | 0.640346 | 0.629637 | 0.636432 | -2.35% (277), $48.46 | 4.17% (231), $107.51 | 94 (183 unfilled) | -4.58% [-28.26%, 18.24%] | $30.28 | 90 (141 unfilled) | -4.26% [-24.61%, 15.33%] | $49.97 |
| map | 2026-06 | 414 | 0.641458 | 0.641087 | 0.650163 | 3.91% (236), $98.54 | 9.56% (215), $113.91 | 49 (187 unfilled) | -2.94% [-31.03%, 30.60%] | $44.36 | 46 (169 unfilled) | 4.40% [-21.35%, 31.35%] | $55.28 |
| map | 2026-07 | 618 | 0.655439 | 0.653475 | 0.647047 | -7.02% (381), $6.57 | -4.52% (347), $16.55 | 86 (295 unfilled) | -9.88% [-31.96%, 13.31%] | $29.45 | 72 (275 unfilled) | -2.33% [-22.60%, 16.21%] | $46.67 |
| map | 2026-08 | 873 | 0.619331 | 0.611896 | 0.623251 | -2.00% (592), $13.90 | 12.02% (388), $306.43 | 116 (476 unfilled) | -8.38% [-28.83%, 13.12%] | $34.38 | 76 (312 unfilled) | 7.81% [-15.64%, 32.66%] | $58.92 |
| map | 2026-09 | 879 | 0.647004 | 0.634692 | 0.631507 | -12.49% (593), $0.07 | -4.76% (379), $25.74 | 207 (386 unfilled) | -26.22% [-42.19%, -10.54%] | $0.66 | 141 (238 unfilled) | -16.86% [-31.68%, -1.14%] | $23.97 |
| map | 2026-10 | 659 | 0.640272 | 0.626361 | 0.628124 | -11.12% (409), $0.42 | 4.96% (212), $51.17 | 154 (255 unfilled) | -29.23% [-44.53%, -13.84%] | $2.58 | 70 (142 unfilled) | -16.21% [-35.48%, 2.96%] | $24.07 |
| series | 2026-01 | 51 | 0.572357 | — | 0.602759 | 22.55% (38), $106.74 | — | 34 (4 unfilled) | 37.27% [-7.13%, 85.27%] | $107.08 | — | — | — |
| series | 2026-02 | 155 | 0.578866 | — | 0.565710 | -13.90% (116), $11.46 | — | 104 (12 unfilled) | -17.00% [-36.36%, 2.19%] | $11.66 | — | — | — |
| series | 2026-03 | 304 | 0.583253 | 0.571458 | 0.590480 | 2.90% (224), $48.26 | 12.07% (197), $292.49 | 174 (50 unfilled) | 1.92% [-14.33%, 19.30%] | $54.45 | 147 (50 unfilled) | 10.54% [-1.33%, 23.53%] | $142.50 |
| series | 2026-04 | 322 | 0.579510 | 0.566600 | 0.580957 | -0.75% (237), $29.17 | 6.76% (223), $127.38 | 170 (67 unfilled) | 4.36% [-14.84%, 26.03%] | $55.34 | 163 (60 unfilled) | 10.67% [-5.08%, 28.47%] | $121.40 |
| series | 2026-05 | 360 | 0.600817 | 0.579972 | 0.584764 | -7.06% (264), $4.36 | 0.94% (247), $68.36 | 213 (51 unfilled) | -9.56% [-24.92%, 5.83%] | $1.97 | 196 (51 unfilled) | -2.27% [-16.29%, 11.35%] | $44.11 |
| series | 2026-06 | 348 | 0.613647 | 0.621359 | 0.633931 | 8.80% (242), $251.80 | 9.18% (215), $133.82 | 157 (85 unfilled) | 18.61% [-1.02%, 38.91%] | $335.07 | 137 (78 unfilled) | 8.87% [-5.58%, 22.97%] | $83.68 |
| series | 2026-07 | 513 | 0.619201 | 0.609705 | 0.614447 | 2.31% (379), $1.37 | 0.73% (342), $19.57 | 241 (138 unfilled) | 1.22% [-15.12%, 20.49%] | $32.27 | 214 (128 unfilled) | -1.67% [-16.10%, 16.17%] | $12.99 |
| series | 2026-08 | 717 | 0.598945 | 0.591806 | 0.614837 | 6.82% (556), $81.61 | 11.63% (449), $638.21 | 272 (284 unfilled) | 2.38% [-12.87%, 18.77%] | $47.37 | 219 (230 unfilled) | 13.25% [-3.09%, 31.47%] | $328.44 |
| series | 2026-09 | 914 | 0.589270 | 0.582209 | 0.602664 | 5.56% (676), $40.70 | 14.89% (535), $2967.71 | 377 (299 unfilled) | -5.18% [-17.19%, 6.83%] | $5.78 | 305 (230 unfilled) | 3.61% [-6.48%, 14.26%] | $160.16 |
| series | 2026-10 | 772 | 0.586725 | 0.575606 | 0.585736 | 0.95% (538), $14.20 | 6.23% (439), $208.24 | 335 (203 unfilled) | -1.48% [-13.61%, 11.03%] | $36.47 | 267 (172 unfilled) | 4.02% [-6.76%, 13.82%] | $80.60 |

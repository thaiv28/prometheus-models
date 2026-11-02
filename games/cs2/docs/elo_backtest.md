# Elo variants benchmark

## Combined summary (validation, all sections)

| Model | Series Δ log loss | Series flat ROI | Series Kelly (LoL caps) $ | Series flat ROI depth-capped | Series Kelly depth-capped $ | Map Δ log loss | Map flat ROI | Map Kelly (LoL caps) $ | Map flat ROI depth-capped | Map Kelly depth-capped $ | Series blended Δ log loss | Series blended flat ROI | Series blended Kelly (LoL caps) $ | Series blended flat ROI depth-capped | Series blended Kelly depth-capped $ | Map blended Δ log loss | Map blended flat ROI | Map blended Kelly (LoL caps) $ | Map blended flat ROI depth-capped | Map blended Kelly depth-capped $ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| team_elo | 0.020181 | -6.01% | $0.09 | -5.04% | $0.07 | 0.023144 | -6.49% | $0.09 | -13.47% | $0.09 | -0.001482 | 2.74% | $19.26 | 5.21% | $101.79 | 0.001097 | -2.31% | $27.38 | -5.97% | $28.26 |
| player_round_glicko | -0.000027 | 2.99% | $0.04 | 0.74% | $0.08 | 0.005952 | -5.22% | $0.08 | -15.32% | $0.08 | -0.011444 | 8.32% | $11754.34 | 5.42% | $922.50 | -0.002606 | 2.34% | $458.93 | -6.20% | $19.97 |
| player_round_glicko_rookie_weights | -0.005690 | 3.25% | $0.07 | 0.65% | $0.07 | 0.004238 | -4.69% | $0.09 | -17.41% | $0.07 | -0.014685 | 9.35% | $11021.94 | 5.93% | $911.00 | -0.003129 | 4.14% | $389.66 | -6.21% | $12.70 |
| team_elo+none | 0.020181 | -6.01% | $0.09 | -5.04% | $0.07 | 0.023144 | -6.49% | $0.09 | -13.47% | $0.09 | -0.001482 | 2.74% | $19.26 | 5.21% | $101.79 | 0.001097 | -2.31% | $27.38 | -5.97% | $28.26 |
| player_round_glicko+none | -0.000027 | 2.99% | $0.04 | 0.74% | $0.08 | 0.005952 | -5.22% | $0.08 | -15.32% | $0.08 | -0.011444 | 8.32% | $11754.34 | 5.42% | $922.50 | -0.002606 | 2.34% | $458.93 | -6.20% | $19.97 |
| player_round_glicko_rookie_weights+none | -0.005690 | 3.25% | $0.07 | 0.65% | $0.07 | 0.004238 | -4.69% | $0.09 | -17.41% | $0.07 | -0.014685 | 9.35% | $11021.94 | 5.93% | $911.00 | -0.003129 | 4.14% | $389.66 | -6.21% | $12.70 |

Series temperatures (stage 1; p′ = σ(T·logit p), T < 1 pulls odds toward 50%): team_elo Bo3 0.71, Bo5 0.63; player_round_glicko_rookie_weights Bo3 0.88, Bo5 0.67; player_round_glicko Bo3 0.83, Bo5 0.60; team_elo+none Bo3 0.71, Bo5 0.63; player_round_glicko+none Bo3 0.83, Bo5 0.60; player_round_glicko_rookie_weights+none Bo3 0.88, Bo5 0.67

Parameters minimize tuning map log loss across all sections. Replay predicts before update; Replay starts at the first map. Tuning: [2024-01-01, 2026-01-01); validation: [2026-01-01, 2026-11-01). Holdout is scored only with --holdout and never selects parameters. Series use the first map prediction and independent maps in an odd best-of; missing/even best-of or unknown results are skipped. Accuracy gives 0.5 predictions half credit; ECE uses 10 equal-width bins. Log loss clips probabilities at 1e-6. Paired bootstrap uses 2,000 resamples, seed 0, clustered by match_id. Differences are the named model minus its comparator; negative favors the model. Significance requires a 95% percentile interval excluding zero. Tuning scores are selection diagnostics, not independent evidence of improvement.

Fit through 2025-12-31. Unknown host-region map rows: 911 (including missing/un).

## Stage 1 — tuning (outcomes)

### Leaderboard

| Model | Best params | Map log loss | Series log loss | Rows |
|---|---|---:|---:|---:|
| player_round_glicko_rookie_weights | {"k": 32, "new_player": "teammates", "online_k": 1.0, "rd_info": 0.125, "rd_new": 350, "rookie_maps": 400, "rookie_penalty": 200, "tau": 0.5, "tier3_k": 0.75} | 0.629726 | 0.598899 | 73819 |
| player_round_glicko | {"k": 32, "new_player": "teammates", "rd_info": 0.125, "rd_new": 350, "tau": 0.5} | 0.639912 | 0.618440 | 73819 |
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
| player_round_glicko | all | 73819 | 0.639912 | 0.224880 | 0.626993 | 0.020898 |
| player_round_glicko | tier1 | 4470 | 0.664719 | 0.235945 | 0.596532 | 0.016189 |
| player_round_glicko | tier2 | 18909 | 0.648033 | 0.228670 | 0.614549 | 0.016297 |
| player_round_glicko | tier3 | 50234 | 0.634639 | 0.222458 | 0.634570 | 0.023351 |
| player_round_glicko | unknown | 206 | 0.642020 | 0.227562 | 0.582524 | 0.068986 |
| player_round_glicko | international=1 | 2557 | 0.660377 | 0.234218 | 0.602464 | 0.020095 |
| player_round_glicko | international=0 | 71262 | 0.639178 | 0.224545 | 0.627873 | 0.021382 |

player_round_glicko − coin (paired log loss):

| Section | Rows | player_round_glicko log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 73819 | 0.639912 | 0.693147 | -0.053235 | [-0.055649, -0.050830] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko_rookie_weights | all | 73819 | 0.629726 | 0.220381 | 0.639199 | 0.016483 |
| player_round_glicko_rookie_weights | tier1 | 4470 | 0.661394 | 0.234129 | 0.609060 | 0.021726 |
| player_round_glicko_rookie_weights | tier2 | 18909 | 0.645455 | 0.227376 | 0.619520 | 0.014379 |
| player_round_glicko_rookie_weights | tier3 | 50234 | 0.620999 | 0.216524 | 0.649321 | 0.017969 |
| player_round_glicko_rookie_weights | unknown | 206 | 0.626999 | 0.220618 | 0.631068 | 0.070928 |
| player_round_glicko_rookie_weights | international=1 | 2557 | 0.656234 | 0.232395 | 0.615761 | 0.025392 |
| player_round_glicko_rookie_weights | international=0 | 71262 | 0.628775 | 0.219950 | 0.640040 | 0.016919 |

player_round_glicko_rookie_weights − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie_weights log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 73819 | 0.629726 | 0.693147 | -0.063421 | [-0.065995, -0.060907] | yes |

player_round_glicko_rookie_weights − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie_weights log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 73819 | 0.629726 | 0.660656 | -0.030930 | [-0.032890, -0.029053] | yes |

player_round_glicko − team_elo (paired log loss):

| Section | Rows | player_round_glicko log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 73819 | 0.639912 | 0.660656 | -0.020744 | [-0.022501, -0.019061] | yes |

player_round_glicko − player_round_glicko_rookie_weights (paired log loss):

| Section | Rows | player_round_glicko log loss | player_round_glicko_rookie_weights log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 73819 | 0.639912 | 0.629726 | 0.010186 | [0.009240, 0.011171] | yes |

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
| player_round_glicko | all | 35914 | 0.618440 | 0.214885 | 0.654745 | 0.028789 |
| player_round_glicko | tier1 | 2047 | 0.649243 | 0.228182 | 0.624573 | 0.024761 |
| player_round_glicko | tier2 | 8853 | 0.623148 | 0.217463 | 0.645996 | 0.028937 |
| player_round_glicko | tier3 | 24957 | 0.614013 | 0.212771 | 0.660736 | 0.031273 |
| player_round_glicko | unknown | 57 | 0.719439 | 0.262146 | 0.473684 | 0.160827 |
| player_round_glicko | international=1 | 1101 | 0.639511 | 0.224860 | 0.626249 | 0.019786 |
| player_round_glicko | international=0 | 34813 | 0.617774 | 0.214569 | 0.655646 | 0.029477 |

player_round_glicko − coin (paired log loss):

| Section | Rows | player_round_glicko log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 35914 | 0.618440 | 0.693147 | -0.074707 | [-0.078501, -0.070858] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko_rookie_weights | all | 35914 | 0.598899 | 0.206204 | 0.674862 | 0.022402 |
| player_round_glicko_rookie_weights | tier1 | 2047 | 0.645500 | 0.225097 | 0.637030 | 0.025680 |
| player_round_glicko_rookie_weights | tier2 | 8853 | 0.618569 | 0.214969 | 0.649667 | 0.022081 |
| player_round_glicko_rookie_weights | tier3 | 24957 | 0.587908 | 0.201458 | 0.687122 | 0.023886 |
| player_round_glicko_rookie_weights | unknown | 57 | 0.682427 | 0.244180 | 0.578947 | 0.104153 |
| player_round_glicko_rookie_weights | international=1 | 1101 | 0.633005 | 0.221803 | 0.645777 | 0.028229 |
| player_round_glicko_rookie_weights | international=0 | 34813 | 0.597820 | 0.205710 | 0.675782 | 0.023459 |

player_round_glicko_rookie_weights − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie_weights log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 35914 | 0.598899 | 0.693147 | -0.094248 | [-0.098398, -0.089793] | yes |

player_round_glicko_rookie_weights − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie_weights log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 35914 | 0.598899 | 0.645151 | -0.046252 | [-0.049631, -0.042863] | yes |

player_round_glicko − team_elo (paired log loss):

| Section | Rows | player_round_glicko log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 35914 | 0.618440 | 0.645151 | -0.026711 | [-0.029653, -0.023797] | yes |

player_round_glicko − player_round_glicko_rookie_weights (paired log loss):

| Section | Rows | player_round_glicko log loss | player_round_glicko_rookie_weights log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 35914 | 0.618440 | 0.598899 | 0.019541 | [0.017528, 0.021440] | yes |

## Stage 2 — validation (outcomes)

### Leaderboard (frozen stage-1 parameters)

| Model | Best params | Map log loss | Series log loss | Rows |
|---|---|---:|---:|---:|
| player_round_glicko_rookie_weights | {"k": 32, "new_player": "teammates", "online_k": 1.0, "rd_info": 0.125, "rd_new": 350, "rookie_maps": 400, "rookie_penalty": 200, "tau": 0.5, "tier3_k": 0.75} | 0.617970 | 0.578513 | 36077 |
| player_round_glicko_rookie_weights+none | {"k": 32, "new_player": "teammates", "online_k": 1.0, "rd_info": 0.125, "rd_new": 350, "rookie_maps": 400, "rookie_penalty": 200, "tau": 0.5, "tier3_k": 0.75} | 0.617970 | 0.578513 | 36077 |
| player_round_glicko | {"k": 32, "new_player": "teammates", "rd_info": 0.125, "rd_new": 350, "tau": 0.5} | 0.625535 | 0.593884 | 36077 |
| player_round_glicko+none | {"k": 32, "new_player": "teammates", "rd_info": 0.125, "rd_new": 350, "tau": 0.5} | 0.625535 | 0.593884 | 36077 |
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
| player_round_glicko | all | 36077 | 0.625535 | 0.218761 | 0.641946 | 0.018002 |
| player_round_glicko | tier1 | 2097 | 0.661062 | 0.234130 | 0.607773 | 0.021601 |
| player_round_glicko | tier2 | 9801 | 0.631050 | 0.221465 | 0.634680 | 0.015619 |
| player_round_glicko | tier3 | 23489 | 0.620963 | 0.216650 | 0.647495 | 0.019786 |
| player_round_glicko | unknown | 690 | 0.594881 | 0.205542 | 0.660145 | 0.055222 |
| player_round_glicko | international=1 | 1194 | 0.642367 | 0.225686 | 0.645310 | 0.041031 |
| player_round_glicko | international=0 | 34883 | 0.624959 | 0.218524 | 0.641831 | 0.018506 |

player_round_glicko − coin (paired log loss):

| Section | Rows | player_round_glicko log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 36077 | 0.625535 | 0.693147 | -0.067612 | [-0.071297, -0.063872] | yes |
| tier1 | 2097 | 0.661062 | 0.693147 | -0.032086 | [-0.043949, -0.020124] | yes |
| tier2 | 9801 | 0.631050 | 0.693147 | -0.062097 | [-0.068451, -0.055953] | yes |
| tier3 | 23489 | 0.620963 | 0.693147 | -0.072184 | [-0.076771, -0.067602] | yes |
| unknown | 690 | 0.594881 | 0.693147 | -0.098267 | [-0.125420, -0.070397] | yes |
| international=1 | 1194 | 0.642367 | 0.693147 | -0.050780 | [-0.066566, -0.035291] | yes |
| international=0 | 34883 | 0.624959 | 0.693147 | -0.068188 | [-0.072020, -0.064359] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko_rookie_weights | all | 36077 | 0.617970 | 0.215465 | 0.650969 | 0.016879 |
| player_round_glicko_rookie_weights | tier1 | 2097 | 0.658267 | 0.232960 | 0.608011 | 0.020642 |
| player_round_glicko_rookie_weights | tier2 | 9801 | 0.630059 | 0.220891 | 0.639731 | 0.024035 |
| player_round_glicko_rookie_weights | tier3 | 23489 | 0.610177 | 0.211993 | 0.659245 | 0.017335 |
| player_round_glicko_rookie_weights | unknown | 690 | 0.589089 | 0.203407 | 0.659420 | 0.061521 |
| player_round_glicko_rookie_weights | international=1 | 1194 | 0.639370 | 0.224329 | 0.641541 | 0.036332 |
| player_round_glicko_rookie_weights | international=0 | 34883 | 0.617237 | 0.215162 | 0.651291 | 0.017460 |

player_round_glicko_rookie_weights − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie_weights log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 36077 | 0.617970 | 0.693147 | -0.075177 | [-0.078988, -0.071249] | yes |
| tier1 | 2097 | 0.658267 | 0.693147 | -0.034880 | [-0.046669, -0.022883] | yes |
| tier2 | 9801 | 0.630059 | 0.693147 | -0.063088 | [-0.069578, -0.056883] | yes |
| tier3 | 23489 | 0.610177 | 0.693147 | -0.082971 | [-0.087831, -0.078232] | yes |
| unknown | 690 | 0.589089 | 0.693147 | -0.104058 | [-0.132340, -0.075507] | yes |
| international=1 | 1194 | 0.639370 | 0.693147 | -0.053777 | [-0.069783, -0.037306] | yes |
| international=0 | 34883 | 0.617237 | 0.693147 | -0.075910 | [-0.079627, -0.072014] | yes |

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
| player_round_glicko+none | all | 36077 | 0.625535 | 0.218761 | 0.641946 | 0.018002 |
| player_round_glicko+none | tier1 | 2097 | 0.661062 | 0.234130 | 0.607773 | 0.021601 |
| player_round_glicko+none | tier2 | 9801 | 0.631050 | 0.221465 | 0.634680 | 0.015619 |
| player_round_glicko+none | tier3 | 23489 | 0.620963 | 0.216650 | 0.647495 | 0.019786 |
| player_round_glicko+none | unknown | 690 | 0.594881 | 0.205542 | 0.660145 | 0.055222 |
| player_round_glicko+none | international=1 | 1194 | 0.642367 | 0.225686 | 0.645310 | 0.041031 |
| player_round_glicko+none | international=0 | 34883 | 0.624959 | 0.218524 | 0.641831 | 0.018506 |

player_round_glicko+none − coin (paired log loss):

| Section | Rows | player_round_glicko+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 36077 | 0.625535 | 0.693147 | -0.067612 | [-0.071297, -0.063872] | yes |
| tier1 | 2097 | 0.661062 | 0.693147 | -0.032086 | [-0.043949, -0.020124] | yes |
| tier2 | 9801 | 0.631050 | 0.693147 | -0.062097 | [-0.068451, -0.055953] | yes |
| tier3 | 23489 | 0.620963 | 0.693147 | -0.072184 | [-0.076771, -0.067602] | yes |
| unknown | 690 | 0.594881 | 0.693147 | -0.098267 | [-0.125420, -0.070397] | yes |
| international=1 | 1194 | 0.642367 | 0.693147 | -0.050780 | [-0.066566, -0.035291] | yes |
| international=0 | 34883 | 0.624959 | 0.693147 | -0.068188 | [-0.072020, -0.064359] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko_rookie_weights+none | all | 36077 | 0.617970 | 0.215465 | 0.650969 | 0.016879 |
| player_round_glicko_rookie_weights+none | tier1 | 2097 | 0.658267 | 0.232960 | 0.608011 | 0.020642 |
| player_round_glicko_rookie_weights+none | tier2 | 9801 | 0.630059 | 0.220891 | 0.639731 | 0.024035 |
| player_round_glicko_rookie_weights+none | tier3 | 23489 | 0.610177 | 0.211993 | 0.659245 | 0.017335 |
| player_round_glicko_rookie_weights+none | unknown | 690 | 0.589089 | 0.203407 | 0.659420 | 0.061521 |
| player_round_glicko_rookie_weights+none | international=1 | 1194 | 0.639370 | 0.224329 | 0.641541 | 0.036332 |
| player_round_glicko_rookie_weights+none | international=0 | 34883 | 0.617237 | 0.215162 | 0.651291 | 0.017460 |

player_round_glicko_rookie_weights+none − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie_weights+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 36077 | 0.617970 | 0.693147 | -0.075177 | [-0.078988, -0.071249] | yes |
| tier1 | 2097 | 0.658267 | 0.693147 | -0.034880 | [-0.046669, -0.022883] | yes |
| tier2 | 9801 | 0.630059 | 0.693147 | -0.063088 | [-0.069578, -0.056883] | yes |
| tier3 | 23489 | 0.610177 | 0.693147 | -0.082971 | [-0.087831, -0.078232] | yes |
| unknown | 690 | 0.589089 | 0.693147 | -0.104058 | [-0.132340, -0.075507] | yes |
| international=1 | 1194 | 0.639370 | 0.693147 | -0.053777 | [-0.069783, -0.037306] | yes |
| international=0 | 34883 | 0.617237 | 0.693147 | -0.075910 | [-0.079627, -0.072014] | yes |

player_round_glicko − team_elo (paired log loss):

| Section | Rows | player_round_glicko log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 36077 | 0.625535 | 0.650234 | -0.024698 | [-0.027319, -0.022143] | yes |

player_round_glicko_rookie_weights − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie_weights log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 36077 | 0.617970 | 0.650234 | -0.032264 | [-0.035030, -0.029415] | yes |

team_elo+none − team_elo (paired log loss):

| Section | Rows | team_elo+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 36077 | 0.650234 | 0.650234 | 0.000000 | [0.000000, 0.000000] | no |

player_round_glicko+none − team_elo (paired log loss):

| Section | Rows | player_round_glicko+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 36077 | 0.625535 | 0.650234 | -0.024698 | [-0.027319, -0.022143] | yes |

player_round_glicko_rookie_weights+none − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie_weights+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 36077 | 0.617970 | 0.650234 | -0.032264 | [-0.035030, -0.029415] | yes |

player_round_glicko − player_round_glicko_rookie_weights (paired log loss):

| Section | Rows | player_round_glicko log loss | player_round_glicko_rookie_weights log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 36077 | 0.625535 | 0.617970 | 0.007565 | [0.006255, 0.008865] | yes |
| tier1 | 2097 | 0.661062 | 0.658267 | 0.002795 | [0.000890, 0.004862] | yes |
| tier2 | 9801 | 0.631050 | 0.630059 | 0.000992 | [-0.000524, 0.002275] | no |
| tier3 | 23489 | 0.620963 | 0.610177 | 0.010786 | [0.008816, 0.012636] | yes |
| unknown | 690 | 0.594881 | 0.589089 | 0.005791 | [0.000926, 0.011293] | yes |
| international=1 | 1194 | 0.642367 | 0.639370 | 0.002997 | [0.000546, 0.005837] | yes |
| international=0 | 34883 | 0.624959 | 0.617237 | 0.007722 | [0.006397, 0.009012] | yes |

team_elo+none − player_round_glicko_rookie_weights (paired log loss):

| Section | Rows | team_elo+none log loss | player_round_glicko_rookie_weights log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 36077 | 0.650234 | 0.617970 | 0.032264 | [0.029415, 0.035030] | yes |
| tier1 | 2097 | 0.671551 | 0.658267 | 0.013285 | [0.003996, 0.023168] | yes |
| tier2 | 9801 | 0.656685 | 0.630059 | 0.026626 | [0.021810, 0.031527] | yes |
| tier3 | 23489 | 0.646743 | 0.610177 | 0.036566 | [0.032797, 0.040194] | yes |
| unknown | 690 | 0.612645 | 0.589089 | 0.023555 | [0.006583, 0.040913] | yes |
| international=1 | 1194 | 0.642206 | 0.639370 | 0.002836 | [-0.008680, 0.014083] | no |
| international=0 | 34883 | 0.650508 | 0.617237 | 0.033271 | [0.030315, 0.036131] | yes |

player_round_glicko+none − player_round_glicko_rookie_weights (paired log loss):

| Section | Rows | player_round_glicko+none log loss | player_round_glicko_rookie_weights log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 36077 | 0.625535 | 0.617970 | 0.007565 | [0.006255, 0.008865] | yes |
| tier1 | 2097 | 0.661062 | 0.658267 | 0.002795 | [0.000890, 0.004862] | yes |
| tier2 | 9801 | 0.631050 | 0.630059 | 0.000992 | [-0.000524, 0.002275] | no |
| tier3 | 23489 | 0.620963 | 0.610177 | 0.010786 | [0.008816, 0.012636] | yes |
| unknown | 690 | 0.594881 | 0.589089 | 0.005791 | [0.000926, 0.011293] | yes |
| international=1 | 1194 | 0.642367 | 0.639370 | 0.002997 | [0.000546, 0.005837] | yes |
| international=0 | 34883 | 0.624959 | 0.617237 | 0.007722 | [0.006397, 0.009012] | yes |

player_round_glicko_rookie_weights+none − player_round_glicko_rookie_weights (paired log loss):

| Section | Rows | player_round_glicko_rookie_weights+none log loss | player_round_glicko_rookie_weights log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 36077 | 0.617970 | 0.617970 | 0.000000 | [0.000000, 0.000000] | no |
| tier1 | 2097 | 0.658267 | 0.658267 | 0.000000 | [0.000000, 0.000000] | no |
| tier2 | 9801 | 0.630059 | 0.630059 | 0.000000 | [0.000000, 0.000000] | no |
| tier3 | 23489 | 0.610177 | 0.610177 | 0.000000 | [0.000000, 0.000000] | no |
| unknown | 690 | 0.589089 | 0.589089 | 0.000000 | [0.000000, 0.000000] | no |
| international=1 | 1194 | 0.639370 | 0.639370 | 0.000000 | [0.000000, 0.000000] | no |
| international=0 | 34883 | 0.617237 | 0.617237 | 0.000000 | [0.000000, 0.000000] | no |

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
| player_round_glicko | all | 16918 | 0.593884 | 0.204562 | 0.678449 | 0.025728 |
| player_round_glicko | tier1 | 897 | 0.641465 | 0.224830 | 0.639353 | 0.048380 |
| player_round_glicko | tier2 | 4498 | 0.596690 | 0.206207 | 0.674744 | 0.024515 |
| player_round_glicko | tier3 | 11240 | 0.590349 | 0.202790 | 0.682206 | 0.027831 |
| player_round_glicko | unknown | 283 | 0.538855 | 0.184548 | 0.712014 | 0.092923 |
| player_round_glicko | international=1 | 503 | 0.612139 | 0.212267 | 0.676938 | 0.063564 |
| player_round_glicko | international=0 | 16415 | 0.593324 | 0.204326 | 0.678495 | 0.026517 |

player_round_glicko − coin (paired log loss):

| Section | Rows | player_round_glicko log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 16918 | 0.593884 | 0.693147 | -0.099263 | [-0.105071, -0.093252] | yes |
| tier1 | 897 | 0.641465 | 0.693147 | -0.051682 | [-0.071615, -0.029722] | yes |
| tier2 | 4498 | 0.596690 | 0.693147 | -0.096457 | [-0.107072, -0.086037] | yes |
| tier3 | 11240 | 0.590349 | 0.693147 | -0.102798 | [-0.110324, -0.095206] | yes |
| unknown | 283 | 0.538855 | 0.693147 | -0.154292 | [-0.195252, -0.111238] | yes |
| international=1 | 503 | 0.612139 | 0.693147 | -0.081008 | [-0.107593, -0.053916] | yes |
| international=0 | 16415 | 0.593324 | 0.693147 | -0.099823 | [-0.105855, -0.093565] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko_rookie_weights | all | 16918 | 0.578513 | 0.197952 | 0.694172 | 0.022368 |
| player_round_glicko_rookie_weights | tier1 | 897 | 0.637813 | 0.223243 | 0.643255 | 0.037363 |
| player_round_glicko_rookie_weights | tier2 | 4498 | 0.592976 | 0.204689 | 0.681859 | 0.030145 |
| player_round_glicko_rookie_weights | tier3 | 11240 | 0.569292 | 0.193679 | 0.702980 | 0.021657 |
| player_round_glicko_rookie_weights | unknown | 283 | 0.526917 | 0.180399 | 0.701413 | 0.085049 |
| player_round_glicko_rookie_weights | international=1 | 503 | 0.607853 | 0.210378 | 0.679920 | 0.056016 |
| player_round_glicko_rookie_weights | international=0 | 16415 | 0.577614 | 0.197571 | 0.694609 | 0.022375 |

player_round_glicko_rookie_weights − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie_weights log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 16918 | 0.578513 | 0.693147 | -0.114634 | [-0.121108, -0.108188] | yes |
| tier1 | 897 | 0.637813 | 0.693147 | -0.055334 | [-0.075993, -0.031737] | yes |
| tier2 | 4498 | 0.592976 | 0.693147 | -0.100171 | [-0.111271, -0.089117] | yes |
| tier3 | 11240 | 0.569292 | 0.693147 | -0.123855 | [-0.131835, -0.115551] | yes |
| unknown | 283 | 0.526917 | 0.693147 | -0.166230 | [-0.208570, -0.122726] | yes |
| international=1 | 503 | 0.607853 | 0.693147 | -0.085295 | [-0.113644, -0.056001] | yes |
| international=0 | 16415 | 0.577614 | 0.693147 | -0.115533 | [-0.122006, -0.108685] | yes |

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
| player_round_glicko+none | all | 16918 | 0.593884 | 0.204562 | 0.678449 | 0.025728 |
| player_round_glicko+none | tier1 | 897 | 0.641465 | 0.224830 | 0.639353 | 0.048380 |
| player_round_glicko+none | tier2 | 4498 | 0.596690 | 0.206207 | 0.674744 | 0.024515 |
| player_round_glicko+none | tier3 | 11240 | 0.590349 | 0.202790 | 0.682206 | 0.027831 |
| player_round_glicko+none | unknown | 283 | 0.538855 | 0.184548 | 0.712014 | 0.092923 |
| player_round_glicko+none | international=1 | 503 | 0.612139 | 0.212267 | 0.676938 | 0.063564 |
| player_round_glicko+none | international=0 | 16415 | 0.593324 | 0.204326 | 0.678495 | 0.026517 |

player_round_glicko+none − coin (paired log loss):

| Section | Rows | player_round_glicko+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 16918 | 0.593884 | 0.693147 | -0.099263 | [-0.105071, -0.093252] | yes |
| tier1 | 897 | 0.641465 | 0.693147 | -0.051682 | [-0.071615, -0.029722] | yes |
| tier2 | 4498 | 0.596690 | 0.693147 | -0.096457 | [-0.107072, -0.086037] | yes |
| tier3 | 11240 | 0.590349 | 0.693147 | -0.102798 | [-0.110324, -0.095206] | yes |
| unknown | 283 | 0.538855 | 0.693147 | -0.154292 | [-0.195252, -0.111238] | yes |
| international=1 | 503 | 0.612139 | 0.693147 | -0.081008 | [-0.107593, -0.053916] | yes |
| international=0 | 16415 | 0.593324 | 0.693147 | -0.099823 | [-0.105855, -0.093565] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko_rookie_weights+none | all | 16918 | 0.578513 | 0.197952 | 0.694172 | 0.022368 |
| player_round_glicko_rookie_weights+none | tier1 | 897 | 0.637813 | 0.223243 | 0.643255 | 0.037363 |
| player_round_glicko_rookie_weights+none | tier2 | 4498 | 0.592976 | 0.204689 | 0.681859 | 0.030145 |
| player_round_glicko_rookie_weights+none | tier3 | 11240 | 0.569292 | 0.193679 | 0.702980 | 0.021657 |
| player_round_glicko_rookie_weights+none | unknown | 283 | 0.526917 | 0.180399 | 0.701413 | 0.085049 |
| player_round_glicko_rookie_weights+none | international=1 | 503 | 0.607853 | 0.210378 | 0.679920 | 0.056016 |
| player_round_glicko_rookie_weights+none | international=0 | 16415 | 0.577614 | 0.197571 | 0.694609 | 0.022375 |

player_round_glicko_rookie_weights+none − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie_weights+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 16918 | 0.578513 | 0.693147 | -0.114634 | [-0.121108, -0.108188] | yes |
| tier1 | 897 | 0.637813 | 0.693147 | -0.055334 | [-0.075993, -0.031737] | yes |
| tier2 | 4498 | 0.592976 | 0.693147 | -0.100171 | [-0.111271, -0.089117] | yes |
| tier3 | 11240 | 0.569292 | 0.693147 | -0.123855 | [-0.131835, -0.115551] | yes |
| unknown | 283 | 0.526917 | 0.693147 | -0.166230 | [-0.208570, -0.122726] | yes |
| international=1 | 503 | 0.607853 | 0.693147 | -0.085295 | [-0.113644, -0.056001] | yes |
| international=0 | 16415 | 0.577614 | 0.693147 | -0.115533 | [-0.122006, -0.108685] | yes |

player_round_glicko − team_elo (paired log loss):

| Section | Rows | player_round_glicko log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 16918 | 0.593884 | 0.626402 | -0.032518 | [-0.036985, -0.028192] | yes |

player_round_glicko_rookie_weights − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie_weights log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 16918 | 0.578513 | 0.626402 | -0.047889 | [-0.052704, -0.043136] | yes |

team_elo+none − team_elo (paired log loss):

| Section | Rows | team_elo+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 16918 | 0.626402 | 0.626402 | 0.000000 | [0.000000, 0.000000] | no |

player_round_glicko+none − team_elo (paired log loss):

| Section | Rows | player_round_glicko+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 16918 | 0.593884 | 0.626402 | -0.032518 | [-0.036985, -0.028192] | yes |

player_round_glicko_rookie_weights+none − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie_weights+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 16918 | 0.578513 | 0.626402 | -0.047889 | [-0.052704, -0.043136] | yes |

player_round_glicko − player_round_glicko_rookie_weights (paired log loss):

| Section | Rows | player_round_glicko log loss | player_round_glicko_rookie_weights log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 16918 | 0.593884 | 0.578513 | 0.015371 | [0.012591, 0.018221] | yes |
| tier1 | 897 | 0.641465 | 0.637813 | 0.003652 | [0.000223, 0.006788] | yes |
| tier2 | 4498 | 0.596690 | 0.592976 | 0.003714 | [0.000874, 0.006511] | yes |
| tier3 | 11240 | 0.590349 | 0.569292 | 0.021057 | [0.017007, 0.024963] | yes |
| unknown | 283 | 0.538855 | 0.526917 | 0.011938 | [0.000319, 0.023591] | yes |
| international=1 | 503 | 0.612139 | 0.607853 | 0.004287 | [-0.000308, 0.008606] | no |
| international=0 | 16415 | 0.593324 | 0.577614 | 0.015710 | [0.012941, 0.018802] | yes |

team_elo+none − player_round_glicko_rookie_weights (paired log loss):

| Section | Rows | team_elo+none log loss | player_round_glicko_rookie_weights log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 16918 | 0.626402 | 0.578513 | 0.047889 | [0.043136, 0.052704] | yes |
| tier1 | 897 | 0.645834 | 0.637813 | 0.008021 | [-0.008940, 0.024655] | no |
| tier2 | 4498 | 0.633288 | 0.592976 | 0.040312 | [0.032486, 0.048833] | yes |
| tier3 | 11240 | 0.623778 | 0.569292 | 0.054486 | [0.047732, 0.060864] | yes |
| unknown | 283 | 0.559580 | 0.526917 | 0.032663 | [0.005823, 0.060436] | yes |
| international=1 | 503 | 0.606870 | 0.607853 | -0.000982 | [-0.018607, 0.016099] | no |
| international=0 | 16415 | 0.627000 | 0.577614 | 0.049386 | [0.044264, 0.054453] | yes |

player_round_glicko+none − player_round_glicko_rookie_weights (paired log loss):

| Section | Rows | player_round_glicko+none log loss | player_round_glicko_rookie_weights log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 16918 | 0.593884 | 0.578513 | 0.015371 | [0.012591, 0.018221] | yes |
| tier1 | 897 | 0.641465 | 0.637813 | 0.003652 | [0.000223, 0.006788] | yes |
| tier2 | 4498 | 0.596690 | 0.592976 | 0.003714 | [0.000874, 0.006511] | yes |
| tier3 | 11240 | 0.590349 | 0.569292 | 0.021057 | [0.017007, 0.024963] | yes |
| unknown | 283 | 0.538855 | 0.526917 | 0.011938 | [0.000319, 0.023591] | yes |
| international=1 | 503 | 0.612139 | 0.607853 | 0.004287 | [-0.000308, 0.008606] | no |
| international=0 | 16415 | 0.593324 | 0.577614 | 0.015710 | [0.012941, 0.018802] | yes |

player_round_glicko_rookie_weights+none − player_round_glicko_rookie_weights (paired log loss):

| Section | Rows | player_round_glicko_rookie_weights+none log loss | player_round_glicko_rookie_weights log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 16918 | 0.578513 | 0.578513 | 0.000000 | [0.000000, 0.000000] | no |
| tier1 | 897 | 0.637813 | 0.637813 | 0.000000 | [0.000000, 0.000000] | no |
| tier2 | 4498 | 0.592976 | 0.592976 | 0.000000 | [0.000000, 0.000000] | no |
| tier3 | 11240 | 0.569292 | 0.569292 | 0.000000 | [0.000000, 0.000000] | no |
| unknown | 283 | 0.526917 | 0.526917 | 0.000000 | [0.000000, 0.000000] | no |
| international=1 | 503 | 0.607853 | 0.607853 | 0.000000 | [0.000000, 0.000000] | no |
| international=0 | 16415 | 0.577614 | 0.577614 | 0.000000 | [0.000000, 0.000000] | no |

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
| series | all | 4456 | 0.600331 | 0.600358 | -0.000027 [-0.008019, 0.007842] | no |
| series | tier1 | 725 | 0.632427 | 0.616830 | 0.015597 [-0.001403, 0.032254] | no |
| series | tier2 | 1962 | 0.597128 | 0.590722 | 0.006406 [-0.003882, 0.017192] | no |
| series | tier3 | 1727 | 0.593099 | 0.607536 | -0.014437 [-0.028553, 0.000194] | no |
| series | unknown | 42 | 0.493300 | 0.471027 | 0.022272 [-0.038790, 0.082968] | no |
| series | international=1 | 448 | 0.604953 | 0.591446 | 0.013507 [-0.009687, 0.034181] | no |
| series | international=0 | 4008 | 0.599815 | 0.601354 | -0.001540 [-0.010026, 0.006759] | no |
| map | all | 4477 | 0.640741 | 0.634789 | 0.005952 [0.000085, 0.011944] | yes |
| map | tier1 | 1176 | 0.656614 | 0.646419 | 0.010195 [-0.001834, 0.021495] | no |
| map | tier2 | 1968 | 0.637327 | 0.631291 | 0.006036 [-0.002158, 0.014120] | no |
| map | tier3 | 1279 | 0.633805 | 0.632601 | 0.001205 [-0.011508, 0.014028] | no |
| map | unknown | 54 | 0.583784 | 0.560856 | 0.022928 [-0.011339, 0.059749] | no |
| map | international=1 | 788 | 0.636177 | 0.630059 | 0.006118 [-0.008416, 0.019902] | no |
| map | international=0 | 3689 | 0.641717 | 0.635800 | 0.005917 [-0.000212, 0.012186] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 3288 | 3283 | 0.0817 | 2.99% [-1.33%, 7.16%] | $0.04 | 0.001× | 99.95% | $8.90 | 2083 (1205 unfilled) | 0.74% [-4.73%, 6.11%] | $0.08 |
| series | tier1 | 532 | 532 | 0.0769 | 0.49% [-11.73%, 12.73%] | $0.09 | 0.002× | 99.92% | $11.52 | 434 (98 unfilled) | -2.33% [-15.95%, 10.12%] | $0.10 |
| series | tier2 | 1387 | 1384 | 0.0720 | -1.66% [-7.84%, 4.80%] | $0.05 | 0.001× | 99.97% | $18.18 | 863 (524 unfilled) | -3.50% [-11.28%, 4.31%] | $0.09 |
| series | tier3 | 1336 | 1334 | 0.0940 | 9.30% [2.65%, 16.53%] | $5246.83 | 104.937× | 85.25% | $249.12 | 764 (572 unfilled) | 7.69% [-1.34%, 16.51%] | $78.44 |
| series | unknown | 33 | 33 | 0.0757 | -16.68% [-47.60%, 16.01%] | $31.32 | 0.626× | 41.12% | $5.10 | 22 (11 unfilled) | -13.08% [-54.22%, 30.96%] | $36.40 |
| series | international=1 | 335 | 335 | 0.0776 | 2.13% [-13.50%, 18.96%] | $1.07 | 0.021× | 99.31% | $10.43 | 292 (43 unfilled) | -2.27% [-17.85%, 13.89%] | $0.75 |
| series | international=0 | 2953 | 2948 | 0.0822 | 3.08% [-1.38%, 7.71%] | $0.03 | 0.001× | 99.96% | $6.25 | 1791 (1162 unfilled) | 1.24% [-4.43%, 6.97%] | $0.07 |
| map | all | 2852 | 1806 | 0.0592 | -5.22% [-9.44%, -0.75%] | $0.08 | 0.002× | 99.97% | $27.75 | 831 (2021 unfilled) | -15.32% [-22.68%, -7.88%] | $0.08 |
| map | tier1 | 753 | 512 | 0.0586 | -5.60% [-14.51%, 3.59%] | $3.42 | 0.068× | 96.05% | $6.47 | 231 (522 unfilled) | -8.11% [-24.17%, 8.53%] | $12.13 |
| map | tier2 | 1213 | 750 | 0.0535 | -4.30% [-10.95%, 2.85%] | $0.08 | 0.002× | 99.95% | $14.50 | 344 (869 unfilled) | -17.84% [-28.61%, -7.07%] | $0.17 |
| map | tier3 | 856 | 524 | 0.0683 | -5.94% [-13.84%, 2.07%] | $5.15 | 0.103× | 98.40% | $17.61 | 244 (612 unfilled) | -18.70% [-32.45%, -3.84%] | $6.17 |
| map | unknown | 30 | 20 | 0.0481 | -12.93% [-43.17%, 18.88%] | $38.22 | 0.764× | 27.55% | $4.78 | 12 (18 unfilled) | -13.86% [-51.82%, 16.78%] | $46.31 |
| map | international=1 | 501 | 345 | 0.0618 | -5.66% [-17.09%, 5.95%] | $20.10 | 0.402× | 88.61% | $17.01 | 161 (340 unfilled) | -4.68% [-26.39%, 16.27%] | $31.97 |
| map | international=0 | 2351 | 1461 | 0.0587 | -5.13% [-9.86%, -0.31%] | $0.09 | 0.002× | 99.92% | $11.11 | 670 (1681 unfilled) | -17.89% [-25.38%, -9.95%] | $0.07 |
| series+map | all | 6140 | 3615 | 0.0713 | -0.82% [-4.38%, 2.86%] | $0.06 | 0.001× | 99.90% | $6.19 | 2914 (3226 unfilled) | -3.84% [-8.60%, 1.27%] | $0.07 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2026-01-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 371 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-01 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-01 | map | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 51 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | map | 63 | 1.000000 | 0.000000 | unfitted |
| 2026-03 | series | 206 | 1.457683 | 0.670061 | fitted |
| 2026-03 | map | 165 | 1.268874 | 0.236759 | fitted |
| 2026-04 | series | 510 | 1.460757 | 0.822807 | fitted |
| 2026-04 | map | 309 | 1.201377 | 0.214366 | fitted |
| 2026-05 | series | 832 | 1.398567 | 0.750781 | fitted |
| 2026-05 | map | 582 | 1.323494 | 0.778151 | fitted |
| 2026-06 | series | 1192 | 1.401278 | 0.687585 | fitted |
| 2026-06 | map | 1034 | 1.361163 | 0.739254 | fitted |
| 2026-07 | series | 1540 | 1.310734 | 0.677269 | fitted |
| 2026-07 | map | 1448 | 1.300132 | 0.704951 | fitted |
| 2026-08 | series | 2053 | 1.244600 | 0.568115 | fitted |
| 2026-08 | map | 2066 | 1.163563 | 0.514510 | fitted |
| 2026-09 | series | 2770 | 1.238726 | 0.617065 | fitted |
| 2026-09 | map | 2939 | 1.226798 | 0.590978 | fitted |
| 2026-10 | series | 3684 | 1.241658 | 0.636202 | fitted |
| 2026-10 | map | 3818 | 1.209386 | 0.500274 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 4250 | 0.590150 | 0.601593 | -0.011444 [-0.016587, -0.006502] | yes |
| series | tier1 | 614 | 0.619079 | 0.616540 | 0.002539 [-0.007325, 0.012628] | no |
| series | tier2 | 1873 | 0.584260 | 0.593752 | -0.009491 [-0.016147, -0.002917] | yes |
| series | tier3 | 1721 | 0.589715 | 0.607981 | -0.018266 [-0.027801, -0.008953] | yes |
| series | unknown | 42 | 0.447665 | 0.471027 | -0.023362 [-0.054518, 0.008630] | no |
| series | international=1 | 370 | 0.585804 | 0.589385 | -0.003581 [-0.015200, 0.008417] | no |
| series | international=0 | 3880 | 0.590564 | 0.602757 | -0.012193 [-0.017534, -0.006768] | yes |
| map | all | 4312 | 0.632663 | 0.635269 | -0.002606 [-0.006224, 0.000974] | no |
| map | tier1 | 1046 | 0.652946 | 0.649504 | 0.003442 [-0.003219, 0.009729] | no |
| map | tier2 | 1936 | 0.626251 | 0.631140 | -0.004889 [-0.009714, 0.000001] | no |
| map | tier3 | 1276 | 0.629250 | 0.633014 | -0.003764 [-0.011538, 0.004686] | no |
| map | unknown | 54 | 0.550291 | 0.560856 | -0.010565 [-0.030483, 0.009099] | no |
| map | international=1 | 686 | 0.627415 | 0.629473 | -0.002058 [-0.008821, 0.005069] | no |
| map | international=0 | 3626 | 0.633656 | 0.636366 | -0.002710 [-0.006783, 0.001233] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 2489 | 2485 | 0.0475 | 8.32% [4.22%, 12.26%] | $11754.34 | 235.087× | 78.81% | $249.12 | 1558 (931 unfilled) | 5.42% [0.34%, 10.39%] | $922.50 |
| series | tier1 | 310 | 310 | 0.0346 | 2.19% [-10.21%, 15.21%] | $16.76 | 0.335× | 85.15% | $6.96 | 240 (70 unfilled) | 1.67% [-12.25%, 15.39%] | $27.72 |
| series | tier2 | 1079 | 1078 | 0.0423 | 6.61% [1.13%, 11.97%] | $4705.22 | 94.104× | 64.57% | $249.12 | 662 (417 unfilled) | 2.46% [-4.37%, 9.46%] | $120.60 |
| series | tier3 | 1070 | 1067 | 0.0567 | 11.92% [5.64%, 18.24%] | $11840.44 | 236.809× | 61.01% | $249.12 | 635 (435 unfilled) | 10.15% [1.62%, 18.89%] | $1154.78 |
| series | unknown | 30 | 30 | 0.0410 | 4.88% [-21.18%, 30.63%] | $65.01 | 1.300× | 10.87% | $6.17 | 21 (9 unfilled) | -1.53% [-34.48%, 34.52%] | $55.91 |
| series | international=1 | 181 | 181 | 0.0319 | 6.95% [-10.95%, 26.25%] | $92.01 | 1.840× | 43.85% | $11.04 | 148 (33 unfilled) | 6.24% [-12.00%, 25.74%] | $94.84 |
| series | international=0 | 2308 | 2304 | 0.0487 | 8.43% [4.39%, 12.53%] | $12357.45 | 247.149× | 77.84% | $249.12 | 1410 (898 unfilled) | 5.33% [0.37%, 10.54%] | $724.55 |
| map | all | 1757 | 1088 | 0.0328 | 2.34% [-2.67%, 7.68%] | $458.93 | 9.179× | 75.31% | $72.95 | 502 (1255 unfilled) | -6.20% [-14.42%, 2.99%] | $19.97 |
| map | tier1 | 334 | 218 | 0.0280 | -0.61% [-13.84%, 13.43%] | $32.27 | 0.645× | 75.98% | $8.18 | 109 (225 unfilled) | -5.07% [-28.02%, 19.81%] | $55.20 |
| map | tier2 | 770 | 474 | 0.0292 | 2.09% [-5.21%, 9.71%] | $176.82 | 3.536× | 48.19% | $29.04 | 203 (567 unfilled) | -10.63% [-22.22%, 0.42%] | $15.92 |
| map | tier3 | 633 | 383 | 0.0400 | 4.03% [-3.86%, 11.84%] | $230.02 | 4.600× | 66.85% | $36.25 | 181 (452 unfilled) | -2.57% [-16.04%, 11.38%] | $47.67 |
| map | unknown | 20 | 13 | 0.0257 | 8.29% [-18.89%, 34.91%] | $54.78 | 1.096× | 3.27% | $4.89 | 9 (11 unfilled) | 7.30% [-29.98%, 45.18%] | $55.53 |
| map | international=1 | 221 | 146 | 0.0273 | 8.70% [-8.77%, 28.20%] | $97.17 | 1.943× | 39.33% | $9.55 | 78 (143 unfilled) | 8.41% [-21.39%, 41.32%] | $86.05 |
| map | international=0 | 1536 | 942 | 0.0336 | 1.43% [-3.60%, 6.61%] | $266.26 | 5.325× | 75.35% | $37.57 | 424 (1112 unfilled) | -8.89% [-17.46%, -0.36%] | $10.54 |
| series+map | all | 4246 | 2614 | 0.0414 | 5.85% [2.13%, 9.35%] | $14190.61 | 283.812× | 65.22% | $249.47 | 2060 (2186 unfilled) | 2.59% [-2.15%, 7.63%] | $580.93 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-01 | 63 | 0.633585 | — | 0.638920 | 3.22% (41), $54.84 | — | 5 (36 unfilled) | -25.03% [-100.00%, 58.85%] | $49.65 | — | — | — |
| map | 2026-02 | 102 | 0.641808 | — | 0.611955 | -17.83% (58), $28.31 | — | 18 (40 unfilled) | -47.80% [-83.47%, -8.95%] | $28.98 | — | — | — |
| map | 2026-03 | 144 | 0.657710 | 0.642971 | 0.642845 | 1.52% (75), $42.01 | 14.98% (32), $63.94 | 39 (36 unfilled) | 1.15% [-40.11%, 44.68%] | $42.63 | 14 (18 unfilled) | 6.12% [-26.77%, 28.96%] | $52.60 |
| map | 2026-04 | 273 | 0.626009 | 0.639056 | 0.647894 | 11.72% (168), $236.70 | 61.15% (36), $66.70 | 52 (116 unfilled) | -13.61% [-40.22%, 14.08%] | $34.04 | 11 (25 unfilled) | -25.94% [-75.30%, 11.17%] | $48.39 |
| map | 2026-05 | 452 | 0.642149 | 0.630445 | 0.636432 | -2.19% (275), $35.93 | 7.26% (230), $88.24 | 91 (184 unfilled) | -0.37% [-23.96%, 22.88%] | $35.64 | 87 (143 unfilled) | 3.54% [-16.54%, 23.57%] | $46.28 |
| map | 2026-06 | 414 | 0.644375 | 0.643558 | 0.650163 | 1.83% (239), $68.71 | 3.05% (225), $96.76 | 45 (194 unfilled) | 5.31% [-24.98%, 36.10%] | $57.10 | 45 (180 unfilled) | 1.96% [-24.62%, 28.90%] | $59.07 |
| map | 2026-07 | 618 | 0.658436 | 0.654324 | 0.647047 | -7.53% (390), $5.14 | -5.37% (338), $16.23 | 94 (296 unfilled) | -13.22% [-34.71%, 8.41%] | $25.85 | 69 (269 unfilled) | -8.15% [-27.01%, 12.11%] | $46.44 |
| map | 2026-08 | 873 | 0.618828 | 0.612466 | 0.623251 | -2.89% (602), $9.37 | 7.79% (349), $344.21 | 117 (485 unfilled) | -9.16% [-29.49%, 11.96%] | $32.70 | 73 (276 unfilled) | 5.22% [-17.26%, 28.93%] | $49.68 |
| map | 2026-09 | 879 | 0.647175 | 0.633400 | 0.631507 | -9.29% (608), $0.29 | -5.94% (353), $37.68 | 222 (386 unfilled) | -19.20% [-34.76%, -2.57%] | $3.42 | 142 (211 unfilled) | -13.06% [-29.96%, 6.62%] | $39.68 |
| map | 2026-10 | 659 | 0.644262 | 0.627898 | 0.628124 | -14.10% (396), $0.10 | 1.50% (194), $40.93 | 148 (248 unfilled) | -31.80% [-48.11%, -15.70%] | $2.04 | 61 (133 unfilled) | -20.84% [-41.39%, -0.81%] | $24.62 |
| series | 2026-01 | 51 | 0.580685 | — | 0.602759 | 15.85% (43), $77.32 | — | 36 (7 unfilled) | 29.00% [-14.57%, 72.84%] | $82.93 | — | — | — |
| series | 2026-02 | 155 | 0.584041 | — | 0.565710 | -10.80% (114), $11.51 | — | 103 (11 unfilled) | -12.71% [-32.33%, 6.54%] | $11.55 | — | — | — |
| series | 2026-03 | 304 | 0.586470 | 0.572541 | 0.590480 | 2.51% (215), $36.70 | 10.96% (197), $298.87 | 163 (52 unfilled) | 2.03% [-15.73%, 20.61%] | $55.38 | 148 (49 unfilled) | 6.84% [-5.26%, 18.87%] | $142.46 |
| series | 2026-04 | 322 | 0.585328 | 0.569443 | 0.580957 | 2.57% (233), $11.81 | 8.11% (222), $160.14 | 175 (58 unfilled) | 4.11% [-15.12%, 26.07%] | $34.37 | 161 (61 unfilled) | 12.62% [-3.98%, 30.60%] | $130.88 |
| series | 2026-05 | 360 | 0.601616 | 0.578633 | 0.584764 | -7.90% (257), $3.26 | 3.55% (224), $41.72 | 210 (47 unfilled) | -8.82% [-25.57%, 7.16%] | $2.91 | 175 (49 unfilled) | 0.69% [-13.07%, 14.54%] | $37.31 |
| series | 2026-06 | 348 | 0.618771 | 0.625520 | 0.633931 | 9.29% (251), $241.58 | 9.77% (214), $75.82 | 166 (85 unfilled) | 17.16% [-2.58%, 36.87%] | $434.47 | 142 (72 unfilled) | 12.63% [-1.56%, 26.43%] | $71.01 |
| series | 2026-07 | 513 | 0.627085 | 0.614589 | 0.614447 | 3.61% (374), $0.90 | 0.06% (328), $20.19 | 237 (137 unfilled) | 0.22% [-16.39%, 18.92%] | $28.64 | 201 (127 unfilled) | -3.38% [-18.82%, 15.88%] | $20.31 |
| series | 2026-08 | 717 | 0.603501 | 0.596392 | 0.614837 | 7.45% (561), $42.07 | 10.94% (421), $696.51 | 272 (289 unfilled) | 1.04% [-13.89%, 17.26%] | $22.27 | 202 (219 unfilled) | 13.16% [-3.72%, 31.90%] | $335.97 |
| series | 2026-09 | 914 | 0.598134 | 0.587240 | 0.602664 | 2.35% (684), $2.46 | 11.78% (489), $1835.00 | 378 (306 unfilled) | -4.61% [-16.30%, 7.06%] | $0.01 | 287 (202 unfilled) | 1.74% [-9.41%, 13.78%] | $137.75 |
| series | 2026-10 | 772 | 0.589584 | 0.576552 | 0.585736 | 3.24% (556), $4.11 | 8.82% (394), $244.03 | 343 (213 unfilled) | 3.42% [-8.44%, 15.49%] | $30.80 | 242 (152 unfilled) | 4.17% [-7.07%, 15.01%] | $101.38 |

### player_round_glicko_rookie_weights: Kalshi comparison and returns



#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 4456 | 0.594668 | 0.600358 | -0.005690 [-0.013363, 0.002082] | no |
| series | tier1 | 725 | 0.628922 | 0.616830 | 0.012092 [-0.003900, 0.028033] | no |
| series | tier2 | 1962 | 0.594077 | 0.590722 | 0.003355 [-0.006731, 0.013978] | no |
| series | tier3 | 1727 | 0.583493 | 0.607536 | -0.024043 [-0.037968, -0.010048] | yes |
| series | unknown | 42 | 0.490548 | 0.471027 | 0.019521 [-0.044998, 0.082868] | no |
| series | international=1 | 448 | 0.600867 | 0.591446 | 0.009421 [-0.011559, 0.028817] | no |
| series | international=0 | 4008 | 0.593975 | 0.601354 | -0.007379 [-0.015579, 0.000557] | no |
| map | all | 4477 | 0.639028 | 0.634789 | 0.004238 [-0.001561, 0.009878] | no |
| map | tier1 | 1176 | 0.654442 | 0.646419 | 0.008023 [-0.003125, 0.018611] | no |
| map | tier2 | 1968 | 0.635842 | 0.631291 | 0.004551 [-0.003417, 0.012349] | no |
| map | tier3 | 1279 | 0.632071 | 0.632601 | -0.000530 [-0.012795, 0.011852] | no |
| map | unknown | 54 | 0.584221 | 0.560856 | 0.023365 [-0.010524, 0.059012] | no |
| map | international=1 | 788 | 0.633669 | 0.630059 | 0.003609 [-0.009543, 0.016984] | no |
| map | international=0 | 3689 | 0.640173 | 0.635800 | 0.004373 [-0.001764, 0.010770] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 3263 | 3258 | 0.0815 | 3.25% [-1.08%, 7.71%] | $0.07 | 0.001× | 99.94% | $12.17 | 2068 (1195 unfilled) | 0.65% [-4.71%, 5.91%] | $0.07 |
| series | tier1 | 527 | 527 | 0.0707 | -0.42% [-11.99%, 11.78%] | $0.09 | 0.002× | 99.94% | $15.55 | 428 (99 unfilled) | -2.47% [-15.20%, 9.51%] | $0.16 |
| series | tier2 | 1379 | 1376 | 0.0718 | -2.01% [-8.31%, 4.46%] | $0.08 | 0.002× | 99.96% | $21.31 | 857 (522 unfilled) | -3.90% [-11.60%, 3.95%] | $0.20 |
| series | tier3 | 1325 | 1323 | 0.0958 | 10.61% [3.78%, 17.20%] | $10891.33 | 217.827× | 79.33% | $249.12 | 761 (564 unfilled) | 7.96% [-0.62%, 17.05%] | $374.89 |
| series | unknown | 32 | 32 | 0.0821 | -14.10% [-45.28%, 20.91%] | $42.64 | 0.853× | 30.66% | $5.91 | 22 (10 unfilled) | -13.08% [-54.22%, 30.96%] | $41.56 |
| series | international=1 | 323 | 323 | 0.0714 | 0.45% [-16.07%, 16.60%] | $2.38 | 0.048× | 98.95% | $13.02 | 279 (44 unfilled) | -2.63% [-17.98%, 13.46%] | $1.06 |
| series | international=0 | 2940 | 2935 | 0.0826 | 3.56% [-0.78%, 8.44%] | $0.07 | 0.001× | 99.89% | $6.56 | 1789 (1151 unfilled) | 1.17% [-4.31%, 6.87%] | $18.47 |
| map | all | 2807 | 1791 | 0.0569 | -4.69% [-9.11%, 0.00%] | $0.09 | 0.002× | 99.97% | $32.46 | 813 (1994 unfilled) | -17.41% [-24.91%, -10.03%] | $0.07 |
| map | tier1 | 747 | 513 | 0.0541 | -4.55% [-13.26%, 4.66%] | $5.60 | 0.112× | 94.34% | $8.04 | 227 (520 unfilled) | -9.08% [-25.64%, 8.32%] | $9.75 |
| map | tier2 | 1182 | 741 | 0.0525 | -3.94% [-10.77%, 3.12%] | $0.09 | 0.002× | 99.94% | $13.16 | 336 (846 unfilled) | -19.55% [-30.64%, -8.32%] | $0.19 |
| map | tier3 | 848 | 516 | 0.0656 | -5.23% [-13.05%, 3.44%] | $2.27 | 0.045× | 99.21% | $15.51 | 239 (609 unfilled) | -22.35% [-35.75%, -8.58%] | $2.79 |
| map | unknown | 30 | 21 | 0.0481 | -22.79% [-53.00%, 6.46%] | $36.05 | 0.721× | 32.18% | $4.78 | 11 (19 unfilled) | -16.99% [-56.80%, 17.05%] | $46.45 |
| map | international=1 | 502 | 348 | 0.0560 | -4.02% [-15.32%, 8.04%] | $37.31 | 0.746× | 82.02% | $19.48 | 160 (342 unfilled) | -6.48% [-27.65%, 16.02%] | $30.90 |
| map | international=0 | 2305 | 1443 | 0.0571 | -4.84% [-9.28%, -0.03%] | $0.10 | 0.002× | 99.92% | $11.51 | 653 (1652 unfilled) | -20.09% [-27.79%, -12.31%] | $0.06 |
| series+map | all | 6070 | 3573 | 0.0701 | -0.42% [-4.14%, 3.14%] | $0.05 | 0.001× | 99.95% | $10.55 | 2881 (3189 unfilled) | -4.44% [-9.03%, 0.56%] | $0.07 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2026-01-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 371 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-01 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-01 | map | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 51 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | map | 63 | 1.000000 | 0.000000 | unfitted |
| 2026-03 | series | 206 | 1.442335 | 0.749188 | fitted |
| 2026-03 | map | 165 | 1.218435 | 0.060951 | fitted |
| 2026-04 | series | 510 | 1.426235 | 0.823474 | fitted |
| 2026-04 | map | 309 | 1.184503 | 0.160308 | fitted |
| 2026-05 | series | 832 | 1.372441 | 0.766276 | fitted |
| 2026-05 | map | 582 | 1.307760 | 0.755416 | fitted |
| 2026-06 | series | 1192 | 1.382460 | 0.712969 | fitted |
| 2026-06 | map | 1034 | 1.359719 | 0.758375 | fitted |
| 2026-07 | series | 1540 | 1.300636 | 0.724478 | fitted |
| 2026-07 | map | 1448 | 1.313794 | 0.756247 | fitted |
| 2026-08 | series | 2053 | 1.240113 | 0.630122 | fitted |
| 2026-08 | map | 2066 | 1.179309 | 0.573594 | fitted |
| 2026-09 | series | 2770 | 1.238566 | 0.673985 | fitted |
| 2026-09 | map | 2939 | 1.244446 | 0.638996 | fitted |
| 2026-10 | series | 3684 | 1.237434 | 0.696647 | fitted |
| 2026-10 | map | 3818 | 1.219471 | 0.534852 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 4250 | 0.586908 | 0.601593 | -0.014685 [-0.020248, -0.009415] | yes |
| series | tier1 | 614 | 0.619582 | 0.616540 | 0.003042 [-0.007231, 0.013817] | no |
| series | tier2 | 1873 | 0.583214 | 0.593752 | -0.010538 [-0.017771, -0.003506] | yes |
| series | tier3 | 1721 | 0.582688 | 0.607981 | -0.025292 [-0.035527, -0.015249] | yes |
| series | unknown | 42 | 0.446865 | 0.471027 | -0.024162 [-0.057715, 0.010999] | no |
| series | international=1 | 370 | 0.586676 | 0.589385 | -0.002709 [-0.014905, 0.009610] | no |
| series | international=0 | 3880 | 0.586930 | 0.602757 | -0.015827 [-0.021575, -0.010037] | yes |
| map | all | 4312 | 0.632141 | 0.635269 | -0.003129 [-0.006722, 0.000485] | no |
| map | tier1 | 1046 | 0.653568 | 0.649504 | 0.004064 [-0.002389, 0.010216] | no |
| map | tier2 | 1936 | 0.625422 | 0.631140 | -0.005718 [-0.010389, -0.001019] | yes |
| map | tier3 | 1276 | 0.628270 | 0.633014 | -0.004744 [-0.012676, 0.003750] | no |
| map | unknown | 54 | 0.549409 | 0.560856 | -0.011447 [-0.032465, 0.009312] | no |
| map | international=1 | 686 | 0.627575 | 0.629473 | -0.001898 [-0.008268, 0.005049] | no |
| map | international=0 | 3626 | 0.633004 | 0.636366 | -0.003362 [-0.007371, 0.000662] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 2651 | 2647 | 0.0511 | 9.35% [5.46%, 13.40%] | $11021.94 | 220.439× | 81.14% | $249.12 | 1645 (1006 unfilled) | 5.93% [0.92%, 10.92%] | $911.00 |
| series | tier1 | 330 | 330 | 0.0360 | -1.90% [-13.35%, 9.36%] | $21.07 | 0.421× | 85.64% | $9.19 | 256 (74 unfilled) | -2.97% [-15.24%, 9.29%] | $29.58 |
| series | tier2 | 1138 | 1137 | 0.0449 | 6.41% [0.88%, 12.03%] | $6349.44 | 126.989× | 57.50% | $249.47 | 696 (442 unfilled) | 2.60% [-4.10%, 9.69%] | $63.62 |
| series | tier3 | 1154 | 1151 | 0.0615 | 15.74% [9.51%, 22.27%] | $12515.65 | 250.313× | 70.72% | $249.12 | 674 (480 unfilled) | 13.09% [5.03%, 21.57%] | $1567.50 |
| series | unknown | 29 | 29 | 0.0499 | -1.00% [-29.09%, 24.82%] | $63.25 | 1.265× | 11.31% | $6.19 | 19 (10 unfilled) | -5.54% [-40.38%, 34.88%] | $53.88 |
| series | international=1 | 196 | 196 | 0.0322 | 1.51% [-13.89%, 18.76%] | $82.22 | 1.644× | 51.99% | $11.84 | 162 (34 unfilled) | -0.30% [-15.41%, 16.31%] | $91.53 |
| series | international=0 | 2455 | 2451 | 0.0526 | 9.98% [5.95%, 14.04%] | $13744.07 | 274.881× | 81.14% | $249.12 | 1483 (972 unfilled) | 6.61% [1.93%, 12.11%] | $716.23 |
| map | all | 1772 | 1114 | 0.0333 | 4.14% [-0.50%, 8.97%] | $389.66 | 7.793× | 76.06% | $68.31 | 503 (1269 unfilled) | -6.21% [-14.18%, 2.28%] | $12.70 |
| map | tier1 | 336 | 230 | 0.0272 | -4.97% [-16.19%, 6.46%] | $19.83 | 0.397× | 76.87% | $6.84 | 103 (233 unfilled) | -4.01% [-23.58%, 16.95%] | $32.50 |
| map | tier2 | 776 | 478 | 0.0290 | 4.48% [-2.22%, 11.75%] | $167.06 | 3.341× | 42.12% | $26.59 | 209 (567 unfilled) | -10.61% [-22.02%, 0.81%] | $21.44 |
| map | tier3 | 639 | 391 | 0.0420 | 8.29% [0.16%, 16.43%] | $357.45 | 7.149× | 63.38% | $38.90 | 183 (456 unfilled) | -3.52% [-17.87%, 10.84%] | $36.03 |
| map | unknown | 21 | 15 | 0.0267 | 11.06% [-17.32%, 37.77%] | $55.83 | 1.117× | 6.61% | $4.93 | 8 (13 unfilled) | 19.37% [-21.20%, 52.77%] | $56.94 |
| map | international=1 | 227 | 158 | 0.0247 | 3.12% [-10.23%, 16.52%] | $63.95 | 1.279× | 46.64% | $8.14 | 78 (149 unfilled) | 6.76% [-15.18%, 31.52%] | $51.80 |
| map | international=0 | 1545 | 956 | 0.0346 | 4.29% [-0.83%, 9.60%] | $384.13 | 7.683× | 72.72% | $42.15 | 425 (1120 unfilled) | -8.59% [-16.99%, -0.31%] | $12.03 |
| series+map | all | 4423 | 2771 | 0.0440 | 7.26% [3.74%, 10.67%] | $15678.79 | 313.576× | 58.80% | $249.12 | 2148 (2275 unfilled) | 3.09% [-1.35%, 7.87%] | $444.22 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-01 | 63 | 0.635848 | — | 0.638920 | 8.32% (41), $56.78 | — | 4 (37 unfilled) | -6.25% [-100.00%, 88.86%] | $49.63 | — | — | — |
| map | 2026-02 | 102 | 0.643874 | — | 0.611955 | -24.21% (62), $26.09 | — | 22 (40 unfilled) | -57.27% [-87.16%, -21.90%] | $26.19 | — | — | — |
| map | 2026-03 | 144 | 0.654158 | 0.643034 | 0.642845 | -1.46% (82), $35.77 | 9.58% (14), $48.38 | 42 (40 unfilled) | 3.29% [-33.78%, 43.93%] | $47.99 | 9 (5 unfilled) | 1.31% [-45.47%, 31.61%] | $47.24 |
| map | 2026-04 | 273 | 0.624236 | 0.640646 | 0.647894 | 15.89% (170), $270.60 | 39.59% (26), $67.01 | 54 (116 unfilled) | -11.78% [-36.75%, 12.72%] | $34.58 | 7 (19 unfilled) | -6.60% [-46.63%, 32.93%] | $50.03 |
| map | 2026-05 | 452 | 0.638671 | 0.628427 | 0.636432 | -1.85% (272), $48.76 | 8.72% (220), $116.39 | 93 (179 unfilled) | -2.85% [-26.35%, 20.05%] | $33.63 | 84 (136 unfilled) | 4.09% [-16.01%, 25.23%] | $51.28 |
| map | 2026-06 | 414 | 0.641939 | 0.641599 | 0.650163 | 5.52% (227), $104.27 | 9.07% (215), $98.84 | 47 (180 unfilled) | -5.39% [-33.12%, 25.68%] | $45.78 | 47 (168 unfilled) | 2.20% [-23.39%, 29.26%] | $54.31 |
| map | 2026-07 | 618 | 0.655724 | 0.653655 | 0.647047 | -7.43% (380), $6.72 | -5.10% (330), $15.85 | 85 (295 unfilled) | -8.48% [-31.45%, 13.97%] | $31.73 | 69 (261 unfilled) | -2.54% [-22.22%, 16.49%] | $46.91 |
| map | 2026-08 | 873 | 0.618866 | 0.611709 | 0.623251 | -2.15% (592), $18.34 | 12.57% (380), $283.88 | 115 (477 unfilled) | -8.99% [-29.43%, 12.51%] | $33.13 | 77 (303 unfilled) | 6.84% [-15.66%, 31.65%] | $59.14 |
| map | 2026-09 | 879 | 0.646626 | 0.634494 | 0.631507 | -11.54% (577), $0.05 | -4.03% (380), $30.74 | 201 (376 unfilled) | -27.34% [-42.23%, -10.86%] | $0.68 | 145 (235 unfilled) | -18.30% [-31.96%, -2.82%] | $20.81 |
| map | 2026-10 | 659 | 0.640736 | 0.626594 | 0.628124 | -11.35% (404), $0.17 | 3.58% (207), $50.93 | 150 (254 unfilled) | -30.64% [-46.08%, -13.79%] | $1.76 | 65 (142 unfilled) | -18.98% [-38.38%, 0.08%] | $25.01 |
| series | 2026-01 | 51 | 0.575621 | — | 0.602759 | 20.50% (41), $103.89 | — | 37 (4 unfilled) | 33.81% [-7.25%, 77.91%] | $101.44 | — | — | — |
| series | 2026-02 | 155 | 0.576456 | — | 0.565710 | -7.52% (116), $13.82 | — | 101 (15 unfilled) | -8.34% [-27.66%, 12.08%] | $15.03 | — | — | — |
| series | 2026-03 | 304 | 0.585765 | 0.572724 | 0.590480 | 4.15% (219), $44.36 | 10.54% (207), $285.02 | 168 (51 unfilled) | 3.32% [-13.17%, 21.35%] | $49.93 | 154 (53 unfilled) | 8.32% [-3.45%, 20.77%] | $124.79 |
| series | 2026-04 | 322 | 0.580884 | 0.567741 | 0.580957 | -2.64% (236), $29.57 | 6.28% (223), $111.06 | 168 (68 unfilled) | 2.35% [-16.11%, 23.43%] | $54.41 | 163 (60 unfilled) | 9.75% [-4.46%, 27.23%] | $98.15 |
| series | 2026-05 | 360 | 0.597081 | 0.577031 | 0.584764 | -3.17% (263), $5.06 | 3.83% (240), $75.67 | 212 (51 unfilled) | -7.74% [-23.36%, 9.39%] | $1.59 | 189 (51 unfilled) | 0.70% [-12.52%, 15.43%] | $36.68 |
| series | 2026-06 | 348 | 0.613493 | 0.621505 | 0.633931 | 9.53% (244), $252.34 | 8.28% (218), $114.40 | 162 (82 unfilled) | 18.15% [-1.04%, 39.19%] | $335.99 | 140 (78 unfilled) | 6.39% [-7.94%, 20.53%] | $78.06 |
| series | 2026-07 | 513 | 0.619614 | 0.610749 | 0.614447 | 2.57% (380), $1.57 | 1.39% (349), $27.34 | 240 (140 unfilled) | 1.68% [-14.89%, 21.99%] | $51.40 | 216 (133 unfilled) | -0.44% [-15.09%, 16.47%] | $26.53 |
| series | 2026-08 | 717 | 0.596834 | 0.590575 | 0.614837 | 7.91% (556), $129.63 | 13.42% (443), $662.20 | 272 (284 unfilled) | 3.22% [-11.73%, 21.21%] | $56.43 | 210 (233 unfilled) | 17.30% [1.20%, 36.12%] | $356.26 |
| series | 2026-09 | 914 | 0.589610 | 0.582475 | 0.602664 | 4.52% (666), $20.16 | 15.72% (540), $3859.97 | 374 (292 unfilled) | -5.59% [-17.41%, 6.11%] | $4.78 | 308 (232 unfilled) | 2.93% [-7.74%, 13.54%] | $201.27 |
| series | 2026-10 | 772 | 0.586629 | 0.575497 | 0.585736 | 0.87% (542), $17.06 | 8.26% (431), $268.85 | 334 (208 unfilled) | -1.49% [-13.65%, 10.79%] | $34.43 | 265 (166 unfilled) | 5.33% [-4.41%, 16.01%] | $88.22 |

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
| series | all | 4456 | 0.600331 | 0.600358 | -0.000027 [-0.008019, 0.007842] | no |
| series | tier1 | 725 | 0.632427 | 0.616830 | 0.015597 [-0.001403, 0.032254] | no |
| series | tier2 | 1962 | 0.597128 | 0.590722 | 0.006406 [-0.003882, 0.017192] | no |
| series | tier3 | 1727 | 0.593099 | 0.607536 | -0.014437 [-0.028553, 0.000194] | no |
| series | unknown | 42 | 0.493300 | 0.471027 | 0.022272 [-0.038790, 0.082968] | no |
| series | international=1 | 448 | 0.604953 | 0.591446 | 0.013507 [-0.009687, 0.034181] | no |
| series | international=0 | 4008 | 0.599815 | 0.601354 | -0.001540 [-0.010026, 0.006759] | no |
| map | all | 4477 | 0.640741 | 0.634789 | 0.005952 [0.000085, 0.011944] | yes |
| map | tier1 | 1176 | 0.656614 | 0.646419 | 0.010195 [-0.001834, 0.021495] | no |
| map | tier2 | 1968 | 0.637327 | 0.631291 | 0.006036 [-0.002158, 0.014120] | no |
| map | tier3 | 1279 | 0.633805 | 0.632601 | 0.001205 [-0.011508, 0.014028] | no |
| map | unknown | 54 | 0.583784 | 0.560856 | 0.022928 [-0.011339, 0.059749] | no |
| map | international=1 | 788 | 0.636177 | 0.630059 | 0.006118 [-0.008416, 0.019902] | no |
| map | international=0 | 3689 | 0.641717 | 0.635800 | 0.005917 [-0.000212, 0.012186] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 3288 | 3283 | 0.0817 | 2.99% [-1.33%, 7.16%] | $0.04 | 0.001× | 99.95% | $8.90 | 2083 (1205 unfilled) | 0.74% [-4.73%, 6.11%] | $0.08 |
| series | tier1 | 532 | 532 | 0.0769 | 0.49% [-11.73%, 12.73%] | $0.09 | 0.002× | 99.92% | $11.52 | 434 (98 unfilled) | -2.33% [-15.95%, 10.12%] | $0.10 |
| series | tier2 | 1387 | 1384 | 0.0720 | -1.66% [-7.84%, 4.80%] | $0.05 | 0.001× | 99.97% | $18.18 | 863 (524 unfilled) | -3.50% [-11.28%, 4.31%] | $0.09 |
| series | tier3 | 1336 | 1334 | 0.0940 | 9.30% [2.65%, 16.53%] | $5246.83 | 104.937× | 85.25% | $249.12 | 764 (572 unfilled) | 7.69% [-1.34%, 16.51%] | $78.44 |
| series | unknown | 33 | 33 | 0.0757 | -16.68% [-47.60%, 16.01%] | $31.32 | 0.626× | 41.12% | $5.10 | 22 (11 unfilled) | -13.08% [-54.22%, 30.96%] | $36.40 |
| series | international=1 | 335 | 335 | 0.0776 | 2.13% [-13.50%, 18.96%] | $1.07 | 0.021× | 99.31% | $10.43 | 292 (43 unfilled) | -2.27% [-17.85%, 13.89%] | $0.75 |
| series | international=0 | 2953 | 2948 | 0.0822 | 3.08% [-1.38%, 7.71%] | $0.03 | 0.001× | 99.96% | $6.25 | 1791 (1162 unfilled) | 1.24% [-4.43%, 6.97%] | $0.07 |
| map | all | 2852 | 1806 | 0.0592 | -5.22% [-9.44%, -0.75%] | $0.08 | 0.002× | 99.97% | $27.75 | 831 (2021 unfilled) | -15.32% [-22.68%, -7.88%] | $0.08 |
| map | tier1 | 753 | 512 | 0.0586 | -5.60% [-14.51%, 3.59%] | $3.42 | 0.068× | 96.05% | $6.47 | 231 (522 unfilled) | -8.11% [-24.17%, 8.53%] | $12.13 |
| map | tier2 | 1213 | 750 | 0.0535 | -4.30% [-10.95%, 2.85%] | $0.08 | 0.002× | 99.95% | $14.50 | 344 (869 unfilled) | -17.84% [-28.61%, -7.07%] | $0.17 |
| map | tier3 | 856 | 524 | 0.0683 | -5.94% [-13.84%, 2.07%] | $5.15 | 0.103× | 98.40% | $17.61 | 244 (612 unfilled) | -18.70% [-32.45%, -3.84%] | $6.17 |
| map | unknown | 30 | 20 | 0.0481 | -12.93% [-43.17%, 18.88%] | $38.22 | 0.764× | 27.55% | $4.78 | 12 (18 unfilled) | -13.86% [-51.82%, 16.78%] | $46.31 |
| map | international=1 | 501 | 345 | 0.0618 | -5.66% [-17.09%, 5.95%] | $20.10 | 0.402× | 88.61% | $17.01 | 161 (340 unfilled) | -4.68% [-26.39%, 16.27%] | $31.97 |
| map | international=0 | 2351 | 1461 | 0.0587 | -5.13% [-9.86%, -0.31%] | $0.09 | 0.002× | 99.92% | $11.11 | 670 (1681 unfilled) | -17.89% [-25.38%, -9.95%] | $0.07 |
| series+map | all | 6140 | 3615 | 0.0713 | -0.82% [-4.38%, 2.86%] | $0.06 | 0.001× | 99.90% | $6.19 | 2914 (3226 unfilled) | -3.84% [-8.60%, 1.27%] | $0.07 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2026-01-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 371 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-01 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-01 | map | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 51 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | map | 63 | 1.000000 | 0.000000 | unfitted |
| 2026-03 | series | 206 | 1.457683 | 0.670061 | fitted |
| 2026-03 | map | 165 | 1.268874 | 0.236759 | fitted |
| 2026-04 | series | 510 | 1.460757 | 0.822807 | fitted |
| 2026-04 | map | 309 | 1.201377 | 0.214366 | fitted |
| 2026-05 | series | 832 | 1.398567 | 0.750781 | fitted |
| 2026-05 | map | 582 | 1.323494 | 0.778151 | fitted |
| 2026-06 | series | 1192 | 1.401278 | 0.687585 | fitted |
| 2026-06 | map | 1034 | 1.361163 | 0.739254 | fitted |
| 2026-07 | series | 1540 | 1.310734 | 0.677269 | fitted |
| 2026-07 | map | 1448 | 1.300132 | 0.704951 | fitted |
| 2026-08 | series | 2053 | 1.244600 | 0.568115 | fitted |
| 2026-08 | map | 2066 | 1.163563 | 0.514510 | fitted |
| 2026-09 | series | 2770 | 1.238726 | 0.617065 | fitted |
| 2026-09 | map | 2939 | 1.226798 | 0.590978 | fitted |
| 2026-10 | series | 3684 | 1.241658 | 0.636202 | fitted |
| 2026-10 | map | 3818 | 1.209386 | 0.500274 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 4250 | 0.590150 | 0.601593 | -0.011444 [-0.016587, -0.006502] | yes |
| series | tier1 | 614 | 0.619079 | 0.616540 | 0.002539 [-0.007325, 0.012628] | no |
| series | tier2 | 1873 | 0.584260 | 0.593752 | -0.009491 [-0.016147, -0.002917] | yes |
| series | tier3 | 1721 | 0.589715 | 0.607981 | -0.018266 [-0.027801, -0.008953] | yes |
| series | unknown | 42 | 0.447665 | 0.471027 | -0.023362 [-0.054518, 0.008630] | no |
| series | international=1 | 370 | 0.585804 | 0.589385 | -0.003581 [-0.015200, 0.008417] | no |
| series | international=0 | 3880 | 0.590564 | 0.602757 | -0.012193 [-0.017534, -0.006768] | yes |
| map | all | 4312 | 0.632663 | 0.635269 | -0.002606 [-0.006224, 0.000974] | no |
| map | tier1 | 1046 | 0.652946 | 0.649504 | 0.003442 [-0.003219, 0.009729] | no |
| map | tier2 | 1936 | 0.626251 | 0.631140 | -0.004889 [-0.009714, 0.000001] | no |
| map | tier3 | 1276 | 0.629250 | 0.633014 | -0.003764 [-0.011538, 0.004686] | no |
| map | unknown | 54 | 0.550291 | 0.560856 | -0.010565 [-0.030483, 0.009099] | no |
| map | international=1 | 686 | 0.627415 | 0.629473 | -0.002058 [-0.008821, 0.005069] | no |
| map | international=0 | 3626 | 0.633656 | 0.636366 | -0.002710 [-0.006783, 0.001233] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 2489 | 2485 | 0.0475 | 8.32% [4.22%, 12.26%] | $11754.34 | 235.087× | 78.81% | $249.12 | 1558 (931 unfilled) | 5.42% [0.34%, 10.39%] | $922.50 |
| series | tier1 | 310 | 310 | 0.0346 | 2.19% [-10.21%, 15.21%] | $16.76 | 0.335× | 85.15% | $6.96 | 240 (70 unfilled) | 1.67% [-12.25%, 15.39%] | $27.72 |
| series | tier2 | 1079 | 1078 | 0.0423 | 6.61% [1.13%, 11.97%] | $4705.22 | 94.104× | 64.57% | $249.12 | 662 (417 unfilled) | 2.46% [-4.37%, 9.46%] | $120.60 |
| series | tier3 | 1070 | 1067 | 0.0567 | 11.92% [5.64%, 18.24%] | $11840.44 | 236.809× | 61.01% | $249.12 | 635 (435 unfilled) | 10.15% [1.62%, 18.89%] | $1154.78 |
| series | unknown | 30 | 30 | 0.0410 | 4.88% [-21.18%, 30.63%] | $65.01 | 1.300× | 10.87% | $6.17 | 21 (9 unfilled) | -1.53% [-34.48%, 34.52%] | $55.91 |
| series | international=1 | 181 | 181 | 0.0319 | 6.95% [-10.95%, 26.25%] | $92.01 | 1.840× | 43.85% | $11.04 | 148 (33 unfilled) | 6.24% [-12.00%, 25.74%] | $94.84 |
| series | international=0 | 2308 | 2304 | 0.0487 | 8.43% [4.39%, 12.53%] | $12357.45 | 247.149× | 77.84% | $249.12 | 1410 (898 unfilled) | 5.33% [0.37%, 10.54%] | $724.55 |
| map | all | 1757 | 1088 | 0.0328 | 2.34% [-2.67%, 7.68%] | $458.93 | 9.179× | 75.31% | $72.95 | 502 (1255 unfilled) | -6.20% [-14.42%, 2.99%] | $19.97 |
| map | tier1 | 334 | 218 | 0.0280 | -0.61% [-13.84%, 13.43%] | $32.27 | 0.645× | 75.98% | $8.18 | 109 (225 unfilled) | -5.07% [-28.02%, 19.81%] | $55.20 |
| map | tier2 | 770 | 474 | 0.0292 | 2.09% [-5.21%, 9.71%] | $176.82 | 3.536× | 48.19% | $29.04 | 203 (567 unfilled) | -10.63% [-22.22%, 0.42%] | $15.92 |
| map | tier3 | 633 | 383 | 0.0400 | 4.03% [-3.86%, 11.84%] | $230.02 | 4.600× | 66.85% | $36.25 | 181 (452 unfilled) | -2.57% [-16.04%, 11.38%] | $47.67 |
| map | unknown | 20 | 13 | 0.0257 | 8.29% [-18.89%, 34.91%] | $54.78 | 1.096× | 3.27% | $4.89 | 9 (11 unfilled) | 7.30% [-29.98%, 45.18%] | $55.53 |
| map | international=1 | 221 | 146 | 0.0273 | 8.70% [-8.77%, 28.20%] | $97.17 | 1.943× | 39.33% | $9.55 | 78 (143 unfilled) | 8.41% [-21.39%, 41.32%] | $86.05 |
| map | international=0 | 1536 | 942 | 0.0336 | 1.43% [-3.60%, 6.61%] | $266.26 | 5.325× | 75.35% | $37.57 | 424 (1112 unfilled) | -8.89% [-17.46%, -0.36%] | $10.54 |
| series+map | all | 4246 | 2614 | 0.0414 | 5.85% [2.13%, 9.35%] | $14190.61 | 283.812× | 65.22% | $249.47 | 2060 (2186 unfilled) | 2.59% [-2.15%, 7.63%] | $580.93 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-01 | 63 | 0.633585 | — | 0.638920 | 3.22% (41), $54.84 | — | 5 (36 unfilled) | -25.03% [-100.00%, 58.85%] | $49.65 | — | — | — |
| map | 2026-02 | 102 | 0.641808 | — | 0.611955 | -17.83% (58), $28.31 | — | 18 (40 unfilled) | -47.80% [-83.47%, -8.95%] | $28.98 | — | — | — |
| map | 2026-03 | 144 | 0.657710 | 0.642971 | 0.642845 | 1.52% (75), $42.01 | 14.98% (32), $63.94 | 39 (36 unfilled) | 1.15% [-40.11%, 44.68%] | $42.63 | 14 (18 unfilled) | 6.12% [-26.77%, 28.96%] | $52.60 |
| map | 2026-04 | 273 | 0.626009 | 0.639056 | 0.647894 | 11.72% (168), $236.70 | 61.15% (36), $66.70 | 52 (116 unfilled) | -13.61% [-40.22%, 14.08%] | $34.04 | 11 (25 unfilled) | -25.94% [-75.30%, 11.17%] | $48.39 |
| map | 2026-05 | 452 | 0.642149 | 0.630445 | 0.636432 | -2.19% (275), $35.93 | 7.26% (230), $88.24 | 91 (184 unfilled) | -0.37% [-23.96%, 22.88%] | $35.64 | 87 (143 unfilled) | 3.54% [-16.54%, 23.57%] | $46.28 |
| map | 2026-06 | 414 | 0.644375 | 0.643558 | 0.650163 | 1.83% (239), $68.71 | 3.05% (225), $96.76 | 45 (194 unfilled) | 5.31% [-24.98%, 36.10%] | $57.10 | 45 (180 unfilled) | 1.96% [-24.62%, 28.90%] | $59.07 |
| map | 2026-07 | 618 | 0.658436 | 0.654324 | 0.647047 | -7.53% (390), $5.14 | -5.37% (338), $16.23 | 94 (296 unfilled) | -13.22% [-34.71%, 8.41%] | $25.85 | 69 (269 unfilled) | -8.15% [-27.01%, 12.11%] | $46.44 |
| map | 2026-08 | 873 | 0.618828 | 0.612466 | 0.623251 | -2.89% (602), $9.37 | 7.79% (349), $344.21 | 117 (485 unfilled) | -9.16% [-29.49%, 11.96%] | $32.70 | 73 (276 unfilled) | 5.22% [-17.26%, 28.93%] | $49.68 |
| map | 2026-09 | 879 | 0.647175 | 0.633400 | 0.631507 | -9.29% (608), $0.29 | -5.94% (353), $37.68 | 222 (386 unfilled) | -19.20% [-34.76%, -2.57%] | $3.42 | 142 (211 unfilled) | -13.06% [-29.96%, 6.62%] | $39.68 |
| map | 2026-10 | 659 | 0.644262 | 0.627898 | 0.628124 | -14.10% (396), $0.10 | 1.50% (194), $40.93 | 148 (248 unfilled) | -31.80% [-48.11%, -15.70%] | $2.04 | 61 (133 unfilled) | -20.84% [-41.39%, -0.81%] | $24.62 |
| series | 2026-01 | 51 | 0.580685 | — | 0.602759 | 15.85% (43), $77.32 | — | 36 (7 unfilled) | 29.00% [-14.57%, 72.84%] | $82.93 | — | — | — |
| series | 2026-02 | 155 | 0.584041 | — | 0.565710 | -10.80% (114), $11.51 | — | 103 (11 unfilled) | -12.71% [-32.33%, 6.54%] | $11.55 | — | — | — |
| series | 2026-03 | 304 | 0.586470 | 0.572541 | 0.590480 | 2.51% (215), $36.70 | 10.96% (197), $298.87 | 163 (52 unfilled) | 2.03% [-15.73%, 20.61%] | $55.38 | 148 (49 unfilled) | 6.84% [-5.26%, 18.87%] | $142.46 |
| series | 2026-04 | 322 | 0.585328 | 0.569443 | 0.580957 | 2.57% (233), $11.81 | 8.11% (222), $160.14 | 175 (58 unfilled) | 4.11% [-15.12%, 26.07%] | $34.37 | 161 (61 unfilled) | 12.62% [-3.98%, 30.60%] | $130.88 |
| series | 2026-05 | 360 | 0.601616 | 0.578633 | 0.584764 | -7.90% (257), $3.26 | 3.55% (224), $41.72 | 210 (47 unfilled) | -8.82% [-25.57%, 7.16%] | $2.91 | 175 (49 unfilled) | 0.69% [-13.07%, 14.54%] | $37.31 |
| series | 2026-06 | 348 | 0.618771 | 0.625520 | 0.633931 | 9.29% (251), $241.58 | 9.77% (214), $75.82 | 166 (85 unfilled) | 17.16% [-2.58%, 36.87%] | $434.47 | 142 (72 unfilled) | 12.63% [-1.56%, 26.43%] | $71.01 |
| series | 2026-07 | 513 | 0.627085 | 0.614589 | 0.614447 | 3.61% (374), $0.90 | 0.06% (328), $20.19 | 237 (137 unfilled) | 0.22% [-16.39%, 18.92%] | $28.64 | 201 (127 unfilled) | -3.38% [-18.82%, 15.88%] | $20.31 |
| series | 2026-08 | 717 | 0.603501 | 0.596392 | 0.614837 | 7.45% (561), $42.07 | 10.94% (421), $696.51 | 272 (289 unfilled) | 1.04% [-13.89%, 17.26%] | $22.27 | 202 (219 unfilled) | 13.16% [-3.72%, 31.90%] | $335.97 |
| series | 2026-09 | 914 | 0.598134 | 0.587240 | 0.602664 | 2.35% (684), $2.46 | 11.78% (489), $1835.00 | 378 (306 unfilled) | -4.61% [-16.30%, 7.06%] | $0.01 | 287 (202 unfilled) | 1.74% [-9.41%, 13.78%] | $137.75 |
| series | 2026-10 | 772 | 0.589584 | 0.576552 | 0.585736 | 3.24% (556), $4.11 | 8.82% (394), $244.03 | 343 (213 unfilled) | 3.42% [-8.44%, 15.49%] | $30.80 | 242 (152 unfilled) | 4.17% [-7.07%, 15.01%] | $101.38 |

### player_round_glicko_rookie_weights+none: Kalshi comparison and returns

none

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 4456 | 0.594668 | 0.600358 | -0.005690 [-0.013363, 0.002082] | no |
| series | tier1 | 725 | 0.628922 | 0.616830 | 0.012092 [-0.003900, 0.028033] | no |
| series | tier2 | 1962 | 0.594077 | 0.590722 | 0.003355 [-0.006731, 0.013978] | no |
| series | tier3 | 1727 | 0.583493 | 0.607536 | -0.024043 [-0.037968, -0.010048] | yes |
| series | unknown | 42 | 0.490548 | 0.471027 | 0.019521 [-0.044998, 0.082868] | no |
| series | international=1 | 448 | 0.600867 | 0.591446 | 0.009421 [-0.011559, 0.028817] | no |
| series | international=0 | 4008 | 0.593975 | 0.601354 | -0.007379 [-0.015579, 0.000557] | no |
| map | all | 4477 | 0.639028 | 0.634789 | 0.004238 [-0.001561, 0.009878] | no |
| map | tier1 | 1176 | 0.654442 | 0.646419 | 0.008023 [-0.003125, 0.018611] | no |
| map | tier2 | 1968 | 0.635842 | 0.631291 | 0.004551 [-0.003417, 0.012349] | no |
| map | tier3 | 1279 | 0.632071 | 0.632601 | -0.000530 [-0.012795, 0.011852] | no |
| map | unknown | 54 | 0.584221 | 0.560856 | 0.023365 [-0.010524, 0.059012] | no |
| map | international=1 | 788 | 0.633669 | 0.630059 | 0.003609 [-0.009543, 0.016984] | no |
| map | international=0 | 3689 | 0.640173 | 0.635800 | 0.004373 [-0.001764, 0.010770] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 3263 | 3258 | 0.0815 | 3.25% [-1.08%, 7.71%] | $0.07 | 0.001× | 99.94% | $12.17 | 2068 (1195 unfilled) | 0.65% [-4.71%, 5.91%] | $0.07 |
| series | tier1 | 527 | 527 | 0.0707 | -0.42% [-11.99%, 11.78%] | $0.09 | 0.002× | 99.94% | $15.55 | 428 (99 unfilled) | -2.47% [-15.20%, 9.51%] | $0.16 |
| series | tier2 | 1379 | 1376 | 0.0718 | -2.01% [-8.31%, 4.46%] | $0.08 | 0.002× | 99.96% | $21.31 | 857 (522 unfilled) | -3.90% [-11.60%, 3.95%] | $0.20 |
| series | tier3 | 1325 | 1323 | 0.0958 | 10.61% [3.78%, 17.20%] | $10891.33 | 217.827× | 79.33% | $249.12 | 761 (564 unfilled) | 7.96% [-0.62%, 17.05%] | $374.89 |
| series | unknown | 32 | 32 | 0.0821 | -14.10% [-45.28%, 20.91%] | $42.64 | 0.853× | 30.66% | $5.91 | 22 (10 unfilled) | -13.08% [-54.22%, 30.96%] | $41.56 |
| series | international=1 | 323 | 323 | 0.0714 | 0.45% [-16.07%, 16.60%] | $2.38 | 0.048× | 98.95% | $13.02 | 279 (44 unfilled) | -2.63% [-17.98%, 13.46%] | $1.06 |
| series | international=0 | 2940 | 2935 | 0.0826 | 3.56% [-0.78%, 8.44%] | $0.07 | 0.001× | 99.89% | $6.56 | 1789 (1151 unfilled) | 1.17% [-4.31%, 6.87%] | $18.47 |
| map | all | 2807 | 1791 | 0.0569 | -4.69% [-9.11%, 0.00%] | $0.09 | 0.002× | 99.97% | $32.46 | 813 (1994 unfilled) | -17.41% [-24.91%, -10.03%] | $0.07 |
| map | tier1 | 747 | 513 | 0.0541 | -4.55% [-13.26%, 4.66%] | $5.60 | 0.112× | 94.34% | $8.04 | 227 (520 unfilled) | -9.08% [-25.64%, 8.32%] | $9.75 |
| map | tier2 | 1182 | 741 | 0.0525 | -3.94% [-10.77%, 3.12%] | $0.09 | 0.002× | 99.94% | $13.16 | 336 (846 unfilled) | -19.55% [-30.64%, -8.32%] | $0.19 |
| map | tier3 | 848 | 516 | 0.0656 | -5.23% [-13.05%, 3.44%] | $2.27 | 0.045× | 99.21% | $15.51 | 239 (609 unfilled) | -22.35% [-35.75%, -8.58%] | $2.79 |
| map | unknown | 30 | 21 | 0.0481 | -22.79% [-53.00%, 6.46%] | $36.05 | 0.721× | 32.18% | $4.78 | 11 (19 unfilled) | -16.99% [-56.80%, 17.05%] | $46.45 |
| map | international=1 | 502 | 348 | 0.0560 | -4.02% [-15.32%, 8.04%] | $37.31 | 0.746× | 82.02% | $19.48 | 160 (342 unfilled) | -6.48% [-27.65%, 16.02%] | $30.90 |
| map | international=0 | 2305 | 1443 | 0.0571 | -4.84% [-9.28%, -0.03%] | $0.10 | 0.002× | 99.92% | $11.51 | 653 (1652 unfilled) | -20.09% [-27.79%, -12.31%] | $0.06 |
| series+map | all | 6070 | 3573 | 0.0701 | -0.42% [-4.14%, 3.14%] | $0.05 | 0.001× | 99.95% | $10.55 | 2881 (3189 unfilled) | -4.44% [-9.03%, 0.56%] | $0.07 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2026-01-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 371 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-01 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-01 | map | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 51 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | map | 63 | 1.000000 | 0.000000 | unfitted |
| 2026-03 | series | 206 | 1.442335 | 0.749188 | fitted |
| 2026-03 | map | 165 | 1.218435 | 0.060951 | fitted |
| 2026-04 | series | 510 | 1.426235 | 0.823474 | fitted |
| 2026-04 | map | 309 | 1.184503 | 0.160308 | fitted |
| 2026-05 | series | 832 | 1.372441 | 0.766276 | fitted |
| 2026-05 | map | 582 | 1.307760 | 0.755416 | fitted |
| 2026-06 | series | 1192 | 1.382460 | 0.712969 | fitted |
| 2026-06 | map | 1034 | 1.359719 | 0.758375 | fitted |
| 2026-07 | series | 1540 | 1.300636 | 0.724478 | fitted |
| 2026-07 | map | 1448 | 1.313794 | 0.756247 | fitted |
| 2026-08 | series | 2053 | 1.240113 | 0.630122 | fitted |
| 2026-08 | map | 2066 | 1.179309 | 0.573594 | fitted |
| 2026-09 | series | 2770 | 1.238566 | 0.673985 | fitted |
| 2026-09 | map | 2939 | 1.244446 | 0.638996 | fitted |
| 2026-10 | series | 3684 | 1.237434 | 0.696647 | fitted |
| 2026-10 | map | 3818 | 1.219471 | 0.534852 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 4250 | 0.586908 | 0.601593 | -0.014685 [-0.020248, -0.009415] | yes |
| series | tier1 | 614 | 0.619582 | 0.616540 | 0.003042 [-0.007231, 0.013817] | no |
| series | tier2 | 1873 | 0.583214 | 0.593752 | -0.010538 [-0.017771, -0.003506] | yes |
| series | tier3 | 1721 | 0.582688 | 0.607981 | -0.025292 [-0.035527, -0.015249] | yes |
| series | unknown | 42 | 0.446865 | 0.471027 | -0.024162 [-0.057715, 0.010999] | no |
| series | international=1 | 370 | 0.586676 | 0.589385 | -0.002709 [-0.014905, 0.009610] | no |
| series | international=0 | 3880 | 0.586930 | 0.602757 | -0.015827 [-0.021575, -0.010037] | yes |
| map | all | 4312 | 0.632141 | 0.635269 | -0.003129 [-0.006722, 0.000485] | no |
| map | tier1 | 1046 | 0.653568 | 0.649504 | 0.004064 [-0.002389, 0.010216] | no |
| map | tier2 | 1936 | 0.625422 | 0.631140 | -0.005718 [-0.010389, -0.001019] | yes |
| map | tier3 | 1276 | 0.628270 | 0.633014 | -0.004744 [-0.012676, 0.003750] | no |
| map | unknown | 54 | 0.549409 | 0.560856 | -0.011447 [-0.032465, 0.009312] | no |
| map | international=1 | 686 | 0.627575 | 0.629473 | -0.001898 [-0.008268, 0.005049] | no |
| map | international=0 | 3626 | 0.633004 | 0.636366 | -0.003362 [-0.007371, 0.000662] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 2651 | 2647 | 0.0511 | 9.35% [5.46%, 13.40%] | $11021.94 | 220.439× | 81.14% | $249.12 | 1645 (1006 unfilled) | 5.93% [0.92%, 10.92%] | $911.00 |
| series | tier1 | 330 | 330 | 0.0360 | -1.90% [-13.35%, 9.36%] | $21.07 | 0.421× | 85.64% | $9.19 | 256 (74 unfilled) | -2.97% [-15.24%, 9.29%] | $29.58 |
| series | tier2 | 1138 | 1137 | 0.0449 | 6.41% [0.88%, 12.03%] | $6349.44 | 126.989× | 57.50% | $249.47 | 696 (442 unfilled) | 2.60% [-4.10%, 9.69%] | $63.62 |
| series | tier3 | 1154 | 1151 | 0.0615 | 15.74% [9.51%, 22.27%] | $12515.65 | 250.313× | 70.72% | $249.12 | 674 (480 unfilled) | 13.09% [5.03%, 21.57%] | $1567.50 |
| series | unknown | 29 | 29 | 0.0499 | -1.00% [-29.09%, 24.82%] | $63.25 | 1.265× | 11.31% | $6.19 | 19 (10 unfilled) | -5.54% [-40.38%, 34.88%] | $53.88 |
| series | international=1 | 196 | 196 | 0.0322 | 1.51% [-13.89%, 18.76%] | $82.22 | 1.644× | 51.99% | $11.84 | 162 (34 unfilled) | -0.30% [-15.41%, 16.31%] | $91.53 |
| series | international=0 | 2455 | 2451 | 0.0526 | 9.98% [5.95%, 14.04%] | $13744.07 | 274.881× | 81.14% | $249.12 | 1483 (972 unfilled) | 6.61% [1.93%, 12.11%] | $716.23 |
| map | all | 1772 | 1114 | 0.0333 | 4.14% [-0.50%, 8.97%] | $389.66 | 7.793× | 76.06% | $68.31 | 503 (1269 unfilled) | -6.21% [-14.18%, 2.28%] | $12.70 |
| map | tier1 | 336 | 230 | 0.0272 | -4.97% [-16.19%, 6.46%] | $19.83 | 0.397× | 76.87% | $6.84 | 103 (233 unfilled) | -4.01% [-23.58%, 16.95%] | $32.50 |
| map | tier2 | 776 | 478 | 0.0290 | 4.48% [-2.22%, 11.75%] | $167.06 | 3.341× | 42.12% | $26.59 | 209 (567 unfilled) | -10.61% [-22.02%, 0.81%] | $21.44 |
| map | tier3 | 639 | 391 | 0.0420 | 8.29% [0.16%, 16.43%] | $357.45 | 7.149× | 63.38% | $38.90 | 183 (456 unfilled) | -3.52% [-17.87%, 10.84%] | $36.03 |
| map | unknown | 21 | 15 | 0.0267 | 11.06% [-17.32%, 37.77%] | $55.83 | 1.117× | 6.61% | $4.93 | 8 (13 unfilled) | 19.37% [-21.20%, 52.77%] | $56.94 |
| map | international=1 | 227 | 158 | 0.0247 | 3.12% [-10.23%, 16.52%] | $63.95 | 1.279× | 46.64% | $8.14 | 78 (149 unfilled) | 6.76% [-15.18%, 31.52%] | $51.80 |
| map | international=0 | 1545 | 956 | 0.0346 | 4.29% [-0.83%, 9.60%] | $384.13 | 7.683× | 72.72% | $42.15 | 425 (1120 unfilled) | -8.59% [-16.99%, -0.31%] | $12.03 |
| series+map | all | 4423 | 2771 | 0.0440 | 7.26% [3.74%, 10.67%] | $15678.79 | 313.576× | 58.80% | $249.12 | 2148 (2275 unfilled) | 3.09% [-1.35%, 7.87%] | $444.22 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-01 | 63 | 0.635848 | — | 0.638920 | 8.32% (41), $56.78 | — | 4 (37 unfilled) | -6.25% [-100.00%, 88.86%] | $49.63 | — | — | — |
| map | 2026-02 | 102 | 0.643874 | — | 0.611955 | -24.21% (62), $26.09 | — | 22 (40 unfilled) | -57.27% [-87.16%, -21.90%] | $26.19 | — | — | — |
| map | 2026-03 | 144 | 0.654158 | 0.643034 | 0.642845 | -1.46% (82), $35.77 | 9.58% (14), $48.38 | 42 (40 unfilled) | 3.29% [-33.78%, 43.93%] | $47.99 | 9 (5 unfilled) | 1.31% [-45.47%, 31.61%] | $47.24 |
| map | 2026-04 | 273 | 0.624236 | 0.640646 | 0.647894 | 15.89% (170), $270.60 | 39.59% (26), $67.01 | 54 (116 unfilled) | -11.78% [-36.75%, 12.72%] | $34.58 | 7 (19 unfilled) | -6.60% [-46.63%, 32.93%] | $50.03 |
| map | 2026-05 | 452 | 0.638671 | 0.628427 | 0.636432 | -1.85% (272), $48.76 | 8.72% (220), $116.39 | 93 (179 unfilled) | -2.85% [-26.35%, 20.05%] | $33.63 | 84 (136 unfilled) | 4.09% [-16.01%, 25.23%] | $51.28 |
| map | 2026-06 | 414 | 0.641939 | 0.641599 | 0.650163 | 5.52% (227), $104.27 | 9.07% (215), $98.84 | 47 (180 unfilled) | -5.39% [-33.12%, 25.68%] | $45.78 | 47 (168 unfilled) | 2.20% [-23.39%, 29.26%] | $54.31 |
| map | 2026-07 | 618 | 0.655724 | 0.653655 | 0.647047 | -7.43% (380), $6.72 | -5.10% (330), $15.85 | 85 (295 unfilled) | -8.48% [-31.45%, 13.97%] | $31.73 | 69 (261 unfilled) | -2.54% [-22.22%, 16.49%] | $46.91 |
| map | 2026-08 | 873 | 0.618866 | 0.611709 | 0.623251 | -2.15% (592), $18.34 | 12.57% (380), $283.88 | 115 (477 unfilled) | -8.99% [-29.43%, 12.51%] | $33.13 | 77 (303 unfilled) | 6.84% [-15.66%, 31.65%] | $59.14 |
| map | 2026-09 | 879 | 0.646626 | 0.634494 | 0.631507 | -11.54% (577), $0.05 | -4.03% (380), $30.74 | 201 (376 unfilled) | -27.34% [-42.23%, -10.86%] | $0.68 | 145 (235 unfilled) | -18.30% [-31.96%, -2.82%] | $20.81 |
| map | 2026-10 | 659 | 0.640736 | 0.626594 | 0.628124 | -11.35% (404), $0.17 | 3.58% (207), $50.93 | 150 (254 unfilled) | -30.64% [-46.08%, -13.79%] | $1.76 | 65 (142 unfilled) | -18.98% [-38.38%, 0.08%] | $25.01 |
| series | 2026-01 | 51 | 0.575621 | — | 0.602759 | 20.50% (41), $103.89 | — | 37 (4 unfilled) | 33.81% [-7.25%, 77.91%] | $101.44 | — | — | — |
| series | 2026-02 | 155 | 0.576456 | — | 0.565710 | -7.52% (116), $13.82 | — | 101 (15 unfilled) | -8.34% [-27.66%, 12.08%] | $15.03 | — | — | — |
| series | 2026-03 | 304 | 0.585765 | 0.572724 | 0.590480 | 4.15% (219), $44.36 | 10.54% (207), $285.02 | 168 (51 unfilled) | 3.32% [-13.17%, 21.35%] | $49.93 | 154 (53 unfilled) | 8.32% [-3.45%, 20.77%] | $124.79 |
| series | 2026-04 | 322 | 0.580884 | 0.567741 | 0.580957 | -2.64% (236), $29.57 | 6.28% (223), $111.06 | 168 (68 unfilled) | 2.35% [-16.11%, 23.43%] | $54.41 | 163 (60 unfilled) | 9.75% [-4.46%, 27.23%] | $98.15 |
| series | 2026-05 | 360 | 0.597081 | 0.577031 | 0.584764 | -3.17% (263), $5.06 | 3.83% (240), $75.67 | 212 (51 unfilled) | -7.74% [-23.36%, 9.39%] | $1.59 | 189 (51 unfilled) | 0.70% [-12.52%, 15.43%] | $36.68 |
| series | 2026-06 | 348 | 0.613493 | 0.621505 | 0.633931 | 9.53% (244), $252.34 | 8.28% (218), $114.40 | 162 (82 unfilled) | 18.15% [-1.04%, 39.19%] | $335.99 | 140 (78 unfilled) | 6.39% [-7.94%, 20.53%] | $78.06 |
| series | 2026-07 | 513 | 0.619614 | 0.610749 | 0.614447 | 2.57% (380), $1.57 | 1.39% (349), $27.34 | 240 (140 unfilled) | 1.68% [-14.89%, 21.99%] | $51.40 | 216 (133 unfilled) | -0.44% [-15.09%, 16.47%] | $26.53 |
| series | 2026-08 | 717 | 0.596834 | 0.590575 | 0.614837 | 7.91% (556), $129.63 | 13.42% (443), $662.20 | 272 (284 unfilled) | 3.22% [-11.73%, 21.21%] | $56.43 | 210 (233 unfilled) | 17.30% [1.20%, 36.12%] | $356.26 |
| series | 2026-09 | 914 | 0.589610 | 0.582475 | 0.602664 | 4.52% (666), $20.16 | 15.72% (540), $3859.97 | 374 (292 unfilled) | -5.59% [-17.41%, 6.11%] | $4.78 | 308 (232 unfilled) | 2.93% [-7.74%, 13.54%] | $201.27 |
| series | 2026-10 | 772 | 0.586629 | 0.575497 | 0.585736 | 0.87% (542), $17.06 | 8.26% (431), $268.85 | 334 (208 unfilled) | -1.49% [-13.65%, 10.79%] | $34.43 | 265 (166 unfilled) | 5.33% [-4.41%, 16.01%] | $88.22 |

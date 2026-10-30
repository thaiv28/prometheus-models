# Elo variants benchmark

## Combined summary (validation, all sections)

| Model | Series Δ log loss | Series flat ROI | Series Kelly (LoL caps) $ | Series flat ROI depth-capped | Series Kelly depth-capped $ | Game Δ log loss | Game flat ROI | Game Kelly (LoL caps) $ | Game flat ROI depth-capped | Game Kelly depth-capped $ | Series blended Δ log loss | Series blended flat ROI | Series blended Kelly (LoL caps) $ | Series blended flat ROI depth-capped | Series blended Kelly depth-capped $ | Game blended Δ log loss | Game blended flat ROI | Game blended Kelly (LoL caps) $ | Game blended flat ROI depth-capped | Game blended Kelly depth-capped $ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| team_elo | 0.024959 | -5.19% | $0.91 | -7.32% | $4.40 | 0.025598 | -4.79% | $16.81 | -20.95% | $33.66 | 0.004297 | -10.37% | $32.56 | -26.86% | $39.46 | 0.071630 | -22.87% | $10.76 | -16.98% | $44.32 |
| player_glicko | -0.000787 | 2.51% | $61.17 | 0.49% | $48.14 | 0.010214 | -6.61% | $15.58 | -21.16% | $41.30 | -0.004193 | 11.82% | $88.24 | 12.31% | $74.91 | 0.005517 | -2.68% | $34.20 | 38.11% | $50.56 |
| team_elo+none | 0.024959 | -5.19% | $0.91 | -7.32% | $4.40 | 0.025598 | -4.79% | $16.81 | -20.95% | $33.66 | 0.004297 | -10.37% | $32.56 | -26.86% | $39.46 | 0.071630 | -22.87% | $10.76 | -16.98% | $44.32 |
| player_glicko+none | -0.000787 | 2.51% | $61.17 | 0.49% | $48.14 | 0.010214 | -6.61% | $15.58 | -21.16% | $41.30 | -0.004193 | 11.82% | $88.24 | 12.31% | $74.91 | 0.005517 | -2.68% | $34.20 | 38.11% | $50.56 |

Series temperatures (stage 1; p′ = σ(T·logit p), T < 1 pulls odds toward 50%): team_elo Bo3 0.68, Bo5 0.61; player_glicko Bo3 0.69, Bo5 0.82; team_elo+none Bo3 0.68, Bo5 0.61; player_glicko+none Bo3 0.69, Bo5 0.82

Parameters minimize tuning game log loss across all sections. Replay predicts before update; Replay starts at the first game. Tuning: [2023-01-01, 2025-11-01); validation: [2025-11-01, 2026-07-01). Holdout is scored only with --holdout and never selects parameters. Series use the first game prediction and independent games in Bo1/Bo3/Bo5; Bo2, unknown/unsupported lengths and unknown results are skipped. Accuracy gives 0.5 predictions half credit; ECE uses 10 equal-width bins. Log loss clips probabilities at 1e-6. Paired bootstrap uses 2,000 resamples, seed 0, clustered by match_id. Differences are the named model minus its comparator; negative favors the model. Significance requires a 95% percentile interval excluding zero. Tuning scores are selection diagnostics, not independent evidence of improvement.

Fit through 2025-10-31. Unknown host-region game rows: 2576 (including missing/un).

## Stage 1 — tuning (outcomes)

### Leaderboard

| Model | Best params | Game log loss | Series log loss | Rows |
|---|---|---:|---:|---:|
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

player_glicko − team_elo (paired log loss):

| Section | Rows | player_glicko log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 38138 | 0.621611 | 0.650054 | -0.028443 | [-0.030994, -0.025778] | yes |

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

player_glicko − team_elo (paired log loss):

| Section | Rows | player_glicko log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 12117 | 0.599064 | 0.638841 | -0.039777 | [-0.044407, -0.034826] | yes |

## Stage 2 — validation (outcomes)

### Leaderboard (frozen stage-1 parameters)

| Model | Best params | Game log loss | Series log loss | Rows |
|---|---|---:|---:|---:|
| player_glicko | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 280} | 0.610785 | 0.584862 | 9328 |
| player_glicko+none | {"k": 24, "new_player": "fixed", "rd_info": 0.0625, "rd_new": 280} | 0.610785 | 0.584862 | 9328 |
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

player_glicko − team_elo (paired log loss):

| Section | Rows | player_glicko log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.610785 | 0.646281 | -0.035496 | [-0.040569, -0.030402] | yes |

team_elo+none − team_elo (paired log loss):

| Section | Rows | team_elo+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.646281 | 0.646281 | 0.000000 | [0.000000, 0.000000] | no |

player_glicko+none − team_elo (paired log loss):

| Section | Rows | player_glicko+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.610785 | 0.646281 | -0.035496 | [-0.040569, -0.030402] | yes |

team_elo+none − player_glicko (paired log loss):

| Section | Rows | team_elo+none log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.646281 | 0.610785 | 0.035496 | [0.030402, 0.040569] | yes |
| tier1 | 3827 | 0.640800 | 0.589637 | 0.051163 | [0.042523, 0.060174] | yes |
| tier2 | 571 | 0.642339 | 0.629961 | 0.012377 | [-0.009580, 0.034577] | no |
| tier3 | 4930 | 0.650992 | 0.624981 | 0.026011 | [0.019825, 0.032332] | yes |
| international=1 | 3843 | 0.640946 | 0.589611 | 0.051335 | [0.042534, 0.060917] | yes |
| international=0 | 5485 | 0.650019 | 0.625620 | 0.024399 | [0.018435, 0.030255] | yes |

player_glicko+none − player_glicko (paired log loss):

| Section | Rows | player_glicko+none log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 9328 | 0.610785 | 0.610785 | 0.000000 | [0.000000, 0.000000] | no |
| tier1 | 3827 | 0.589637 | 0.589637 | 0.000000 | [0.000000, 0.000000] | no |
| tier2 | 571 | 0.629961 | 0.629961 | 0.000000 | [0.000000, 0.000000] | no |
| tier3 | 4930 | 0.624981 | 0.624981 | 0.000000 | [0.000000, 0.000000] | no |
| international=1 | 3843 | 0.589611 | 0.589611 | 0.000000 | [0.000000, 0.000000] | no |
| international=0 | 5485 | 0.625620 | 0.625620 | 0.000000 | [0.000000, 0.000000] | no |

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

player_glicko − team_elo (paired log loss):

| Section | Rows | player_glicko log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.584862 | 0.638539 | -0.053677 | [-0.061296, -0.045900] | yes |

team_elo+none − team_elo (paired log loss):

| Section | Rows | team_elo+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.638539 | 0.638539 | 0.000000 | [0.000000, 0.000000] | no |

player_glicko+none − team_elo (paired log loss):

| Section | Rows | player_glicko+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.584862 | 0.638539 | -0.053677 | [-0.061296, -0.045900] | yes |

team_elo+none − player_glicko (paired log loss):

| Section | Rows | team_elo+none log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.638539 | 0.584862 | 0.053677 | [0.045900, 0.061296] | yes |
| tier1 | 1960 | 0.627551 | 0.550511 | 0.077040 | [0.064125, 0.090206] | yes |
| tier2 | 268 | 0.614341 | 0.590452 | 0.023888 | [-0.010775, 0.057766] | no |
| tier3 | 2138 | 0.651646 | 0.615654 | 0.035993 | [0.026116, 0.045434] | yes |
| international=1 | 1974 | 0.628065 | 0.550617 | 0.077448 | [0.065380, 0.090447] | yes |
| international=0 | 2392 | 0.647183 | 0.613123 | 0.034059 | [0.024809, 0.043047] | yes |

player_glicko+none − player_glicko (paired log loss):

| Section | Rows | player_glicko+none log loss | player_glicko log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 4366 | 0.584862 | 0.584862 | 0.000000 | [0.000000, 0.000000] | no |
| tier1 | 1960 | 0.550511 | 0.550511 | 0.000000 | [0.000000, 0.000000] | no |
| tier2 | 268 | 0.590452 | 0.590452 | 0.000000 | [0.000000, 0.000000] | no |
| tier3 | 2138 | 0.615654 | 0.615654 | 0.000000 | [0.000000, 0.000000] | no |
| international=1 | 1974 | 0.550617 | 0.550617 | 0.000000 | [0.000000, 0.000000] | no |
| international=0 | 2392 | 0.613123 | 0.613123 | 0.000000 | [0.000000, 0.000000] | no |

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

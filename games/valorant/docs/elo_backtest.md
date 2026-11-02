# Elo variants benchmark

## Combined summary (validation, all sections)

| Model | Series Δ log loss | Series flat ROI | Series Kelly (LoL caps) $ | Series flat ROI depth-capped | Series Kelly depth-capped $ | Map Δ log loss | Map flat ROI | Map Kelly (LoL caps) $ | Map flat ROI depth-capped | Map Kelly depth-capped $ | Series blended Δ log loss | Series blended flat ROI | Series blended Kelly (LoL caps) $ | Series blended flat ROI depth-capped | Series blended Kelly depth-capped $ | Map blended Δ log loss | Map blended flat ROI | Map blended Kelly (LoL caps) $ | Map blended flat ROI depth-capped | Map blended Kelly depth-capped $ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| team_elo | 0.026644 | -2.01% | $0.55 | 15.98% | $128.56 | 0.005994 | 12.02% | $480.61 | 52.76% | $203.47 | 0.000161 | -5.01% | $35.62 | 16.91% | $57.12 | 0.011243 | -8.06% | $7.27 | -5.79% | $38.70 |
| player_round_glicko | -0.001344 | 8.45% | $220.43 | 19.26% | $655.33 | -0.006855 | 18.30% | $4234.75 | 58.09% | $240.23 | -0.007587 | 13.36% | $357.15 | 17.40% | $157.92 | 0.006616 | -3.73% | $29.53 | 4.42% | $47.42 |
| player_round_glicko_rookie_tier_revert_perf_rating | -0.010659 | 13.05% | $1247.73 | 19.94% | $698.18 | -0.011432 | 20.69% | $7961.60 | 57.21% | $291.11 | -0.014470 | 16.36% | $1721.04 | 20.19% | $615.60 | -0.000110 | 17.83% | $188.33 | 98.26% | $159.11 |
| player_round_glicko_rookie_tier_revert_perf_kda | -0.011866 | 13.60% | $1322.94 | 19.95% | $644.08 | -0.012234 | 21.06% | $8139.37 | 63.63% | $297.96 | -0.014865 | 17.59% | $1572.97 | 22.97% | $485.65 | -0.000728 | 18.12% | $172.73 | 92.33% | $136.60 |
| team_elo+none | 0.026644 | -2.01% | $0.55 | 15.98% | $128.56 | 0.005994 | 12.02% | $480.61 | 52.76% | $203.47 | 0.000161 | -5.01% | $35.62 | 16.91% | $57.12 | 0.011243 | -8.06% | $7.27 | -5.79% | $38.70 |
| player_round_glicko+none | -0.001344 | 8.45% | $220.43 | 19.26% | $655.33 | -0.006855 | 18.30% | $4234.75 | 58.09% | $240.23 | -0.007587 | 13.36% | $357.15 | 17.40% | $157.92 | 0.006616 | -3.73% | $29.53 | 4.42% | $47.42 |
| player_round_glicko_rookie_tier_revert_perf_rating+none | -0.010659 | 13.05% | $1247.73 | 19.94% | $698.18 | -0.011432 | 20.69% | $7961.60 | 57.21% | $291.11 | -0.014470 | 16.36% | $1721.04 | 20.19% | $615.60 | -0.000110 | 17.83% | $188.33 | 98.26% | $159.11 |
| player_round_glicko_rookie_tier_revert_perf_kda+none | -0.011866 | 13.60% | $1322.94 | 19.95% | $644.08 | -0.012234 | 21.06% | $8139.37 | 63.63% | $297.96 | -0.014865 | 17.59% | $1572.97 | 22.97% | $485.65 | -0.000728 | 18.12% | $172.73 | 92.33% | $136.60 |

Series momentum: off.

Series temperatures (stage 1; p′ = σ(T·logit p), T < 1 pulls odds toward 50%): team_elo Bo3 0.70, Bo5 0.62; player_round_glicko Bo3 0.87, Bo5 0.84; player_round_glicko_rookie_tier_revert_perf_kda Bo3 0.87, Bo5 0.82; player_round_glicko_rookie_tier_revert_perf_rating Bo3 0.87, Bo5 0.82; team_elo+none Bo3 0.70, Bo5 0.62; player_round_glicko+none Bo3 0.87, Bo5 0.84; player_round_glicko_rookie_tier_revert_perf_rating+none Bo3 0.87, Bo5 0.82; player_round_glicko_rookie_tier_revert_perf_kda+none Bo3 0.87, Bo5 0.82

Parameters minimize tuning map log loss across all sections. Replay predicts before update; Replay starts at the first map. Tuning: [2023-01-01, 2025-09-01); validation: [2025-09-01, 2026-07-01). Holdout is scored only with --holdout and never selects parameters. Series use the first map prediction and an odd best-of map chain (independent when m=0); missing/even best-of or unknown results are skipped. Accuracy gives 0.5 predictions half credit; ECE uses 10 equal-width bins. Log loss clips probabilities at 1e-6. Paired bootstrap uses 2,000 resamples, seed 0, clustered by match_id. Differences are the named model minus its comparator; negative favors the model. Significance requires a 95% percentile interval excluding zero. Tuning scores are selection diagnostics, not independent evidence of improvement.

Fit through 2025-08-31. Unknown host-region map rows: 7142 (including missing/un).

## Stage 1 — tuning (outcomes)

### Leaderboard

| Model | Best params | Map log loss | Series log loss | Rows |
|---|---|---:|---:|---:|
| player_round_glicko_rookie_tier_revert_perf_rating | {"inactive_half_life": 0, "k": 32, "new_player": "teammates", "perf_k": 7, "rd_info": 0.25, "rd_new": 280, "rookie_maps": 400, "rookie_penalty": 200, "season_month": 11, "season_revert": 0.2, "tau": 0.5} | 0.618894 | 0.578453 | 25649 |
| player_round_glicko_rookie_tier_revert_perf_kda | {"inactive_half_life": 0, "k": 32, "new_player": "teammates", "perf_k": 7, "rd_info": 0.25, "rd_new": 280, "rookie_maps": 400, "rookie_penalty": 200, "season_month": 11, "season_revert": 0.2, "tau": 0.5} | 0.618971 | 0.578554 | 25649 |
| player_round_glicko_rookie_tier_revert | {"inactive_half_life": 0, "k": 32, "new_player": "teammates", "rd_info": 0.25, "rd_new": 280, "rookie_maps": 400, "rookie_penalty": 200, "season_month": 11, "season_revert": 0.2, "tau": 0.5} | 0.621941 | 0.582554 | 25649 |
| player_round_glicko_rookie_revert | {"inactive_half_life": 0, "k": 32, "new_player": "teammates", "rd_info": 0.25, "rd_new": 280, "rookie_maps": 400, "rookie_penalty": 200, "season_month": 1, "season_revert": 0.2, "tau": 0.5} | 0.622031 | 0.582771 | 25649 |
| player_round_glicko_rookie_maps | {"k": 32, "map_k": 4, "map_unit": "team", "new_player": "teammates", "pick_bonus": 3, "rd_info": 0.25, "rd_new": 280, "rookie_maps": 400, "rookie_penalty": 200, "tau": 0.5} | 0.622244 | 0.584458 | 25649 |
| player_round_glicko_rookie_pick | {"k": 32, "map_k": 0, "new_player": "teammates", "pick_bonus": 5, "rd_info": 0.25, "rd_new": 280, "rookie_maps": 400, "rookie_penalty": 200, "tau": 0.5} | 0.622402 | 0.585012 | 25649 |
| player_round_glicko_rookie | {"k": 32, "new_player": "teammates", "rd_info": 0.25, "rd_new": 280, "rookie_maps": 400, "rookie_penalty": 200, "tau": 0.5} | 0.622668 | 0.584466 | 25649 |
| player_round_glicko_rookie_moves | {"k": 32, "move_down_bonus": 0, "move_up_penalty": 50, "new_player": "teammates", "rd_info": 0.25, "rd_new": 280, "rookie_maps": 400, "rookie_penalty": 200, "tau": 0.5} | 0.623140 | 0.584873 | 25649 |
| player_round_region_glicko | {"k": 32, "new_player": "fixed", "rd_info": 0.125, "rd_new": 280, "region_k": 2, "tau": 0.5} | 0.628443 | 0.594415 | 25649 |
| player_round_glicko | {"k": 32, "new_player": "fixed", "rd_info": 0.125, "rd_new": 280, "tau": 0.5} | 0.628478 | 0.594535 | 25649 |
| player_round_glicko_moves | {"k": 32, "move_down_bonus": 0, "move_up_penalty": 50, "new_player": "teammates", "rd_info": 0.25, "rd_new": 280, "tau": 0.5} | 0.630448 | 0.598122 | 25649 |
| player_round | {"k": 48, "new_player": "fixed", "tau": 0.5} | 0.630762 | 0.595894 | 25649 |
| player_round_region | {"k": 48, "new_player": "fixed", "region_k": 2, "tau": 0.5} | 0.630806 | 0.596003 | 25649 |
| player_margin | {"c": 6, "k": 64, "new_player": "fixed"} | 0.632889 | 0.599403 | 25649 |
| player_margin_region | {"c": 6, "k": 64, "new_player": "fixed", "region_k": 2} | 0.632896 | 0.599402 | 25649 |
| player_binary_region | {"k": 32, "new_player": "fixed", "region_k": 2} | 0.638726 | 0.606012 | 25649 |
| player_binary | {"k": 32, "new_player": "fixed"} | 0.638835 | 0.606314 | 25649 |
| team_round | {"k": 48, "tau": 0.5} | 0.642208 | 0.616336 | 25649 |
| team_round_region | {"k": 48, "region_k": 2, "tau": 0.5} | 0.642348 | 0.616693 | 25649 |
| team_margin | {"c": 6, "k": 64} | 0.643471 | 0.619078 | 25649 |
| team_margin_region | {"c": 6, "k": 64, "region_k": 2} | 0.643562 | 0.619298 | 25649 |
| team_elo | {"k": 32} | 0.651782 | 0.626711 | 25649 |
| team_binary_region | {"k": 32, "region_k": 2} | 0.651794 | 0.626708 | 25649 |

Kalshi uses the first hourly bid/ask (midpoint for log loss, ask/bid for bets) ending ≥30 min after the market opened and ≥2 h before the scheduled start, with a spread ≤ 0.06: a price a bot could trade before any veto. Markets without such a quote are skipped. oriented to team1 using aliases. One contract per event, preferring team1. Compare identical rows; map predictions use the first map's pre-match chance. Missing links, aliases or candles are skipped; unplayed maps are not in the rows. Returns use frozen stage-1 parameters. Each bet buys $1 of contracts, fees extra; order fees ceil to a cent (0.07 × contracts × price × (1−price)). Edge selection uses unrounded per-contract fees. ROI divides profit by stake plus fees; intervals resample matches 2,000 times. Unlimited depth and depth-capped returns are shown together. Depth uses 0.5 of acceptable-price tape volume in the 6 hours after the quote, missing tapes give zero fills. Partial Kelly fills are allowed; flat bets require the full $1 stake. Kelly uses LoL caps and rounded-fee affordability, from a $50 seed. Each slice runs independently. Tape volume is a fill proxy; no slippage is modeled.

### Maps

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| coin | all | 25649 | 0.693147 | 0.250000 | 0.500000 | 0.042087 |
| coin | vct | 3333 | 0.693147 | 0.250000 | 0.500000 | 0.018152 |
| coin | vcl | 14263 | 0.693147 | 0.250000 | 0.500000 | 0.028150 |
| coin | gc | 4129 | 0.693147 | 0.250000 | 0.500000 | 0.084887 |
| coin | t3 | 1455 | 0.693147 | 0.250000 | 0.500000 | 0.071821 |
| coin | collegiate | 95 | 0.693147 | 0.250000 | 0.500000 | 0.089474 |
| coin | offseason | 2374 | 0.693147 | 0.250000 | 0.500000 | 0.064869 |
| coin | unknown | 0 | — | — | — | — |
| coin | international=1 | 751 | 0.693147 | 0.250000 | 0.500000 | 0.004660 |
| coin | international=0 | 24898 | 0.693147 | 0.250000 | 0.500000 | 0.043216 |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| team_elo | all | 25649 | 0.651782 | 0.229929 | 0.615989 | 0.023986 |
| team_elo | vct | 3333 | 0.677574 | 0.240943 | 0.581758 | 0.063446 |
| team_elo | vcl | 14263 | 0.650388 | 0.229421 | 0.618734 | 0.018886 |
| team_elo | gc | 4129 | 0.626845 | 0.218485 | 0.645193 | 0.051156 |
| team_elo | t3 | 1455 | 0.665545 | 0.236579 | 0.598969 | 0.059461 |
| team_elo | collegiate | 95 | 0.656779 | 0.233016 | 0.594737 | 0.079508 |
| team_elo | offseason | 2374 | 0.658675 | 0.233225 | 0.608045 | 0.032891 |
| team_elo | unknown | 0 | — | — | — | — |
| team_elo | international=1 | 751 | 0.679081 | 0.241826 | 0.585885 | 0.050186 |
| team_elo | international=0 | 24898 | 0.650958 | 0.229570 | 0.616897 | 0.024461 |

team_elo − coin (paired log loss):

| Section | Rows | team_elo log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 25649 | 0.651782 | 0.693147 | -0.041366 | [-0.046095, -0.037066] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko | all | 25649 | 0.628478 | 0.219731 | 0.640961 | 0.012564 |
| player_round_glicko | vct | 3333 | 0.663878 | 0.235584 | 0.602010 | 0.016655 |
| player_round_glicko | vcl | 14263 | 0.629769 | 0.220135 | 0.639697 | 0.011984 |
| player_round_glicko | gc | 4129 | 0.591798 | 0.203687 | 0.683701 | 0.031510 |
| player_round_glicko | t3 | 1455 | 0.635774 | 0.223026 | 0.629553 | 0.046617 |
| player_round_glicko | collegiate | 95 | 0.622474 | 0.218097 | 0.594737 | 0.096005 |
| player_round_glicko | offseason | 2374 | 0.630582 | 0.220996 | 0.637742 | 0.019085 |
| player_round_glicko | unknown | 0 | — | — | — | — |
| player_round_glicko | international=1 | 751 | 0.660817 | 0.234258 | 0.609188 | 0.040330 |
| player_round_glicko | international=0 | 24898 | 0.627502 | 0.219293 | 0.641919 | 0.012363 |

player_round_glicko − coin (paired log loss):

| Section | Rows | player_round_glicko log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 25649 | 0.628478 | 0.693147 | -0.064669 | [-0.069105, -0.060322] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko_rookie_tier_revert_perf_rating | all | 25649 | 0.618894 | 0.215682 | 0.647433 | 0.013194 |
| player_round_glicko_rookie_tier_revert_perf_rating | vct | 3333 | 0.658864 | 0.233209 | 0.603060 | 0.012290 |
| player_round_glicko_rookie_tier_revert_perf_rating | vcl | 14263 | 0.622739 | 0.217177 | 0.645061 | 0.011355 |
| player_round_glicko_rookie_tier_revert_perf_rating | gc | 4129 | 0.572512 | 0.196245 | 0.695447 | 0.029166 |
| player_round_glicko_rookie_tier_revert_perf_rating | t3 | 1455 | 0.619727 | 0.215765 | 0.639519 | 0.038836 |
| player_round_glicko_rookie_tier_revert_perf_rating | collegiate | 95 | 0.604108 | 0.210877 | 0.678947 | 0.088048 |
| player_round_glicko_rookie_tier_revert_perf_rating | offseason | 2374 | 0.620430 | 0.216043 | 0.644061 | 0.018078 |
| player_round_glicko_rookie_tier_revert_perf_rating | unknown | 0 | — | — | — | — |
| player_round_glicko_rookie_tier_revert_perf_rating | international=1 | 751 | 0.655597 | 0.231831 | 0.616511 | 0.026828 |
| player_round_glicko_rookie_tier_revert_perf_rating | international=0 | 24898 | 0.617787 | 0.215195 | 0.648365 | 0.013674 |

player_round_glicko_rookie_tier_revert_perf_rating − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie_tier_revert_perf_rating log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 25649 | 0.618894 | 0.693147 | -0.074253 | [-0.079040, -0.069687] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko_rookie_tier_revert_perf_kda | all | 25649 | 0.618971 | 0.215693 | 0.647589 | 0.013285 |
| player_round_glicko_rookie_tier_revert_perf_kda | vct | 3333 | 0.658715 | 0.233094 | 0.604560 | 0.013280 |
| player_round_glicko_rookie_tier_revert_perf_kda | vcl | 14263 | 0.622662 | 0.217140 | 0.644605 | 0.011055 |
| player_round_glicko_rookie_tier_revert_perf_kda | gc | 4129 | 0.572946 | 0.196366 | 0.694841 | 0.031137 |
| player_round_glicko_rookie_tier_revert_perf_kda | t3 | 1455 | 0.619732 | 0.215705 | 0.644330 | 0.036505 |
| player_round_glicko_rookie_tier_revert_perf_kda | collegiate | 95 | 0.606202 | 0.211403 | 0.689474 | 0.102204 |
| player_round_glicko_rookie_tier_revert_perf_kda | offseason | 2374 | 0.621088 | 0.216354 | 0.644061 | 0.018371 |
| player_round_glicko_rookie_tier_revert_perf_kda | unknown | 0 | — | — | — | — |
| player_round_glicko_rookie_tier_revert_perf_kda | international=1 | 751 | 0.653741 | 0.230964 | 0.617843 | 0.038533 |
| player_round_glicko_rookie_tier_revert_perf_kda | international=0 | 24898 | 0.617922 | 0.215233 | 0.648486 | 0.013680 |

player_round_glicko_rookie_tier_revert_perf_kda − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie_tier_revert_perf_kda log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 25649 | 0.618971 | 0.693147 | -0.074176 | [-0.078896, -0.069598] | yes |

team_binary_region − team_elo (paired log loss):

| Section | Rows | team_binary_region log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 25649 | 0.651794 | 0.651782 | 0.000012 | [-0.000193, 0.000223] | no |

team_margin − team_elo (paired log loss):

| Section | Rows | team_margin log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 25649 | 0.643471 | 0.651782 | -0.008310 | [-0.009866, -0.006848] | yes |

team_margin_region − team_elo (paired log loss):

| Section | Rows | team_margin_region log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 25649 | 0.643562 | 0.651782 | -0.008219 | [-0.009762, -0.006764] | yes |

team_round − team_elo (paired log loss):

| Section | Rows | team_round log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 25649 | 0.642208 | 0.651782 | -0.009573 | [-0.011455, -0.007791] | yes |

team_round_region − team_elo (paired log loss):

| Section | Rows | team_round_region log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 25649 | 0.642348 | 0.651782 | -0.009434 | [-0.011322, -0.007647] | yes |

player_binary − team_elo (paired log loss):

| Section | Rows | player_binary log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 25649 | 0.638835 | 0.651782 | -0.012947 | [-0.015628, -0.010381] | yes |

player_binary_region − team_elo (paired log loss):

| Section | Rows | player_binary_region log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 25649 | 0.638726 | 0.651782 | -0.013055 | [-0.015738, -0.010487] | yes |

player_margin − team_elo (paired log loss):

| Section | Rows | player_margin log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 25649 | 0.632889 | 0.651782 | -0.018892 | [-0.021581, -0.016153] | yes |

player_margin_region − team_elo (paired log loss):

| Section | Rows | player_margin_region log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 25649 | 0.632896 | 0.651782 | -0.018885 | [-0.021556, -0.016140] | yes |

player_round − team_elo (paired log loss):

| Section | Rows | player_round log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 25649 | 0.630762 | 0.651782 | -0.021020 | [-0.023885, -0.018149] | yes |

player_round_region − team_elo (paired log loss):

| Section | Rows | player_round_region log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 25649 | 0.630806 | 0.651782 | -0.020975 | [-0.023841, -0.018113] | yes |

player_round_glicko − team_elo (paired log loss):

| Section | Rows | player_round_glicko log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 25649 | 0.628478 | 0.651782 | -0.023304 | [-0.026369, -0.020135] | yes |

player_round_region_glicko − team_elo (paired log loss):

| Section | Rows | player_round_region_glicko log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 25649 | 0.628443 | 0.651782 | -0.023339 | [-0.026399, -0.020191] | yes |

player_round_glicko_rookie − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 25649 | 0.622668 | 0.651782 | -0.029113 | [-0.032734, -0.025553] | yes |

player_round_glicko_moves − team_elo (paired log loss):

| Section | Rows | player_round_glicko_moves log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 25649 | 0.630448 | 0.651782 | -0.021333 | [-0.024517, -0.018097] | yes |

player_round_glicko_rookie_moves − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie_moves log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 25649 | 0.623140 | 0.651782 | -0.028641 | [-0.032275, -0.025000] | yes |

player_round_glicko_rookie_maps − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie_maps log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 25649 | 0.622244 | 0.651782 | -0.029537 | [-0.033247, -0.025947] | yes |

player_round_glicko_rookie_pick − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie_pick log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 25649 | 0.622402 | 0.651782 | -0.029380 | [-0.033080, -0.025840] | yes |

player_round_glicko_rookie_revert − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie_revert log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 25649 | 0.622031 | 0.651782 | -0.029750 | [-0.033131, -0.026441] | yes |

player_round_glicko_rookie_tier_revert − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie_tier_revert log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 25649 | 0.621941 | 0.651782 | -0.029840 | [-0.033182, -0.026520] | yes |

player_round_glicko_rookie_tier_revert_perf_kda − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie_tier_revert_perf_kda log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 25649 | 0.618971 | 0.651782 | -0.032811 | [-0.036367, -0.029427] | yes |

player_round_glicko_rookie_tier_revert_perf_rating − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie_tier_revert_perf_rating log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 25649 | 0.618894 | 0.651782 | -0.032887 | [-0.036491, -0.029412] | yes |

### Series

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| coin | all | 11288 | 0.693147 | 0.250000 | 0.500000 | 0.054128 |
| coin | vct | 1322 | 0.693147 | 0.250000 | 0.500000 | 0.037065 |
| coin | vcl | 6463 | 0.693147 | 0.250000 | 0.500000 | 0.035510 |
| coin | gc | 1698 | 0.693147 | 0.250000 | 0.500000 | 0.106007 |
| coin | t3 | 650 | 0.693147 | 0.250000 | 0.500000 | 0.092308 |
| coin | collegiate | 42 | 0.693147 | 0.250000 | 0.500000 | 0.095238 |
| coin | offseason | 1113 | 0.693147 | 0.250000 | 0.500000 | 0.079515 |
| coin | unknown | 0 | — | — | — | — |
| coin | international=1 | 310 | 0.693147 | 0.250000 | 0.500000 | 0.016129 |
| coin | international=0 | 10978 | 0.693147 | 0.250000 | 0.500000 | 0.055201 |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| team_elo | all | 11288 | 0.626711 | 0.218731 | 0.643692 | 0.027296 |
| team_elo | vct | 1322 | 0.641839 | 0.225179 | 0.627837 | 0.034264 |
| team_elo | vcl | 6463 | 0.624950 | 0.217878 | 0.650549 | 0.018614 |
| team_elo | gc | 1698 | 0.601043 | 0.207539 | 0.657833 | 0.070171 |
| team_elo | t3 | 650 | 0.656447 | 0.232376 | 0.603846 | 0.081441 |
| team_elo | collegiate | 42 | 0.643076 | 0.226759 | 0.630952 | 0.119004 |
| team_elo | offseason | 1113 | 0.640138 | 0.224827 | 0.624888 | 0.034341 |
| team_elo | unknown | 0 | — | — | — | — |
| team_elo | international=1 | 310 | 0.663269 | 0.234321 | 0.619355 | 0.046489 |
| team_elo | international=0 | 10978 | 0.625678 | 0.218291 | 0.644380 | 0.028178 |

team_elo − coin (paired log loss):

| Section | Rows | team_elo log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 11288 | 0.626711 | 0.693147 | -0.066437 | [-0.072453, -0.059803] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko | all | 11288 | 0.594535 | 0.204833 | 0.672218 | 0.019080 |
| player_round_glicko | vct | 1322 | 0.633346 | 0.221626 | 0.629728 | 0.029111 |
| player_round_glicko | vcl | 6463 | 0.594866 | 0.204762 | 0.674300 | 0.012414 |
| player_round_glicko | gc | 1698 | 0.548365 | 0.185351 | 0.714664 | 0.042344 |
| player_round_glicko | t3 | 650 | 0.617678 | 0.214101 | 0.653846 | 0.066299 |
| player_round_glicko | collegiate | 42 | 0.610469 | 0.213245 | 0.607143 | 0.133285 |
| player_round_glicko | offseason | 1113 | 0.602831 | 0.209289 | 0.659030 | 0.041620 |
| player_round_glicko | unknown | 0 | — | — | — | — |
| player_round_glicko | international=1 | 310 | 0.636824 | 0.223335 | 0.641935 | 0.038932 |
| player_round_glicko | international=0 | 10978 | 0.593340 | 0.204311 | 0.673073 | 0.020085 |

player_round_glicko − coin (paired log loss):

| Section | Rows | player_round_glicko log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 11288 | 0.594535 | 0.693147 | -0.098613 | [-0.106008, -0.091108] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko_rookie_tier_revert_perf_rating | all | 11288 | 0.578453 | 0.197874 | 0.687411 | 0.016667 |
| player_round_glicko_rookie_tier_revert_perf_rating | vct | 1322 | 0.622623 | 0.217284 | 0.647504 | 0.021249 |
| player_round_glicko_rookie_tier_revert_perf_rating | vcl | 6463 | 0.583228 | 0.199848 | 0.684512 | 0.011993 |
| player_round_glicko_rookie_tier_revert_perf_rating | gc | 1698 | 0.511630 | 0.170233 | 0.746466 | 0.032181 |
| player_round_glicko_rookie_tier_revert_perf_rating | t3 | 650 | 0.589595 | 0.200985 | 0.660769 | 0.059471 |
| player_round_glicko_rookie_tier_revert_perf_rating | collegiate | 42 | 0.630693 | 0.221021 | 0.726190 | 0.201735 |
| player_round_glicko_rookie_tier_revert_perf_rating | offseason | 1113 | 0.591723 | 0.202832 | 0.675651 | 0.027702 |
| player_round_glicko_rookie_tier_revert_perf_rating | unknown | 0 | — | — | — | — |
| player_round_glicko_rookie_tier_revert_perf_rating | international=1 | 310 | 0.628911 | 0.219622 | 0.648387 | 0.039059 |
| player_round_glicko_rookie_tier_revert_perf_rating | international=0 | 10978 | 0.577028 | 0.197260 | 0.688513 | 0.017230 |

player_round_glicko_rookie_tier_revert_perf_rating − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie_tier_revert_perf_rating log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 11288 | 0.578453 | 0.693147 | -0.114695 | [-0.122752, -0.106634] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko_rookie_tier_revert_perf_kda | all | 11288 | 0.578554 | 0.197896 | 0.687899 | 0.015815 |
| player_round_glicko_rookie_tier_revert_perf_kda | vct | 1322 | 0.622116 | 0.217011 | 0.646747 | 0.025363 |
| player_round_glicko_rookie_tier_revert_perf_kda | vcl | 6463 | 0.583191 | 0.199836 | 0.684357 | 0.010381 |
| player_round_glicko_rookie_tier_revert_perf_kda | gc | 1698 | 0.511744 | 0.170231 | 0.750589 | 0.037981 |
| player_round_glicko_rookie_tier_revert_perf_kda | t3 | 650 | 0.589559 | 0.200914 | 0.669231 | 0.053329 |
| player_round_glicko_rookie_tier_revert_perf_kda | collegiate | 42 | 0.638643 | 0.222338 | 0.726190 | 0.187232 |
| player_round_glicko_rookie_tier_revert_perf_kda | offseason | 1113 | 0.593115 | 0.203445 | 0.671159 | 0.029441 |
| player_round_glicko_rookie_tier_revert_perf_kda | unknown | 0 | — | — | — | — |
| player_round_glicko_rookie_tier_revert_perf_kda | international=1 | 310 | 0.623866 | 0.217425 | 0.651613 | 0.040007 |
| player_round_glicko_rookie_tier_revert_perf_kda | international=0 | 10978 | 0.577274 | 0.197344 | 0.688923 | 0.016374 |

player_round_glicko_rookie_tier_revert_perf_kda − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie_tier_revert_perf_kda log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 11288 | 0.578554 | 0.693147 | -0.114593 | [-0.122594, -0.106618] | yes |

team_binary_region − team_elo (paired log loss):

| Section | Rows | team_binary_region log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 11288 | 0.626708 | 0.626711 | -0.000003 | [-0.000366, 0.000366] | no |

team_margin − team_elo (paired log loss):

| Section | Rows | team_margin log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 11288 | 0.619078 | 0.626711 | -0.007632 | [-0.010051, -0.005320] | yes |

team_margin_region − team_elo (paired log loss):

| Section | Rows | team_margin_region log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 11288 | 0.619298 | 0.626711 | -0.007413 | [-0.009823, -0.005109] | yes |

team_round − team_elo (paired log loss):

| Section | Rows | team_round log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 11288 | 0.616336 | 0.626711 | -0.010375 | [-0.013160, -0.007556] | yes |

team_round_region − team_elo (paired log loss):

| Section | Rows | team_round_region log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 11288 | 0.616693 | 0.626711 | -0.010017 | [-0.012879, -0.007206] | yes |

player_binary − team_elo (paired log loss):

| Section | Rows | player_binary log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 11288 | 0.606314 | 0.626711 | -0.020396 | [-0.024969, -0.016112] | yes |

player_binary_region − team_elo (paired log loss):

| Section | Rows | player_binary_region log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 11288 | 0.606012 | 0.626711 | -0.020699 | [-0.025296, -0.016431] | yes |

player_margin − team_elo (paired log loss):

| Section | Rows | player_margin log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 11288 | 0.599403 | 0.626711 | -0.027308 | [-0.032003, -0.022622] | yes |

player_margin_region − team_elo (paired log loss):

| Section | Rows | player_margin_region log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 11288 | 0.599402 | 0.626711 | -0.027308 | [-0.032022, -0.022648] | yes |

player_round − team_elo (paired log loss):

| Section | Rows | player_round log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 11288 | 0.595894 | 0.626711 | -0.030816 | [-0.035940, -0.025796] | yes |

player_round_region − team_elo (paired log loss):

| Section | Rows | player_round_region log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 11288 | 0.596003 | 0.626711 | -0.030708 | [-0.035801, -0.025664] | yes |

player_round_glicko − team_elo (paired log loss):

| Section | Rows | player_round_glicko log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 11288 | 0.594535 | 0.626711 | -0.032176 | [-0.037405, -0.027019] | yes |

player_round_region_glicko − team_elo (paired log loss):

| Section | Rows | player_round_region_glicko log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 11288 | 0.594415 | 0.626711 | -0.032296 | [-0.037510, -0.027073] | yes |

player_round_glicko_rookie − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 11288 | 0.584466 | 0.626711 | -0.042245 | [-0.048494, -0.036019] | yes |

player_round_glicko_moves − team_elo (paired log loss):

| Section | Rows | player_round_glicko_moves log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 11288 | 0.598122 | 0.626711 | -0.028588 | [-0.034064, -0.023040] | yes |

player_round_glicko_rookie_moves − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie_moves log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 11288 | 0.584873 | 0.626711 | -0.041838 | [-0.048172, -0.035670] | yes |

player_round_glicko_rookie_maps − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie_maps log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 11288 | 0.584458 | 0.626711 | -0.042253 | [-0.048466, -0.036079] | yes |

player_round_glicko_rookie_pick − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie_pick log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 11288 | 0.585012 | 0.626711 | -0.041699 | [-0.047904, -0.035502] | yes |

player_round_glicko_rookie_revert − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie_revert log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 11288 | 0.582771 | 0.626711 | -0.043939 | [-0.049839, -0.037997] | yes |

player_round_glicko_rookie_tier_revert − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie_tier_revert log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 11288 | 0.582554 | 0.626711 | -0.044157 | [-0.050092, -0.038130] | yes |

player_round_glicko_rookie_tier_revert_perf_kda − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie_tier_revert_perf_kda log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 11288 | 0.578554 | 0.626711 | -0.048157 | [-0.054202, -0.042073] | yes |

player_round_glicko_rookie_tier_revert_perf_rating − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie_tier_revert_perf_rating log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 11288 | 0.578453 | 0.626711 | -0.048258 | [-0.054403, -0.041950] | yes |

## Stage 2 — validation (outcomes)

### Leaderboard (frozen stage-1 parameters)

| Model | Best params | Map log loss | Series log loss | Rows |
|---|---|---:|---:|---:|
| player_round_glicko_rookie_tier_revert_perf_kda | {"inactive_half_life": 0, "k": 32, "new_player": "teammates", "perf_k": 7, "rd_info": 0.25, "rd_new": 280, "rookie_maps": 400, "rookie_penalty": 200, "season_month": 11, "season_revert": 0.2, "tau": 0.5} | 0.635951 | 0.600674 | 6337 |
| player_round_glicko_rookie_tier_revert_perf_kda+none | {"inactive_half_life": 0, "k": 32, "new_player": "teammates", "perf_k": 7, "rd_info": 0.25, "rd_new": 280, "rookie_maps": 400, "rookie_penalty": 200, "season_month": 11, "season_revert": 0.2, "tau": 0.5} | 0.635951 | 0.600674 | 6337 |
| player_round_glicko_rookie_tier_revert_perf_rating | {"inactive_half_life": 0, "k": 32, "new_player": "teammates", "perf_k": 7, "rd_info": 0.25, "rd_new": 280, "rookie_maps": 400, "rookie_penalty": 200, "season_month": 11, "season_revert": 0.2, "tau": 0.5} | 0.636239 | 0.600934 | 6337 |
| player_round_glicko_rookie_tier_revert_perf_rating+none | {"inactive_half_life": 0, "k": 32, "new_player": "teammates", "perf_k": 7, "rd_info": 0.25, "rd_new": 280, "rookie_maps": 400, "rookie_penalty": 200, "season_month": 11, "season_revert": 0.2, "tau": 0.5} | 0.636239 | 0.600934 | 6337 |
| player_round_glicko | {"k": 32, "new_player": "fixed", "rd_info": 0.125, "rd_new": 280, "tau": 0.5} | 0.642512 | 0.616378 | 6337 |
| player_round_glicko+none | {"k": 32, "new_player": "fixed", "rd_info": 0.125, "rd_new": 280, "tau": 0.5} | 0.642512 | 0.616378 | 6337 |
| team_elo | {"k": 32} | 0.662947 | 0.643432 | 6337 |
| team_elo+none | {"k": 32} | 0.662947 | 0.643432 | 6337 |

### Maps

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| coin | all | 6337 | 0.693147 | 0.250000 | 0.500000 | 0.043475 |
| coin | vct | 1080 | 0.693147 | 0.250000 | 0.500000 | 0.016667 |
| coin | vcl | 3374 | 0.693147 | 0.250000 | 0.500000 | 0.047125 |
| coin | gc | 1005 | 0.693147 | 0.250000 | 0.500000 | 0.103980 |
| coin | t3 | 16 | 0.693147 | 0.250000 | 0.500000 | 0.250000 |
| coin | collegiate | 7 | 0.693147 | 0.250000 | 0.500000 | 0.071429 |
| coin | offseason | 855 | 0.693147 | 0.250000 | 0.500000 | 0.030994 |
| coin | unknown | 0 | — | — | — | — |
| coin | international=1 | 268 | 0.693147 | 0.250000 | 0.500000 | 0.003731 |
| coin | international=0 | 6069 | 0.693147 | 0.250000 | 0.500000 | 0.045230 |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| team_elo | all | 6337 | 0.662947 | 0.234966 | 0.602730 | 0.031254 |
| team_elo | vct | 1080 | 0.685646 | 0.245671 | 0.564815 | 0.063606 |
| team_elo | vcl | 3374 | 0.666871 | 0.236503 | 0.604624 | 0.042181 |
| team_elo | gc | 1005 | 0.631112 | 0.221113 | 0.637313 | 0.043127 |
| team_elo | t3 | 16 | 0.458119 | 0.148245 | 0.750000 | 0.220932 |
| team_elo | collegiate | 7 | 0.735155 | 0.270941 | 0.285714 | 0.236280 |
| team_elo | offseason | 855 | 0.659448 | 0.232990 | 0.602339 | 0.029427 |
| team_elo | unknown | 0 | — | — | — | — |
| team_elo | international=1 | 268 | 0.672124 | 0.240160 | 0.589552 | 0.065781 |
| team_elo | international=0 | 6069 | 0.662541 | 0.234737 | 0.603312 | 0.030130 |

team_elo − coin (paired log loss):

| Section | Rows | team_elo log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6337 | 0.662947 | 0.693147 | -0.030201 | [-0.038540, -0.021979] | yes |
| vct | 1080 | 0.685646 | 0.693147 | -0.007501 | [-0.027539, 0.011220] | no |
| vcl | 3374 | 0.666871 | 0.693147 | -0.026276 | [-0.037134, -0.014615] | yes |
| gc | 1005 | 0.631112 | 0.693147 | -0.062035 | [-0.085840, -0.039958] | yes |
| t3 | 16 | 0.458119 | 0.693147 | -0.235028 | [-0.504444, -0.062593] | yes |
| collegiate | 7 | 0.735155 | 0.693147 | 0.042008 | [0.035882, 0.046602] | yes |
| offseason | 855 | 0.659448 | 0.693147 | -0.033700 | [-0.057063, -0.010644] | yes |
| international=1 | 268 | 0.672124 | 0.693147 | -0.021024 | [-0.063385, 0.018346] | no |
| international=0 | 6069 | 0.662541 | 0.693147 | -0.030606 | [-0.039247, -0.021872] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko | all | 6337 | 0.642512 | 0.225904 | 0.624980 | 0.017046 |
| player_round_glicko | vct | 1080 | 0.665615 | 0.236969 | 0.596759 | 0.033042 |
| player_round_glicko | vcl | 3374 | 0.646406 | 0.227401 | 0.621814 | 0.033282 |
| player_round_glicko | gc | 1005 | 0.601915 | 0.208076 | 0.668657 | 0.036133 |
| player_round_glicko | t3 | 16 | 0.556141 | 0.190378 | 0.750000 | 0.221812 |
| player_round_glicko | collegiate | 7 | 0.748682 | 0.277371 | 0.428571 | 0.141317 |
| player_round_glicko | offseason | 855 | 0.646431 | 0.227223 | 0.621053 | 0.018024 |
| player_round_glicko | unknown | 0 | — | — | — | — |
| player_round_glicko | international=1 | 268 | 0.668746 | 0.238344 | 0.602612 | 0.061224 |
| player_round_glicko | international=0 | 6069 | 0.641354 | 0.225355 | 0.625968 | 0.018125 |

player_round_glicko − coin (paired log loss):

| Section | Rows | player_round_glicko log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6337 | 0.642512 | 0.693147 | -0.050635 | [-0.059102, -0.042387] | yes |
| vct | 1080 | 0.665615 | 0.693147 | -0.027533 | [-0.043626, -0.012209] | yes |
| vcl | 3374 | 0.646406 | 0.693147 | -0.046741 | [-0.058625, -0.034942] | yes |
| gc | 1005 | 0.601915 | 0.693147 | -0.091232 | [-0.114980, -0.068516] | yes |
| t3 | 16 | 0.556141 | 0.693147 | -0.137006 | [-0.433244, 0.057324] | no |
| collegiate | 7 | 0.748682 | 0.693147 | 0.055535 | [0.031353, 0.087777] | yes |
| offseason | 855 | 0.646431 | 0.693147 | -0.046716 | [-0.069716, -0.024406] | yes |
| international=1 | 268 | 0.668746 | 0.693147 | -0.024401 | [-0.056066, 0.004539] | no |
| international=0 | 6069 | 0.641354 | 0.693147 | -0.051793 | [-0.060460, -0.043631] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko_rookie_tier_revert_perf_rating | all | 6337 | 0.636239 | 0.223008 | 0.635237 | 0.014997 |
| player_round_glicko_rookie_tier_revert_perf_rating | vct | 1080 | 0.666843 | 0.237265 | 0.596759 | 0.034821 |
| player_round_glicko_rookie_tier_revert_perf_rating | vcl | 3374 | 0.642174 | 0.225256 | 0.629075 | 0.030705 |
| player_round_glicko_rookie_tier_revert_perf_rating | gc | 1005 | 0.593066 | 0.204580 | 0.691045 | 0.037564 |
| player_round_glicko_rookie_tier_revert_perf_rating | t3 | 16 | 0.494421 | 0.166002 | 0.687500 | 0.204775 |
| player_round_glicko_rookie_tier_revert_perf_rating | collegiate | 7 | 0.740178 | 0.273507 | 0.285714 | 0.393072 |
| player_round_glicko_rookie_tier_revert_perf_rating | offseason | 855 | 0.626714 | 0.218446 | 0.644444 | 0.024790 |
| player_round_glicko_rookie_tier_revert_perf_rating | unknown | 0 | — | — | — | — |
| player_round_glicko_rookie_tier_revert_perf_rating | international=1 | 268 | 0.660917 | 0.234694 | 0.598881 | 0.018335 |
| player_round_glicko_rookie_tier_revert_perf_rating | international=0 | 6069 | 0.635150 | 0.222492 | 0.636843 | 0.015753 |

player_round_glicko_rookie_tier_revert_perf_rating − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie_tier_revert_perf_rating log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6337 | 0.636239 | 0.693147 | -0.056908 | [-0.065838, -0.048252] | yes |
| vct | 1080 | 0.666843 | 0.693147 | -0.026304 | [-0.042277, -0.011283] | yes |
| vcl | 3374 | 0.642174 | 0.693147 | -0.050973 | [-0.063180, -0.038346] | yes |
| gc | 1005 | 0.593066 | 0.693147 | -0.100081 | [-0.125452, -0.076664] | yes |
| t3 | 16 | 0.494421 | 0.693147 | -0.198726 | [-0.472658, -0.030360] | yes |
| collegiate | 7 | 0.740178 | 0.693147 | 0.047031 | [0.043263, 0.049857] | yes |
| offseason | 855 | 0.626714 | 0.693147 | -0.066433 | [-0.091306, -0.041614] | yes |
| international=1 | 268 | 0.660917 | 0.693147 | -0.032231 | [-0.060903, -0.006293] | yes |
| international=0 | 6069 | 0.635150 | 0.693147 | -0.057997 | [-0.067414, -0.049158] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko_rookie_tier_revert_perf_kda | all | 6337 | 0.635951 | 0.222930 | 0.633659 | 0.013933 |
| player_round_glicko_rookie_tier_revert_perf_kda | vct | 1080 | 0.666892 | 0.237266 | 0.598148 | 0.032302 |
| player_round_glicko_rookie_tier_revert_perf_kda | vcl | 3374 | 0.641423 | 0.225003 | 0.628038 | 0.029431 |
| player_round_glicko_rookie_tier_revert_perf_kda | gc | 1005 | 0.593081 | 0.204576 | 0.689055 | 0.035206 |
| player_round_glicko_rookie_tier_revert_perf_kda | t3 | 16 | 0.510340 | 0.172690 | 0.687500 | 0.216481 |
| player_round_glicko_rookie_tier_revert_perf_kda | collegiate | 7 | 0.742029 | 0.274394 | 0.285714 | 0.393758 |
| player_round_glicko_rookie_tier_revert_perf_kda | offseason | 855 | 0.627149 | 0.218731 | 0.637427 | 0.019672 |
| player_round_glicko_rookie_tier_revert_perf_kda | unknown | 0 | — | — | — | — |
| player_round_glicko_rookie_tier_revert_perf_kda | international=1 | 268 | 0.662914 | 0.235645 | 0.589552 | 0.012482 |
| player_round_glicko_rookie_tier_revert_perf_kda | international=0 | 6069 | 0.634761 | 0.222368 | 0.635607 | 0.014737 |

player_round_glicko_rookie_tier_revert_perf_kda − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie_tier_revert_perf_kda log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6337 | 0.635951 | 0.693147 | -0.057196 | [-0.066029, -0.048673] | yes |
| vct | 1080 | 0.666892 | 0.693147 | -0.026255 | [-0.042092, -0.011162] | yes |
| vcl | 3374 | 0.641423 | 0.693147 | -0.051724 | [-0.063883, -0.039181] | yes |
| gc | 1005 | 0.593081 | 0.693147 | -0.100067 | [-0.125259, -0.077064] | yes |
| t3 | 16 | 0.510340 | 0.693147 | -0.182807 | [-0.455281, -0.019419] | yes |
| collegiate | 7 | 0.742029 | 0.693147 | 0.048882 | [0.045211, 0.051636] | yes |
| offseason | 855 | 0.627149 | 0.693147 | -0.065998 | [-0.090663, -0.041596] | yes |
| international=1 | 268 | 0.662914 | 0.693147 | -0.030233 | [-0.057762, -0.005331] | yes |
| international=0 | 6069 | 0.634761 | 0.693147 | -0.058386 | [-0.067720, -0.049509] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| team_elo+none | all | 6337 | 0.662947 | 0.234966 | 0.602730 | 0.031254 |
| team_elo+none | vct | 1080 | 0.685646 | 0.245671 | 0.564815 | 0.063606 |
| team_elo+none | vcl | 3374 | 0.666871 | 0.236503 | 0.604624 | 0.042181 |
| team_elo+none | gc | 1005 | 0.631112 | 0.221113 | 0.637313 | 0.043127 |
| team_elo+none | t3 | 16 | 0.458119 | 0.148245 | 0.750000 | 0.220932 |
| team_elo+none | collegiate | 7 | 0.735155 | 0.270941 | 0.285714 | 0.236280 |
| team_elo+none | offseason | 855 | 0.659448 | 0.232990 | 0.602339 | 0.029427 |
| team_elo+none | unknown | 0 | — | — | — | — |
| team_elo+none | international=1 | 268 | 0.672124 | 0.240160 | 0.589552 | 0.065781 |
| team_elo+none | international=0 | 6069 | 0.662541 | 0.234737 | 0.603312 | 0.030130 |

team_elo+none − coin (paired log loss):

| Section | Rows | team_elo+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6337 | 0.662947 | 0.693147 | -0.030201 | [-0.038540, -0.021979] | yes |
| vct | 1080 | 0.685646 | 0.693147 | -0.007501 | [-0.027539, 0.011220] | no |
| vcl | 3374 | 0.666871 | 0.693147 | -0.026276 | [-0.037134, -0.014615] | yes |
| gc | 1005 | 0.631112 | 0.693147 | -0.062035 | [-0.085840, -0.039958] | yes |
| t3 | 16 | 0.458119 | 0.693147 | -0.235028 | [-0.504444, -0.062593] | yes |
| collegiate | 7 | 0.735155 | 0.693147 | 0.042008 | [0.035882, 0.046602] | yes |
| offseason | 855 | 0.659448 | 0.693147 | -0.033700 | [-0.057063, -0.010644] | yes |
| international=1 | 268 | 0.672124 | 0.693147 | -0.021024 | [-0.063385, 0.018346] | no |
| international=0 | 6069 | 0.662541 | 0.693147 | -0.030606 | [-0.039247, -0.021872] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko+none | all | 6337 | 0.642512 | 0.225904 | 0.624980 | 0.017046 |
| player_round_glicko+none | vct | 1080 | 0.665615 | 0.236969 | 0.596759 | 0.033042 |
| player_round_glicko+none | vcl | 3374 | 0.646406 | 0.227401 | 0.621814 | 0.033282 |
| player_round_glicko+none | gc | 1005 | 0.601915 | 0.208076 | 0.668657 | 0.036133 |
| player_round_glicko+none | t3 | 16 | 0.556141 | 0.190378 | 0.750000 | 0.221812 |
| player_round_glicko+none | collegiate | 7 | 0.748682 | 0.277371 | 0.428571 | 0.141317 |
| player_round_glicko+none | offseason | 855 | 0.646431 | 0.227223 | 0.621053 | 0.018024 |
| player_round_glicko+none | unknown | 0 | — | — | — | — |
| player_round_glicko+none | international=1 | 268 | 0.668746 | 0.238344 | 0.602612 | 0.061224 |
| player_round_glicko+none | international=0 | 6069 | 0.641354 | 0.225355 | 0.625968 | 0.018125 |

player_round_glicko+none − coin (paired log loss):

| Section | Rows | player_round_glicko+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6337 | 0.642512 | 0.693147 | -0.050635 | [-0.059102, -0.042387] | yes |
| vct | 1080 | 0.665615 | 0.693147 | -0.027533 | [-0.043626, -0.012209] | yes |
| vcl | 3374 | 0.646406 | 0.693147 | -0.046741 | [-0.058625, -0.034942] | yes |
| gc | 1005 | 0.601915 | 0.693147 | -0.091232 | [-0.114980, -0.068516] | yes |
| t3 | 16 | 0.556141 | 0.693147 | -0.137006 | [-0.433244, 0.057324] | no |
| collegiate | 7 | 0.748682 | 0.693147 | 0.055535 | [0.031353, 0.087777] | yes |
| offseason | 855 | 0.646431 | 0.693147 | -0.046716 | [-0.069716, -0.024406] | yes |
| international=1 | 268 | 0.668746 | 0.693147 | -0.024401 | [-0.056066, 0.004539] | no |
| international=0 | 6069 | 0.641354 | 0.693147 | -0.051793 | [-0.060460, -0.043631] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko_rookie_tier_revert_perf_rating+none | all | 6337 | 0.636239 | 0.223008 | 0.635237 | 0.014997 |
| player_round_glicko_rookie_tier_revert_perf_rating+none | vct | 1080 | 0.666843 | 0.237265 | 0.596759 | 0.034821 |
| player_round_glicko_rookie_tier_revert_perf_rating+none | vcl | 3374 | 0.642174 | 0.225256 | 0.629075 | 0.030705 |
| player_round_glicko_rookie_tier_revert_perf_rating+none | gc | 1005 | 0.593066 | 0.204580 | 0.691045 | 0.037564 |
| player_round_glicko_rookie_tier_revert_perf_rating+none | t3 | 16 | 0.494421 | 0.166002 | 0.687500 | 0.204775 |
| player_round_glicko_rookie_tier_revert_perf_rating+none | collegiate | 7 | 0.740178 | 0.273507 | 0.285714 | 0.393072 |
| player_round_glicko_rookie_tier_revert_perf_rating+none | offseason | 855 | 0.626714 | 0.218446 | 0.644444 | 0.024790 |
| player_round_glicko_rookie_tier_revert_perf_rating+none | unknown | 0 | — | — | — | — |
| player_round_glicko_rookie_tier_revert_perf_rating+none | international=1 | 268 | 0.660917 | 0.234694 | 0.598881 | 0.018335 |
| player_round_glicko_rookie_tier_revert_perf_rating+none | international=0 | 6069 | 0.635150 | 0.222492 | 0.636843 | 0.015753 |

player_round_glicko_rookie_tier_revert_perf_rating+none − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie_tier_revert_perf_rating+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6337 | 0.636239 | 0.693147 | -0.056908 | [-0.065838, -0.048252] | yes |
| vct | 1080 | 0.666843 | 0.693147 | -0.026304 | [-0.042277, -0.011283] | yes |
| vcl | 3374 | 0.642174 | 0.693147 | -0.050973 | [-0.063180, -0.038346] | yes |
| gc | 1005 | 0.593066 | 0.693147 | -0.100081 | [-0.125452, -0.076664] | yes |
| t3 | 16 | 0.494421 | 0.693147 | -0.198726 | [-0.472658, -0.030360] | yes |
| collegiate | 7 | 0.740178 | 0.693147 | 0.047031 | [0.043263, 0.049857] | yes |
| offseason | 855 | 0.626714 | 0.693147 | -0.066433 | [-0.091306, -0.041614] | yes |
| international=1 | 268 | 0.660917 | 0.693147 | -0.032231 | [-0.060903, -0.006293] | yes |
| international=0 | 6069 | 0.635150 | 0.693147 | -0.057997 | [-0.067414, -0.049158] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko_rookie_tier_revert_perf_kda+none | all | 6337 | 0.635951 | 0.222930 | 0.633659 | 0.013933 |
| player_round_glicko_rookie_tier_revert_perf_kda+none | vct | 1080 | 0.666892 | 0.237266 | 0.598148 | 0.032302 |
| player_round_glicko_rookie_tier_revert_perf_kda+none | vcl | 3374 | 0.641423 | 0.225003 | 0.628038 | 0.029431 |
| player_round_glicko_rookie_tier_revert_perf_kda+none | gc | 1005 | 0.593081 | 0.204576 | 0.689055 | 0.035206 |
| player_round_glicko_rookie_tier_revert_perf_kda+none | t3 | 16 | 0.510340 | 0.172690 | 0.687500 | 0.216481 |
| player_round_glicko_rookie_tier_revert_perf_kda+none | collegiate | 7 | 0.742029 | 0.274394 | 0.285714 | 0.393758 |
| player_round_glicko_rookie_tier_revert_perf_kda+none | offseason | 855 | 0.627149 | 0.218731 | 0.637427 | 0.019672 |
| player_round_glicko_rookie_tier_revert_perf_kda+none | unknown | 0 | — | — | — | — |
| player_round_glicko_rookie_tier_revert_perf_kda+none | international=1 | 268 | 0.662914 | 0.235645 | 0.589552 | 0.012482 |
| player_round_glicko_rookie_tier_revert_perf_kda+none | international=0 | 6069 | 0.634761 | 0.222368 | 0.635607 | 0.014737 |

player_round_glicko_rookie_tier_revert_perf_kda+none − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie_tier_revert_perf_kda+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6337 | 0.635951 | 0.693147 | -0.057196 | [-0.066029, -0.048673] | yes |
| vct | 1080 | 0.666892 | 0.693147 | -0.026255 | [-0.042092, -0.011162] | yes |
| vcl | 3374 | 0.641423 | 0.693147 | -0.051724 | [-0.063883, -0.039181] | yes |
| gc | 1005 | 0.593081 | 0.693147 | -0.100067 | [-0.125259, -0.077064] | yes |
| t3 | 16 | 0.510340 | 0.693147 | -0.182807 | [-0.455281, -0.019419] | yes |
| collegiate | 7 | 0.742029 | 0.693147 | 0.048882 | [0.045211, 0.051636] | yes |
| offseason | 855 | 0.627149 | 0.693147 | -0.065998 | [-0.090663, -0.041596] | yes |
| international=1 | 268 | 0.662914 | 0.693147 | -0.030233 | [-0.057762, -0.005331] | yes |
| international=0 | 6069 | 0.634761 | 0.693147 | -0.058386 | [-0.067720, -0.049509] | yes |

player_round_glicko − team_elo (paired log loss):

| Section | Rows | player_round_glicko log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6337 | 0.642512 | 0.662947 | -0.020434 | [-0.026736, -0.014494] | yes |

player_round_glicko_rookie_tier_revert_perf_rating − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie_tier_revert_perf_rating log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6337 | 0.636239 | 0.662947 | -0.026707 | [-0.033483, -0.020180] | yes |

player_round_glicko_rookie_tier_revert_perf_kda − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie_tier_revert_perf_kda log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6337 | 0.635951 | 0.662947 | -0.026995 | [-0.033749, -0.020585] | yes |

team_elo+none − team_elo (paired log loss):

| Section | Rows | team_elo+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6337 | 0.662947 | 0.662947 | 0.000000 | [0.000000, 0.000000] | no |

player_round_glicko+none − team_elo (paired log loss):

| Section | Rows | player_round_glicko+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6337 | 0.642512 | 0.662947 | -0.020434 | [-0.026736, -0.014494] | yes |

player_round_glicko_rookie_tier_revert_perf_rating+none − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie_tier_revert_perf_rating+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6337 | 0.636239 | 0.662947 | -0.026707 | [-0.033483, -0.020180] | yes |

player_round_glicko_rookie_tier_revert_perf_kda+none − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie_tier_revert_perf_kda+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 6337 | 0.635951 | 0.662947 | -0.026995 | [-0.033749, -0.020585] | yes |

### Series

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| coin | all | 2618 | 0.693147 | 0.250000 | 0.500000 | 0.056532 |
| coin | vct | 415 | 0.693147 | 0.250000 | 0.500000 | 0.018072 |
| coin | vcl | 1351 | 0.693147 | 0.250000 | 0.500000 | 0.058105 |
| coin | gc | 409 | 0.693147 | 0.250000 | 0.500000 | 0.143032 |
| coin | t3 | 6 | 0.693147 | 0.250000 | 0.500000 | 0.333333 |
| coin | collegiate | 2 | 0.693147 | 0.250000 | 0.500000 | 0.000000 |
| coin | offseason | 435 | 0.693147 | 0.250000 | 0.500000 | 0.037931 |
| coin | unknown | 0 | — | — | — | — |
| coin | international=1 | 103 | 0.693147 | 0.250000 | 0.500000 | 0.024272 |
| coin | international=0 | 2515 | 0.693147 | 0.250000 | 0.500000 | 0.057853 |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| team_elo | all | 2618 | 0.643432 | 0.225839 | 0.630443 | 0.030124 |
| team_elo | vct | 415 | 0.664437 | 0.235728 | 0.612048 | 0.059909 |
| team_elo | vcl | 1351 | 0.649305 | 0.227962 | 0.633605 | 0.044519 |
| team_elo | gc | 409 | 0.596811 | 0.206447 | 0.658924 | 0.073475 |
| team_elo | t3 | 6 | 0.292563 | 0.076004 | 1.000000 | 0.240926 |
| team_elo | collegiate | 2 | 0.748653 | 0.277657 | 0.000000 | 0.526357 |
| team_elo | offseason | 435 | 0.653339 | 0.229875 | 0.609195 | 0.047433 |
| team_elo | unknown | 0 | — | — | — | — |
| team_elo | international=1 | 103 | 0.639781 | 0.225951 | 0.631068 | 0.069954 |
| team_elo | international=0 | 2515 | 0.643581 | 0.225835 | 0.630417 | 0.030105 |

team_elo − coin (paired log loss):

| Section | Rows | team_elo log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 2618 | 0.643432 | 0.693147 | -0.049716 | [-0.063008, -0.036807] | yes |
| vct | 415 | 0.664437 | 0.693147 | -0.028710 | [-0.062897, 0.006215] | no |
| vcl | 1351 | 0.649305 | 0.693147 | -0.043842 | [-0.061912, -0.025614] | yes |
| gc | 409 | 0.596811 | 0.693147 | -0.096336 | [-0.129011, -0.061504] | yes |
| t3 | 6 | 0.292563 | 0.693147 | -0.400584 | [-0.535592, -0.240596] | yes |
| collegiate | 2 | 0.748653 | 0.693147 | 0.055505 | [0.003500, 0.107511] | yes |
| offseason | 435 | 0.653339 | 0.693147 | -0.039808 | [-0.072346, -0.004089] | yes |
| international=1 | 103 | 0.639781 | 0.693147 | -0.053366 | [-0.121532, 0.013749] | no |
| international=0 | 2515 | 0.643581 | 0.693147 | -0.049566 | [-0.063305, -0.035982] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko | all | 2618 | 0.616378 | 0.214350 | 0.661956 | 0.035082 |
| player_round_glicko | vct | 415 | 0.638544 | 0.224649 | 0.632530 | 0.045849 |
| player_round_glicko | vcl | 1351 | 0.621685 | 0.215927 | 0.662102 | 0.042438 |
| player_round_glicko | gc | 409 | 0.546728 | 0.186208 | 0.731051 | 0.085784 |
| player_round_glicko | t3 | 6 | 0.576088 | 0.206130 | 0.666667 | 0.368691 |
| player_round_glicko | collegiate | 2 | 0.577301 | 0.192460 | 1.000000 | 0.438182 |
| player_round_glicko | offseason | 435 | 0.644973 | 0.226302 | 0.622989 | 0.025406 |
| player_round_glicko | unknown | 0 | — | — | — | — |
| player_round_glicko | international=1 | 103 | 0.646011 | 0.226998 | 0.645631 | 0.073640 |
| player_round_glicko | international=0 | 2515 | 0.615165 | 0.213832 | 0.662624 | 0.035525 |

player_round_glicko − coin (paired log loss):

| Section | Rows | player_round_glicko log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 2618 | 0.616378 | 0.693147 | -0.076769 | [-0.091836, -0.061270] | yes |
| vct | 415 | 0.638544 | 0.693147 | -0.054603 | [-0.086060, -0.022740] | yes |
| vcl | 1351 | 0.621685 | 0.693147 | -0.071463 | [-0.093963, -0.048800] | yes |
| gc | 409 | 0.546728 | 0.693147 | -0.146419 | [-0.183424, -0.107609] | yes |
| t3 | 6 | 0.576088 | 0.693147 | -0.117059 | [-0.505263, 0.308892] | no |
| collegiate | 2 | 0.577301 | 0.693147 | -0.115847 | [-0.153906, -0.077787] | yes |
| offseason | 435 | 0.644973 | 0.693147 | -0.048174 | [-0.082811, -0.012639] | yes |
| international=1 | 103 | 0.646011 | 0.693147 | -0.047137 | [-0.114527, 0.016619] | no |
| international=0 | 2515 | 0.615165 | 0.693147 | -0.077983 | [-0.092803, -0.062200] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko_rookie_tier_revert_perf_rating | all | 2618 | 0.600934 | 0.207916 | 0.675516 | 0.029770 |
| player_round_glicko_rookie_tier_revert_perf_rating | vct | 415 | 0.639544 | 0.225387 | 0.640964 | 0.051740 |
| player_round_glicko_rookie_tier_revert_perf_rating | vcl | 1351 | 0.609327 | 0.210802 | 0.666543 | 0.043267 |
| player_round_glicko_rookie_tier_revert_perf_rating | gc | 409 | 0.529198 | 0.178620 | 0.748166 | 0.041066 |
| player_round_glicko_rookie_tier_revert_perf_rating | t3 | 6 | 0.429573 | 0.146128 | 0.666667 | 0.205227 |
| player_round_glicko_rookie_tier_revert_perf_rating | collegiate | 2 | 0.553011 | 0.182585 | 0.500000 | 0.417972 |
| player_round_glicko_rookie_tier_revert_perf_rating | offseason | 435 | 0.608067 | 0.210797 | 0.668966 | 0.043917 |
| player_round_glicko_rookie_tier_revert_perf_rating | unknown | 0 | — | — | — | — |
| player_round_glicko_rookie_tier_revert_perf_rating | international=1 | 103 | 0.630172 | 0.220543 | 0.640777 | 0.071229 |
| player_round_glicko_rookie_tier_revert_perf_rating | international=0 | 2515 | 0.599737 | 0.207399 | 0.676938 | 0.031182 |

player_round_glicko_rookie_tier_revert_perf_rating − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie_tier_revert_perf_rating log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 2618 | 0.600934 | 0.693147 | -0.092213 | [-0.108596, -0.075774] | yes |
| vct | 415 | 0.639544 | 0.693147 | -0.053603 | [-0.083715, -0.022652] | yes |
| vcl | 1351 | 0.609327 | 0.693147 | -0.083820 | [-0.107254, -0.059714] | yes |
| gc | 409 | 0.529198 | 0.693147 | -0.163949 | [-0.203837, -0.122172] | yes |
| t3 | 6 | 0.429573 | 0.693147 | -0.263574 | [-0.537499, 0.017051] | no |
| collegiate | 2 | 0.553011 | 0.693147 | -0.140137 | [-0.293896, 0.013623] | no |
| offseason | 435 | 0.608067 | 0.693147 | -0.085081 | [-0.124732, -0.044442] | yes |
| international=1 | 103 | 0.630172 | 0.693147 | -0.062975 | [-0.120409, -0.007758] | yes |
| international=0 | 2515 | 0.599737 | 0.693147 | -0.093410 | [-0.109525, -0.075717] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko_rookie_tier_revert_perf_kda | all | 2618 | 0.600674 | 0.207849 | 0.671887 | 0.019180 |
| player_round_glicko_rookie_tier_revert_perf_kda | vct | 415 | 0.639810 | 0.225332 | 0.638554 | 0.051419 |
| player_round_glicko_rookie_tier_revert_perf_kda | vcl | 1351 | 0.608286 | 0.210428 | 0.663953 | 0.037441 |
| player_round_glicko_rookie_tier_revert_perf_kda | gc | 409 | 0.529607 | 0.178854 | 0.753056 | 0.056573 |
| player_round_glicko_rookie_tier_revert_perf_kda | t3 | 6 | 0.457426 | 0.157930 | 0.666667 | 0.121959 |
| player_round_glicko_rookie_tier_revert_perf_kda | collegiate | 2 | 0.561488 | 0.186567 | 0.500000 | 0.422938 |
| player_round_glicko_rookie_tier_revert_perf_kda | offseason | 435 | 0.608673 | 0.211208 | 0.652874 | 0.038327 |
| player_round_glicko_rookie_tier_revert_perf_kda | unknown | 0 | — | — | — | — |
| player_round_glicko_rookie_tier_revert_perf_kda | international=1 | 103 | 0.632479 | 0.221585 | 0.621359 | 0.090296 |
| player_round_glicko_rookie_tier_revert_perf_kda | international=0 | 2515 | 0.599371 | 0.207286 | 0.673956 | 0.022188 |

player_round_glicko_rookie_tier_revert_perf_kda − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie_tier_revert_perf_kda log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 2618 | 0.600674 | 0.693147 | -0.092473 | [-0.108414, -0.076329] | yes |
| vct | 415 | 0.639810 | 0.693147 | -0.053338 | [-0.083173, -0.022662] | yes |
| vcl | 1351 | 0.608286 | 0.693147 | -0.084861 | [-0.107908, -0.061071] | yes |
| gc | 409 | 0.529607 | 0.693147 | -0.163540 | [-0.202866, -0.122050] | yes |
| t3 | 6 | 0.457426 | 0.693147 | -0.235721 | [-0.517318, 0.049663] | no |
| collegiate | 2 | 0.561488 | 0.693147 | -0.131659 | [-0.284809, 0.021491] | no |
| offseason | 435 | 0.608673 | 0.693147 | -0.084474 | [-0.122656, -0.045164] | yes |
| international=1 | 103 | 0.632479 | 0.693147 | -0.060668 | [-0.116434, -0.007609] | yes |
| international=0 | 2515 | 0.599371 | 0.693147 | -0.093776 | [-0.109625, -0.076575] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| team_elo+none | all | 2618 | 0.643432 | 0.225839 | 0.630443 | 0.030124 |
| team_elo+none | vct | 415 | 0.664437 | 0.235728 | 0.612048 | 0.059909 |
| team_elo+none | vcl | 1351 | 0.649305 | 0.227962 | 0.633605 | 0.044519 |
| team_elo+none | gc | 409 | 0.596811 | 0.206447 | 0.658924 | 0.073475 |
| team_elo+none | t3 | 6 | 0.292563 | 0.076004 | 1.000000 | 0.240926 |
| team_elo+none | collegiate | 2 | 0.748653 | 0.277657 | 0.000000 | 0.526357 |
| team_elo+none | offseason | 435 | 0.653339 | 0.229875 | 0.609195 | 0.047433 |
| team_elo+none | unknown | 0 | — | — | — | — |
| team_elo+none | international=1 | 103 | 0.639781 | 0.225951 | 0.631068 | 0.069954 |
| team_elo+none | international=0 | 2515 | 0.643581 | 0.225835 | 0.630417 | 0.030105 |

team_elo+none − coin (paired log loss):

| Section | Rows | team_elo+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 2618 | 0.643432 | 0.693147 | -0.049716 | [-0.063008, -0.036807] | yes |
| vct | 415 | 0.664437 | 0.693147 | -0.028710 | [-0.062897, 0.006215] | no |
| vcl | 1351 | 0.649305 | 0.693147 | -0.043842 | [-0.061912, -0.025614] | yes |
| gc | 409 | 0.596811 | 0.693147 | -0.096336 | [-0.129011, -0.061504] | yes |
| t3 | 6 | 0.292563 | 0.693147 | -0.400584 | [-0.535592, -0.240596] | yes |
| collegiate | 2 | 0.748653 | 0.693147 | 0.055505 | [0.003500, 0.107511] | yes |
| offseason | 435 | 0.653339 | 0.693147 | -0.039808 | [-0.072346, -0.004089] | yes |
| international=1 | 103 | 0.639781 | 0.693147 | -0.053366 | [-0.121532, 0.013749] | no |
| international=0 | 2515 | 0.643581 | 0.693147 | -0.049566 | [-0.063305, -0.035982] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko+none | all | 2618 | 0.616378 | 0.214350 | 0.661956 | 0.035082 |
| player_round_glicko+none | vct | 415 | 0.638544 | 0.224649 | 0.632530 | 0.045849 |
| player_round_glicko+none | vcl | 1351 | 0.621685 | 0.215927 | 0.662102 | 0.042438 |
| player_round_glicko+none | gc | 409 | 0.546728 | 0.186208 | 0.731051 | 0.085784 |
| player_round_glicko+none | t3 | 6 | 0.576088 | 0.206130 | 0.666667 | 0.368691 |
| player_round_glicko+none | collegiate | 2 | 0.577301 | 0.192460 | 1.000000 | 0.438182 |
| player_round_glicko+none | offseason | 435 | 0.644973 | 0.226302 | 0.622989 | 0.025406 |
| player_round_glicko+none | unknown | 0 | — | — | — | — |
| player_round_glicko+none | international=1 | 103 | 0.646011 | 0.226998 | 0.645631 | 0.073640 |
| player_round_glicko+none | international=0 | 2515 | 0.615165 | 0.213832 | 0.662624 | 0.035525 |

player_round_glicko+none − coin (paired log loss):

| Section | Rows | player_round_glicko+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 2618 | 0.616378 | 0.693147 | -0.076769 | [-0.091836, -0.061270] | yes |
| vct | 415 | 0.638544 | 0.693147 | -0.054603 | [-0.086060, -0.022740] | yes |
| vcl | 1351 | 0.621685 | 0.693147 | -0.071463 | [-0.093963, -0.048800] | yes |
| gc | 409 | 0.546728 | 0.693147 | -0.146419 | [-0.183424, -0.107609] | yes |
| t3 | 6 | 0.576088 | 0.693147 | -0.117059 | [-0.505263, 0.308892] | no |
| collegiate | 2 | 0.577301 | 0.693147 | -0.115847 | [-0.153906, -0.077787] | yes |
| offseason | 435 | 0.644973 | 0.693147 | -0.048174 | [-0.082811, -0.012639] | yes |
| international=1 | 103 | 0.646011 | 0.693147 | -0.047137 | [-0.114527, 0.016619] | no |
| international=0 | 2515 | 0.615165 | 0.693147 | -0.077983 | [-0.092803, -0.062200] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko_rookie_tier_revert_perf_rating+none | all | 2618 | 0.600934 | 0.207916 | 0.675516 | 0.029770 |
| player_round_glicko_rookie_tier_revert_perf_rating+none | vct | 415 | 0.639544 | 0.225387 | 0.640964 | 0.051740 |
| player_round_glicko_rookie_tier_revert_perf_rating+none | vcl | 1351 | 0.609327 | 0.210802 | 0.666543 | 0.043267 |
| player_round_glicko_rookie_tier_revert_perf_rating+none | gc | 409 | 0.529198 | 0.178620 | 0.748166 | 0.041066 |
| player_round_glicko_rookie_tier_revert_perf_rating+none | t3 | 6 | 0.429573 | 0.146128 | 0.666667 | 0.205227 |
| player_round_glicko_rookie_tier_revert_perf_rating+none | collegiate | 2 | 0.553011 | 0.182585 | 0.500000 | 0.417972 |
| player_round_glicko_rookie_tier_revert_perf_rating+none | offseason | 435 | 0.608067 | 0.210797 | 0.668966 | 0.043917 |
| player_round_glicko_rookie_tier_revert_perf_rating+none | unknown | 0 | — | — | — | — |
| player_round_glicko_rookie_tier_revert_perf_rating+none | international=1 | 103 | 0.630172 | 0.220543 | 0.640777 | 0.071229 |
| player_round_glicko_rookie_tier_revert_perf_rating+none | international=0 | 2515 | 0.599737 | 0.207399 | 0.676938 | 0.031182 |

player_round_glicko_rookie_tier_revert_perf_rating+none − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie_tier_revert_perf_rating+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 2618 | 0.600934 | 0.693147 | -0.092213 | [-0.108596, -0.075774] | yes |
| vct | 415 | 0.639544 | 0.693147 | -0.053603 | [-0.083715, -0.022652] | yes |
| vcl | 1351 | 0.609327 | 0.693147 | -0.083820 | [-0.107254, -0.059714] | yes |
| gc | 409 | 0.529198 | 0.693147 | -0.163949 | [-0.203837, -0.122172] | yes |
| t3 | 6 | 0.429573 | 0.693147 | -0.263574 | [-0.537499, 0.017051] | no |
| collegiate | 2 | 0.553011 | 0.693147 | -0.140137 | [-0.293896, 0.013623] | no |
| offseason | 435 | 0.608067 | 0.693147 | -0.085081 | [-0.124732, -0.044442] | yes |
| international=1 | 103 | 0.630172 | 0.693147 | -0.062975 | [-0.120409, -0.007758] | yes |
| international=0 | 2515 | 0.599737 | 0.693147 | -0.093410 | [-0.109525, -0.075717] | yes |

| Model | Section | Rows | Log loss | Brier | Accuracy | ECE |
|---|---|---:|---:|---:|---:|---:|
| player_round_glicko_rookie_tier_revert_perf_kda+none | all | 2618 | 0.600674 | 0.207849 | 0.671887 | 0.019180 |
| player_round_glicko_rookie_tier_revert_perf_kda+none | vct | 415 | 0.639810 | 0.225332 | 0.638554 | 0.051419 |
| player_round_glicko_rookie_tier_revert_perf_kda+none | vcl | 1351 | 0.608286 | 0.210428 | 0.663953 | 0.037441 |
| player_round_glicko_rookie_tier_revert_perf_kda+none | gc | 409 | 0.529607 | 0.178854 | 0.753056 | 0.056573 |
| player_round_glicko_rookie_tier_revert_perf_kda+none | t3 | 6 | 0.457426 | 0.157930 | 0.666667 | 0.121959 |
| player_round_glicko_rookie_tier_revert_perf_kda+none | collegiate | 2 | 0.561488 | 0.186567 | 0.500000 | 0.422938 |
| player_round_glicko_rookie_tier_revert_perf_kda+none | offseason | 435 | 0.608673 | 0.211208 | 0.652874 | 0.038327 |
| player_round_glicko_rookie_tier_revert_perf_kda+none | unknown | 0 | — | — | — | — |
| player_round_glicko_rookie_tier_revert_perf_kda+none | international=1 | 103 | 0.632479 | 0.221585 | 0.621359 | 0.090296 |
| player_round_glicko_rookie_tier_revert_perf_kda+none | international=0 | 2515 | 0.599371 | 0.207286 | 0.673956 | 0.022188 |

player_round_glicko_rookie_tier_revert_perf_kda+none − coin (paired log loss):

| Section | Rows | player_round_glicko_rookie_tier_revert_perf_kda+none log loss | coin log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 2618 | 0.600674 | 0.693147 | -0.092473 | [-0.108414, -0.076329] | yes |
| vct | 415 | 0.639810 | 0.693147 | -0.053338 | [-0.083173, -0.022662] | yes |
| vcl | 1351 | 0.608286 | 0.693147 | -0.084861 | [-0.107908, -0.061071] | yes |
| gc | 409 | 0.529607 | 0.693147 | -0.163540 | [-0.202866, -0.122050] | yes |
| t3 | 6 | 0.457426 | 0.693147 | -0.235721 | [-0.517318, 0.049663] | no |
| collegiate | 2 | 0.561488 | 0.693147 | -0.131659 | [-0.284809, 0.021491] | no |
| offseason | 435 | 0.608673 | 0.693147 | -0.084474 | [-0.122656, -0.045164] | yes |
| international=1 | 103 | 0.632479 | 0.693147 | -0.060668 | [-0.116434, -0.007609] | yes |
| international=0 | 2515 | 0.599371 | 0.693147 | -0.093776 | [-0.109625, -0.076575] | yes |

player_round_glicko − team_elo (paired log loss):

| Section | Rows | player_round_glicko log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 2618 | 0.616378 | 0.643432 | -0.027053 | [-0.038642, -0.015020] | yes |

player_round_glicko_rookie_tier_revert_perf_rating − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie_tier_revert_perf_rating log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 2618 | 0.600934 | 0.643432 | -0.042497 | [-0.055944, -0.029292] | yes |

player_round_glicko_rookie_tier_revert_perf_kda − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie_tier_revert_perf_kda log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 2618 | 0.600674 | 0.643432 | -0.042758 | [-0.055876, -0.029610] | yes |

team_elo+none − team_elo (paired log loss):

| Section | Rows | team_elo+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 2618 | 0.643432 | 0.643432 | 0.000000 | [0.000000, 0.000000] | no |

player_round_glicko+none − team_elo (paired log loss):

| Section | Rows | player_round_glicko+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 2618 | 0.616378 | 0.643432 | -0.027053 | [-0.038642, -0.015020] | yes |

player_round_glicko_rookie_tier_revert_perf_rating+none − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie_tier_revert_perf_rating+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 2618 | 0.600934 | 0.643432 | -0.042497 | [-0.055944, -0.029292] | yes |

player_round_glicko_rookie_tier_revert_perf_kda+none − team_elo (paired log loss):

| Section | Rows | player_round_glicko_rookie_tier_revert_perf_kda+none log loss | team_elo log loss | Difference | 95% interval | Significant |
|---|---:|---:|---:|---:|---|---|
| all | 2618 | 0.600674 | 0.643432 | -0.042758 | [-0.055876, -0.029610] | yes |

## Stage 2 — validation vs Kalshi

### team_elo: Kalshi comparison and returns



#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 677 | 0.659884 | 0.633240 | 0.026644 [0.005070, 0.049198] | yes |
| series | vct | 278 | 0.656875 | 0.634755 | 0.022120 [-0.008080, 0.052332] | no |
| series | vcl | 340 | 0.653448 | 0.619968 | 0.033480 [-0.002273, 0.068144] | no |
| series | gc | 0 | — | — | — | — |
| series | t3 | 0 | — | — | — | — |
| series | collegiate | 0 | — | — | — | — |
| series | offseason | 59 | 0.711150 | 0.702587 | 0.008563 [-0.038647, 0.057958] | no |
| series | international=1 | 41 | 0.651212 | 0.653397 | -0.002184 [-0.046947, 0.045515] | no |
| series | international=0 | 636 | 0.660443 | 0.631941 | 0.028502 [0.005725, 0.053222] | yes |
| map | all | 1049 | 0.674219 | 0.668225 | 0.005994 [-0.016072, 0.025667] | no |
| map | vct | 461 | 0.678620 | 0.665762 | 0.012858 [-0.012004, 0.036805] | no |
| map | vcl | 490 | 0.669823 | 0.668365 | 0.001458 [-0.038888, 0.036008] | no |
| map | gc | 0 | — | — | — | — |
| map | t3 | 0 | — | — | — | — |
| map | collegiate | 0 | — | — | — | — |
| map | offseason | 98 | 0.675493 | 0.679111 | -0.003618 [-0.033834, 0.028482] | no |
| map | international=1 | 59 | 0.669039 | 0.649653 | 0.019386 [-0.020368, 0.061334] | no |
| map | international=0 | 990 | 0.674527 | 0.669332 | 0.005196 [-0.018272, 0.026420] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 473 | 473 | 0.0894 | -2.01% [-15.18%, 11.35%] | $0.55 | 0.011× | 99.52% | $9.89 | 260 (213 unfilled) | 15.98% [-1.36%, 35.27%] | $128.56 |
| series | vct | 180 | 180 | 0.0796 | -2.47% [-21.83%, 19.63%] | $17.90 | 0.358× | 72.48% | $5.29 | 107 (73 unfilled) | 15.75% [-9.72%, 43.70%] | $93.96 |
| series | vcl | 257 | 257 | 0.1004 | -3.13% [-20.74%, 15.40%] | $2.78 | 0.056× | 97.26% | $8.12 | 126 (131 unfilled) | 20.99% [-5.94%, 48.89%] | $127.28 |
| series | gc | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | t3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | collegiate | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | offseason | 36 | 36 | 0.0591 | 8.33% [-29.51%, 48.08%] | $43.23 | 0.865× | 59.45% | $7.21 | 27 (9 unfilled) | -6.59% [-46.54%, 37.00%] | $37.07 |
| series | international=1 | 32 | 32 | 0.0514 | 5.76% [-27.15%, 40.29%] | $45.99 | 0.920× | 41.06% | $6.36 | 31 (1 unfilled) | 4.29% [-31.31%, 39.31%] | $44.04 |
| series | international=0 | 441 | 441 | 0.0921 | -2.57% [-15.72%, 11.09%] | $0.62 | 0.012× | 99.31% | $7.62 | 229 (212 unfilled) | 17.55% [-1.89%, 37.48%] | $152.11 |
| map | all | 698 | 372 | 0.0762 | 12.02% [-4.33%, 32.11%] | $480.61 | 9.612× | 80.53% | $143.37 | 108 (590 unfilled) | 52.76% [3.09%, 115.44%] | $203.47 |
| map | vct | 286 | 151 | 0.0699 | 3.93% [-12.79%, 27.90%] | $62.89 | 1.258× | 50.73% | $7.89 | 42 (244 unfilled) | 70.04% [-9.28%, 197.74%] | $93.56 |
| map | vcl | 350 | 190 | 0.0874 | 19.95% [-7.26%, 52.36%] | $366.07 | 7.321× | 72.37% | $80.85 | 57 (293 unfilled) | 48.44% [-12.85%, 131.95%] | $117.23 |
| map | gc | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | t3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | collegiate | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | offseason | 62 | 31 | 0.0420 | 4.29% [-20.29%, 28.35%] | $43.32 | 0.866× | 27.84% | $3.31 | 9 (53 unfilled) | -0.67% [-57.18%, 35.88%] | $47.13 |
| map | international=1 | 42 | 23 | 0.0572 | -9.87% [-32.61%, 11.40%] | $38.60 | 0.772× | 30.42% | $2.84 | 11 (31 unfilled) | 19.70% [-26.58%, 56.05%] | $52.92 |
| map | international=0 | 656 | 349 | 0.0775 | 13.41% [-3.61%, 34.83%] | $622.19 | 12.444× | 74.78% | $143.30 | 97 (559 unfilled) | 56.48% [-0.76%, 129.18%] | $198.48 |
| series+map | all | 1171 | 544 | 0.0815 | 6.33% [-5.87%, 19.78%] | $48.89 | 0.978× | 97.29% | $123.59 | 368 (803 unfilled) | 26.77% [7.20%, 49.68%] | $202.77 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-09-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 240 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-01 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 21 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | map | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-03 | series | 72 | 1.000000 | 0.000000 | unfitted |
| 2026-03 | map | 48 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | series | 136 | 1.042825 | 0.215516 | fitted |
| 2026-04 | map | 104 | 1.439410 | 0.208235 | fitted |
| 2026-05 | series | 357 | 0.942242 | 0.232480 | fitted |
| 2026-05 | map | 456 | 0.879130 | 0.568385 | fitted |
| 2026-06 | series | 556 | 0.860932 | 0.124059 | fitted |
| 2026-06 | map | 833 | 0.763049 | 0.405197 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 541 | 0.634508 | 0.634347 | 0.000161 [-0.005143, 0.005135] | no |
| series | vct | 201 | 0.643137 | 0.644147 | -0.001010 [-0.009242, 0.007156] | no |
| series | vcl | 291 | 0.622082 | 0.621829 | 0.000253 [-0.007141, 0.007684] | no |
| series | gc | 0 | — | — | — | — |
| series | t3 | 0 | — | — | — | — |
| series | collegiate | 0 | — | — | — | — |
| series | offseason | 49 | 0.672904 | 0.668490 | 0.004414 [-0.008452, 0.016494] | no |
| series | international=1 | 24 | 0.680037 | 0.682705 | -0.002669 [-0.027187, 0.017497] | no |
| series | international=0 | 517 | 0.632394 | 0.632102 | 0.000292 [-0.005051, 0.005662] | no |
| map | all | 945 | 0.684435 | 0.673192 | 0.011243 [0.002676, 0.019848] | yes |
| map | vct | 392 | 0.675770 | 0.667249 | 0.008520 [-0.004749, 0.022586] | no |
| map | vcl | 456 | 0.693354 | 0.676303 | 0.017051 [0.003772, 0.030048] | yes |
| map | gc | 0 | — | — | — | — |
| map | t3 | 0 | — | — | — | — |
| map | collegiate | 0 | — | — | — | — |
| map | offseason | 97 | 0.677523 | 0.682581 | -0.005057 [-0.019598, 0.009568] | no |
| map | international=1 | 50 | 0.658711 | 0.651359 | 0.007353 [-0.007823, 0.021042] | no |
| map | international=0 | 895 | 0.685872 | 0.674412 | 0.011460 [0.001858, 0.020438] | yes |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 82 | 82 | 0.0152 | -5.01% [-38.32%, 28.44%] | $35.62 | 0.712× | 43.57% | $5.46 | 49 (33 unfilled) | 16.91% [-25.46%, 65.25%] | $57.12 |
| series | vct | 28 | 28 | 0.0196 | 14.92% [-47.96%, 87.75%] | $45.59 | 0.912× | 34.31% | $4.96 | 18 (10 unfilled) | 63.04% [-26.71%, 163.05%] | $62.32 |
| series | vcl | 50 | 50 | 0.0135 | -8.62% [-45.61%, 31.17%] | $40.94 | 0.819× | 19.74% | $4.61 | 27 (23 unfilled) | 3.28% [-40.89%, 50.22%] | $47.76 |
| series | gc | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | t3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | collegiate | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | offseason | 4 | 4 | 0.0065 | -100.00% [-100.00%, -100.00%] | $47.79 | 0.956× | 4.42% | $1.19 | 4 (0 unfilled) | -100.00% [-100.00%, -100.00%] | $47.79 |
| series | international=1 | 5 | 5 | 0.0076 | 128.58% [-40.93%, 298.09%] | $54.96 | 1.099× | 1.20% | $0.70 | 5 (0 unfilled) | 128.58% [-40.93%, 298.09%] | $54.96 |
| series | international=0 | 77 | 77 | 0.0157 | -13.74% [-45.15%, 22.22%] | $32.39 | 0.648× | 44.19% | $5.46 | 44 (33 unfilled) | 4.13% [-38.95%, 48.31%] | $51.92 |
| map | all | 435 | 244 | 0.0302 | -8.06% [-17.18%, 1.76%] | $7.27 | 0.145× | 88.32% | $5.68 | 69 (366 unfilled) | -5.79% [-25.63%, 15.35%] | $38.70 |
| map | vct | 184 | 100 | 0.0327 | -5.21% [-18.93%, 9.43%] | $28.54 | 0.571× | 50.48% | $5.13 | 30 (154 unfilled) | 1.27% [-36.69%, 39.63%] | $52.39 |
| map | vcl | 222 | 129 | 0.0296 | -11.48% [-23.80%, 1.98%] | $13.80 | 0.276× | 75.99% | $5.19 | 36 (186 unfilled) | -8.56% [-34.11%, 13.90%] | $40.07 |
| map | gc | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | t3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | collegiate | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | offseason | 29 | 15 | 0.0195 | 0.15% [-31.48%, 32.90%] | $48.32 | 0.966× | 9.94% | $2.85 | 3 (26 unfilled) | -42.95% [-100.00%, -14.15%] | $46.34 |
| map | international=1 | 16 | 10 | 0.0119 | -21.91% [-67.31%, 29.28%] | $46.48 | 0.930× | 7.05% | $2.46 | 4 (12 unfilled) | -59.26% [-100.00%, 64.55%] | $48.87 |
| map | international=0 | 419 | 234 | 0.0309 | -7.52% [-16.46%, 2.12%] | $7.90 | 0.158× | 87.34% | $5.68 | 65 (354 unfilled) | -2.49% [-23.23%, 18.34%] | $39.58 |
| series+map | all | 517 | 268 | 0.0278 | -7.57% [-18.34%, 3.94%] | $5.97 | 0.119× | 90.40% | $5.67 | 118 (399 unfilled) | 3.72% [-17.74%, 27.80%] | $39.19 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-02 | 48 | 0.701058 | — | 0.690786 | -19.10% (25), $33.55 | — | 9 (16 unfilled) | -1.84% [-100.00%, 65.78%] | $45.89 | — | — | — |
| map | 2026-03 | 56 | 0.637862 | — | 0.565065 | -31.56% (35), $21.54 | — | 10 (25 unfilled) | -27.24% [-81.79%, 41.92%] | $37.51 | — | — | — |
| map | 2026-04 | 352 | 0.660671 | 0.707440 | 0.690793 | 49.03% (241), $6279.98 | -9.38% (188), $17.46 | 29 (212 unfilled) | 183.25% [4.69%, 428.45%] | $242.59 | 33 (155 unfilled) | -12.13% [-31.69%, 6.10%] | $41.36 |
| map | 2026-05 | 377 | 0.704442 | 0.690344 | 0.687018 | -1.28% (249), $26.14 | -0.66% (155), $42.94 | 36 (213 unfilled) | 10.12% [-22.78%, 41.28%] | $54.33 | 25 (130 unfilled) | 11.32% [-34.86%, 53.52%] | $53.62 |
| map | 2026-06 | 216 | 0.647007 | 0.636631 | 0.620377 | -10.26% (148), $16.82 | -17.81% (92), $25.67 | 24 (124 unfilled) | 12.50% [-21.08%, 41.11%] | $46.58 | 11 (81 unfilled) | -26.18% [-100.00%, 29.50%] | $44.04 |
| series | 2026-01 | 21 | 0.684822 | — | 0.661069 | 4.92% (16), $45.78 | — | 9 (7 unfilled) | -25.46% [-81.66%, 48.91%] | $36.49 | — | — | — |
| series | 2026-02 | 51 | 0.659130 | — | 0.694525 | 25.18% (34), $95.24 | — | 22 (12 unfilled) | 49.18% [-13.77%, 132.77%] | $129.91 | — | — | — |
| series | 2026-03 | 64 | 0.662527 | — | 0.565917 | -31.86% (49), $10.02 | — | 37 (12 unfilled) | -19.68% [-50.47%, 13.73%] | $18.83 | — | — | — |
| series | 2026-04 | 221 | 0.645922 | 0.624471 | 0.627690 | 3.92% (146), $67.65 | 5.82% (25), $48.53 | 59 (87 unfilled) | 58.07% [8.98%, 114.67%] | $210.98 | 16 (9 unfilled) | 27.95% [-31.97%, 85.50%] | $58.32 |
| series | 2026-05 | 199 | 0.690980 | 0.663840 | 0.663719 | 0.07% (133), $9.78 | -33.91% (33), $36.72 | 83 (50 unfilled) | -1.88% [-27.64%, 26.71%] | $36.33 | 22 (11 unfilled) | -11.15% [-73.62%, 72.74%] | $50.32 |
| series | 2026-06 | 121 | 0.628835 | 0.604598 | 0.598199 | -9.59% (95), $9.03 | 23.37% (24), $50.00 | 50 (45 unfilled) | 14.89% [-15.83%, 48.34%] | $44.61 | 11 (13 unfilled) | 56.86% [-46.08%, 168.60%] | $48.32 |

### player_round_glicko: Kalshi comparison and returns



#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 677 | 0.631896 | 0.633240 | -0.001344 [-0.023684, 0.021712] | no |
| series | vct | 278 | 0.629718 | 0.634755 | -0.005037 [-0.035239, 0.023644] | no |
| series | vcl | 340 | 0.622985 | 0.619968 | 0.003017 [-0.034835, 0.040819] | no |
| series | gc | 0 | — | — | — | — |
| series | t3 | 0 | — | — | — | — |
| series | collegiate | 0 | — | — | — | — |
| series | offseason | 59 | 0.693516 | 0.702587 | -0.009071 [-0.070439, 0.050068] | no |
| series | international=1 | 41 | 0.622775 | 0.653397 | -0.030622 [-0.076037, 0.019882] | no |
| series | international=0 | 636 | 0.632485 | 0.631941 | 0.000544 [-0.024166, 0.024627] | no |
| map | all | 1049 | 0.661370 | 0.668225 | -0.006855 [-0.028831, 0.011834] | no |
| map | vct | 461 | 0.658507 | 0.665762 | -0.007255 [-0.027207, 0.011052] | no |
| map | vcl | 490 | 0.658544 | 0.668365 | -0.009820 [-0.052216, 0.025600] | no |
| map | gc | 0 | — | — | — | — |
| map | t3 | 0 | — | — | — | — |
| map | collegiate | 0 | — | — | — | — |
| map | offseason | 98 | 0.688964 | 0.679111 | 0.009853 [-0.018553, 0.038849] | no |
| map | international=1 | 59 | 0.666817 | 0.649653 | 0.017165 [-0.014406, 0.053245] | no |
| map | international=0 | 990 | 0.661045 | 0.669332 | -0.008286 [-0.030282, 0.011757] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 501 | 501 | 0.0922 | 8.45% [-4.14%, 20.32%] | $220.43 | 4.409× | 82.96% | $55.92 | 290 (211 unfilled) | 19.26% [3.85%, 35.68%] | $655.33 |
| series | vct | 196 | 196 | 0.0781 | 8.21% [-10.88%, 29.43%] | $56.76 | 1.135× | 67.37% | $7.96 | 122 (74 unfilled) | 24.93% [-1.16%, 50.89%] | $237.04 |
| series | vcl | 263 | 263 | 0.1059 | 10.40% [-6.17%, 28.87%] | $139.98 | 2.800× | 62.91% | $29.19 | 135 (128 unfilled) | 20.58% [-4.27%, 47.85%] | $147.27 |
| series | gc | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | t3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | collegiate | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | offseason | 42 | 42 | 0.0725 | -2.68% [-40.11%, 35.04%] | $72.88 | 1.458× | 50.25% | $10.15 | 33 (9 unfilled) | -7.08% [-46.30%, 35.97%] | $51.73 |
| series | international=1 | 28 | 28 | 0.0506 | 30.78% [-14.12%, 74.42%] | $78.74 | 1.575× | 18.17% | $6.27 | 28 (0 unfilled) | 30.78% [-14.12%, 74.42%] | $79.77 |
| series | international=0 | 473 | 473 | 0.0947 | 7.13% [-5.57%, 20.78%] | $140.25 | 2.805× | 82.96% | $44.65 | 262 (211 unfilled) | 18.03% [0.77%, 36.43%] | $392.46 |
| map | all | 647 | 346 | 0.0735 | 18.30% [1.51%, 38.72%] | $4234.75 | 84.695× | 31.14% | $245.53 | 95 (552 unfilled) | 58.09% [-2.02%, 127.43%] | $240.23 |
| map | vct | 273 | 143 | 0.0567 | 10.98% [-6.46%, 33.54%] | $175.34 | 3.507× | 35.24% | $16.59 | 48 (225 unfilled) | 68.04% [-0.24%, 188.15%] | $122.55 |
| map | vcl | 324 | 179 | 0.0917 | 27.18% [-2.22%, 65.83%] | $1495.03 | 29.901× | 49.34% | $221.23 | 42 (282 unfilled) | 43.57% [-40.39%, 161.86%] | $118.48 |
| map | gc | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | t3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | collegiate | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | offseason | 50 | 24 | 0.0469 | 0.49% [-26.79%, 30.69%] | $52.19 | 1.044× | 21.58% | $3.83 | 5 (45 unfilled) | 85.42% [23.05%, 209.00%] | $56.76 |
| map | international=1 | 35 | 19 | 0.0478 | -20.19% [-46.33%, 6.10%] | $33.51 | 0.670× | 35.86% | $4.79 | 14 (21 unfilled) | -3.63% [-41.12%, 35.47%] | $49.18 |
| map | international=0 | 612 | 327 | 0.0749 | 20.49% [2.22%, 41.17%] | $5088.26 | 101.765× | 26.74% | $245.53 | 81 (531 unfilled) | 68.66% [2.57%, 162.06%] | $243.09 |
| series+map | all | 1148 | 532 | 0.0817 | 13.99% [1.86%, 27.64%] | $4152.97 | 83.059× | 45.69% | $247.91 | 385 (763 unfilled) | 28.85% [9.06%, 52.15%] | $378.90 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-09-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 240 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-01 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 21 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | map | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-03 | series | 72 | 1.000000 | 0.000000 | unfitted |
| 2026-03 | map | 48 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | series | 136 | 1.268851 | 0.758810 | fitted |
| 2026-04 | map | 104 | 1.441942 | 0.315911 | fitted |
| 2026-05 | series | 357 | 1.050991 | 0.617096 | fitted |
| 2026-05 | map | 456 | 1.061734 | 0.860054 | fitted |
| 2026-06 | series | 556 | 0.985933 | 0.545120 | fitted |
| 2026-06 | map | 833 | 0.928229 | 0.717006 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 541 | 0.626760 | 0.634347 | -0.007587 [-0.024047, 0.008406] | no |
| series | vct | 201 | 0.640311 | 0.644147 | -0.003836 [-0.026236, 0.019731] | no |
| series | vcl | 291 | 0.607219 | 0.621829 | -0.014609 [-0.038829, 0.011600] | no |
| series | gc | 0 | — | — | — | — |
| series | t3 | 0 | — | — | — | — |
| series | collegiate | 0 | — | — | — | — |
| series | offseason | 49 | 0.687222 | 0.668490 | 0.018732 [-0.016580, 0.052524] | no |
| series | international=1 | 24 | 0.664309 | 0.682705 | -0.018396 [-0.056673, 0.023117] | no |
| series | international=0 | 517 | 0.625017 | 0.632102 | -0.007085 [-0.023322, 0.009467] | no |
| map | all | 945 | 0.679807 | 0.673192 | 0.006616 [-0.002325, 0.016233] | no |
| map | vct | 392 | 0.667363 | 0.667249 | 0.000114 [-0.012507, 0.012026] | no |
| map | vcl | 456 | 0.688112 | 0.676303 | 0.011809 [-0.002897, 0.026976] | no |
| map | gc | 0 | — | — | — | — |
| map | t3 | 0 | — | — | — | — |
| map | collegiate | 0 | — | — | — | — |
| map | offseason | 97 | 0.691057 | 0.682581 | 0.008477 [-0.017985, 0.035315] | no |
| map | international=1 | 50 | 0.664037 | 0.651359 | 0.012679 [-0.011599, 0.037675] | no |
| map | international=0 | 895 | 0.680689 | 0.674412 | 0.006277 [-0.003449, 0.015828] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 312 | 312 | 0.0552 | 13.36% [-1.27%, 28.44%] | $357.15 | 7.143× | 54.88% | $54.32 | 164 (148 unfilled) | 17.40% [-3.33%, 38.59%] | $157.92 |
| series | vct | 115 | 115 | 0.0490 | 7.22% [-15.10%, 34.22%] | $47.98 | 0.960× | 44.56% | $6.46 | 65 (50 unfilled) | 24.78% [-5.86%, 58.78%] | $120.67 |
| series | vcl | 176 | 176 | 0.0608 | 20.30% [0.74%, 41.46%] | $402.85 | 8.057× | 39.77% | $50.83 | 84 (92 unfilled) | 22.66% [-6.64%, 53.09%] | $95.11 |
| series | gc | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | t3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | collegiate | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | offseason | 21 | 21 | 0.0427 | -11.24% [-60.66%, 43.01%] | $42.78 | 0.856× | 29.96% | $4.67 | 15 (6 unfilled) | -43.92% [-86.70%, 8.31%] | $34.72 |
| series | international=1 | 12 | 12 | 0.0306 | 38.18% [-40.27%, 122.51%] | $57.08 | 1.142× | 10.90% | $4.92 | 12 (0 unfilled) | 38.18% [-40.27%, 122.51%] | $57.08 |
| series | international=0 | 300 | 300 | 0.0562 | 12.36% [-2.43%, 29.05%] | $312.63 | 6.253× | 55.48% | $54.32 | 152 (148 unfilled) | 15.75% [-3.98%, 37.22%] | $136.04 |
| map | all | 493 | 262 | 0.0402 | -3.73% [-12.52%, 5.23%] | $29.53 | 0.591× | 67.03% | $8.01 | 72 (421 unfilled) | 4.42% [-15.57%, 27.34%] | $47.42 |
| map | vct | 199 | 103 | 0.0343 | -1.21% [-13.95%, 12.16%] | $43.08 | 0.862× | 37.46% | $5.47 | 34 (165 unfilled) | 26.55% [-4.48%, 59.92%] | $61.50 |
| map | vcl | 253 | 139 | 0.0447 | -6.16% [-18.52%, 6.13%] | $30.96 | 0.619× | 58.28% | $6.73 | 34 (219 unfilled) | -21.90% [-48.30%, 6.15%] | $36.17 |
| map | gc | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | t3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | collegiate | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | offseason | 41 | 20 | 0.0412 | -0.95% [-32.70%, 27.97%] | $52.85 | 1.057× | 13.08% | $4.05 | 4 (37 unfilled) | 40.32% [13.38%, 92.31%] | $53.26 |
| map | international=1 | 28 | 13 | 0.0311 | -17.31% [-48.85%, 12.57%] | $37.48 | 0.750× | 25.04% | $2.29 | 10 (18 unfilled) | 2.53% [-38.68%, 45.73%] | $48.75 |
| map | international=0 | 465 | 249 | 0.0408 | -2.91% [-12.22%, 5.95%] | $39.57 | 0.791× | 55.90% | $8.01 | 62 (403 unfilled) | 4.72% [-19.91%, 31.38%] | $48.75 |
| series+map | all | 805 | 365 | 0.0460 | 2.91% [-7.32%, 12.41%] | $100.49 | 2.010× | 62.98% | $18.38 | 236 (569 unfilled) | 13.45% [-2.55%, 29.35%] | $106.41 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-02 | 48 | 0.700298 | — | 0.690786 | -0.33% (33), $49.91 | — | 9 (24 unfilled) | -1.52% [-100.00%, 53.63%] | $50.52 | — | — | — |
| map | 2026-03 | 56 | 0.602878 | — | 0.565065 | -8.66% (30), $42.68 | — | 10 (20 unfilled) | -14.58% [-73.52%, 41.60%] | $53.58 | — | — | — |
| map | 2026-04 | 352 | 0.639411 | 0.693277 | 0.690793 | 56.02% (240), $5454.71 | -4.42% (182), $47.77 | 25 (215 unfilled) | 200.11% [4.36%, 454.64%] | $230.50 | 25 (157 unfilled) | -5.33% [-28.60%, 16.00%] | $50.18 |
| map | 2026-05 | 377 | 0.688223 | 0.687082 | 0.687018 | 4.32% (205), $67.35 | 4.78% (186), $69.26 | 28 (177 unfilled) | 41.04% [-4.44%, 87.63%] | $66.47 | 26 (160 unfilled) | 29.05% [-16.98%, 72.34%] | $58.55 |
| map | 2026-06 | 216 | 0.656799 | 0.645160 | 0.620377 | -15.93% (139), $20.34 | -15.38% (125), $22.25 | 23 (116 unfilled) | -22.14% [-56.38%, 13.75%] | $37.76 | 21 (104 unfilled) | -14.73% [-49.02%, 22.33%] | $40.54 |
| series | 2026-01 | 21 | 0.631734 | — | 0.661069 | 4.35% (17), $55.03 | — | 9 (8 unfilled) | -20.27% [-77.53%, 40.89%] | $46.20 | — | — | — |
| series | 2026-02 | 51 | 0.651868 | — | 0.694525 | 26.91% (42), $104.54 | — | 31 (11 unfilled) | 38.73% [-14.29%, 103.12%] | $107.87 | — | — | — |
| series | 2026-03 | 64 | 0.594068 | — | 0.565917 | 3.56% (49), $43.82 | — | 39 (10 unfilled) | 16.22% [-14.34%, 47.26%] | $66.69 | — | — | — |
| series | 2026-04 | 221 | 0.618228 | 0.614779 | 0.627690 | 11.25% (167), $87.77 | 16.57% (146), $290.96 | 73 (94 unfilled) | 49.13% [10.11%, 91.86%] | $249.05 | 64 (82 unfilled) | 36.60% [4.58%, 71.15%] | $158.46 |
| series | 2026-05 | 199 | 0.666706 | 0.658801 | 0.663719 | 4.82% (137), $49.50 | 8.94% (99), $52.08 | 90 (47 unfilled) | -7.69% [-32.21%, 20.06%] | $28.84 | 65 (34 unfilled) | -7.75% [-37.08%, 26.09%] | $32.43 |
| series | 2026-06 | 121 | 0.611232 | 0.595946 | 0.598199 | 3.52% (89), $61.27 | 12.93% (67), $58.06 | 48 (41 unfilled) | 21.61% [-10.19%, 56.31%] | $114.15 | 35 (32 unfilled) | 29.10% [-10.55%, 72.15%] | $66.84 |

### player_round_glicko_rookie_tier_revert_perf_rating: Kalshi comparison and returns



#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 677 | 0.622581 | 0.633240 | -0.010659 [-0.034278, 0.014381] | no |
| series | vct | 278 | 0.617874 | 0.634755 | -0.016881 [-0.048694, 0.011911] | no |
| series | vcl | 340 | 0.615723 | 0.619968 | -0.004245 [-0.045096, 0.037620] | no |
| series | gc | 0 | — | — | — | — |
| series | t3 | 0 | — | — | — | — |
| series | collegiate | 0 | — | — | — | — |
| series | offseason | 59 | 0.684286 | 0.702587 | -0.018301 [-0.077101, 0.036317] | no |
| series | international=1 | 41 | 0.614481 | 0.653397 | -0.038915 [-0.082381, 0.001995] | no |
| series | international=0 | 636 | 0.623104 | 0.631941 | -0.008837 [-0.035171, 0.016837] | no |
| map | all | 1049 | 0.656792 | 0.668225 | -0.011432 [-0.033746, 0.006996] | no |
| map | vct | 461 | 0.655037 | 0.665762 | -0.010725 [-0.030935, 0.006607] | no |
| map | vcl | 490 | 0.651838 | 0.668365 | -0.016527 [-0.059658, 0.019158] | no |
| map | gc | 0 | — | — | — | — |
| map | t3 | 0 | — | — | — | — |
| map | collegiate | 0 | — | — | — | — |
| map | offseason | 98 | 0.689821 | 0.679111 | 0.010710 [-0.025196, 0.044230] | no |
| map | international=1 | 59 | 0.658482 | 0.649653 | 0.008830 [-0.016035, 0.032809] | no |
| map | international=0 | 990 | 0.656692 | 0.669332 | -0.012640 [-0.034651, 0.007371] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 500 | 500 | 0.0945 | 13.05% [0.08%, 26.07%] | $1247.73 | 24.955× | 71.91% | $246.88 | 288 (212 unfilled) | 19.94% [3.75%, 37.52%] | $698.18 |
| series | vct | 194 | 194 | 0.0764 | 10.83% [-8.16%, 31.31%] | $115.51 | 2.310× | 70.62% | $9.20 | 119 (75 unfilled) | 21.40% [-4.89%, 48.02%] | $243.66 |
| series | vcl | 266 | 266 | 0.1103 | 14.50% [-2.23%, 32.45%] | $602.10 | 12.042× | 53.36% | $101.11 | 137 (129 unfilled) | 22.74% [-1.49%, 50.19%] | $182.79 |
| series | gc | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | t3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | collegiate | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | offseason | 40 | 40 | 0.0769 | 14.10% [-25.65%, 56.39%] | $76.51 | 1.530× | 47.88% | $9.30 | 32 (8 unfilled) | 2.62% [-41.95%, 47.74%] | $53.21 |
| series | international=1 | 27 | 27 | 0.0407 | 26.51% [-21.47%, 76.49%] | $87.55 | 1.751× | 16.14% | $6.97 | 26 (1 unfilled) | 25.55% [-19.79%, 74.83%] | $87.55 |
| series | international=0 | 473 | 473 | 0.0976 | 12.28% [0.08%, 25.15%] | $1008.74 | 20.175× | 71.91% | $240.40 | 262 (211 unfilled) | 19.39% [1.95%, 38.48%] | $414.08 |
| map | all | 666 | 360 | 0.0725 | 20.69% [4.47%, 41.87%] | $7961.60 | 159.232× | 38.49% | $245.53 | 105 (561 unfilled) | 57.21% [6.02%, 126.06%] | $291.11 |
| map | vct | 260 | 140 | 0.0568 | 14.08% [-3.44%, 38.93%] | $256.25 | 5.125× | 28.51% | $19.50 | 55 (205 unfilled) | 61.51% [0.10%, 158.79%] | $134.77 |
| map | vcl | 353 | 192 | 0.0878 | 28.10% [1.00%, 62.22%] | $1827.47 | 36.549× | 54.87% | $245.53 | 46 (307 unfilled) | 48.73% [-27.83%, 156.97%] | $126.16 |
| map | gc | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | t3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | collegiate | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | offseason | 53 | 28 | 0.0475 | 3.63% [-31.00%, 41.69%] | $50.44 | 1.009× | 21.63% | $3.12 | 4 (49 unfilled) | 95.88% [13.38%, 262.84%] | $59.24 |
| map | international=1 | 32 | 18 | 0.0368 | -5.00% [-29.61%, 20.35%] | $44.81 | 0.896× | 14.84% | $2.30 | 13 (19 unfilled) | 18.38% [-13.71%, 65.38%] | $52.91 |
| map | international=0 | 634 | 342 | 0.0743 | 21.98% [4.18%, 42.31%] | $7882.73 | 157.655× | 35.28% | $245.53 | 92 (542 unfilled) | 62.64% [4.15%, 143.64%] | $276.18 |
| series+map | all | 1166 | 530 | 0.0819 | 17.41% [4.71%, 30.63%] | $5145.34 | 102.907× | 52.50% | $247.91 | 393 (773 unfilled) | 29.90% [10.58%, 51.06%] | $483.98 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-09-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 240 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-01 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 21 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | map | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-03 | series | 72 | 1.000000 | 0.000000 | unfitted |
| 2026-03 | map | 48 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | series | 136 | 1.267176 | 0.750920 | fitted |
| 2026-04 | map | 104 | 1.627590 | 0.713957 | fitted |
| 2026-05 | series | 357 | 1.062964 | 0.648336 | fitted |
| 2026-05 | map | 456 | 1.153494 | 0.991215 | fitted |
| 2026-06 | series | 556 | 1.050288 | 0.721129 | fitted |
| 2026-06 | map | 833 | 0.983301 | 0.823368 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 541 | 0.619876 | 0.634347 | -0.014470 [-0.031535, 0.002690] | no |
| series | vct | 201 | 0.630796 | 0.644147 | -0.013351 [-0.034647, 0.008530] | no |
| series | vcl | 291 | 0.603617 | 0.621829 | -0.018212 [-0.045786, 0.012158] | no |
| series | gc | 0 | — | — | — | — |
| series | t3 | 0 | — | — | — | — |
| series | collegiate | 0 | — | — | — | — |
| series | offseason | 49 | 0.671644 | 0.668490 | 0.003154 [-0.038413, 0.038545] | no |
| series | international=1 | 24 | 0.648347 | 0.682705 | -0.034359 [-0.076455, 0.006536] | no |
| series | international=0 | 517 | 0.618555 | 0.632102 | -0.013547 [-0.030762, 0.006195] | no |
| map | all | 945 | 0.673082 | 0.673192 | -0.000110 [-0.013124, 0.012958] | no |
| map | vct | 392 | 0.664106 | 0.667249 | -0.003144 [-0.019709, 0.013847] | no |
| map | vcl | 456 | 0.676307 | 0.676303 | 0.000004 [-0.022261, 0.021009] | no |
| map | gc | 0 | — | — | — | — |
| map | t3 | 0 | — | — | — | — |
| map | collegiate | 0 | — | — | — | — |
| map | offseason | 97 | 0.694197 | 0.682581 | 0.011616 [-0.019833, 0.046336] | no |
| map | international=1 | 50 | 0.656274 | 0.651359 | 0.004916 [-0.016085, 0.024702] | no |
| map | international=0 | 895 | 0.674021 | 0.674412 | -0.000391 [-0.014140, 0.012080] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 333 | 333 | 0.0563 | 16.36% [1.93%, 31.47%] | $1721.04 | 34.421× | 45.80% | $246.88 | 175 (158 unfilled) | 20.19% [1.86%, 40.27%] | $615.60 |
| series | vct | 117 | 117 | 0.0420 | 14.94% [-9.28%, 39.89%] | $141.39 | 2.828× | 49.06% | $11.26 | 68 (49 unfilled) | 25.53% [-6.17%, 58.58%] | $173.05 |
| series | vcl | 188 | 188 | 0.0679 | 20.71% [2.64%, 40.61%] | $698.44 | 13.969× | 35.70% | $88.23 | 87 (101 unfilled) | 28.44% [1.73%, 57.46%] | $222.37 |
| series | gc | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | t3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | collegiate | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | offseason | 28 | 28 | 0.0382 | -6.82% [-50.82%, 40.46%] | $56.36 | 1.127× | 17.78% | $5.94 | 20 (8 unfilled) | -33.55% [-76.55%, 13.37%] | $45.06 |
| series | international=1 | 12 | 12 | 0.0363 | 55.56% [-17.15%, 139.25%] | $80.26 | 1.605× | 6.12% | $6.39 | 12 (0 unfilled) | 55.56% [-17.15%, 139.25%] | $80.26 |
| series | international=0 | 321 | 321 | 0.0571 | 14.89% [0.89%, 29.96%] | $1433.93 | 28.679× | 49.47% | $234.23 | 163 (158 unfilled) | 17.59% [-1.80%, 37.64%] | $390.70 |
| map | all | 582 | 306 | 0.0526 | 17.83% [-0.07%, 40.59%] | $188.33 | 3.767× | 66.69% | $34.32 | 62 (520 unfilled) | 98.26% [16.40%, 212.76%] | $159.11 |
| map | vct | 220 | 114 | 0.0502 | 14.75% [-4.91%, 42.55%] | $68.62 | 1.372× | 44.21% | $5.56 | 28 (192 unfilled) | 125.33% [18.66%, 326.93%] | $108.49 |
| map | vcl | 313 | 167 | 0.0557 | 25.53% [-3.70%, 65.62%] | $157.72 | 3.154× | 62.43% | $31.79 | 31 (282 unfilled) | 79.67% [-30.16%, 233.51%] | $69.79 |
| map | gc | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | t3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | collegiate | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | offseason | 49 | 25 | 0.0438 | -17.46% [-43.77%, 11.60%] | $36.89 | 0.738× | 26.38% | $4.26 | 3 (46 unfilled) | 39.52% [13.38%, 92.31%] | $52.97 |
| map | international=1 | 21 | 10 | 0.0364 | 3.08% [-29.44%, 34.82%] | $49.22 | 0.984× | 7.46% | $2.51 | 7 (14 unfilled) | 24.65% [-17.02%, 64.55%] | $51.49 |
| map | international=0 | 561 | 296 | 0.0532 | 18.39% [-0.11%, 40.93%] | $191.00 | 3.820× | 66.21% | $34.32 | 55 (506 unfilled) | 107.63% [13.03%, 240.82%] | $152.27 |
| series+map | all | 915 | 401 | 0.0540 | 17.30% [3.42%, 32.73%] | $1995.47 | 39.909× | 45.67% | $242.03 | 237 (678 unfilled) | 40.57% [12.99%, 73.49%] | $537.96 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-02 | 48 | 0.697147 | — | 0.690786 | 7.78% (39), $48.89 | — | 15 (24 unfilled) | 20.10% [-48.76%, 67.15%] | $50.19 | — | — | — |
| map | 2026-03 | 56 | 0.578315 | — | 0.565065 | -7.16% (40), $35.94 | — | 15 (25 unfilled) | -11.94% [-60.19%, 35.68%] | $44.71 | — | — | — |
| map | 2026-04 | 352 | 0.635433 | 0.675820 | 0.690793 | 59.73% (228), $7545.06 | 44.80% (242), $275.50 | 28 (200 unfilled) | 188.63% [7.04%, 428.45%] | $259.30 | 24 (218 unfilled) | 229.09% [15.20%, 497.82%] | $147.85 |
| map | 2026-05 | 377 | 0.682959 | 0.684864 | 0.687018 | 7.96% (218), $98.84 | 5.62% (213), $67.72 | 26 (192 unfilled) | 30.62% [-17.56%, 81.78%] | $76.04 | 21 (192 unfilled) | 41.51% [-9.88%, 92.45%] | $72.11 |
| map | 2026-06 | 216 | 0.657308 | 0.648055 | 0.620377 | -11.25% (141), $22.10 | -12.56% (127), $24.52 | 21 (120 unfilled) | -11.04% [-46.02%, 25.18%] | $39.32 | 17 (110 unfilled) | -14.55% [-54.70%, 27.55%] | $37.59 |
| series | 2026-01 | 21 | 0.606191 | — | 0.661069 | 7.89% (15), $62.09 | — | 9 (6 unfilled) | -6.29% [-76.58%, 69.25%] | $54.05 | — | — | — |
| series | 2026-02 | 51 | 0.661244 | — | 0.694525 | 33.73% (40), $98.25 | — | 29 (11 unfilled) | 43.74% [-10.97%, 110.44%] | $88.81 | — | — | — |
| series | 2026-03 | 64 | 0.584054 | — | 0.565917 | -5.56% (48), $28.95 | — | 35 (13 unfilled) | 2.48% [-28.66%, 33.54%] | $38.29 | — | — | — |
| series | 2026-04 | 221 | 0.618019 | 0.613930 | 0.627690 | 20.86% (161), $339.34 | 20.62% (138), $300.53 | 69 (92 unfilled) | 50.16% [6.85%, 98.58%] | $212.84 | 60 (78 unfilled) | 41.57% [7.94%, 78.05%] | $162.77 |
| series | 2026-05 | 199 | 0.635029 | 0.638277 | 0.663719 | 17.93% (140), $231.59 | 21.29% (117), $315.56 | 92 (48 unfilled) | 6.14% [-20.06%, 34.13%] | $65.42 | 73 (44 unfilled) | 7.81% [-19.02%, 39.19%] | $117.43 |
| series | 2026-06 | 121 | 0.617371 | 0.600477 | 0.598199 | -5.70% (96), $53.60 | 1.46% (78), $59.53 | 54 (42 unfilled) | 7.69% [-23.29%, 41.59%] | $106.67 | 42 (36 unfilled) | 11.30% [-22.27%, 47.31%] | $88.43 |

### player_round_glicko_rookie_tier_revert_perf_kda: Kalshi comparison and returns



#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 677 | 0.621374 | 0.633240 | -0.011866 [-0.034993, 0.012721] | no |
| series | vct | 278 | 0.617598 | 0.634755 | -0.017157 [-0.048467, 0.011503] | no |
| series | vcl | 340 | 0.613874 | 0.619968 | -0.006094 [-0.046104, 0.035420] | no |
| series | gc | 0 | — | — | — | — |
| series | t3 | 0 | — | — | — | — |
| series | collegiate | 0 | — | — | — | — |
| series | offseason | 59 | 0.682384 | 0.702587 | -0.020202 [-0.076605, 0.034610] | no |
| series | international=1 | 41 | 0.615983 | 0.653397 | -0.037414 [-0.083653, 0.005413] | no |
| series | international=0 | 636 | 0.621721 | 0.631941 | -0.010219 [-0.035910, 0.015362] | no |
| map | all | 1049 | 0.655991 | 0.668225 | -0.012234 [-0.034648, 0.006219] | no |
| map | vct | 461 | 0.655488 | 0.665762 | -0.010274 [-0.030513, 0.006979] | no |
| map | vcl | 490 | 0.650148 | 0.668365 | -0.018216 [-0.061294, 0.017213] | no |
| map | gc | 0 | — | — | — | — |
| map | t3 | 0 | — | — | — | — |
| map | collegiate | 0 | — | — | — | — |
| map | offseason | 98 | 0.687571 | 0.679111 | 0.008460 [-0.025512, 0.040647] | no |
| map | international=1 | 59 | 0.661062 | 0.649653 | 0.011410 [-0.012520, 0.034417] | no |
| map | international=0 | 990 | 0.655689 | 0.669332 | -0.013643 [-0.035478, 0.006502] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 500 | 500 | 0.0928 | 13.60% [1.18%, 26.30%] | $1322.94 | 26.459× | 70.47% | $246.88 | 287 (213 unfilled) | 19.95% [3.44%, 37.25%] | $644.08 |
| series | vct | 196 | 196 | 0.0758 | 10.14% [-8.61%, 30.45%] | $132.88 | 2.658× | 70.63% | $10.58 | 119 (77 unfilled) | 19.33% [-5.30%, 45.44%] | $256.32 |
| series | vcl | 265 | 265 | 0.1078 | 15.67% [-0.92%, 33.69%] | $472.95 | 9.459× | 53.46% | $84.49 | 138 (127 unfilled) | 22.80% [-1.93%, 48.19%] | $173.96 |
| series | gc | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | t3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | collegiate | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | offseason | 39 | 39 | 0.0753 | 16.92% [-23.07%, 61.88%] | $81.93 | 1.639× | 42.68% | $9.40 | 30 (9 unfilled) | 9.35% [-36.74%, 57.05%] | $58.86 |
| series | international=1 | 27 | 27 | 0.0445 | 29.29% [-15.59%, 79.58%] | $87.33 | 1.747× | 20.15% | $6.95 | 27 (0 unfilled) | 29.29% [-15.59%, 79.58%] | $87.77 |
| series | international=0 | 473 | 473 | 0.0955 | 12.71% [-0.70%, 25.84%] | $1029.36 | 20.587× | 70.47% | $240.40 | 260 (213 unfilled) | 18.98% [1.61%, 37.94%] | $381.63 |
| map | all | 659 | 354 | 0.0708 | 21.06% [4.11%, 41.10%] | $8139.37 | 162.787× | 40.58% | $245.53 | 98 (561 unfilled) | 63.63% [7.64%, 131.34%] | $297.96 |
| map | vct | 260 | 138 | 0.0560 | 12.39% [-5.49%, 35.14%] | $243.55 | 4.871× | 33.00% | $17.66 | 50 (210 unfilled) | 70.75% [3.85%, 178.04%] | $131.80 |
| map | vcl | 347 | 189 | 0.0859 | 29.84% [1.67%, 66.06%] | $1827.79 | 36.556× | 54.02% | $245.53 | 44 (303 unfilled) | 52.66% [-27.16%, 167.38%] | $125.65 |
| map | gc | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | t3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | collegiate | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | offseason | 52 | 27 | 0.0443 | 5.62% [-28.75%, 42.61%] | $52.43 | 1.049× | 17.08% | $3.51 | 4 (48 unfilled) | 95.88% [13.38%, 262.84%] | $59.51 |
| map | international=1 | 32 | 18 | 0.0362 | -16.45% [-46.81%, 14.85%] | $42.49 | 0.850× | 19.35% | $2.88 | 11 (21 unfilled) | 26.07% [-11.94%, 68.72%] | $52.35 |
| map | international=0 | 627 | 336 | 0.0726 | 22.97% [5.34%, 44.20%] | $8618.33 | 172.367× | 35.75% | $245.53 | 87 (540 unfilled) | 68.34% [4.60%, 146.66%] | $280.31 |
| series+map | all | 1159 | 530 | 0.0803 | 17.84% [6.33%, 31.63%] | $6737.12 | 134.742× | 51.44% | $247.91 | 385 (774 unfilled) | 31.07% [11.00%, 54.37%] | $543.12 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-09-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 240 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-01 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 21 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | map | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-03 | series | 72 | 1.000000 | 0.000000 | unfitted |
| 2026-03 | map | 48 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | series | 136 | 1.282910 | 0.773480 | fitted |
| 2026-04 | map | 104 | 1.603656 | 0.677463 | fitted |
| 2026-05 | series | 357 | 1.074872 | 0.666986 | fitted |
| 2026-05 | map | 456 | 1.160706 | 0.996846 | fitted |
| 2026-06 | series | 556 | 1.056557 | 0.731526 | fitted |
| 2026-06 | map | 833 | 0.996457 | 0.842484 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 541 | 0.619482 | 0.634347 | -0.014865 [-0.031928, 0.002876] | no |
| series | vct | 201 | 0.630931 | 0.644147 | -0.013216 [-0.034787, 0.009062] | no |
| series | vcl | 291 | 0.602781 | 0.621829 | -0.019048 [-0.047277, 0.011856] | no |
| series | gc | 0 | — | — | — | — |
| series | t3 | 0 | — | — | — | — |
| series | collegiate | 0 | — | — | — | — |
| series | offseason | 49 | 0.671704 | 0.668490 | 0.003214 [-0.036797, 0.038268] | no |
| series | international=1 | 24 | 0.647241 | 0.682705 | -0.035464 [-0.080556, 0.007815] | no |
| series | international=0 | 517 | 0.618194 | 0.632102 | -0.013908 [-0.031483, 0.005894] | no |
| map | all | 945 | 0.672464 | 0.673192 | -0.000728 [-0.013141, 0.011996] | no |
| map | vct | 392 | 0.663982 | 0.667249 | -0.003268 [-0.019067, 0.013142] | no |
| map | vcl | 456 | 0.675584 | 0.676303 | -0.000719 [-0.021766, 0.020072] | no |
| map | gc | 0 | — | — | — | — |
| map | t3 | 0 | — | — | — | — |
| map | collegiate | 0 | — | — | — | — |
| map | offseason | 97 | 0.692075 | 0.682581 | 0.009494 [-0.020706, 0.042281] | no |
| map | international=1 | 50 | 0.658611 | 0.651359 | 0.007253 [-0.013363, 0.027401] | no |
| map | international=0 | 895 | 0.673238 | 0.674412 | -0.001174 [-0.014366, 0.011013] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 332 | 332 | 0.0560 | 17.59% [3.87%, 32.71%] | $1572.97 | 31.459× | 42.62% | $225.35 | 171 (161 unfilled) | 22.97% [4.03%, 43.69%] | $485.65 |
| series | vct | 116 | 116 | 0.0424 | 18.21% [-5.32%, 43.61%] | $114.99 | 2.300× | 50.11% | $9.16 | 68 (48 unfilled) | 29.39% [-1.16%, 63.34%] | $149.18 |
| series | vcl | 191 | 191 | 0.0663 | 20.30% [1.59%, 40.28%] | $730.49 | 14.610× | 35.71% | $92.84 | 85 (106 unfilled) | 28.26% [1.03%, 57.61%] | $178.77 |
| series | gc | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | t3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | collegiate | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | offseason | 25 | 25 | 0.0403 | -5.86% [-53.48%, 44.10%] | $56.57 | 1.131× | 13.83% | $5.93 | 18 (7 unfilled) | -26.06% [-73.62%, 26.93%] | $45.08 |
| series | international=1 | 13 | 13 | 0.0334 | 43.49% [-27.47%, 123.73%] | $81.81 | 1.636× | 7.01% | $6.51 | 13 (0 unfilled) | 43.49% [-27.47%, 123.73%] | $81.81 |
| series | international=0 | 319 | 319 | 0.0569 | 16.54% [2.73%, 32.22%] | $1198.28 | 23.966× | 49.76% | $196.85 | 158 (161 unfilled) | 21.28% [1.64%, 42.26%] | $285.64 |
| map | all | 572 | 297 | 0.0500 | 18.12% [-1.26%, 41.58%] | $172.73 | 3.455× | 65.99% | $27.24 | 64 (508 unfilled) | 92.33% [11.27%, 202.71%] | $136.60 |
| map | vct | 222 | 113 | 0.0467 | 14.59% [-4.96%, 43.00%] | $75.73 | 1.515× | 42.06% | $5.70 | 28 (194 unfilled) | 125.33% [18.66%, 326.93%] | $99.97 |
| map | vcl | 305 | 162 | 0.0535 | 25.47% [-4.30%, 67.38%] | $126.43 | 2.529× | 63.86% | $25.83 | 33 (272 unfilled) | 69.31% [-32.53%, 223.40%] | $64.79 |
| map | gc | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | t3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | collegiate | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | offseason | 45 | 22 | 0.0433 | -14.30% [-42.70%, 17.31%] | $39.48 | 0.790× | 22.52% | $4.24 | 3 (42 unfilled) | 39.52% [13.38%, 92.31%] | $52.98 |
| map | international=1 | 24 | 11 | 0.0328 | -9.92% [-42.63%, 21.30%] | $47.61 | 0.952× | 9.07% | $2.43 | 7 (17 unfilled) | 24.65% [-17.02%, 64.55%] | $51.51 |
| map | international=0 | 548 | 286 | 0.0508 | 19.35% [1.13%, 43.56%] | $181.12 | 3.622× | 64.34% | $27.24 | 57 (491 unfilled) | 100.64% [9.48%, 215.72%] | $130.42 |
| series+map | all | 904 | 396 | 0.0522 | 17.93% [3.86%, 34.14%] | $1405.56 | 28.111× | 52.96% | $197.49 | 235 (669 unfilled) | 41.82% [14.73%, 75.46%] | $404.73 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-02 | 48 | 0.698252 | — | 0.690786 | 5.56% (38), $47.77 | — | 14 (24 unfilled) | 14.94% [-49.57%, 63.44%] | $49.21 | — | — | — |
| map | 2026-03 | 56 | 0.579719 | — | 0.565065 | -7.16% (40), $36.07 | — | 15 (25 unfilled) | -11.94% [-60.19%, 35.68%] | $44.01 | — | — | — |
| map | 2026-04 | 352 | 0.635796 | 0.676468 | 0.690793 | 58.67% (225), $7689.25 | 45.97% (236), $224.57 | 28 (197 unfilled) | 188.63% [7.04%, 428.45%] | $254.76 | 25 (211 unfilled) | 215.94% [15.49%, 473.82%] | $126.62 |
| map | 2026-05 | 377 | 0.681495 | 0.683578 | 0.687018 | 10.90% (218), $115.27 | 6.89% (210), $85.41 | 23 (195 unfilled) | 47.65% [-4.53%, 102.05%] | $80.55 | 23 (187 unfilled) | 35.38% [-12.09%, 83.26%] | $72.41 |
| map | 2026-06 | 216 | 0.654770 | 0.646540 | 0.620377 | -11.71% (138), $19.96 | -14.78% (126), $21.90 | 18 (120 unfilled) | -11.51% [-51.57%, 31.85%] | $38.60 | 16 (110 unfilled) | -17.01% [-61.40%, 29.95%] | $37.45 |
| series | 2026-01 | 21 | 0.609608 | — | 0.661069 | 18.69% (16), $61.73 | — | 9 (7 unfilled) | -6.29% [-76.58%, 69.25%] | $52.71 | — | — | — |
| series | 2026-02 | 51 | 0.660801 | — | 0.694525 | 33.23% (38), $97.85 | — | 27 (11 unfilled) | 49.39% [-8.56%, 115.58%] | $87.08 | — | — | — |
| series | 2026-03 | 64 | 0.581920 | — | 0.565917 | -3.40% (49), $28.67 | — | 36 (13 unfilled) | 5.20% [-26.20%, 36.57%] | $35.65 | — | — | — |
| series | 2026-04 | 221 | 0.616128 | 0.613476 | 0.627690 | 18.80% (159), $306.27 | 20.18% (142), $281.17 | 67 (92 unfilled) | 45.17% [1.74%, 91.15%] | $196.92 | 59 (83 unfilled) | 38.91% [4.70%, 76.97%] | $134.18 |
| series | 2026-05 | 199 | 0.636247 | 0.639276 | 0.663719 | 20.28% (142), $273.87 | 25.54% (113), $283.09 | 93 (49 unfilled) | 8.98% [-15.89%, 35.80%] | $76.37 | 71 (42 unfilled) | 14.39% [-13.97%, 45.76%] | $107.97 |
| series | 2026-06 | 121 | 0.612785 | 0.597897 | 0.598199 | -4.86% (96), $50.65 | 1.20% (77), $60.79 | 55 (41 unfilled) | 7.20% [-25.17%, 42.21%] | $97.35 | 41 (36 unfilled) | 14.97% [-22.21%, 54.43%] | $80.27 |

### team_elo+none: Kalshi comparison and returns

none

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 677 | 0.659884 | 0.633240 | 0.026644 [0.005070, 0.049198] | yes |
| series | vct | 278 | 0.656875 | 0.634755 | 0.022120 [-0.008080, 0.052332] | no |
| series | vcl | 340 | 0.653448 | 0.619968 | 0.033480 [-0.002273, 0.068144] | no |
| series | gc | 0 | — | — | — | — |
| series | t3 | 0 | — | — | — | — |
| series | collegiate | 0 | — | — | — | — |
| series | offseason | 59 | 0.711150 | 0.702587 | 0.008563 [-0.038647, 0.057958] | no |
| series | international=1 | 41 | 0.651212 | 0.653397 | -0.002184 [-0.046947, 0.045515] | no |
| series | international=0 | 636 | 0.660443 | 0.631941 | 0.028502 [0.005725, 0.053222] | yes |
| map | all | 1049 | 0.674219 | 0.668225 | 0.005994 [-0.016072, 0.025667] | no |
| map | vct | 461 | 0.678620 | 0.665762 | 0.012858 [-0.012004, 0.036805] | no |
| map | vcl | 490 | 0.669823 | 0.668365 | 0.001458 [-0.038888, 0.036008] | no |
| map | gc | 0 | — | — | — | — |
| map | t3 | 0 | — | — | — | — |
| map | collegiate | 0 | — | — | — | — |
| map | offseason | 98 | 0.675493 | 0.679111 | -0.003618 [-0.033834, 0.028482] | no |
| map | international=1 | 59 | 0.669039 | 0.649653 | 0.019386 [-0.020368, 0.061334] | no |
| map | international=0 | 990 | 0.674527 | 0.669332 | 0.005196 [-0.018272, 0.026420] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 473 | 473 | 0.0894 | -2.01% [-15.18%, 11.35%] | $0.55 | 0.011× | 99.52% | $9.89 | 260 (213 unfilled) | 15.98% [-1.36%, 35.27%] | $128.56 |
| series | vct | 180 | 180 | 0.0796 | -2.47% [-21.83%, 19.63%] | $17.90 | 0.358× | 72.48% | $5.29 | 107 (73 unfilled) | 15.75% [-9.72%, 43.70%] | $93.96 |
| series | vcl | 257 | 257 | 0.1004 | -3.13% [-20.74%, 15.40%] | $2.78 | 0.056× | 97.26% | $8.12 | 126 (131 unfilled) | 20.99% [-5.94%, 48.89%] | $127.28 |
| series | gc | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | t3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | collegiate | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | offseason | 36 | 36 | 0.0591 | 8.33% [-29.51%, 48.08%] | $43.23 | 0.865× | 59.45% | $7.21 | 27 (9 unfilled) | -6.59% [-46.54%, 37.00%] | $37.07 |
| series | international=1 | 32 | 32 | 0.0514 | 5.76% [-27.15%, 40.29%] | $45.99 | 0.920× | 41.06% | $6.36 | 31 (1 unfilled) | 4.29% [-31.31%, 39.31%] | $44.04 |
| series | international=0 | 441 | 441 | 0.0921 | -2.57% [-15.72%, 11.09%] | $0.62 | 0.012× | 99.31% | $7.62 | 229 (212 unfilled) | 17.55% [-1.89%, 37.48%] | $152.11 |
| map | all | 698 | 372 | 0.0762 | 12.02% [-4.33%, 32.11%] | $480.61 | 9.612× | 80.53% | $143.37 | 108 (590 unfilled) | 52.76% [3.09%, 115.44%] | $203.47 |
| map | vct | 286 | 151 | 0.0699 | 3.93% [-12.79%, 27.90%] | $62.89 | 1.258× | 50.73% | $7.89 | 42 (244 unfilled) | 70.04% [-9.28%, 197.74%] | $93.56 |
| map | vcl | 350 | 190 | 0.0874 | 19.95% [-7.26%, 52.36%] | $366.07 | 7.321× | 72.37% | $80.85 | 57 (293 unfilled) | 48.44% [-12.85%, 131.95%] | $117.23 |
| map | gc | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | t3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | collegiate | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | offseason | 62 | 31 | 0.0420 | 4.29% [-20.29%, 28.35%] | $43.32 | 0.866× | 27.84% | $3.31 | 9 (53 unfilled) | -0.67% [-57.18%, 35.88%] | $47.13 |
| map | international=1 | 42 | 23 | 0.0572 | -9.87% [-32.61%, 11.40%] | $38.60 | 0.772× | 30.42% | $2.84 | 11 (31 unfilled) | 19.70% [-26.58%, 56.05%] | $52.92 |
| map | international=0 | 656 | 349 | 0.0775 | 13.41% [-3.61%, 34.83%] | $622.19 | 12.444× | 74.78% | $143.30 | 97 (559 unfilled) | 56.48% [-0.76%, 129.18%] | $198.48 |
| series+map | all | 1171 | 544 | 0.0815 | 6.33% [-5.87%, 19.78%] | $48.89 | 0.978× | 97.29% | $123.59 | 368 (803 unfilled) | 26.77% [7.20%, 49.68%] | $202.77 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-09-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 240 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-01 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 21 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | map | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-03 | series | 72 | 1.000000 | 0.000000 | unfitted |
| 2026-03 | map | 48 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | series | 136 | 1.042825 | 0.215516 | fitted |
| 2026-04 | map | 104 | 1.439410 | 0.208235 | fitted |
| 2026-05 | series | 357 | 0.942242 | 0.232480 | fitted |
| 2026-05 | map | 456 | 0.879130 | 0.568385 | fitted |
| 2026-06 | series | 556 | 0.860932 | 0.124059 | fitted |
| 2026-06 | map | 833 | 0.763049 | 0.405197 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 541 | 0.634508 | 0.634347 | 0.000161 [-0.005143, 0.005135] | no |
| series | vct | 201 | 0.643137 | 0.644147 | -0.001010 [-0.009242, 0.007156] | no |
| series | vcl | 291 | 0.622082 | 0.621829 | 0.000253 [-0.007141, 0.007684] | no |
| series | gc | 0 | — | — | — | — |
| series | t3 | 0 | — | — | — | — |
| series | collegiate | 0 | — | — | — | — |
| series | offseason | 49 | 0.672904 | 0.668490 | 0.004414 [-0.008452, 0.016494] | no |
| series | international=1 | 24 | 0.680037 | 0.682705 | -0.002669 [-0.027187, 0.017497] | no |
| series | international=0 | 517 | 0.632394 | 0.632102 | 0.000292 [-0.005051, 0.005662] | no |
| map | all | 945 | 0.684435 | 0.673192 | 0.011243 [0.002676, 0.019848] | yes |
| map | vct | 392 | 0.675770 | 0.667249 | 0.008520 [-0.004749, 0.022586] | no |
| map | vcl | 456 | 0.693354 | 0.676303 | 0.017051 [0.003772, 0.030048] | yes |
| map | gc | 0 | — | — | — | — |
| map | t3 | 0 | — | — | — | — |
| map | collegiate | 0 | — | — | — | — |
| map | offseason | 97 | 0.677523 | 0.682581 | -0.005057 [-0.019598, 0.009568] | no |
| map | international=1 | 50 | 0.658711 | 0.651359 | 0.007353 [-0.007823, 0.021042] | no |
| map | international=0 | 895 | 0.685872 | 0.674412 | 0.011460 [0.001858, 0.020438] | yes |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 82 | 82 | 0.0152 | -5.01% [-38.32%, 28.44%] | $35.62 | 0.712× | 43.57% | $5.46 | 49 (33 unfilled) | 16.91% [-25.46%, 65.25%] | $57.12 |
| series | vct | 28 | 28 | 0.0196 | 14.92% [-47.96%, 87.75%] | $45.59 | 0.912× | 34.31% | $4.96 | 18 (10 unfilled) | 63.04% [-26.71%, 163.05%] | $62.32 |
| series | vcl | 50 | 50 | 0.0135 | -8.62% [-45.61%, 31.17%] | $40.94 | 0.819× | 19.74% | $4.61 | 27 (23 unfilled) | 3.28% [-40.89%, 50.22%] | $47.76 |
| series | gc | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | t3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | collegiate | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | offseason | 4 | 4 | 0.0065 | -100.00% [-100.00%, -100.00%] | $47.79 | 0.956× | 4.42% | $1.19 | 4 (0 unfilled) | -100.00% [-100.00%, -100.00%] | $47.79 |
| series | international=1 | 5 | 5 | 0.0076 | 128.58% [-40.93%, 298.09%] | $54.96 | 1.099× | 1.20% | $0.70 | 5 (0 unfilled) | 128.58% [-40.93%, 298.09%] | $54.96 |
| series | international=0 | 77 | 77 | 0.0157 | -13.74% [-45.15%, 22.22%] | $32.39 | 0.648× | 44.19% | $5.46 | 44 (33 unfilled) | 4.13% [-38.95%, 48.31%] | $51.92 |
| map | all | 435 | 244 | 0.0302 | -8.06% [-17.18%, 1.76%] | $7.27 | 0.145× | 88.32% | $5.68 | 69 (366 unfilled) | -5.79% [-25.63%, 15.35%] | $38.70 |
| map | vct | 184 | 100 | 0.0327 | -5.21% [-18.93%, 9.43%] | $28.54 | 0.571× | 50.48% | $5.13 | 30 (154 unfilled) | 1.27% [-36.69%, 39.63%] | $52.39 |
| map | vcl | 222 | 129 | 0.0296 | -11.48% [-23.80%, 1.98%] | $13.80 | 0.276× | 75.99% | $5.19 | 36 (186 unfilled) | -8.56% [-34.11%, 13.90%] | $40.07 |
| map | gc | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | t3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | collegiate | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | offseason | 29 | 15 | 0.0195 | 0.15% [-31.48%, 32.90%] | $48.32 | 0.966× | 9.94% | $2.85 | 3 (26 unfilled) | -42.95% [-100.00%, -14.15%] | $46.34 |
| map | international=1 | 16 | 10 | 0.0119 | -21.91% [-67.31%, 29.28%] | $46.48 | 0.930× | 7.05% | $2.46 | 4 (12 unfilled) | -59.26% [-100.00%, 64.55%] | $48.87 |
| map | international=0 | 419 | 234 | 0.0309 | -7.52% [-16.46%, 2.12%] | $7.90 | 0.158× | 87.34% | $5.68 | 65 (354 unfilled) | -2.49% [-23.23%, 18.34%] | $39.58 |
| series+map | all | 517 | 268 | 0.0278 | -7.57% [-18.34%, 3.94%] | $5.97 | 0.119× | 90.40% | $5.67 | 118 (399 unfilled) | 3.72% [-17.74%, 27.80%] | $39.19 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-02 | 48 | 0.701058 | — | 0.690786 | -19.10% (25), $33.55 | — | 9 (16 unfilled) | -1.84% [-100.00%, 65.78%] | $45.89 | — | — | — |
| map | 2026-03 | 56 | 0.637862 | — | 0.565065 | -31.56% (35), $21.54 | — | 10 (25 unfilled) | -27.24% [-81.79%, 41.92%] | $37.51 | — | — | — |
| map | 2026-04 | 352 | 0.660671 | 0.707440 | 0.690793 | 49.03% (241), $6279.98 | -9.38% (188), $17.46 | 29 (212 unfilled) | 183.25% [4.69%, 428.45%] | $242.59 | 33 (155 unfilled) | -12.13% [-31.69%, 6.10%] | $41.36 |
| map | 2026-05 | 377 | 0.704442 | 0.690344 | 0.687018 | -1.28% (249), $26.14 | -0.66% (155), $42.94 | 36 (213 unfilled) | 10.12% [-22.78%, 41.28%] | $54.33 | 25 (130 unfilled) | 11.32% [-34.86%, 53.52%] | $53.62 |
| map | 2026-06 | 216 | 0.647007 | 0.636631 | 0.620377 | -10.26% (148), $16.82 | -17.81% (92), $25.67 | 24 (124 unfilled) | 12.50% [-21.08%, 41.11%] | $46.58 | 11 (81 unfilled) | -26.18% [-100.00%, 29.50%] | $44.04 |
| series | 2026-01 | 21 | 0.684822 | — | 0.661069 | 4.92% (16), $45.78 | — | 9 (7 unfilled) | -25.46% [-81.66%, 48.91%] | $36.49 | — | — | — |
| series | 2026-02 | 51 | 0.659130 | — | 0.694525 | 25.18% (34), $95.24 | — | 22 (12 unfilled) | 49.18% [-13.77%, 132.77%] | $129.91 | — | — | — |
| series | 2026-03 | 64 | 0.662527 | — | 0.565917 | -31.86% (49), $10.02 | — | 37 (12 unfilled) | -19.68% [-50.47%, 13.73%] | $18.83 | — | — | — |
| series | 2026-04 | 221 | 0.645922 | 0.624471 | 0.627690 | 3.92% (146), $67.65 | 5.82% (25), $48.53 | 59 (87 unfilled) | 58.07% [8.98%, 114.67%] | $210.98 | 16 (9 unfilled) | 27.95% [-31.97%, 85.50%] | $58.32 |
| series | 2026-05 | 199 | 0.690980 | 0.663840 | 0.663719 | 0.07% (133), $9.78 | -33.91% (33), $36.72 | 83 (50 unfilled) | -1.88% [-27.64%, 26.71%] | $36.33 | 22 (11 unfilled) | -11.15% [-73.62%, 72.74%] | $50.32 |
| series | 2026-06 | 121 | 0.628835 | 0.604598 | 0.598199 | -9.59% (95), $9.03 | 23.37% (24), $50.00 | 50 (45 unfilled) | 14.89% [-15.83%, 48.34%] | $44.61 | 11 (13 unfilled) | 56.86% [-46.08%, 168.60%] | $48.32 |

### player_round_glicko+none: Kalshi comparison and returns

none

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 677 | 0.631896 | 0.633240 | -0.001344 [-0.023684, 0.021712] | no |
| series | vct | 278 | 0.629718 | 0.634755 | -0.005037 [-0.035239, 0.023644] | no |
| series | vcl | 340 | 0.622985 | 0.619968 | 0.003017 [-0.034835, 0.040819] | no |
| series | gc | 0 | — | — | — | — |
| series | t3 | 0 | — | — | — | — |
| series | collegiate | 0 | — | — | — | — |
| series | offseason | 59 | 0.693516 | 0.702587 | -0.009071 [-0.070439, 0.050068] | no |
| series | international=1 | 41 | 0.622775 | 0.653397 | -0.030622 [-0.076037, 0.019882] | no |
| series | international=0 | 636 | 0.632485 | 0.631941 | 0.000544 [-0.024166, 0.024627] | no |
| map | all | 1049 | 0.661370 | 0.668225 | -0.006855 [-0.028831, 0.011834] | no |
| map | vct | 461 | 0.658507 | 0.665762 | -0.007255 [-0.027207, 0.011052] | no |
| map | vcl | 490 | 0.658544 | 0.668365 | -0.009820 [-0.052216, 0.025600] | no |
| map | gc | 0 | — | — | — | — |
| map | t3 | 0 | — | — | — | — |
| map | collegiate | 0 | — | — | — | — |
| map | offseason | 98 | 0.688964 | 0.679111 | 0.009853 [-0.018553, 0.038849] | no |
| map | international=1 | 59 | 0.666817 | 0.649653 | 0.017165 [-0.014406, 0.053245] | no |
| map | international=0 | 990 | 0.661045 | 0.669332 | -0.008286 [-0.030282, 0.011757] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 501 | 501 | 0.0922 | 8.45% [-4.14%, 20.32%] | $220.43 | 4.409× | 82.96% | $55.92 | 290 (211 unfilled) | 19.26% [3.85%, 35.68%] | $655.33 |
| series | vct | 196 | 196 | 0.0781 | 8.21% [-10.88%, 29.43%] | $56.76 | 1.135× | 67.37% | $7.96 | 122 (74 unfilled) | 24.93% [-1.16%, 50.89%] | $237.04 |
| series | vcl | 263 | 263 | 0.1059 | 10.40% [-6.17%, 28.87%] | $139.98 | 2.800× | 62.91% | $29.19 | 135 (128 unfilled) | 20.58% [-4.27%, 47.85%] | $147.27 |
| series | gc | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | t3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | collegiate | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | offseason | 42 | 42 | 0.0725 | -2.68% [-40.11%, 35.04%] | $72.88 | 1.458× | 50.25% | $10.15 | 33 (9 unfilled) | -7.08% [-46.30%, 35.97%] | $51.73 |
| series | international=1 | 28 | 28 | 0.0506 | 30.78% [-14.12%, 74.42%] | $78.74 | 1.575× | 18.17% | $6.27 | 28 (0 unfilled) | 30.78% [-14.12%, 74.42%] | $79.77 |
| series | international=0 | 473 | 473 | 0.0947 | 7.13% [-5.57%, 20.78%] | $140.25 | 2.805× | 82.96% | $44.65 | 262 (211 unfilled) | 18.03% [0.77%, 36.43%] | $392.46 |
| map | all | 647 | 346 | 0.0735 | 18.30% [1.51%, 38.72%] | $4234.75 | 84.695× | 31.14% | $245.53 | 95 (552 unfilled) | 58.09% [-2.02%, 127.43%] | $240.23 |
| map | vct | 273 | 143 | 0.0567 | 10.98% [-6.46%, 33.54%] | $175.34 | 3.507× | 35.24% | $16.59 | 48 (225 unfilled) | 68.04% [-0.24%, 188.15%] | $122.55 |
| map | vcl | 324 | 179 | 0.0917 | 27.18% [-2.22%, 65.83%] | $1495.03 | 29.901× | 49.34% | $221.23 | 42 (282 unfilled) | 43.57% [-40.39%, 161.86%] | $118.48 |
| map | gc | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | t3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | collegiate | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | offseason | 50 | 24 | 0.0469 | 0.49% [-26.79%, 30.69%] | $52.19 | 1.044× | 21.58% | $3.83 | 5 (45 unfilled) | 85.42% [23.05%, 209.00%] | $56.76 |
| map | international=1 | 35 | 19 | 0.0478 | -20.19% [-46.33%, 6.10%] | $33.51 | 0.670× | 35.86% | $4.79 | 14 (21 unfilled) | -3.63% [-41.12%, 35.47%] | $49.18 |
| map | international=0 | 612 | 327 | 0.0749 | 20.49% [2.22%, 41.17%] | $5088.26 | 101.765× | 26.74% | $245.53 | 81 (531 unfilled) | 68.66% [2.57%, 162.06%] | $243.09 |
| series+map | all | 1148 | 532 | 0.0817 | 13.99% [1.86%, 27.64%] | $4152.97 | 83.059× | 45.69% | $247.91 | 385 (763 unfilled) | 28.85% [9.06%, 52.15%] | $378.90 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-09-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 240 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-01 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 21 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | map | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-03 | series | 72 | 1.000000 | 0.000000 | unfitted |
| 2026-03 | map | 48 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | series | 136 | 1.268851 | 0.758810 | fitted |
| 2026-04 | map | 104 | 1.441942 | 0.315911 | fitted |
| 2026-05 | series | 357 | 1.050991 | 0.617096 | fitted |
| 2026-05 | map | 456 | 1.061734 | 0.860054 | fitted |
| 2026-06 | series | 556 | 0.985933 | 0.545120 | fitted |
| 2026-06 | map | 833 | 0.928229 | 0.717006 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 541 | 0.626760 | 0.634347 | -0.007587 [-0.024047, 0.008406] | no |
| series | vct | 201 | 0.640311 | 0.644147 | -0.003836 [-0.026236, 0.019731] | no |
| series | vcl | 291 | 0.607219 | 0.621829 | -0.014609 [-0.038829, 0.011600] | no |
| series | gc | 0 | — | — | — | — |
| series | t3 | 0 | — | — | — | — |
| series | collegiate | 0 | — | — | — | — |
| series | offseason | 49 | 0.687222 | 0.668490 | 0.018732 [-0.016580, 0.052524] | no |
| series | international=1 | 24 | 0.664309 | 0.682705 | -0.018396 [-0.056673, 0.023117] | no |
| series | international=0 | 517 | 0.625017 | 0.632102 | -0.007085 [-0.023322, 0.009467] | no |
| map | all | 945 | 0.679807 | 0.673192 | 0.006616 [-0.002325, 0.016233] | no |
| map | vct | 392 | 0.667363 | 0.667249 | 0.000114 [-0.012507, 0.012026] | no |
| map | vcl | 456 | 0.688112 | 0.676303 | 0.011809 [-0.002897, 0.026976] | no |
| map | gc | 0 | — | — | — | — |
| map | t3 | 0 | — | — | — | — |
| map | collegiate | 0 | — | — | — | — |
| map | offseason | 97 | 0.691057 | 0.682581 | 0.008477 [-0.017985, 0.035315] | no |
| map | international=1 | 50 | 0.664037 | 0.651359 | 0.012679 [-0.011599, 0.037675] | no |
| map | international=0 | 895 | 0.680689 | 0.674412 | 0.006277 [-0.003449, 0.015828] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 312 | 312 | 0.0552 | 13.36% [-1.27%, 28.44%] | $357.15 | 7.143× | 54.88% | $54.32 | 164 (148 unfilled) | 17.40% [-3.33%, 38.59%] | $157.92 |
| series | vct | 115 | 115 | 0.0490 | 7.22% [-15.10%, 34.22%] | $47.98 | 0.960× | 44.56% | $6.46 | 65 (50 unfilled) | 24.78% [-5.86%, 58.78%] | $120.67 |
| series | vcl | 176 | 176 | 0.0608 | 20.30% [0.74%, 41.46%] | $402.85 | 8.057× | 39.77% | $50.83 | 84 (92 unfilled) | 22.66% [-6.64%, 53.09%] | $95.11 |
| series | gc | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | t3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | collegiate | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | offseason | 21 | 21 | 0.0427 | -11.24% [-60.66%, 43.01%] | $42.78 | 0.856× | 29.96% | $4.67 | 15 (6 unfilled) | -43.92% [-86.70%, 8.31%] | $34.72 |
| series | international=1 | 12 | 12 | 0.0306 | 38.18% [-40.27%, 122.51%] | $57.08 | 1.142× | 10.90% | $4.92 | 12 (0 unfilled) | 38.18% [-40.27%, 122.51%] | $57.08 |
| series | international=0 | 300 | 300 | 0.0562 | 12.36% [-2.43%, 29.05%] | $312.63 | 6.253× | 55.48% | $54.32 | 152 (148 unfilled) | 15.75% [-3.98%, 37.22%] | $136.04 |
| map | all | 493 | 262 | 0.0402 | -3.73% [-12.52%, 5.23%] | $29.53 | 0.591× | 67.03% | $8.01 | 72 (421 unfilled) | 4.42% [-15.57%, 27.34%] | $47.42 |
| map | vct | 199 | 103 | 0.0343 | -1.21% [-13.95%, 12.16%] | $43.08 | 0.862× | 37.46% | $5.47 | 34 (165 unfilled) | 26.55% [-4.48%, 59.92%] | $61.50 |
| map | vcl | 253 | 139 | 0.0447 | -6.16% [-18.52%, 6.13%] | $30.96 | 0.619× | 58.28% | $6.73 | 34 (219 unfilled) | -21.90% [-48.30%, 6.15%] | $36.17 |
| map | gc | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | t3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | collegiate | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | offseason | 41 | 20 | 0.0412 | -0.95% [-32.70%, 27.97%] | $52.85 | 1.057× | 13.08% | $4.05 | 4 (37 unfilled) | 40.32% [13.38%, 92.31%] | $53.26 |
| map | international=1 | 28 | 13 | 0.0311 | -17.31% [-48.85%, 12.57%] | $37.48 | 0.750× | 25.04% | $2.29 | 10 (18 unfilled) | 2.53% [-38.68%, 45.73%] | $48.75 |
| map | international=0 | 465 | 249 | 0.0408 | -2.91% [-12.22%, 5.95%] | $39.57 | 0.791× | 55.90% | $8.01 | 62 (403 unfilled) | 4.72% [-19.91%, 31.38%] | $48.75 |
| series+map | all | 805 | 365 | 0.0460 | 2.91% [-7.32%, 12.41%] | $100.49 | 2.010× | 62.98% | $18.38 | 236 (569 unfilled) | 13.45% [-2.55%, 29.35%] | $106.41 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-02 | 48 | 0.700298 | — | 0.690786 | -0.33% (33), $49.91 | — | 9 (24 unfilled) | -1.52% [-100.00%, 53.63%] | $50.52 | — | — | — |
| map | 2026-03 | 56 | 0.602878 | — | 0.565065 | -8.66% (30), $42.68 | — | 10 (20 unfilled) | -14.58% [-73.52%, 41.60%] | $53.58 | — | — | — |
| map | 2026-04 | 352 | 0.639411 | 0.693277 | 0.690793 | 56.02% (240), $5454.71 | -4.42% (182), $47.77 | 25 (215 unfilled) | 200.11% [4.36%, 454.64%] | $230.50 | 25 (157 unfilled) | -5.33% [-28.60%, 16.00%] | $50.18 |
| map | 2026-05 | 377 | 0.688223 | 0.687082 | 0.687018 | 4.32% (205), $67.35 | 4.78% (186), $69.26 | 28 (177 unfilled) | 41.04% [-4.44%, 87.63%] | $66.47 | 26 (160 unfilled) | 29.05% [-16.98%, 72.34%] | $58.55 |
| map | 2026-06 | 216 | 0.656799 | 0.645160 | 0.620377 | -15.93% (139), $20.34 | -15.38% (125), $22.25 | 23 (116 unfilled) | -22.14% [-56.38%, 13.75%] | $37.76 | 21 (104 unfilled) | -14.73% [-49.02%, 22.33%] | $40.54 |
| series | 2026-01 | 21 | 0.631734 | — | 0.661069 | 4.35% (17), $55.03 | — | 9 (8 unfilled) | -20.27% [-77.53%, 40.89%] | $46.20 | — | — | — |
| series | 2026-02 | 51 | 0.651868 | — | 0.694525 | 26.91% (42), $104.54 | — | 31 (11 unfilled) | 38.73% [-14.29%, 103.12%] | $107.87 | — | — | — |
| series | 2026-03 | 64 | 0.594068 | — | 0.565917 | 3.56% (49), $43.82 | — | 39 (10 unfilled) | 16.22% [-14.34%, 47.26%] | $66.69 | — | — | — |
| series | 2026-04 | 221 | 0.618228 | 0.614779 | 0.627690 | 11.25% (167), $87.77 | 16.57% (146), $290.96 | 73 (94 unfilled) | 49.13% [10.11%, 91.86%] | $249.05 | 64 (82 unfilled) | 36.60% [4.58%, 71.15%] | $158.46 |
| series | 2026-05 | 199 | 0.666706 | 0.658801 | 0.663719 | 4.82% (137), $49.50 | 8.94% (99), $52.08 | 90 (47 unfilled) | -7.69% [-32.21%, 20.06%] | $28.84 | 65 (34 unfilled) | -7.75% [-37.08%, 26.09%] | $32.43 |
| series | 2026-06 | 121 | 0.611232 | 0.595946 | 0.598199 | 3.52% (89), $61.27 | 12.93% (67), $58.06 | 48 (41 unfilled) | 21.61% [-10.19%, 56.31%] | $114.15 | 35 (32 unfilled) | 29.10% [-10.55%, 72.15%] | $66.84 |

### player_round_glicko_rookie_tier_revert_perf_rating+none: Kalshi comparison and returns

none

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 677 | 0.622581 | 0.633240 | -0.010659 [-0.034278, 0.014381] | no |
| series | vct | 278 | 0.617874 | 0.634755 | -0.016881 [-0.048694, 0.011911] | no |
| series | vcl | 340 | 0.615723 | 0.619968 | -0.004245 [-0.045096, 0.037620] | no |
| series | gc | 0 | — | — | — | — |
| series | t3 | 0 | — | — | — | — |
| series | collegiate | 0 | — | — | — | — |
| series | offseason | 59 | 0.684286 | 0.702587 | -0.018301 [-0.077101, 0.036317] | no |
| series | international=1 | 41 | 0.614481 | 0.653397 | -0.038915 [-0.082381, 0.001995] | no |
| series | international=0 | 636 | 0.623104 | 0.631941 | -0.008837 [-0.035171, 0.016837] | no |
| map | all | 1049 | 0.656792 | 0.668225 | -0.011432 [-0.033746, 0.006996] | no |
| map | vct | 461 | 0.655037 | 0.665762 | -0.010725 [-0.030935, 0.006607] | no |
| map | vcl | 490 | 0.651838 | 0.668365 | -0.016527 [-0.059658, 0.019158] | no |
| map | gc | 0 | — | — | — | — |
| map | t3 | 0 | — | — | — | — |
| map | collegiate | 0 | — | — | — | — |
| map | offseason | 98 | 0.689821 | 0.679111 | 0.010710 [-0.025196, 0.044230] | no |
| map | international=1 | 59 | 0.658482 | 0.649653 | 0.008830 [-0.016035, 0.032809] | no |
| map | international=0 | 990 | 0.656692 | 0.669332 | -0.012640 [-0.034651, 0.007371] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 500 | 500 | 0.0945 | 13.05% [0.08%, 26.07%] | $1247.73 | 24.955× | 71.91% | $246.88 | 288 (212 unfilled) | 19.94% [3.75%, 37.52%] | $698.18 |
| series | vct | 194 | 194 | 0.0764 | 10.83% [-8.16%, 31.31%] | $115.51 | 2.310× | 70.62% | $9.20 | 119 (75 unfilled) | 21.40% [-4.89%, 48.02%] | $243.66 |
| series | vcl | 266 | 266 | 0.1103 | 14.50% [-2.23%, 32.45%] | $602.10 | 12.042× | 53.36% | $101.11 | 137 (129 unfilled) | 22.74% [-1.49%, 50.19%] | $182.79 |
| series | gc | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | t3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | collegiate | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | offseason | 40 | 40 | 0.0769 | 14.10% [-25.65%, 56.39%] | $76.51 | 1.530× | 47.88% | $9.30 | 32 (8 unfilled) | 2.62% [-41.95%, 47.74%] | $53.21 |
| series | international=1 | 27 | 27 | 0.0407 | 26.51% [-21.47%, 76.49%] | $87.55 | 1.751× | 16.14% | $6.97 | 26 (1 unfilled) | 25.55% [-19.79%, 74.83%] | $87.55 |
| series | international=0 | 473 | 473 | 0.0976 | 12.28% [0.08%, 25.15%] | $1008.74 | 20.175× | 71.91% | $240.40 | 262 (211 unfilled) | 19.39% [1.95%, 38.48%] | $414.08 |
| map | all | 666 | 360 | 0.0725 | 20.69% [4.47%, 41.87%] | $7961.60 | 159.232× | 38.49% | $245.53 | 105 (561 unfilled) | 57.21% [6.02%, 126.06%] | $291.11 |
| map | vct | 260 | 140 | 0.0568 | 14.08% [-3.44%, 38.93%] | $256.25 | 5.125× | 28.51% | $19.50 | 55 (205 unfilled) | 61.51% [0.10%, 158.79%] | $134.77 |
| map | vcl | 353 | 192 | 0.0878 | 28.10% [1.00%, 62.22%] | $1827.47 | 36.549× | 54.87% | $245.53 | 46 (307 unfilled) | 48.73% [-27.83%, 156.97%] | $126.16 |
| map | gc | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | t3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | collegiate | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | offseason | 53 | 28 | 0.0475 | 3.63% [-31.00%, 41.69%] | $50.44 | 1.009× | 21.63% | $3.12 | 4 (49 unfilled) | 95.88% [13.38%, 262.84%] | $59.24 |
| map | international=1 | 32 | 18 | 0.0368 | -5.00% [-29.61%, 20.35%] | $44.81 | 0.896× | 14.84% | $2.30 | 13 (19 unfilled) | 18.38% [-13.71%, 65.38%] | $52.91 |
| map | international=0 | 634 | 342 | 0.0743 | 21.98% [4.18%, 42.31%] | $7882.73 | 157.655× | 35.28% | $245.53 | 92 (542 unfilled) | 62.64% [4.15%, 143.64%] | $276.18 |
| series+map | all | 1166 | 530 | 0.0819 | 17.41% [4.71%, 30.63%] | $5145.34 | 102.907× | 52.50% | $247.91 | 393 (773 unfilled) | 29.90% [10.58%, 51.06%] | $483.98 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-09-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 240 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-01 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 21 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | map | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-03 | series | 72 | 1.000000 | 0.000000 | unfitted |
| 2026-03 | map | 48 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | series | 136 | 1.267176 | 0.750920 | fitted |
| 2026-04 | map | 104 | 1.627590 | 0.713957 | fitted |
| 2026-05 | series | 357 | 1.062964 | 0.648336 | fitted |
| 2026-05 | map | 456 | 1.153494 | 0.991215 | fitted |
| 2026-06 | series | 556 | 1.050288 | 0.721129 | fitted |
| 2026-06 | map | 833 | 0.983301 | 0.823368 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 541 | 0.619876 | 0.634347 | -0.014470 [-0.031535, 0.002690] | no |
| series | vct | 201 | 0.630796 | 0.644147 | -0.013351 [-0.034647, 0.008530] | no |
| series | vcl | 291 | 0.603617 | 0.621829 | -0.018212 [-0.045786, 0.012158] | no |
| series | gc | 0 | — | — | — | — |
| series | t3 | 0 | — | — | — | — |
| series | collegiate | 0 | — | — | — | — |
| series | offseason | 49 | 0.671644 | 0.668490 | 0.003154 [-0.038413, 0.038545] | no |
| series | international=1 | 24 | 0.648347 | 0.682705 | -0.034359 [-0.076455, 0.006536] | no |
| series | international=0 | 517 | 0.618555 | 0.632102 | -0.013547 [-0.030762, 0.006195] | no |
| map | all | 945 | 0.673082 | 0.673192 | -0.000110 [-0.013124, 0.012958] | no |
| map | vct | 392 | 0.664106 | 0.667249 | -0.003144 [-0.019709, 0.013847] | no |
| map | vcl | 456 | 0.676307 | 0.676303 | 0.000004 [-0.022261, 0.021009] | no |
| map | gc | 0 | — | — | — | — |
| map | t3 | 0 | — | — | — | — |
| map | collegiate | 0 | — | — | — | — |
| map | offseason | 97 | 0.694197 | 0.682581 | 0.011616 [-0.019833, 0.046336] | no |
| map | international=1 | 50 | 0.656274 | 0.651359 | 0.004916 [-0.016085, 0.024702] | no |
| map | international=0 | 895 | 0.674021 | 0.674412 | -0.000391 [-0.014140, 0.012080] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 333 | 333 | 0.0563 | 16.36% [1.93%, 31.47%] | $1721.04 | 34.421× | 45.80% | $246.88 | 175 (158 unfilled) | 20.19% [1.86%, 40.27%] | $615.60 |
| series | vct | 117 | 117 | 0.0420 | 14.94% [-9.28%, 39.89%] | $141.39 | 2.828× | 49.06% | $11.26 | 68 (49 unfilled) | 25.53% [-6.17%, 58.58%] | $173.05 |
| series | vcl | 188 | 188 | 0.0679 | 20.71% [2.64%, 40.61%] | $698.44 | 13.969× | 35.70% | $88.23 | 87 (101 unfilled) | 28.44% [1.73%, 57.46%] | $222.37 |
| series | gc | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | t3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | collegiate | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | offseason | 28 | 28 | 0.0382 | -6.82% [-50.82%, 40.46%] | $56.36 | 1.127× | 17.78% | $5.94 | 20 (8 unfilled) | -33.55% [-76.55%, 13.37%] | $45.06 |
| series | international=1 | 12 | 12 | 0.0363 | 55.56% [-17.15%, 139.25%] | $80.26 | 1.605× | 6.12% | $6.39 | 12 (0 unfilled) | 55.56% [-17.15%, 139.25%] | $80.26 |
| series | international=0 | 321 | 321 | 0.0571 | 14.89% [0.89%, 29.96%] | $1433.93 | 28.679× | 49.47% | $234.23 | 163 (158 unfilled) | 17.59% [-1.80%, 37.64%] | $390.70 |
| map | all | 582 | 306 | 0.0526 | 17.83% [-0.07%, 40.59%] | $188.33 | 3.767× | 66.69% | $34.32 | 62 (520 unfilled) | 98.26% [16.40%, 212.76%] | $159.11 |
| map | vct | 220 | 114 | 0.0502 | 14.75% [-4.91%, 42.55%] | $68.62 | 1.372× | 44.21% | $5.56 | 28 (192 unfilled) | 125.33% [18.66%, 326.93%] | $108.49 |
| map | vcl | 313 | 167 | 0.0557 | 25.53% [-3.70%, 65.62%] | $157.72 | 3.154× | 62.43% | $31.79 | 31 (282 unfilled) | 79.67% [-30.16%, 233.51%] | $69.79 |
| map | gc | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | t3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | collegiate | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | offseason | 49 | 25 | 0.0438 | -17.46% [-43.77%, 11.60%] | $36.89 | 0.738× | 26.38% | $4.26 | 3 (46 unfilled) | 39.52% [13.38%, 92.31%] | $52.97 |
| map | international=1 | 21 | 10 | 0.0364 | 3.08% [-29.44%, 34.82%] | $49.22 | 0.984× | 7.46% | $2.51 | 7 (14 unfilled) | 24.65% [-17.02%, 64.55%] | $51.49 |
| map | international=0 | 561 | 296 | 0.0532 | 18.39% [-0.11%, 40.93%] | $191.00 | 3.820× | 66.21% | $34.32 | 55 (506 unfilled) | 107.63% [13.03%, 240.82%] | $152.27 |
| series+map | all | 915 | 401 | 0.0540 | 17.30% [3.42%, 32.73%] | $1995.47 | 39.909× | 45.67% | $242.03 | 237 (678 unfilled) | 40.57% [12.99%, 73.49%] | $537.96 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-02 | 48 | 0.697147 | — | 0.690786 | 7.78% (39), $48.89 | — | 15 (24 unfilled) | 20.10% [-48.76%, 67.15%] | $50.19 | — | — | — |
| map | 2026-03 | 56 | 0.578315 | — | 0.565065 | -7.16% (40), $35.94 | — | 15 (25 unfilled) | -11.94% [-60.19%, 35.68%] | $44.71 | — | — | — |
| map | 2026-04 | 352 | 0.635433 | 0.675820 | 0.690793 | 59.73% (228), $7545.06 | 44.80% (242), $275.50 | 28 (200 unfilled) | 188.63% [7.04%, 428.45%] | $259.30 | 24 (218 unfilled) | 229.09% [15.20%, 497.82%] | $147.85 |
| map | 2026-05 | 377 | 0.682959 | 0.684864 | 0.687018 | 7.96% (218), $98.84 | 5.62% (213), $67.72 | 26 (192 unfilled) | 30.62% [-17.56%, 81.78%] | $76.04 | 21 (192 unfilled) | 41.51% [-9.88%, 92.45%] | $72.11 |
| map | 2026-06 | 216 | 0.657308 | 0.648055 | 0.620377 | -11.25% (141), $22.10 | -12.56% (127), $24.52 | 21 (120 unfilled) | -11.04% [-46.02%, 25.18%] | $39.32 | 17 (110 unfilled) | -14.55% [-54.70%, 27.55%] | $37.59 |
| series | 2026-01 | 21 | 0.606191 | — | 0.661069 | 7.89% (15), $62.09 | — | 9 (6 unfilled) | -6.29% [-76.58%, 69.25%] | $54.05 | — | — | — |
| series | 2026-02 | 51 | 0.661244 | — | 0.694525 | 33.73% (40), $98.25 | — | 29 (11 unfilled) | 43.74% [-10.97%, 110.44%] | $88.81 | — | — | — |
| series | 2026-03 | 64 | 0.584054 | — | 0.565917 | -5.56% (48), $28.95 | — | 35 (13 unfilled) | 2.48% [-28.66%, 33.54%] | $38.29 | — | — | — |
| series | 2026-04 | 221 | 0.618019 | 0.613930 | 0.627690 | 20.86% (161), $339.34 | 20.62% (138), $300.53 | 69 (92 unfilled) | 50.16% [6.85%, 98.58%] | $212.84 | 60 (78 unfilled) | 41.57% [7.94%, 78.05%] | $162.77 |
| series | 2026-05 | 199 | 0.635029 | 0.638277 | 0.663719 | 17.93% (140), $231.59 | 21.29% (117), $315.56 | 92 (48 unfilled) | 6.14% [-20.06%, 34.13%] | $65.42 | 73 (44 unfilled) | 7.81% [-19.02%, 39.19%] | $117.43 |
| series | 2026-06 | 121 | 0.617371 | 0.600477 | 0.598199 | -5.70% (96), $53.60 | 1.46% (78), $59.53 | 54 (42 unfilled) | 7.69% [-23.29%, 41.59%] | $106.67 | 42 (36 unfilled) | 11.30% [-22.27%, 47.31%] | $88.43 |

### player_round_glicko_rookie_tier_revert_perf_kda+none: Kalshi comparison and returns

none

#### Log loss vs Kalshi

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 677 | 0.621374 | 0.633240 | -0.011866 [-0.034993, 0.012721] | no |
| series | vct | 278 | 0.617598 | 0.634755 | -0.017157 [-0.048467, 0.011503] | no |
| series | vcl | 340 | 0.613874 | 0.619968 | -0.006094 [-0.046104, 0.035420] | no |
| series | gc | 0 | — | — | — | — |
| series | t3 | 0 | — | — | — | — |
| series | collegiate | 0 | — | — | — | — |
| series | offseason | 59 | 0.682384 | 0.702587 | -0.020202 [-0.076605, 0.034610] | no |
| series | international=1 | 41 | 0.615983 | 0.653397 | -0.037414 [-0.083653, 0.005413] | no |
| series | international=0 | 636 | 0.621721 | 0.631941 | -0.010219 [-0.035910, 0.015362] | no |
| map | all | 1049 | 0.655991 | 0.668225 | -0.012234 [-0.034648, 0.006219] | no |
| map | vct | 461 | 0.655488 | 0.665762 | -0.010274 [-0.030513, 0.006979] | no |
| map | vcl | 490 | 0.650148 | 0.668365 | -0.018216 [-0.061294, 0.017213] | no |
| map | gc | 0 | — | — | — | — |
| map | t3 | 0 | — | — | — | — |
| map | collegiate | 0 | — | — | — | — |
| map | offseason | 98 | 0.687571 | 0.679111 | 0.008460 [-0.025512, 0.040647] | no |
| map | international=1 | 59 | 0.661062 | 0.649653 | 0.011410 [-0.012520, 0.034417] | no |
| map | international=0 | 990 | 0.655689 | 0.669332 | -0.013643 [-0.035478, 0.006502] | no |

#### Full-Kelly returns

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 500 | 500 | 0.0928 | 13.60% [1.18%, 26.30%] | $1322.94 | 26.459× | 70.47% | $246.88 | 287 (213 unfilled) | 19.95% [3.44%, 37.25%] | $644.08 |
| series | vct | 196 | 196 | 0.0758 | 10.14% [-8.61%, 30.45%] | $132.88 | 2.658× | 70.63% | $10.58 | 119 (77 unfilled) | 19.33% [-5.30%, 45.44%] | $256.32 |
| series | vcl | 265 | 265 | 0.1078 | 15.67% [-0.92%, 33.69%] | $472.95 | 9.459× | 53.46% | $84.49 | 138 (127 unfilled) | 22.80% [-1.93%, 48.19%] | $173.96 |
| series | gc | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | t3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | collegiate | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | offseason | 39 | 39 | 0.0753 | 16.92% [-23.07%, 61.88%] | $81.93 | 1.639× | 42.68% | $9.40 | 30 (9 unfilled) | 9.35% [-36.74%, 57.05%] | $58.86 |
| series | international=1 | 27 | 27 | 0.0445 | 29.29% [-15.59%, 79.58%] | $87.33 | 1.747× | 20.15% | $6.95 | 27 (0 unfilled) | 29.29% [-15.59%, 79.58%] | $87.77 |
| series | international=0 | 473 | 473 | 0.0955 | 12.71% [-0.70%, 25.84%] | $1029.36 | 20.587× | 70.47% | $240.40 | 260 (213 unfilled) | 18.98% [1.61%, 37.94%] | $381.63 |
| map | all | 659 | 354 | 0.0708 | 21.06% [4.11%, 41.10%] | $8139.37 | 162.787× | 40.58% | $245.53 | 98 (561 unfilled) | 63.63% [7.64%, 131.34%] | $297.96 |
| map | vct | 260 | 138 | 0.0560 | 12.39% [-5.49%, 35.14%] | $243.55 | 4.871× | 33.00% | $17.66 | 50 (210 unfilled) | 70.75% [3.85%, 178.04%] | $131.80 |
| map | vcl | 347 | 189 | 0.0859 | 29.84% [1.67%, 66.06%] | $1827.79 | 36.556× | 54.02% | $245.53 | 44 (303 unfilled) | 52.66% [-27.16%, 167.38%] | $125.65 |
| map | gc | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | t3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | collegiate | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | offseason | 52 | 27 | 0.0443 | 5.62% [-28.75%, 42.61%] | $52.43 | 1.049× | 17.08% | $3.51 | 4 (48 unfilled) | 95.88% [13.38%, 262.84%] | $59.51 |
| map | international=1 | 32 | 18 | 0.0362 | -16.45% [-46.81%, 14.85%] | $42.49 | 0.850× | 19.35% | $2.88 | 11 (21 unfilled) | 26.07% [-11.94%, 68.72%] | $52.35 |
| map | international=0 | 627 | 336 | 0.0726 | 22.97% [5.34%, 44.20%] | $8618.33 | 172.367× | 35.75% | $245.53 | 87 (540 unfilled) | 68.34% [4.60%, 146.66%] | $280.31 |
| series+map | all | 1159 | 530 | 0.0803 | 17.84% [6.33%, 31.63%] | $6737.12 | 134.742× | 51.44% | $247.91 | 385 (774 unfilled) | 31.07% [11.00%, 54.37%] | $543.12 |

#### Monthly market blend fits

UTC monthly fits use earlier rows of the same kind from 2025-09-01, excluding holdout; minimum 100 rows. logit(p_blend) = a·logit(mid) + b·(logit(p_model) − logit(mid)); inputs clipped to [0.01, 0.99], no intercept, ridge 1e-6. Unfitted rows use mid unchanged; excluded from blended tables: 240 rows. Rating parameters remain selected on the tuning window.

| Month | Kind | n | a | b | Status |
|---|---|---:|---:|---:|---|
| 2026-01 | series | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | series | 21 | 1.000000 | 0.000000 | unfitted |
| 2026-02 | map | 0 | 1.000000 | 0.000000 | unfitted |
| 2026-03 | series | 72 | 1.000000 | 0.000000 | unfitted |
| 2026-03 | map | 48 | 1.000000 | 0.000000 | unfitted |
| 2026-04 | series | 136 | 1.282910 | 0.773480 | fitted |
| 2026-04 | map | 104 | 1.603656 | 0.677463 | fitted |
| 2026-05 | series | 357 | 1.074872 | 0.666986 | fitted |
| 2026-05 | map | 456 | 1.160706 | 0.996846 | fitted |
| 2026-06 | series | 556 | 1.056557 | 0.731526 | fitted |
| 2026-06 | map | 833 | 0.996457 | 0.842484 | fitted |

#### Log loss vs Kalshi (blended)

| Kind | Slice | Rows | Model log loss | Kalshi log loss | Difference [95% interval] | Significant |
|---|---|---:|---:|---:|---|---|
| series | all | 541 | 0.619482 | 0.634347 | -0.014865 [-0.031928, 0.002876] | no |
| series | vct | 201 | 0.630931 | 0.644147 | -0.013216 [-0.034787, 0.009062] | no |
| series | vcl | 291 | 0.602781 | 0.621829 | -0.019048 [-0.047277, 0.011856] | no |
| series | gc | 0 | — | — | — | — |
| series | t3 | 0 | — | — | — | — |
| series | collegiate | 0 | — | — | — | — |
| series | offseason | 49 | 0.671704 | 0.668490 | 0.003214 [-0.036797, 0.038268] | no |
| series | international=1 | 24 | 0.647241 | 0.682705 | -0.035464 [-0.080556, 0.007815] | no |
| series | international=0 | 517 | 0.618194 | 0.632102 | -0.013908 [-0.031483, 0.005894] | no |
| map | all | 945 | 0.672464 | 0.673192 | -0.000728 [-0.013141, 0.011996] | no |
| map | vct | 392 | 0.663982 | 0.667249 | -0.003268 [-0.019067, 0.013142] | no |
| map | vcl | 456 | 0.675584 | 0.676303 | -0.000719 [-0.021766, 0.020072] | no |
| map | gc | 0 | — | — | — | — |
| map | t3 | 0 | — | — | — | — |
| map | collegiate | 0 | — | — | — | — |
| map | offseason | 97 | 0.692075 | 0.682581 | 0.009494 [-0.020706, 0.042281] | no |
| map | international=1 | 50 | 0.658611 | 0.651359 | 0.007253 [-0.013363, 0.027401] | no |
| map | international=0 | 895 | 0.673238 | 0.674412 | -0.001174 [-0.014366, 0.011013] | no |

#### Full-Kelly returns (blended)

| Kind | Slice | Bets | Matches | Mean edge | Flat ROI [95% interval] | Kelly, LoL caps ($50 start) | Multiple | Max drawdown | Largest stake | Bets filled | Flat ROI depth-capped [95% interval] | Kelly depth-capped final |
|---|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|
| series | all | 332 | 332 | 0.0560 | 17.59% [3.87%, 32.71%] | $1572.97 | 31.459× | 42.62% | $225.35 | 171 (161 unfilled) | 22.97% [4.03%, 43.69%] | $485.65 |
| series | vct | 116 | 116 | 0.0424 | 18.21% [-5.32%, 43.61%] | $114.99 | 2.300× | 50.11% | $9.16 | 68 (48 unfilled) | 29.39% [-1.16%, 63.34%] | $149.18 |
| series | vcl | 191 | 191 | 0.0663 | 20.30% [1.59%, 40.28%] | $730.49 | 14.610× | 35.71% | $92.84 | 85 (106 unfilled) | 28.26% [1.03%, 57.61%] | $178.77 |
| series | gc | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | t3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | collegiate | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| series | offseason | 25 | 25 | 0.0403 | -5.86% [-53.48%, 44.10%] | $56.57 | 1.131× | 13.83% | $5.93 | 18 (7 unfilled) | -26.06% [-73.62%, 26.93%] | $45.08 |
| series | international=1 | 13 | 13 | 0.0334 | 43.49% [-27.47%, 123.73%] | $81.81 | 1.636× | 7.01% | $6.51 | 13 (0 unfilled) | 43.49% [-27.47%, 123.73%] | $81.81 |
| series | international=0 | 319 | 319 | 0.0569 | 16.54% [2.73%, 32.22%] | $1198.28 | 23.966× | 49.76% | $196.85 | 158 (161 unfilled) | 21.28% [1.64%, 42.26%] | $285.64 |
| map | all | 572 | 297 | 0.0500 | 18.12% [-1.26%, 41.58%] | $172.73 | 3.455× | 65.99% | $27.24 | 64 (508 unfilled) | 92.33% [11.27%, 202.71%] | $136.60 |
| map | vct | 222 | 113 | 0.0467 | 14.59% [-4.96%, 43.00%] | $75.73 | 1.515× | 42.06% | $5.70 | 28 (194 unfilled) | 125.33% [18.66%, 326.93%] | $99.97 |
| map | vcl | 305 | 162 | 0.0535 | 25.47% [-4.30%, 67.38%] | $126.43 | 2.529× | 63.86% | $25.83 | 33 (272 unfilled) | 69.31% [-32.53%, 223.40%] | $64.79 |
| map | gc | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | t3 | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | collegiate | 0 | 0 | — | — | $50.00 | 1.000× | 0.00% | $0.00 | 0 (0 unfilled) | — | $50.00 |
| map | offseason | 45 | 22 | 0.0433 | -14.30% [-42.70%, 17.31%] | $39.48 | 0.790× | 22.52% | $4.24 | 3 (42 unfilled) | 39.52% [13.38%, 92.31%] | $52.98 |
| map | international=1 | 24 | 11 | 0.0328 | -9.92% [-42.63%, 21.30%] | $47.61 | 0.952× | 9.07% | $2.43 | 7 (17 unfilled) | 24.65% [-17.02%, 64.55%] | $51.51 |
| map | international=0 | 548 | 286 | 0.0508 | 19.35% [1.13%, 43.56%] | $181.12 | 3.622× | 64.34% | $27.24 | 57 (491 unfilled) | 100.64% [9.48%, 215.72%] | $130.42 |
| series+map | all | 904 | 396 | 0.0522 | 17.93% [3.86%, 34.14%] | $1405.56 | 28.111× | 52.96% | $197.49 | 235 (669 unfilled) | 41.82% [14.73%, 75.46%] | $404.73 |

#### Monthly breakdown

All metrics use identical linked rows within each kind/month. Unfitted blend months show —; counts include all rows.

| Kind | Month | Rows | Model log loss | Blended log loss | Kalshi log loss | Raw flat ROI (bets), unlimited Kelly final | Blended flat ROI (bets), unlimited Kelly final | Raw bets filled | Raw Flat ROI depth-capped [95% interval] | Raw Kelly depth-capped final | Blended bets filled | Blended Flat ROI depth-capped [95% interval] | Blended Kelly depth-capped final |
|---|---|---:|---:|---:|---:|---|---|---:|---|---:|---:|---|---:|
| map | 2026-02 | 48 | 0.698252 | — | 0.690786 | 5.56% (38), $47.77 | — | 14 (24 unfilled) | 14.94% [-49.57%, 63.44%] | $49.21 | — | — | — |
| map | 2026-03 | 56 | 0.579719 | — | 0.565065 | -7.16% (40), $36.07 | — | 15 (25 unfilled) | -11.94% [-60.19%, 35.68%] | $44.01 | — | — | — |
| map | 2026-04 | 352 | 0.635796 | 0.676468 | 0.690793 | 58.67% (225), $7689.25 | 45.97% (236), $224.57 | 28 (197 unfilled) | 188.63% [7.04%, 428.45%] | $254.76 | 25 (211 unfilled) | 215.94% [15.49%, 473.82%] | $126.62 |
| map | 2026-05 | 377 | 0.681495 | 0.683578 | 0.687018 | 10.90% (218), $115.27 | 6.89% (210), $85.41 | 23 (195 unfilled) | 47.65% [-4.53%, 102.05%] | $80.55 | 23 (187 unfilled) | 35.38% [-12.09%, 83.26%] | $72.41 |
| map | 2026-06 | 216 | 0.654770 | 0.646540 | 0.620377 | -11.71% (138), $19.96 | -14.78% (126), $21.90 | 18 (120 unfilled) | -11.51% [-51.57%, 31.85%] | $38.60 | 16 (110 unfilled) | -17.01% [-61.40%, 29.95%] | $37.45 |
| series | 2026-01 | 21 | 0.609608 | — | 0.661069 | 18.69% (16), $61.73 | — | 9 (7 unfilled) | -6.29% [-76.58%, 69.25%] | $52.71 | — | — | — |
| series | 2026-02 | 51 | 0.660801 | — | 0.694525 | 33.23% (38), $97.85 | — | 27 (11 unfilled) | 49.39% [-8.56%, 115.58%] | $87.08 | — | — | — |
| series | 2026-03 | 64 | 0.581920 | — | 0.565917 | -3.40% (49), $28.67 | — | 36 (13 unfilled) | 5.20% [-26.20%, 36.57%] | $35.65 | — | — | — |
| series | 2026-04 | 221 | 0.616128 | 0.613476 | 0.627690 | 18.80% (159), $306.27 | 20.18% (142), $281.17 | 67 (92 unfilled) | 45.17% [1.74%, 91.15%] | $196.92 | 59 (83 unfilled) | 38.91% [4.70%, 76.97%] | $134.18 |
| series | 2026-05 | 199 | 0.636247 | 0.639276 | 0.663719 | 20.28% (142), $273.87 | 25.54% (113), $283.09 | 93 (49 unfilled) | 8.98% [-15.89%, 35.80%] | $76.37 | 71 (42 unfilled) | 14.39% [-13.97%, 45.76%] | $107.97 |
| series | 2026-06 | 121 | 0.612785 | 0.597897 | 0.598199 | -4.86% (96), $50.65 | 1.20% (77), $60.79 | 55 (41 unfilled) | 7.20% [-25.17%, 42.21%] | $97.35 | 41 (36 unfilled) | 14.97% [-22.21%, 54.43%] | $80.27 |

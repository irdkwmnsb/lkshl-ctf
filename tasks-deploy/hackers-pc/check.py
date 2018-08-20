def check(attempt, context):
    if attempt.answer == flags[attempt.participant.id % len(flags)]:
        return Checked(True)
    if attempt.answer in flags:
        return CheckedPlagiarist(False, flags.index(attempt.answer))
    return Checked(False)
flags = ['LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_L0h6AfyRtd}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_auR2hDr5k4}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_srT5jyOSNQ}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_dLRVhTRswA}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_a2mOFBw9xb}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_4YFOei2FnY}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_cdVeTAjxeI}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_vVytoy3Dna}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_OErcfKtLTM}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_YoIqY22lSF}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_DUsx34wAL3}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_1wX8ZNllmQ}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_gOQsHL1nwO}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_bDJM1bxKAR}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_u6UdvRX1hF}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_XxxDF6WXIh}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_0kMJ1mg2PL}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_aHYFpWGwDd}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_MgOFfgQiN4}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_pFnvjX4fVv}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_sXMhdzo99e}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_GitwjR0VOg}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_QLahPCVSjc}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_HPGc34n60t}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_pw0xx8zcoD}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_jdgt9UX8Vl}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_ItQZHQ5aVO}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_qv5wGpIMt4}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_OakwkUi8uY}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_3xuv5QxR7S}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_SaOHbntPjq}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_qrboxJM9jZ}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_FvSFEO7eMl}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_kDrGY6xT5N}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_xTCTekIowy}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_NYavs0IRqV}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_k3MpVs6BPv}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_FTRFBYAHwo}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_RyPU6mVJhW}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_dNv1vRn82n}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_iwAgDSGPVW}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_ZlJXX9Z4vF}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_GSYLhElf5A}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_PC819EPEoS}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_DM8cBJWTpd}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_6r4iHTUVis}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_deGgQker8i}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_O5gtlU11yZ}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_VhWhVwHfvP}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_iyAyiBJ1IU}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_0bKPsSyph5}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_QFj1zxOLUS}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_mfSvizpOAZ}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_WtTQGylJVD}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_C8K7WgXFgc}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_XaaiPessbi}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_oMmFEtaovA}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_tPPo00zmlS}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_UTfPrIalNP}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_5ylhS0pxbt}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_WReYWrRP5p}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_bGf4OxOJ3x}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_ETUbFvuGFO}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_nkmp3Zr6Tk}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_vQGZ3EA0MO}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_0C0JUE4Qlh}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_OCqsFQHmgA}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_rXNvTwT2MR}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_mRWng1HXoZ}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_wUxgFf7czl}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_v0VBCujLqS}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_PRIStebu7P}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_M4CZ5SSmXQ}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_E11pk0Q8z1}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_yj3RAMHDMU}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_nLoI98MDHM}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_CExUcm0K8B}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_DVahHl501b}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_Q47sFWvYqn}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_4AAwC6hFmD}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_u2AM6RnUNY}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_VKcT0y2SWa}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_E4QQewpYgK}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_yHVFADvwhj}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_3fy3C6eBOO}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_iXBUJeGHLd}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_YCXWqyp55p}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_ugzrfUWL2T}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_AjjJ6GjeJM}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_W2t2oRudMU}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_Us0QK6oo60}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_Xfm94B2j6Z}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_OAuW0hPYkL}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_vDAHIDYR0f}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_Ad5ChidXnb}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_CkDWrlQoBw}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_euhElzBuaB}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_1Ix1FU7uGa}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_psp8nRXyHh}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_SujXYXQjZI}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_cHQbrbBS6m}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_QQsUJ6YaOo}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_HKAE9f2yqP}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_o2j5zR3FHR}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_YIOo5ALCAH}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_G2YhApCFMH}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_MfLtpvxsRd}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_xFCMZYkc0R}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_47C7dtXmAw}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_ePmX97eVOI}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_iIlGZ1eW7F}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_c6VXgUAjur}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_rgpzg1TnWj}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_vHKJOozABc}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_nhigQv4PhR}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_m9cI2Iozpn}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_RirbrashQz}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_As6TmfYckC}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_btHF9llnUd}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_bhFVNfnW0K}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_h5RYdGjaxZ}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_30Kxe2Q1fz}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_eKJdMoW92r}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_sSS8b59C6W}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_TyTMbUDZhU}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_DIeYL4Ih7C}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_p5mIpjJm5B}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_FbA0SRb861}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_dnd228vvCS}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_3wUPvEV9Cv}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_YyZZzrimpG}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_X1FEvZntP1}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_CxlVRgWu0S}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_Rwdab5IfBo}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_1vIJamerRR}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_py7K6jdVyb}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_FgGEKZh6cb}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_5BFIqtQDLC}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_9YkyuBYRNE}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_cxl1plWcyR}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_uJGDxAaabE}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_WGuUz360wD}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_CoYG7GMqpE}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_b2ooHLZJ8O}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_INpfHUqdDP}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_kZcHYxOOYo}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_rYiG4bS6qh}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_v5usmO2dVg}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_chQGwCxzEI}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_9hTubu9Lav}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_zdqNYz3QRl}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_OPYO5HHr5R}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_Hy5yTvj09G}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_fH5AsFvdy3}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_IN442s2ESb}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_T9TrVtMUdA}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_ZY2twxdzN4}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_mgWHUhR47I}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_lfrk3eWjIR}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_N2vNZLme82}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_hNxqpFWQlv}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_t59NfyDfME}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_3YQkSllxhf}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_If1MApgd6O}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_tfD8sV6QzV}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_yGRpfVM2ed}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_42s0MVWPac}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_7gDmO0py2G}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_eGQKPFW6nt}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_I5DQhysMAI}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_7c872dk1Pk}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_bSmyLwOPWo}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_SMVvuWAUQn}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_HB1pHdCkCH}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_baKeZ7p7w4}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_vvdhWo3BXv}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_YkZ9CTw9I6}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_cLn9Xezq7d}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_04MjTF4wEG}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_78OmCRnmg6}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_Dqo7wNTTY8}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_7CA5lzZeLy}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_gxbGvdBi7V}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_LSQrjirQm3}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_RWXqWIARVm}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_xsePnZx8RO}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_9XSq013DfZ}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_4j83WPvtQr}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_UKtyAw00Sj}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_k1VPzJTYgt}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_UKPm3zyy0k}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_ibxYZEKy7G}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_B7eO7NobtY}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_UzF1jg7yLG}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_LnjiuOt0hW}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_m7Flxc54mn}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_DW1Lz25jVV}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_Ck5VBASOCl}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_1ykDXgivwO}', 'LKL{Y3T_AN0TH3R_SIMPL3_D0TNET_R3VER5E_QdW3LGv9FJ}']

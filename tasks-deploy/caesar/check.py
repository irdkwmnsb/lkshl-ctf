def check(attempt, context):
    if attempt.answer == flags[attempt.participant.id % len(flags)]:
        return Checked(True)
    if attempt.answer in flags:
        return CheckedPlagiarist(False, flags.index(attempt.answer))
    return Checked(False)

    
flags = ['LKL{crypto_w4rmup_YesVN4L9}', 'LKL{crypto_w4rmup_udLGbxyV}', 'LKL{crypto_w4rmup_aGPd7oFA}', 'LKL{crypto_w4rmup_0ir81k3D}', 'LKL{crypto_w4rmup_rebcCnXt}', 'LKL{crypto_w4rmup_lMtaXSCm}', 'LKL{crypto_w4rmup_6GDFQsrm}', 'LKL{crypto_w4rmup_P8JhAshL}', 'LKL{crypto_w4rmup_zGS0AjJ8}', 'LKL{crypto_w4rmup_MGPS7FXV}', 'LKL{crypto_w4rmup_htgKfgiR}', 'LKL{crypto_w4rmup_8FfbMsZB}', 'LKL{crypto_w4rmup_79gKWm9u}', 'LKL{crypto_w4rmup_IBL3i44l}', 'LKL{crypto_w4rmup_fSFHnr95}', 'LKL{crypto_w4rmup_2658kKMF}', 'LKL{crypto_w4rmup_xUXIYB0Q}', 'LKL{crypto_w4rmup_SAVYZWA7}', 'LKL{crypto_w4rmup_nHbdknpA}', 'LKL{crypto_w4rmup_GLmfFKZe}', 'LKL{crypto_w4rmup_93miPFxR}', 'LKL{crypto_w4rmup_yZdkHlbT}', 'LKL{crypto_w4rmup_E1eIRs9l}', 'LKL{crypto_w4rmup_6FpYH6Fj}', 'LKL{crypto_w4rmup_7TiGj5VP}', 'LKL{crypto_w4rmup_JMQ7bc0s}', 'LKL{crypto_w4rmup_2PrUofZO}', 'LKL{crypto_w4rmup_MsZt0NSg}', 'LKL{crypto_w4rmup_S8GhLUcD}', 'LKL{crypto_w4rmup_Hmwwb9Yx}', 'LKL{crypto_w4rmup_RTC3M2XK}', 'LKL{crypto_w4rmup_40NMFD5X}', 'LKL{crypto_w4rmup_aTA7BSax}', 'LKL{crypto_w4rmup_STHle92F}', 'LKL{crypto_w4rmup_aDUQTVVF}', 'LKL{crypto_w4rmup_20a1QP64}', 'LKL{crypto_w4rmup_PmhxgbbF}', 'LKL{crypto_w4rmup_jvsj70uX}', 'LKL{crypto_w4rmup_QWkDLrWK}', 'LKL{crypto_w4rmup_8nNgZA7w}', 'LKL{crypto_w4rmup_OdV5hzEf}', 'LKL{crypto_w4rmup_rhMtl2Bd}', 'LKL{crypto_w4rmup_mywSOQdu}', 'LKL{crypto_w4rmup_eRInheC3}', 'LKL{crypto_w4rmup_ej35J2DT}', 'LKL{crypto_w4rmup_FIT2x8JJ}', 'LKL{crypto_w4rmup_t1vmXyJ6}', 'LKL{crypto_w4rmup_HQT9LYL4}', 'LKL{crypto_w4rmup_2OFxAGfR}', 'LKL{crypto_w4rmup_GnIbsDpy}', 'LKL{crypto_w4rmup_PnRYdJg2}', 'LKL{crypto_w4rmup_Hr0O1XC8}', 'LKL{crypto_w4rmup_ddi57Ub7}', 'LKL{crypto_w4rmup_o2EGaHNN}', 'LKL{crypto_w4rmup_ZW7HUkPa}', 'LKL{crypto_w4rmup_bB8sh87N}', 'LKL{crypto_w4rmup_nN4Zaq7A}', 'LKL{crypto_w4rmup_AS52IA7i}', 'LKL{crypto_w4rmup_RxspmsIY}', 'LKL{crypto_w4rmup_vnX8jzXy}', 'LKL{crypto_w4rmup_4Qj28CkF}', 'LKL{crypto_w4rmup_kbrYe8Ev}', 'LKL{crypto_w4rmup_xxbHXATB}', 'LKL{crypto_w4rmup_T6XNZMaF}', 'LKL{crypto_w4rmup_LPCBeUia}', 'LKL{crypto_w4rmup_inE1Hf9A}', 'LKL{crypto_w4rmup_kHXgZC95}', 'LKL{crypto_w4rmup_T2qKX5Ea}', 'LKL{crypto_w4rmup_IUGgrVhI}', 'LKL{crypto_w4rmup_Zz5LWvqi}', 'LKL{crypto_w4rmup_hJyboebI}', 'LKL{crypto_w4rmup_SzB2DgJM}', 'LKL{crypto_w4rmup_YnfhgzMt}', 'LKL{crypto_w4rmup_7AbXycC8}', 'LKL{crypto_w4rmup_l3ZyzejC}', 'LKL{crypto_w4rmup_2V1fCuAR}', 'LKL{crypto_w4rmup_GkY1CYJX}', 'LKL{crypto_w4rmup_q8F3J2gH}', 'LKL{crypto_w4rmup_mTwmSxqh}', 'LKL{crypto_w4rmup_mMM3nLfV}', 'LKL{crypto_w4rmup_POuE66LJ}', 'LKL{crypto_w4rmup_BI6118p5}', 'LKL{crypto_w4rmup_Rb81YuRf}', 'LKL{crypto_w4rmup_idBCYLUN}', 'LKL{crypto_w4rmup_DEju0psL}', 'LKL{crypto_w4rmup_WyFbVTWA}', 'LKL{crypto_w4rmup_0ZLsltbL}', 'LKL{crypto_w4rmup_RE3MEMew}', 'LKL{crypto_w4rmup_aVWWpya1}', 'LKL{crypto_w4rmup_BdtOGbmh}', 'LKL{crypto_w4rmup_PYpIJBmF}', 'LKL{crypto_w4rmup_h0bqv7pN}', 'LKL{crypto_w4rmup_AHlPJiaC}', 'LKL{crypto_w4rmup_wlmcsnvZ}', 'LKL{crypto_w4rmup_kvss81xx}', 'LKL{crypto_w4rmup_TyenyOjw}', 'LKL{crypto_w4rmup_PPeWEyGR}', 'LKL{crypto_w4rmup_5w5Qcbt4}', 'LKL{crypto_w4rmup_gSwiR0Zu}', 'LKL{crypto_w4rmup_0f7whbwX}', 'LKL{crypto_w4rmup_eq8CHMKv}', 'LKL{crypto_w4rmup_rF0xyqtz}', 'LKL{crypto_w4rmup_IuBqDwpG}', 'LKL{crypto_w4rmup_l6qoJHKf}', 'LKL{crypto_w4rmup_4B974gN6}', 'LKL{crypto_w4rmup_FuldoyoC}', 'LKL{crypto_w4rmup_dx7YucVN}', 'LKL{crypto_w4rmup_MCHQ93WG}', 'LKL{crypto_w4rmup_mghCUFhO}', 'LKL{crypto_w4rmup_iHt34E0C}', 'LKL{crypto_w4rmup_9akUgSXk}', 'LKL{crypto_w4rmup_jF6e3Mwj}', 'LKL{crypto_w4rmup_1W4AxnqL}', 'LKL{crypto_w4rmup_YyPl7y9I}', 'LKL{crypto_w4rmup_9xOuDfB4}', 'LKL{crypto_w4rmup_yg5ZiO3G}', 'LKL{crypto_w4rmup_9lYFmLJt}', 'LKL{crypto_w4rmup_XmmvApYC}', 'LKL{crypto_w4rmup_NjsqOJLC}', 'LKL{crypto_w4rmup_XeMkRgco}', 'LKL{crypto_w4rmup_kG2b29ku}', 'LKL{crypto_w4rmup_QltTLlt4}', 'LKL{crypto_w4rmup_AGDrpOGW}', 'LKL{crypto_w4rmup_uOtEPXuG}', 'LKL{crypto_w4rmup_IodYJGeH}', 'LKL{crypto_w4rmup_l7P8Wf8T}', 'LKL{crypto_w4rmup_WtnmZDVU}', 'LKL{crypto_w4rmup_RPNDV9E5}', 'LKL{crypto_w4rmup_iZVfhJy5}', 'LKL{crypto_w4rmup_qleq07wU}', 'LKL{crypto_w4rmup_RNpePkQj}', 'LKL{crypto_w4rmup_bqHXaipK}', 'LKL{crypto_w4rmup_xh0ddQMx}', 'LKL{crypto_w4rmup_HDspGfeH}', 'LKL{crypto_w4rmup_nks23yVP}', 'LKL{crypto_w4rmup_xYs4xx6l}', 'LKL{crypto_w4rmup_wbVvGKbp}', 'LKL{crypto_w4rmup_IMXjUtJe}', 'LKL{crypto_w4rmup_WI0DvgLI}', 'LKL{crypto_w4rmup_TX3YH1Wm}', 'LKL{crypto_w4rmup_mSa0lwpf}', 'LKL{crypto_w4rmup_5mz4QdNp}', 'LKL{crypto_w4rmup_LnfZxiuZ}', 'LKL{crypto_w4rmup_vCsMEtCg}', 'LKL{crypto_w4rmup_kHLyb3aH}', 'LKL{crypto_w4rmup_88qr06fC}', 'LKL{crypto_w4rmup_zR9v6CEi}', 'LKL{crypto_w4rmup_yQ3hqdtk}', 'LKL{crypto_w4rmup_8K4kQjyl}', 'LKL{crypto_w4rmup_hQMJCrCf}', 'LKL{crypto_w4rmup_V2y45Z5Z}', 'LKL{crypto_w4rmup_3KBWsmsM}', 'LKL{crypto_w4rmup_YVMZGpJf}', 'LKL{crypto_w4rmup_bomM3U1i}', 'LKL{crypto_w4rmup_RgZIW6CW}', 'LKL{crypto_w4rmup_lDgdKvNS}', 'LKL{crypto_w4rmup_VblQZXQO}', 'LKL{crypto_w4rmup_kbgxlVwh}', 'LKL{crypto_w4rmup_0MIjHfpK}', 'LKL{crypto_w4rmup_D43tmfbJ}', 'LKL{crypto_w4rmup_vtWM04yj}', 'LKL{crypto_w4rmup_cXP3nvWr}', 'LKL{crypto_w4rmup_6E1ybnjN}', 'LKL{crypto_w4rmup_4CmZIY4u}', 'LKL{crypto_w4rmup_txFDi90i}', 'LKL{crypto_w4rmup_F1tl5ps2}', 'LKL{crypto_w4rmup_QsrE73Yx}', 'LKL{crypto_w4rmup_uwxWrL9J}', 'LKL{crypto_w4rmup_C8BUElTA}', 'LKL{crypto_w4rmup_l59ffsEg}', 'LKL{crypto_w4rmup_C2IWIQoj}', 'LKL{crypto_w4rmup_q9fuhXAE}', 'LKL{crypto_w4rmup_wYTUg5Sk}', 'LKL{crypto_w4rmup_ukh3zXHn}', 'LKL{crypto_w4rmup_2pSc8ffF}', 'LKL{crypto_w4rmup_tUI2d2MH}', 'LKL{crypto_w4rmup_23CUVOaU}', 'LKL{crypto_w4rmup_TvKrb5DT}', 'LKL{crypto_w4rmup_unOgsaeY}', 'LKL{crypto_w4rmup_OeQrkykn}', 'LKL{crypto_w4rmup_Jpi6mlZV}', 'LKL{crypto_w4rmup_6qWUo8Au}', 'LKL{crypto_w4rmup_qv0ILPJh}', 'LKL{crypto_w4rmup_mr3bZ5jQ}', 'LKL{crypto_w4rmup_AvbtVqAE}', 'LKL{crypto_w4rmup_rZLywZX6}', 'LKL{crypto_w4rmup_ee2TDg12}', 'LKL{crypto_w4rmup_nqZL7WeH}', 'LKL{crypto_w4rmup_14nxd0jb}', 'LKL{crypto_w4rmup_GaBCVUwC}', 'LKL{crypto_w4rmup_edU4pUmb}', 'LKL{crypto_w4rmup_Fa0736qI}', 'LKL{crypto_w4rmup_LcwRkgOT}', 'LKL{crypto_w4rmup_GQUA6GxD}', 'LKL{crypto_w4rmup_pudKLMxT}', 'LKL{crypto_w4rmup_w467yR8V}', 'LKL{crypto_w4rmup_XnbApZkZ}', 'LKL{crypto_w4rmup_z5Lo78bl}', 'LKL{crypto_w4rmup_2TBlow1N}', 'LKL{crypto_w4rmup_x3O4w4cQ}']
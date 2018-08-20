def check(attempt, context):
    if attempt.answer == flags[attempt.participant.id % len(flags)]:
        return Checked(True)
    if attempt.answer in flags:
        return CheckedPlagiarist(False, flags.index(attempt.answer))
    return Checked(False)
    
flags = ['LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_lmpFmMCm}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_OuEgWt8G}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_OnKirjt3}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_KOodydBm}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_E0c1sc1k}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_wJdqBIFZ}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_rW01tYwA}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_UP544cZN}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_0Wigfnq7}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_HLNDsdU4}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_F1uUl8Py}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_SAlDd2T6}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_aNt3dzvV}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_vNNUFeqg}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_qyU2oub8}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_S23NJfYl}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_r6sNDBRf}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_riAP4fvJ}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_iUr3Spfm}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_SW0pyvoc}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_R28IyQD2}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_aALdguGb}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_knxCGRXg}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_f7eM6CZ2}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_lCyWXrzS}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_o742Txym}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_Kr7Xxxa7}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_H1SKtwlf}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_Fy2juCqm}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_K6m63lVi}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_fjWTHmOI}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_JEjLNLN2}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_OCVSIkhN}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_I9mY53rY}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_wcIzMw05}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_oMs6xVZ5}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_sMWqRf3P}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_M1zdtE7v}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_nFvdHlZC}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_PDEQnRgP}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_Un0j2ntL}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_fOtv6NBu}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_V9Ibwof6}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_cFj2crjI}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_2BHV1U9J}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_ly8WweWV}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_zZG2MRs5}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_Jp3msWlv}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_LzCS1sD0}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_rj4T3VEM}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_AkGlBlr1}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_bhoSHuww}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_J053FSCx}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_iyE9u9RC}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_0KuOxW8i}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_DOV9c9vg}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_WHmfprJx}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_jPh0p3UQ}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_UsbsoWcl}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_9RUzBz88}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_dV5eh26Q}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_vGLgDmEO}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_4t0aZoJ8}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_HVcobM4l}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_XRYMXBEB}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_jWas99sa}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_YDLPnced}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_mIGPkx2D}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_H1YDHX7e}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_R4i94UiN}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_jC4DnejJ}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_tTE0VEjh}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_ohqMEKgh}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_XVp78tBI}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_BPylqC8x}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_x4bZJjwK}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_6kPAqnUM}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_SgiaeADQ}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_VW2FnuQg}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_hQqp9xuF}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_35oJ14kS}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_mG9MbaP4}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_WYVyxI8n}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_P3DFL2pg}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_KcbFJWfL}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_EK2Wwrfu}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_NdZvFSO8}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_L5Rco7vZ}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_qvhwQPvS}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_1ZJQ3DPK}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_nASs2w9m}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_jVU45hTT}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_mYd37cH0}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_DFE05fw9}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_5Xebukq0}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_nWAl1P2H}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_R25qtkWQ}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_2WZqftfo}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_5DLEuA7x}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_noGLbQlN}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_9ApeptKU}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_LmSbT4hJ}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_HYEks4HJ}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_m6FEXo5e}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_3gyWL6IK}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_0VEWsk88}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_ow3UWKX6}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_WJZNvZZS}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_trB5on4j}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_mbrPTOHP}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_hK2XMOMR}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_1nEUGAyR}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_RF9HsQXH}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_KCXpAfGZ}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_atIpjH1l}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_4B55YTom}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_r6Vh39f7}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_VKCQnQ0Z}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_1MKjebf1}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_A5lniKJC}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_NNOR8N0B}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_zNwldW6p}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_R2dNr6F8}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_EAViBuc4}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_HT8E8NMd}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_9cEYBSiQ}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_QLUVIXD5}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_c95X82BU}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_zgEuluZR}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_kqRVbogy}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_uHdIWhrb}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_PFvdl20L}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_OJzTEcgd}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_HgYjjpxP}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_E6M7b36T}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_U5KHmNSJ}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_4T5wS7CI}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_jn7Ok2cv}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_HZdAieMb}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_vwitLxL3}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_mgSKf2J8}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_4oiez4CN}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_Mz7VmDdx}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_CMgB5Mtv}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_uaLF9EzN}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_O8HJM5Jg}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_inYCAggq}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_PGK7CsVV}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_ywmGeiBL}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_HSlq5ajJ}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_2WYXn5XZ}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_fDkREvel}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_mbS3XP9O}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_Jyp3wyX2}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_1HAuhW67}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_sd03C1b0}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_aLUWDKpF}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_Yb3IyZEF}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_ZfCTs7sm}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_oyReCrC7}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_zPKvWX2P}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_W0lfFuXu}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_nrz2gM1Z}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_h2kj4AKy}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_8sMX709Q}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_6EdrgCxp}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_sNMUt0lb}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_YpBV2S1s}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_rslFyXwy}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_uXrRTIGS}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_pbtmib1u}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_LfxPIlBy}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_TYW7c2N9}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_D3nYtN1v}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_Vaza5jXc}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_ZJ7lKsOH}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_VkXeVBBN}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_AWaAKP7X}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_GsK9hEq2}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_z2KEKpSK}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_XtaznnNA}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_0eurs2id}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_PPXoJqwq}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_qGdE1fRb}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_hrIXvyCM}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_oygYE1pO}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_TNlmv3Fl}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_a9pzlNvs}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_gTOXiOPi}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_IiHEMvAj}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_UZlc5nAk}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_m7GL3b9a}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_Wf2CrNO1}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_gwMdLomK}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_zhsqW5FQ}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_ZOuv7HLD}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_SYBkONdq}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_NGe5sqlm}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_hwjI26QS}', 'LKSHL{th1s_is_a_trivial_t4sk_on_a_CTF_8saSWAP8}']
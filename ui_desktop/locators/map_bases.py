# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class MapBasesControls:

    # Вкладки выбора города и карта яндекса
    mapBasesRegionCfo = (By.CSS_SELECTOR, "div[data-region-code='r_cfo']")
    mapBasesRegionSpb = (By.CSS_SELECTOR, "div[data-region-code='r_spb']")
    mapBasesRegionSzfo = (By.CSS_SELECTOR, "div[data-region-code='r_szfo']")
    mapBasesYmaps = (By.XPATH, "//ymaps[@class='ymaps-glass-pane ymaps-events-pane']")

    # Список строительных центров и офисов продаж СПБ
    mapBasesSpbIndustr = (By.CSS_SELECTOR, "div['data-bases-map-code='spb_industr']")
    mapBasesSpbParnas = (By.CSS_SELECTOR, "div['data-bases-map-code='spb_prns']")
    mapBasesSpbSever = (By.CSS_SELECTOR, "div['data-bases-map-code='spb_sever']")
    mapBasesSpbPlaner = (By.CSS_SELECTOR, "div['data-bases-map-code='spb_plnrn']")
    mapBasesSpbSlavyanka = (By.CSS_SELECTOR, "div['data-bases-map-code='spb_slvnk']")
    mapBasesSpbSofia = (By.CSS_SELECTOR, "div['data-bases-map-code='spb_sfska']")
    mapBasesSpbTallin = (By.CSS_SELECTOR, "div['data-bases-map-code='spb_tlnk']")
    mapBasesSpbMurman = (By.CSS_SELECTOR, "div['data-bases-map-code='spb_mrmnsk']")
    mapBasesSpbZhelez = (By.CSS_SELECTOR, "div['data-bases-map-code='spb_zhlzn']")
    mapBasesSpbVsevolozhsk = (By.CSS_SELECTOR, "div['data-bases-map-code='spb_vsk']")
    mapBasesSpbLenin = (By.CSS_SELECTOR, "div['data-bases-map-code='spb_na_lnsk']")

    # Список строительных центров и офисов продаж СЗФО
    mapBasesSzfoNovgorod = (By.CSS_SELECTOR, "div['data-bases-map-code='nvr_nvr']")
    mapBasesSzfoVyborg = (By.CSS_SELECTOR, "div['data-bases-map-code='vbg_vbg']")
    mapBasesSzfoGatchina = (By.CSS_SELECTOR, "div['data-bases-map-code='gtn_gtn']")
    mapBasesSzfoLuga = (By.CSS_SELECTOR, "div['data-bases-map-code='lug_lug']")
    mapBasesSzfoKingisepp = (By.CSS_SELECTOR, "div['data-bases-map-code='kgs_kgs']")
    mapBasesSzfoPetrozavodsk = (By.CSS_SELECTOR, "div['data-bases-map-code='pzv_pzv']")
    mapBasesSzfoLugaOffice = (By.CSS_SELECTOR, "div['data-bases-map-code='lug_mshnsk']")

    # Список строительных центров и офисов продаж Москва и ЦФО
    mapBasesMskGorkovka = (By.CSS_SELECTOR, "div['data-bases-map-code='msk_gorsh']")
    mapBasesMskNovayaRiga = (By.CSS_SELECTOR, "div['data-bases-map-code='msk_newrg']")
    mapBasesMskNovoryazan = (By.CSS_SELECTOR, "div['data-bases-map-code='msk_nvraz']")
    mapBasesMskAltufevo = (By.CSS_SELECTOR, "div['data-bases-map-code='msk_altf']")
    mapBasesMskTver = (By.CSS_SELECTOR, "div['data-bases-map-code='tvr_tvr']")
    mapBasesMskSolnechnogorsk = (By.CSS_SELECTOR, "div['data-bases-map-code='msk_slnrsk']")
    mapBasesMskLobnya = (By.CSS_SELECTOR, "div['data-bases-map-code='msk_lob']")
    mapBasesMskHimki = (By.CSS_SELECTOR, "div['data-bases-map-code='msk_hmk']")
    mapBasesMskKaluga = (By.CSS_SELECTOR, "div['data-bases-map-code='klg_klg']")
    mapBasesMskVladimir = (By.CSS_SELECTOR, "div['data-bases-map-code='vld_vld']")
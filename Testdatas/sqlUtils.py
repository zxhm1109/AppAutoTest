#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author    : zhaofy
# @Datetime  : 2021/1/4 20:28 
# @File      : sqlUtils.py 
# @desc      :


select_User_audit_status = "SELECT audit_status from tb_mf_mem_info as mi LEFT JOIN tb_mf_anchor_audit aa on mi.mem_id=aa.mem_id where mem_phone='16666666663'"
updata_User_withdraw_record = "UPDATE tb_mf_mem_withdraw SET withdraw_status ='DISABLE1' where mem_id=(SELECT mem_id from tb_mf_mem_info WHERE mem_phone='13120806671')"
updata_User_audit_status = "UPDATE tb_mf_anchor_audit SET audit_status ='FAILED' where mem_id=(SELECT mem_id from tb_mf_mem_info WHERE mem_phone='16666666663')"

# Corrections apply log


## T1087.001 test #11
File: `/content/ART/ART/T1087.001/T1087_001_test11_predicates.json`
  [OK] Renamed 'file-exists' -> 'plink-executable-missing' in preconditions.
  -> saved.

## T1082 test #30 (elevated)
File: `/content/ART/ART/T1082/elevated/T1082_test30_predicates.json`
  [OK] Renamed 'not-bios-info-discovered' -> 'bios-information-discovered' in effects.
  -> saved.

## T1053.005 test #12
File: `/content/ART/ART/T1053.005/T1053_005_test12_predicates.json`
  [OK] Renamed 'scheduled-task-created' -> 'not-scheduled-task-created' in effects.
  [OK] Renamed 'not-scheduled-task-created' -> 'not-scheduled-task-created' in effects.
  -> saved.

## T1082 test #37 (normal)
File: `/content/ART/ART/T1082/normal/T1082_test37_predicates.json`
  [OK] Dropped 'command-prompt-invokable' from preconditions.
  -> saved.

## T1560.001 test #10
File: `/content/ART/ART/T1560.001/T1560_001_test10_predicates.json`
  [OK] Dropped 'command-not-found-error' from effects.
  -> saved.

## T1082 test #15 (elevated)
File: `/content/ART/ART/T1082/elevated/T1082_test15_predicates.json`
  [OK] Renamed 'not-information-system-info-discovered' -> 'not-system-info-discovered' in effects.
  [OK] Dropped 'process-spawned' from unconsumed_or_uncertain.
  -> saved.

## T1055 test #6
File: `/content/ART/ART/T1055/T1055_test6_predicates.json`
  [OK] Added 'av-active' to preconditions.
  [OK] Dropped 'elevated-privilege' from unconsumed_or_uncertain.
  [OK] Renamed 'file-exists' -> 'file-exists' in preconditions.
  -> saved.

## T1055 test #7
File: `/content/ART/ART/T1055/T1055_test7_predicates.json`
  [OK] Added 'av-active' to preconditions.
  [OK] Dropped 'elevated-privilege' from unconsumed_or_uncertain.
  [OK] Renamed 'file-exists' -> 'file-exists' in preconditions.
  -> saved.

## T1055 test #8
File: `/content/ART/ART/T1055/T1055_test8_predicates.json`
  [OK] Added 'av-active' to preconditions.
  [OK] Dropped 'elevated-privilege' from unconsumed_or_uncertain.
  [OK] Dropped 'access-denied' from unconsumed_or_uncertain.
  [OK] Renamed 'file-exists' -> 'file-exists' in preconditions.
  -> saved.

## T1055 test #11
File: `/content/ART/ART/T1055/T1055_test11_predicates.json`
  [OK] Added 'av-active' to preconditions.
  [OK] Dropped 'elevated-privilege' from unconsumed_or_uncertain.
  [OK] Renamed 'file-exists' -> 'file-exists' in preconditions.
  -> saved.

## T1112 test #72
File: `/content/ART/ART/T1112/T1112/T1112_test72_predicates.json`
  [OK] Renamed 'registry-key-set' -> 'registry-key-not-modified' in effects.
  -> saved.

## T1560.001 test #11
File: `/content/ART/ART/T1560.001/T1560_001_test11_predicates.json`
  [OK] Dropped 'executor-failure' from unconsumed_or_uncertain.
  [OK] Renamed 'file-exists' -> 'file-exists' in preconditions.
  -> saved.

## T1560.001 test #3
File: `/content/ART/ART/T1560.001/T1560_001_test3_predicates.json`
  [OK] Renamed 'file-compressed' -> 'file-created' in effects.
  -> saved.

## T1082 test #36 (elevated)
File: `/content/ART/ART/T1082/elevated/T1082_test36_predicates.json`
  [OK] Dropped 'cmd-invokable' from preconditions.
  -> saved.

## T1021.002 test #2
File: `/content/ART/ART/T1021 002/T1021_002_test2_predicates.json`
  [OK] Renamed 'valid-credentials-for-admin-share' -> 'current-session-has-local-admin-rights' in preconditions.
  [OK] Renamed 'network-access-to-target' -> 'loopback-share-accessible' in preconditions.
  -> saved.

## T1112 test #26
File: `/content/ART/ART/T1112/T1112/T1112_test26_predicates.json`
  [OK] Dropped 'cmd-invokable' from preconditions.
  [OK] Moved 'registry-key-modified' from unconsumed_or_uncertain -> effects as 'registry-key-not-modified' (schema normalized: name/category/justification).
  -> saved.

## T1112 test #44
File: `/content/ART/ART/T1112/T1112/T1112_test44_predicates.json`
  [OK] Dropped 'cmd-invokable' from preconditions.
  [OK] Moved 'registry-key-modified' from unconsumed_or_uncertain -> effects as 'registry-key-not-modified' (schema normalized: name/category/justification).
  -> saved.

## T1112 test #45
File: `/content/ART/ART/T1112/T1112/T1112_test45_predicates.json`
  [OK] Dropped 'access-denied' from effects.
  [OK] Moved 'registry-key-modified' from unconsumed_or_uncertain -> effects as 'registry-key-not-modified' (schema normalized: name/category/justification).
  -> saved.

## T1112 test #49
File: `/content/ART/ART/T1112/T1112/T1112_test49_predicates.json`
  [OK] Dropped 'cmd-invokable' from preconditions.
  [OK] Dropped 'access-denied' from effects.
  [OK] Moved 'registry-key-modified' from unconsumed_or_uncertain -> effects as 'registry-key-not-modified' (schema normalized: name/category/justification).
  -> saved.

## T1112 test #61
File: `/content/ART/ART/T1112/T1112/T1112_test61_predicates.json`
  [OK] Dropped 'cmd-invokable' from preconditions.
  [OK] Dropped 'user-is-admin' from preconditions.
  [OK] Moved 'registry-key-modified' from unconsumed_or_uncertain -> effects as 'registry-key-not-modified' (schema normalized: name/category/justification).
  -> saved.

## T1112 test #62
File: `/content/ART/ART/T1112/T1112/T1112_test62_predicates.json`
  [OK] Dropped 'user-is-admin' from preconditions.
  [OK] Moved 'registry-key-modified' from unconsumed_or_uncertain -> effects as 'registry-key-not-modified' (schema normalized: name/category/justification).
  -> saved.

## T1112 test #63
File: `/content/ART/ART/T1112/T1112/T1112_test63_predicates.json`
  [OK] Dropped 'user-is-admin' from preconditions.
  [OK] Moved 'registry-key-modified' from unconsumed_or_uncertain -> effects as 'registry-key-not-modified' (schema normalized: name/category/justification).
  -> saved.

## T1112 test #7
File: `/content/ART/ART/T1112/T1112/T1112_test7_predicates.json`
  [OK] Dropped 'user-is-not-admin' from preconditions.
  [OK] Dropped 'execution-policy-bypass-attempted' from unconsumed_or_uncertain.
  -> saved.

## T1112 test #82
File: `/content/ART/ART/T1112/T1112/T1112_test82_predicates.json`
  [OK] Dropped 'cmd-invokable' from preconditions.
  [OK] Moved 'registry-key-modified' from unconsumed_or_uncertain -> effects as 'registry-key-not-modified' (schema normalized: name/category/justification).
  -> saved.

## T1112 test #86
File: `/content/ART/ART/T1112/T1112/T1112_test86_predicates.json`
  [OK] Dropped 'access-denied' from effects.
  [OK] Moved 'registry-key-modified' from unconsumed_or_uncertain -> effects as 'registry-key-not-modified' (schema normalized: name/category/justification).
  -> saved.

## T1112 test #88
File: `/content/ART/ART/T1112/T1112/T1112_test88_predicates.json`
  [OK] Moved 'registry-key-modified' from unconsumed_or_uncertain -> effects as 'registry-key-not-modified' (schema normalized: name/category/justification).
  -> saved.

## T1112 test #50
File: `/content/ART/ART/T1112/T1112/T1112_test50_predicates.json`
  [OK] Moved 'registry-key-modified' from unconsumed_or_uncertain -> effects as 'registry-key-not-modified' (schema normalized: name/category/justification).
  -> saved.

## T1112 test #54
File: `/content/ART/ART/T1112/T1112/T1112_test54_predicates.json`
  [OK] Moved 'registry-key-modified' from unconsumed_or_uncertain -> effects as 'registry-key-not-modified' (schema normalized: name/category/justification).
  -> saved.

## T1112 test #57
File: `/content/ART/ART/T1112/T1112/T1112_test57_predicates.json`
  [OK] Dropped 'registry-key-write-failed' from unconsumed_or_uncertain.
  [OK] Added 'access-denied' to effects.
  [OK] Added 'registry-key-not-modified' to effects.
  -> saved.

## T1112 test #66
File: `/content/ART/ART/T1112/T1112/T1112_test66_predicates.json`
  [OK] Dropped 'user-is-admin' from preconditions.
  -> saved.

## T1112 test #67
File: `/content/ART/ART/T1112/T1112/T1112_test67_predicates.json`
  [OK] Dropped 'user-is-admin' from preconditions.
  -> saved.

## T1112 test #68
File: `/content/ART/ART/T1112/T1112/T1112_test68_predicates.json`
  [OK] Dropped 'user-is-admin' from preconditions.
  -> saved.

## T1112 test #40
File: `/content/ART/ART/T1112/T1112/T1112_test40_predicates.json`
  [OK] Added 'registry-key-modified' to effects.
  -> saved.

## T1112 test #41
File: `/content/ART/ART/T1112/T1112/T1112_test41_predicates.json`
  [OK] Added 'registry-key-modified' to effects.
  -> saved.

## T1560.001 test #2
File: `/content/ART/ART/T1560.001/T1560_001_test2_predicates.json`
  [OK] Renamed 'file-compressed' -> 'file-compression-failed' in effects.
  [OK] Dropped 'winrar-installed' from preconditions.
  -> saved.

## T1560.001 test #4
File: `/content/ART/ART/T1560.001/T1560_001_test4_predicates.json`
  [OK] Renamed 'file-compressed' -> 'file-created' in effects.
  -> saved.

## T1082 test #36 (normal)
File: `/content/ART/ART/T1082/normal/T1082_test36_predicates.json`
  [OK] Added 'elevation-required-for-vssadmin' to preconditions.
  -> saved.

## T1046 test #7
File: `/content/ART/ART/T1046/T1046_test7_predicates.json`
  [OK] Added 'external-payload-unreachable' to preconditions.
  -> saved.

## T1082 test #34 (elevated)
File: `/content/ART/ART/T1082/elevated/T1082_test34_predicates.json`
  [OK] Renamed 'os-information-discovered' -> 'cim-query-executed-output-unconfirmed' in effects.
  -> saved.

## T1082 test #34 (normal)
File: `/content/ART/ART/T1082/normal/T1082_test34_predicates.json`
  [OK] Renamed 'os-information-discovered' -> 'cim-query-executed-output-unconfirmed' in effects.
  -> saved.

## T1018 test #18
File: `/content/ART/ART/T1018/T1018_test18_predicates.json`
  [OK] Renamed 'domain-joined' -> 'domain-joined' in preconditions.
  -> saved.

## T1018 test #22
File: `/content/ART/ART/T1018/T1018_test22_predicates.json`
  [OK] Renamed 'file-exists' -> 'file-exists' in preconditions.
  -> saved.

## T1041 test #1
File: `/content/ART/ART/T1041/T1041_test1_predicates.json`
  [OK] Renamed 'file-exists' -> 'file-exists' in preconditions.
  -> saved.

## T1053.005 test #10
File: `/content/ART/ART/T1053.005/T1053_005_test10_predicates.json`
  [OK] Renamed 'file-exists' -> 'file-exists' in preconditions.
  -> saved.

## T1053.005 test #6
File: `/content/ART/ART/T1053.005/T1053_005_test6_predicates.json`
  [OK] Renamed 'file-exists' -> 'file-exists' in preconditions.
  -> saved.

## T1053.005 test #8
File: `/content/ART/ART/T1053.005/T1053_005_test8_predicates.json`
  [OK] Renamed 'file-exists' -> 'file-exists' in preconditions.
  -> saved.

## T1053.005 test #9
File: `/content/ART/ART/T1053.005/T1053_005_test9_predicates.json`
  [OK] Renamed 'not-scheduled-task-created' -> 'not-scheduled-task-created' in effects.
  -> saved.

## T1055 test #10
File: `/content/ART/ART/T1055/T1055_test10_predicates.json`
  [OK] Renamed 'file-exists' -> 'file-exists' in preconditions.
  -> saved.

## T1055 test #12
File: `/content/ART/ART/T1055/T1055_test12_predicates.json`
  [OK] Renamed 'file-exists' -> 'file-exists' in preconditions.
  -> saved.

## T1055 test #13
File: `/content/ART/ART/T1055/T1055_test13_predicates.json`
  [OK] Renamed 'file-exists' -> 'file-exists' in preconditions.
  -> saved.

## T1055 test #1
File: `/content/ART/ART/T1055/T1055_test1_predicates.json`
  [OK] Renamed 'file-exists' -> 'file-exists' in preconditions.
  -> saved.

## T1055 test #3
File: `/content/ART/ART/T1055/T1055_test3_predicates.json`
  [OK] Renamed 'file-exists' -> 'file-exists' in preconditions.
  -> saved.

## T1055 test #4
File: `/content/ART/ART/T1055/T1055_test4_predicates.json`
  [OK] Renamed 'file-exists' -> 'file-exists' in preconditions.
  -> saved.

## T1055 test #5
File: `/content/ART/ART/T1055/T1055_test5_predicates.json`
  [OK] Renamed 'file-exists' -> 'file-exists' in preconditions.
  -> saved.

## T1055 test #9
File: `/content/ART/ART/T1055/T1055_test9_predicates.json`
  [OK] Renamed 'file-exists' -> 'file-exists' in preconditions.
  -> saved.

## T1070.004 test #10
File: `/content/ART/ART/T1070.004/T1070_004_test10_predicates.json`
  [OK] Renamed 'file-exists' -> 'file-exists' in preconditions.
  [OK] Renamed 'file-deleted' -> 'file-deleted' in effects.
  -> saved.

## T1070.004 test #4
File: `/content/ART/ART/T1070.004/T1070_004_test4_predicates.json`
  [OK] Renamed 'file-exists' -> 'file-exists' in preconditions.
  -> saved.

## T1070.004 test #6
File: `/content/ART/ART/T1070.004/T1070_004_test6_predicates.json`
  [OK] Renamed 'file-exists' -> 'file-exists' in preconditions.
  -> saved.

## T1070.004 test #9
File: `/content/ART/ART/T1070.004/T1070_004_test9_predicates.json`
  [OK] Renamed 'file-exists' -> 'file-exists' in preconditions.
  -> saved.

## T1082 test #24 (normal)
File: `/content/ART/ART/T1082/normal/T1082_test24_predicates.json`
  [OK] Renamed 'not-azuread-connected' -> 'not-azuread-connected' in effects.
  -> saved.

---
Files touched: 60   Files missing: 0
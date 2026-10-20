;; T1070.004 File Deletion - Test #10
(define (problem t1070-004-p1)
  (:domain aurora-mini)
  (:init (file-exists))
  (:goal (and (file-deleted)))
)

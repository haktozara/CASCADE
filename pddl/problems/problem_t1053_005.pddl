;; T1053.005 Scheduled Task - Test #7 primary, Test #2 corroborating
(define (problem t1053-005-p1)
  (:domain aurora-mini)
  (:init (cmd-invokable))
  (:goal (and (scheduled-task-created) (registry-key-written)))
)

#lang typed/racket

(: big-sum (-> Integer Integer Integer Integer))
(define (big-sum lower upper diff)
  (if (> (+ lower diff) upper)
      lower
      (+ lower (big-sum (+ lower diff) upper diff))))

(: big-sum-tail (-> Integer Integer Integer Integer))
(define (big-sum-tail lower upper diff)
  (let loop ([acc 0] [cur lower])
    (if (> cur upper)
        acc
        (loop (+ acc cur) (+ cur diff)))))

(big-sum 1 10 3)
(big-sum-tail 1 10 3)

#lang racket

(define (big-sum lower upper diff)
  (if (> (+ lower diff) upper)
      lower
      (+ lower (big-sum (+ lower diff) upper diff))))

(define (big-sum-tail lower upper diff)
  (define (loop acc cur l u d)
    (if (> cur u)
        acc
        (loop (+ acc cur) (+ cur d) l u d)))
  (loop 0 lower lower upper diff))

(printf "big-sum: ~a\n" (big-sum 1 10 3))
(printf "big-sum-tail: ~a\n" (big-sum-tail 1 10 3))

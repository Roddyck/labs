#lang racket

(define (big-sum term a next b)
  (if (> a b)
      0
      (+ (term a) (big-sum term (next a) next b))))

(define (pi-approx n)
  (define (term i)
    (/ (expt -1.0 (- i 1.0))
       (- (* 2.0 i) 1.0)))

  (define (next i) (+ i 1.0))

  (* 4.0 (big-sum term 1.0 next n)))

(pi-approx 1000)

(define (fold f a n)
  (let loop ([k 0] [current a])
    (if (>= k n)
        current
        (loop (+ k 1) (f k current)))))

(define (factorial n)
  (define (fact-rec k current)
    (* current (+ k 1)))

  (fold fact-rec 1 n))

(factorial 5)

(define (pow x y)
  (define (pow-rec _ current)
    (* current x))

  (fold pow-rec 1 y))

(pow 2 5)

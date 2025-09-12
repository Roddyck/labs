#lang racket

(define epsilon 0.001)

(define (square x)
  (* x x))

(define (close-enough? x y)
  (if (< (abs (- x y)) epsilon)
      #t
      #f))

(define (average x y)
  (/ (+ x y) 2))

(define (improve y x)
  (average y (/ x y)))

(define (sqrt-loop y x)
  (if (close-enough? x (square y))
      y
      (sqrt-loop (improve y x) x)))

(define (sqrt x)
  (sqrt-loop 1.0 x))

(printf "sqrt(2) = ~a~n" (sqrt 2.0))
(printf "sqrt(4) = ~a~n" (sqrt 4.0))

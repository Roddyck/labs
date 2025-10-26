#lang racket

(define (foldr f init lst)
  (if (empty? lst)
      init
      (f (first lst) (foldr f init (rest lst)))))

(foldr / 1 (list 1 2 3))

(define (foldl f init lst)
  (define (iter result rest-of-list)
    (if (empty? rest-of-list)
        result
        (iter (f result (first rest-of-list)) (rest rest-of-list))))
  (iter init lst))

(foldl / 1 (list 1 2 3))

(define (length lst)
  (foldr (lambda (_ y) (add1 y)) 0 lst))

(length (list 1 2 3))

;(define (map f lst)
;  (foldr (lambda (x y) (cons (f x) y)) '() lst))

(map (lambda (x) (* x x)) (list 1 2 3))

(define (filter f lst)
  (foldr (lambda (x y) (if (f x) (cons x y) y)) '() lst))

(filter (lambda (x) (> x 0)) (list 1 2 3 -1))

(define (horner poly x)
  (foldl (lambda (coeff term)
           (+ (* coeff x) term))
         0
         poly))

(horner '(1 0 -2 3) 2) ; 1 * 2^3 + 0 * 2^2 - 2 * 2^1 + 3 = 8 - 4 + 3 = 7

(define (transpose mat)
  (if (null? mat)
      '()
      (apply map list mat)))

(transpose '((1 2 3) (4 5 6)))

(define (dot-product u v)
  (foldr + 0 (map * u v)))

(define (matrix-*-vector m v)
  (map (lambda (row) (dot-product row v)) m))

(define (matrix-*-matrix m n)
  (let ([cols (transpose n)])
    (map (lambda (row)
           (map (lambda (col)
                  (dot-product row col))
                cols))
         m)))

(define A '((1 2 3)
            (4 5 6)))


(define I '((1 0 0)
            (0 1 0)
            (0 0 1)))

(define B '((7 8)
            (9 10)
            (11 12)))

(matrix-*-matrix A I)
(matrix-*-matrix A B)

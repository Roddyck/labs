#lang racket

(define (snoc l a)
  (if (null? l)
      (list a)
      (cons (car l) (snoc (cdr l) a))))

(snoc '(1 2) 3)

(define (reverse l)
  (if (null? l)
      l
      (snoc (reverse (cdr l)) (car l))))

(reverse '(1 2 3))

(define (reverse-tail-recursive l)
  (let loop ([lst l] [acc '()])
    (if (null? lst)
        acc
        (loop (cdr lst) (cons (car lst) acc)))))

(reverse-tail-recursive '(1 2 3))

(define (flatten l)
  (cond
    [(null? l) '()]
    [(pair? l) (append (flatten (car l)) (flatten (cdr l)))]
    [else (list l)]))

(flatten '((1 . 2) () ((3 4) 5)))

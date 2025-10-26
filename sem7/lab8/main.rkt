#lang racket
(require r5rs)
(print-as-expression #f)
(print-mpair-curly-braces #f)

(define (last-pair-of-list l)
  (if (null? (cdr l))
      l
      (last-pair-of-list (cdr l))))

(define (snoc! l x)
  (cond
    [(empty? l) (error "can't add element to empty list")]
    [(empty? (cdr l)) (set-cdr! l (list x))]
    [else (snoc! (cdr l) x)]))

(define l '(1 2 3))
(snoc! l 4)
(displayln l)

(define (append! l1 l2)
  (cond
    [(empty? l1) (error "can't append to empty list")]
    [(empty? (cdr l1)) (set-cdr! l1 l2)]
    [else (append! (cdr l1) l2)]))

(define l1 '(1 2 3))
(define l2 '(4 5 6))
(append! l1 l2)
(displayln l1)

(define (delete! x l)
  (cond
    [(null? l) (error "can't delete from empty list")]
    [(equal? (car l) x) (error "can't delete head of the list")]
    [(equal? x (cadr l)) (set-cdr! l (cddr l))]
    [else (delete! x (cdr l))]))

(define lst '(1 2 3 4 5))
(delete! 3 lst)
(displayln lst)

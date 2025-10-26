#lang racket

(define (square x)
  (* x x))

(define (fast-expt b n)
  (cond ((= n 0) 1)
        ((even? n) (square (fast-expt b (/ n 2))))
        (else (* b (fast-expt b (sub1 n))))))

(define (fast-expt-tail b n)
  (let iter ([b b] [n n] [a 1])
    (cond
      [(= n 0) a]
      [(even? n) (iter (square b) (/ n 2) a)]
      [else (iter b (sub1 n) (* b a))])))

(fast-expt-tail 2 10)

(define (double a)
  (+ a a))

(define (halve a)
  (if (even? a)
      (/ a 2)
      (error "Can't halve odd number")))

; a * b = a + a + a + ... + a
; a * 2 = double a
; a * 4 = double (a * (halve 4))
(define (fast-prod a b)
  (cond
    [(= b 0) 0]
    [(even? b) (double (fast-prod a (halve b)))]
    [else (+ a (fast-prod a (sub1 b)))]))

(fast-prod 2 4)

(define (fast-prod-tail a b)
  (let iter ([a a] [b b] [c 0])
    (cond
      [(= b 0) c]
      [(even? b) (iter (double a) (halve b) c)]
      [else (iter a (sub1 b) (+ a c))])))

(fast-prod-tail 2 4)
(fast-prod-tail 2 5)

(define (merge l1 l2)
  (cond
    [(empty? l1) l2]
    [(empty? l2) l1]
    [else
     (if (< (first l1) (first l2))
         (cons (first l1) (merge (rest l1) l2))
         (cons (first l2) (merge l1 (rest l2))))]))

(merge '(2 5 6) '(1 3 4))

(define (halve-list l)
  (let* ([mid (floor (/ (length l) 2))]
         [left (take l mid)]
         [right (drop l mid)])
    (cons left right)))

(define halved-list (halve-list '(1 2 3 4 5 6 7 8 9)))
(car halved-list)
(cdr halved-list)

(define (msort l)
  (cond
    [(or (empty? l) (= (length l) 1)) l]
    [else
     (let* ([halved-list (halve-list l)]
            [left (car halved-list)]
            [right (cdr halved-list)])
       (merge (msort left) (msort right)))]))

(msort '(5 2 4 1 3 6))

(define (apply-n f x n)
  (if (zero? n)
      x
      (apply-n f (f x) (sub1 n))))

(define (fold f a n)
  (cdr (apply-n
        (lambda (pair)
          (let ([k (car pair)]
                [x (cdr pair)])
            (cons (add1 k) (f k x))))
        (cons 0 a)
        n)))

(fold (lambda (n p) (+ n p)) 0 10)

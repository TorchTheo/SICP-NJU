; Problem 1
(define-macro
 (list-of map-expr for var in lst if filter-expr)
 `(map (lambda (,var) ,map-expr)
       (filter (lambda (,var) ,filter-expr) ,lst)))

; Problem 2
(define (map-stream f s)
  (if (null? s)
      nil
      (cons-stream (f (car s))
                   (map-stream f (cdr-stream s)))))

(define multiples-of-three
        (cons-stream 3
                     (map-stream (lambda (x) (+ x 3))
                                 multiples-of-three)))

; Problem 3
(define (rle s)
    (define (helper ele lst num)
          (cond ((null? lst) (cons-stream (list ele num) nil))
          ((= ele (car lst)) (helper ele (cdr-stream lst) (+ num 1)))
          (else (cons-stream (list ele num) (rle lst)))))
    (if (null? s)
      nil
      (helper (car s) (cdr-stream s) 1))
)

(define (rle_ s)
  (define (track-run elem st len)
    (cond ((null? st) (cons-stream (list elem len) nil))
          ((= elem (car st)) (track-run elem (cdr-stream st) (+ len 1)))
          (else (cons-stream (list elem len) (rle st))))
  )
  (if (null? s)
      nil
      (track-run (car s) (cdr-stream s) 1))
)

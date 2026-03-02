Lemma plus_0_r : forall n, n + 0 = n.
Proof.
induction n as [| n IH].
* reflexivity.
* simpl. rewrite IH. reflexivity.
Qed.

Lemma plus_S_r : forall m n, m + S n = S (m + n).
Proof.
induction m as [| m IH].
* intro n. reflexivity.
* intro n. simpl. now rewrite IH.
Qed.

Theorem plus_comm : forall m n, m + n = n + m.
Proof.
induction m as [| m IH].
* intro n. (* simpl. *) rewrite plus_0_r. reflexivity.
* intro n. simpl. rewrite plus_S_r, IH. reflexivity.
Qed.

Theorem plus_assoc : forall m n k, (m + n) + k = m + (n + k).
Proof.
induction m as [| m IH]; [reflexivity |]. 
intros n k. simpl. rewrite IH. reflexivity.
Qed.

Lemma times_0_r : forall n, n * 0 = 0.
Proof.
induction n as [| n IH]; [reflexivity |].
simpl. rewrite IH. reflexivity.
Qed.

Lemma times_S_r : forall m n, m * S n = m + m * n.
Proof.
induction m as [| m IH]; [reflexivity |].
intro n. simpl. rewrite IH. rewrite plus_comm, plus_assoc, (plus_comm (m * n) n).
reflexivity.
Qed.

Theorem times_comm : forall m n, m * n = n * m.
Proof.
induction m as [| m IH].
* intro n. rewrite times_0_r. reflexivity.
* intro n. simpl. rewrite times_S_r, IH. reflexivity.
Qed.

Theorem times_plus_distr_l :
  forall m n k, m * (n + k) = m * n + m * k.
Proof.
induction m as [| m IH]; [reflexivity |].
intros n k. simpl. rewrite IH, plus_assoc, (plus_comm k (m * n + m * k)),
!plus_assoc, (plus_comm (m * k) k). reflexivity.
Qed.

Theorem times_plus_distr_r :
  forall m n k, (m + n) * k = m * k + n * k.
Proof.
induction m as [| m IH]; [reflexivity |].
intros n k. rewrite times_comm, times_plus_distr_l, times_comm, (times_comm n k).
reflexivity.
Qed.

Theorem times_assoc : forall m n k, (m * n) * k = m * (n * k).
Proof.
induction m as [| m IH]; [reflexivity |].
intros n k. simpl. rewrite <- IH, times_plus_distr_r. reflexivity.
Qed.

Definition even n := exists k, n = 2 * k.

Definition odd n := exists k, n = 2 * k + 1.

Theorem even_times : forall m n, even m -> even (m * n).
Proof.
intros m n [k H]. rewrite H, times_assoc. unfold even. exists (k * n). reflexivity.
Qed.

Theorem times_1_l : forall m, 1 * m = m.
Proof.
induction m as [| m IH]; [reflexivity |].
simpl. rewrite plus_0_r. reflexivity.
Qed.

Theorem times_1_r : forall m, m * 1 = m.
Proof.
intro m. rewrite times_comm. apply times_1_l.
Qed.

Theorem odd_times : forall m n, odd m -> odd n -> odd (m * n).
Proof.

intros m n [k H1] [l H2]. rewrite H1, H2.
rewrite times_plus_distr_r.
rewrite times_plus_distr_l.
rewrite times_plus_distr_l.

rewrite times_1_r.
rewrite times_1_l.
rewrite times_1_l.

rewrite times_assoc.
rewrite <- plus_assoc.
rewrite <- times_plus_distr_l.
rewrite <- times_plus_distr_l.

exists (k * (2 * l) + k + l).
reflexivity.
Qed.


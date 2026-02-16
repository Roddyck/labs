Section Homework02.

Variable T : Type.
Variables P1 P2 : T -> Prop.

Theorem t3 : (forall x : T, P1 x) \/ (forall x : T, P2 x) ->
  (forall x : T, P1 x \/ P2 x).
Proof.
  intros H x. destruct H as [H | H]; [left | right]; trivial.
Qed.

Theorem t4 : (exists x, P1 x /\ P2 x) -> (exists x, P1 x) /\ (exists x, P2 x).
Proof.
  intro H. split; destruct H as [a H]; exists a; destruct H as [H1 H2]; assumption.
Qed.

Theorem t5 : ((exists x, P1 x) -> forall x, P2 x) ->
  forall x, P1 x -> P2 x.
Proof.
  intros H1 y H2. apply H1. exists y. assumption.
Qed.

Theorem t6 : (~exists x, P1 x) -> forall x, ~P1 x.
Proof.
  intros H1 y H2. apply H1. exists y. assumption.
Qed.

Theorem t7 : (forall x, P1 x) -> ~(exists y, ~P1 y).
Proof.
  unfold not.
  intros H1 H2. destruct H2 as [y H2]. apply H2. apply H1.
Qed.

End Homework02.

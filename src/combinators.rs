use std::{cell::RefCell, process::Output};

#[derive(Debug, Copy, Clone)]
pub struct Position(usize);

pub struct ParserState<'a, T> {
    input: &'a [T],
    position: Position,
}

impl<'a, T> ParserState<'a, T> {
    pub fn new(input: &'a [T]) -> Self {
        Self {
            input,
            position: Position(0),
        }
    }
}

pub trait Parse<'a, T>
where
    T: Clone,
{
    type Output;

    fn parse(&self, state: &mut ParserState<'a, T>) -> Result<Self::Output, String>;
}

pub trait ParseExt<'a, T>: Parse<'a, T>
where
    T: Clone,
{
    fn with<P>(self, other: P) -> With<Self, P>
    where
        Self: Sized,
        // P: Parse<'a, T>,
    {
        With { a: self, b: other }
    }

    fn and<P>(self, other: P) -> And<Self, P>
    where
        Self: Sized,
        P: Parse<'a, T>,
    {
        And { a: self, b: other }
    }

    fn skip<P>(self, other: P) -> Skip<Self, P>
    where
        Self: Sized,
        // P: Parse<'a, T>,
    {
        Skip { a: self, b: other }
    }

    fn map<F, O>(self, f: F) -> Map<Self, F>
    where
        Self: Sized,
        F: Fn(Self::Output) -> O + Clone,
    {
        Map { a: self, f }
    }

    fn or<P>(self, p: P) -> Or<Self, P>
    where
        Self: Sized,
        // P: Parse<'a, T>,
    {
        Or { a: self, b: p }
    }
}

impl<'a, T, P> ParseExt<'a, T> for P
where
    P: Parse<'a, T>,
    T: Clone,
{
}

pub struct Satisfy<F>
where
    F: Clone,
{
    f: F,
}

pub fn satisfy<F>(f: F) -> Satisfy<F>
where
    F: Clone,
{
    Satisfy { f }
}

impl<'a, F, T> Parse<'a, T> for Satisfy<F>
where
    F: Fn(&T) -> bool + Clone,
    T: Clone,
{
    type Output = T;

    fn parse(&self, state: &mut ParserState<'a, T>) -> Result<Self::Output, String> {
        let t = &state.input[state.position.0];
        if (self.f)(t) {
            state.position.0 += 1;
            Ok(t.clone())
        } else {
            Err("match failed".into())
        }
    }
}

pub struct SatisfyMap<F>
where
    F: Clone,
{
    f: F,
}

pub fn satisfy_map<F>(f: F) -> SatisfyMap<F>
where
    F: Clone,
{
    SatisfyMap { f }
}

impl<'a, F, T, U> Parse<'a, T> for SatisfyMap<F>
where
    F: Fn(&T) -> Option<U> + Clone,
    T: Clone,
{
    type Output = U;

    fn parse(&self, state: &mut ParserState<'a, T>) -> Result<Self::Output, String> {
        let t = &state.input[state.position.0];
        if let Some(u) = (self.f)(t) {
            state.position.0 += 1;
            Ok(u)
        } else {
            Err("match failed".into())
        }
    }
}

pub struct SkipUntil<P> {
    p: P,
}

pub fn skip_until<P>(p: P) -> SkipUntil<P> {
    SkipUntil { p }
}

impl<'a, P, T, U> Parse<'a, T> for SkipUntil<P>
where
    P: Parse<'a, T, Output = U>,
    T: Clone,
{
    type Output = U;

    fn parse(&self, state: &mut ParserState<'a, T>) -> Result<Self::Output, String> {
        while state.position.0 < state.input.len() {
            if let Ok(u) = self.p.parse(state) {
                return Ok(u);
            } else {
                state.position.0 += 1;
            }
        }

        Err("encountered end of input unexpectedly".into())
    }
}

pub struct With<A, B> {
    a: A,
    b: B,
}

impl<'a, T, A, B> Parse<'a, T> for With<A, B>
where
    A: Parse<'a, T>,
    B: Parse<'a, T>,
    T: Clone,
{
    type Output = B::Output;

    fn parse(&self, state: &mut ParserState<'a, T>) -> Result<Self::Output, String> {
        if let Ok(_) = self.a.parse(state) {
            if let Ok(b) = self.b.parse(state) {
                return Ok(b);
            }

            return Err("failed to match parser B".into());
        }

        Err("failed to match parser A".into())
    }
}

pub struct And<A, B> {
    a: A,
    b: B,
}

impl<'a, T, A, B> Parse<'a, T> for And<A, B>
where
    A: Parse<'a, T>,
    B: Parse<'a, T>,
    T: Clone,
{
    type Output = (A::Output, B::Output);

    fn parse(&self, state: &mut ParserState<'a, T>) -> Result<Self::Output, String> {
        if let Ok(a) = self.a.parse(state) {
            if let Ok(b) = self.b.parse(state) {
                return Ok((a, b));
            }

            return Err("failed to match parser B".into());
        }

        Err("failed to match parser A".into())
    }
}

pub struct Skip<A, B> {
    a: A,
    b: B,
}

impl<'a, T, A, B> Parse<'a, T> for Skip<A, B>
where
    A: Parse<'a, T>,
    B: Parse<'a, T>,
    T: Clone,
{
    type Output = A::Output;

    fn parse(&self, state: &mut ParserState<'a, T>) -> Result<Self::Output, String> {
        if let Ok(a) = self.a.parse(state) {
            if let Ok(_) = self.b.parse(state) {
                return Ok(a);
            }

            return Err("failed to match parser B".into());
        }

        Err("failed to match parser A".into())
    }
}

pub struct Map<A, F> {
    a: A,
    f: F,
}

impl<'a, T, A, F, U> Parse<'a, T> for Map<A, F>
where
    A: Parse<'a, T>,
    F: Fn(A::Output) -> U + Clone,
    T: Clone,
{
    type Output = U;

    fn parse(&self, state: &mut ParserState<'a, T>) -> Result<Self::Output, String> {
        self.a.parse(state).map(|a| (self.f)(a))
    }
}

pub struct ZeroOrMore<A> {
    a: A,
}

pub fn zero_or_more<A>(a: A) -> ZeroOrMore<A> {
    ZeroOrMore { a }
}

impl<'a, T, A, U> Parse<'a, T> for ZeroOrMore<A>
where
    A: Parse<'a, T, Output = U>,
    T: Clone,
{
    type Output = Vec<U>;

    fn parse(&self, state: &mut ParserState<'a, T>) -> Result<Self::Output, String> {
        let mut result = vec![];

        while state.position.0 < state.input.len() {
            if let Ok(u) = self.a.parse(state) {
                result.push(u);
            } else {
                break;
            }
        }

        Ok(result)
    }
}

pub struct SeparatedBy<A, B> {
    a: A,
    b: B,
}

pub fn separated_by<A, B>(a: A, b: B) -> SeparatedBy<A, B> {
    SeparatedBy { a, b }
}

impl<'a, T, A, B, U> Parse<'a, T> for SeparatedBy<A, B>
where
    A: Parse<'a, T, Output = U>,
    B: Parse<'a, T>,
    T: Clone,
{
    type Output = Vec<U>;

    fn parse(&self, state: &mut ParserState<'a, T>) -> Result<Self::Output, String> {
        let mut result = vec![];

        while state.position.0 < state.input.len() {
            if let Ok(u) = self.a.parse(state) {
                result.push(u);
                if let Err(_) = self.b.parse(state) {
                    break;
                }
            } else {
                break;
            }
        }

        Ok(result)
    }
}

pub struct Or<A, B> {
    a: A,
    b: B,
}

impl<'a, T, A, B, U> Parse<'a, T> for Or<A, B>
where
    A: Parse<'a, T, Output = U>,
    B: Parse<'a, T, Output = U>,
    T: Clone,
{
    type Output = U;

    fn parse(&self, state: &mut ParserState<'a, T>) -> Result<Self::Output, String> {
        self.a.parse(state).or_else(|_| self.b.parse(state))
    }
}

pub struct Optional<A> {
    a: A,
}

pub fn optional<A>(a: A) -> Optional<A> {
    Optional { a }
}

impl<'a, T, A, U> Parse<'a, T> for Optional<A>
where
    A: Parse<'a, T, Output = U>,
    T: Clone,
{
    type Output = Option<U>;

    fn parse(&self, state: &mut ParserState<'a, T>) -> Result<Self::Output, String> {
        if let Ok(u) = self.a.parse(state) {
            Ok(Some(u))
        } else {
            Ok(None)
        }
    }
}

pub struct ByRef<'a, A> {
    a: &'a A,
}

pub fn by_ref<'a, A>(a: &'a A) -> ByRef<'a, A> {
    ByRef { a }
}

impl<'a, 'b, T, A, U> Parse<'a, T> for ByRef<'b, A>
where
    A: Parse<'a, T, Output = U>,
    T: Clone,
    U: Clone,
    'a: 'b,
{
    type Output = U;

    fn parse(&self, state: &mut ParserState<'a, T>) -> Result<Self::Output, String> {
        self.a.parse(state)
    }
}

pub struct Opaque<F> {
    f: F,
}

pub fn opaque<'a, T, U, F>(f: F) -> Opaque<F>
where
    F: Fn() -> Box<dyn Parse<'a, T, Output = U>>,
    T: Clone,
    U: Clone,
{
    Opaque { f }
}

impl<'a, T, U, F> Parse<'a, T> for Opaque<F>
where
    F: Fn() -> Box<dyn Parse<'a, T, Output = U> + 'a>,
    T: Clone,
    U: Clone,
{
    type Output = U;

    fn parse(&self, state: &mut ParserState<'a, T>) -> Result<Self::Output, String> {
        let a = (self.f)();

        // a.parse(state)
        Err("not implemented".into())
    }
}

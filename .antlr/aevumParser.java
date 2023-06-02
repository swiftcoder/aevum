// Generated from c:\Users\swift\Developer\GitHub\aevum\aevum.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class aevumParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, IDENT=20, NUMBER=21, STRING=22, WS=23, COMMENT=24;
	public static final int
		RULE_module = 0, RULE_declaration = 1, RULE_struct = 2, RULE_field_list = 3, 
		RULE_field = 4, RULE_type = 5, RULE_function = 6, RULE_statement_list = 7, 
		RULE_statement = 8, RULE_expr_list = 9, RULE_expr = 10, RULE_atom = 11, 
		RULE_struct_literal = 12, RULE_field_initialiser_list = 13, RULE_field_initialiser = 14, 
		RULE_array_literal = 15;
	private static String[] makeRuleNames() {
		return new String[] {
			"module", "declaration", "struct", "field_list", "field", "type", "function", 
			"statement_list", "statement", "expr_list", "expr", "atom", "struct_literal", 
			"field_initialiser_list", "field_initialiser", "array_literal"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'struct'", "'{'", "'}'", "','", "':'", "'['", "']'", "'fn'", "'('", 
			"')'", "'->'", "';'", "'let'", "'='", "'.'", "'*'", "'/'", "'+'", "'-'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, "IDENT", "NUMBER", "STRING", 
			"WS", "COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "aevum.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public aevumParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ModuleContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(aevumParser.EOF, 0); }
		public List<DeclarationContext> declaration() {
			return getRuleContexts(DeclarationContext.class);
		}
		public DeclarationContext declaration(int i) {
			return getRuleContext(DeclarationContext.class,i);
		}
		public ModuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_module; }
	}

	public final ModuleContext module() throws RecognitionException {
		ModuleContext _localctx = new ModuleContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_module);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(35);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__0 || _la==T__7) {
				{
				{
				setState(32);
				declaration();
				}
				}
				setState(37);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(38);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DeclarationContext extends ParserRuleContext {
		public StructContext struct() {
			return getRuleContext(StructContext.class,0);
		}
		public FunctionContext function() {
			return getRuleContext(FunctionContext.class,0);
		}
		public DeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaration; }
	}

	public final DeclarationContext declaration() throws RecognitionException {
		DeclarationContext _localctx = new DeclarationContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_declaration);
		try {
			setState(42);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
				enterOuterAlt(_localctx, 1);
				{
				setState(40);
				struct();
				}
				break;
			case T__7:
				enterOuterAlt(_localctx, 2);
				{
				setState(41);
				function();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StructContext extends ParserRuleContext {
		public TerminalNode IDENT() { return getToken(aevumParser.IDENT, 0); }
		public Field_listContext field_list() {
			return getRuleContext(Field_listContext.class,0);
		}
		public StructContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_struct; }
	}

	public final StructContext struct() throws RecognitionException {
		StructContext _localctx = new StructContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_struct);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(44);
			match(T__0);
			setState(45);
			match(IDENT);
			setState(46);
			match(T__1);
			setState(47);
			field_list();
			setState(48);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Field_listContext extends ParserRuleContext {
		public List<FieldContext> field() {
			return getRuleContexts(FieldContext.class);
		}
		public FieldContext field(int i) {
			return getRuleContext(FieldContext.class,i);
		}
		public Field_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_field_list; }
	}

	public final Field_listContext field_list() throws RecognitionException {
		Field_listContext _localctx = new Field_listContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_field_list);
		int _la;
		try {
			int _alt;
			setState(62);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENT:
				enterOuterAlt(_localctx, 1);
				{
				setState(50);
				field();
				setState(55);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(51);
						match(T__3);
						setState(52);
						field();
						}
						} 
					}
					setState(57);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
				}
				setState(59);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__3) {
					{
					setState(58);
					match(T__3);
					}
				}

				}
				break;
			case T__2:
			case T__9:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FieldContext extends ParserRuleContext {
		public TerminalNode IDENT() { return getToken(aevumParser.IDENT, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public FieldContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_field; }
	}

	public final FieldContext field() throws RecognitionException {
		FieldContext _localctx = new FieldContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_field);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(64);
			match(IDENT);
			setState(65);
			match(T__4);
			setState(66);
			type();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TypeContext extends ParserRuleContext {
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
	 
		public TypeContext() { }
		public void copyFrom(TypeContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ArrayTypeContext extends TypeContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public ArrayTypeContext(TypeContext ctx) { copyFrom(ctx); }
	}
	public static class BasicTypeContext extends TypeContext {
		public TerminalNode IDENT() { return getToken(aevumParser.IDENT, 0); }
		public BasicTypeContext(TypeContext ctx) { copyFrom(ctx); }
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_type);
		try {
			setState(73);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENT:
				_localctx = new BasicTypeContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(68);
				match(IDENT);
				}
				break;
			case T__5:
				_localctx = new ArrayTypeContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(69);
				match(T__5);
				setState(70);
				type();
				setState(71);
				match(T__6);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunctionContext extends ParserRuleContext {
		public TerminalNode IDENT() { return getToken(aevumParser.IDENT, 0); }
		public Field_listContext field_list() {
			return getRuleContext(Field_listContext.class,0);
		}
		public Statement_listContext statement_list() {
			return getRuleContext(Statement_listContext.class,0);
		}
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public FunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function; }
	}

	public final FunctionContext function() throws RecognitionException {
		FunctionContext _localctx = new FunctionContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_function);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			match(T__7);
			setState(76);
			match(IDENT);
			setState(77);
			match(T__8);
			setState(78);
			field_list();
			setState(79);
			match(T__9);
			setState(82);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__10) {
				{
				setState(80);
				match(T__10);
				setState(81);
				type();
				}
			}

			setState(84);
			match(T__1);
			setState(85);
			statement_list();
			setState(86);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Statement_listContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public Statement_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement_list; }
	}

	public final Statement_listContext statement_list() throws RecognitionException {
		Statement_listContext _localctx = new Statement_listContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_statement_list);
		int _la;
		try {
			int _alt;
			setState(100);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__5:
			case T__12:
			case IDENT:
			case NUMBER:
			case STRING:
				enterOuterAlt(_localctx, 1);
				{
				setState(88);
				statement();
				setState(93);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(89);
						match(T__11);
						setState(90);
						statement();
						}
						} 
					}
					setState(95);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
				}
				setState(97);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__11) {
					{
					setState(96);
					match(T__11);
					}
				}

				}
				break;
			case T__2:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	 
		public StatementContext() { }
		public void copyFrom(StatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ExprStatementContext extends StatementContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ExprStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class LetStatementContext extends StatementContext {
		public TerminalNode IDENT() { return getToken(aevumParser.IDENT, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public LetStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_statement);
		try {
			setState(107);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__12:
				_localctx = new LetStatementContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(102);
				match(T__12);
				setState(103);
				match(IDENT);
				setState(104);
				match(T__13);
				setState(105);
				expr(0);
				}
				break;
			case T__5:
			case IDENT:
			case NUMBER:
			case STRING:
				_localctx = new ExprStatementContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(106);
				expr(0);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expr_listContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public Expr_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr_list; }
	}

	public final Expr_listContext expr_list() throws RecognitionException {
		Expr_listContext _localctx = new Expr_listContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_expr_list);
		int _la;
		try {
			int _alt;
			setState(121);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__5:
			case IDENT:
			case NUMBER:
			case STRING:
				enterOuterAlt(_localctx, 1);
				{
				setState(109);
				expr(0);
				setState(114);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(110);
						match(T__3);
						setState(111);
						expr(0);
						}
						} 
					}
					setState(116);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
				}
				setState(118);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__3) {
					{
					setState(117);
					match(T__3);
					}
				}

				}
				break;
			case T__6:
			case T__9:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	 
		public ExprContext() { }
		public void copyFrom(ExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class AdditionContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public AdditionContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class MemberAccessContext extends ExprContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode IDENT() { return getToken(aevumParser.IDENT, 0); }
		public MemberAccessContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class MultplicationContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public MultplicationContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class FunctionCallContext extends ExprContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Expr_listContext expr_list() {
			return getRuleContext(Expr_listContext.class,0);
		}
		public FunctionCallContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class AtomExprContext extends ExprContext {
		public AtomContext atom() {
			return getRuleContext(AtomContext.class,0);
		}
		public AtomExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class ArrayIndexContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public ArrayIndexContext(ExprContext ctx) { copyFrom(ctx); }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 20;
		enterRecursionRule(_localctx, 20, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			_localctx = new AtomExprContext(_localctx);
			_ctx = _localctx;
			_prevctx = _localctx;

			setState(124);
			atom();
			}
			_ctx.stop = _input.LT(-1);
			setState(147);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(145);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
					case 1:
						{
						_localctx = new MultplicationContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(126);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(127);
						_la = _input.LA(1);
						if ( !(_la==T__15 || _la==T__16) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(128);
						expr(4);
						}
						break;
					case 2:
						{
						_localctx = new AdditionContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(129);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(130);
						_la = _input.LA(1);
						if ( !(_la==T__17 || _la==T__18) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(131);
						expr(3);
						}
						break;
					case 3:
						{
						_localctx = new ArrayIndexContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(132);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(133);
						match(T__5);
						setState(134);
						expr(0);
						setState(135);
						match(T__6);
						}
						break;
					case 4:
						{
						_localctx = new FunctionCallContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(137);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(138);
						match(T__8);
						setState(139);
						expr_list();
						setState(140);
						match(T__9);
						}
						break;
					case 5:
						{
						_localctx = new MemberAccessContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(142);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(143);
						match(T__14);
						setState(144);
						match(IDENT);
						}
						break;
					}
					} 
				}
				setState(149);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class AtomContext extends ParserRuleContext {
		public TerminalNode IDENT() { return getToken(aevumParser.IDENT, 0); }
		public TerminalNode NUMBER() { return getToken(aevumParser.NUMBER, 0); }
		public TerminalNode STRING() { return getToken(aevumParser.STRING, 0); }
		public Struct_literalContext struct_literal() {
			return getRuleContext(Struct_literalContext.class,0);
		}
		public Array_literalContext array_literal() {
			return getRuleContext(Array_literalContext.class,0);
		}
		public AtomContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atom; }
	}

	public final AtomContext atom() throws RecognitionException {
		AtomContext _localctx = new AtomContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_atom);
		try {
			setState(155);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(150);
				match(IDENT);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(151);
				match(NUMBER);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(152);
				match(STRING);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(153);
				struct_literal();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(154);
				array_literal();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Struct_literalContext extends ParserRuleContext {
		public TerminalNode IDENT() { return getToken(aevumParser.IDENT, 0); }
		public Field_initialiser_listContext field_initialiser_list() {
			return getRuleContext(Field_initialiser_listContext.class,0);
		}
		public Struct_literalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_struct_literal; }
	}

	public final Struct_literalContext struct_literal() throws RecognitionException {
		Struct_literalContext _localctx = new Struct_literalContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_struct_literal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(157);
			match(IDENT);
			setState(158);
			match(T__1);
			setState(159);
			field_initialiser_list();
			setState(160);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Field_initialiser_listContext extends ParserRuleContext {
		public List<Field_initialiserContext> field_initialiser() {
			return getRuleContexts(Field_initialiserContext.class);
		}
		public Field_initialiserContext field_initialiser(int i) {
			return getRuleContext(Field_initialiserContext.class,i);
		}
		public Field_initialiser_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_field_initialiser_list; }
	}

	public final Field_initialiser_listContext field_initialiser_list() throws RecognitionException {
		Field_initialiser_listContext _localctx = new Field_initialiser_listContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_field_initialiser_list);
		int _la;
		try {
			int _alt;
			setState(174);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENT:
				enterOuterAlt(_localctx, 1);
				{
				setState(162);
				field_initialiser();
				setState(167);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(163);
						match(T__3);
						setState(164);
						field_initialiser();
						}
						} 
					}
					setState(169);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
				}
				setState(171);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__3) {
					{
					setState(170);
					match(T__3);
					}
				}

				}
				break;
			case T__2:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Field_initialiserContext extends ParserRuleContext {
		public TerminalNode IDENT() { return getToken(aevumParser.IDENT, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Field_initialiserContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_field_initialiser; }
	}

	public final Field_initialiserContext field_initialiser() throws RecognitionException {
		Field_initialiserContext _localctx = new Field_initialiserContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_field_initialiser);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(176);
			match(IDENT);
			setState(177);
			match(T__4);
			setState(178);
			expr(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Array_literalContext extends ParserRuleContext {
		public Expr_listContext expr_list() {
			return getRuleContext(Expr_listContext.class,0);
		}
		public Array_literalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array_literal; }
	}

	public final Array_literalContext array_literal() throws RecognitionException {
		Array_literalContext _localctx = new Array_literalContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_array_literal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(180);
			match(T__5);
			setState(181);
			expr_list();
			setState(182);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 10:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 3);
		case 1:
			return precpred(_ctx, 2);
		case 2:
			return precpred(_ctx, 6);
		case 3:
			return precpred(_ctx, 5);
		case 4:
			return precpred(_ctx, 4);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\32\u00bb\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\7\2"+
		"$\n\2\f\2\16\2\'\13\2\3\2\3\2\3\3\3\3\5\3-\n\3\3\4\3\4\3\4\3\4\3\4\3\4"+
		"\3\5\3\5\3\5\7\58\n\5\f\5\16\5;\13\5\3\5\5\5>\n\5\3\5\5\5A\n\5\3\6\3\6"+
		"\3\6\3\6\3\7\3\7\3\7\3\7\3\7\5\7L\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b"+
		"U\n\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\7\t^\n\t\f\t\16\ta\13\t\3\t\5\td\n\t"+
		"\3\t\5\tg\n\t\3\n\3\n\3\n\3\n\3\n\5\nn\n\n\3\13\3\13\3\13\7\13s\n\13\f"+
		"\13\16\13v\13\13\3\13\5\13y\n\13\3\13\5\13|\n\13\3\f\3\f\3\f\3\f\3\f\3"+
		"\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\7\f"+
		"\u0094\n\f\f\f\16\f\u0097\13\f\3\r\3\r\3\r\3\r\3\r\5\r\u009e\n\r\3\16"+
		"\3\16\3\16\3\16\3\16\3\17\3\17\3\17\7\17\u00a8\n\17\f\17\16\17\u00ab\13"+
		"\17\3\17\5\17\u00ae\n\17\3\17\5\17\u00b1\n\17\3\20\3\20\3\20\3\20\3\21"+
		"\3\21\3\21\3\21\3\21\2\3\26\22\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36"+
		" \2\4\3\2\22\23\3\2\24\25\2\u00c4\2%\3\2\2\2\4,\3\2\2\2\6.\3\2\2\2\b@"+
		"\3\2\2\2\nB\3\2\2\2\fK\3\2\2\2\16M\3\2\2\2\20f\3\2\2\2\22m\3\2\2\2\24"+
		"{\3\2\2\2\26}\3\2\2\2\30\u009d\3\2\2\2\32\u009f\3\2\2\2\34\u00b0\3\2\2"+
		"\2\36\u00b2\3\2\2\2 \u00b6\3\2\2\2\"$\5\4\3\2#\"\3\2\2\2$\'\3\2\2\2%#"+
		"\3\2\2\2%&\3\2\2\2&(\3\2\2\2\'%\3\2\2\2()\7\2\2\3)\3\3\2\2\2*-\5\6\4\2"+
		"+-\5\16\b\2,*\3\2\2\2,+\3\2\2\2-\5\3\2\2\2./\7\3\2\2/\60\7\26\2\2\60\61"+
		"\7\4\2\2\61\62\5\b\5\2\62\63\7\5\2\2\63\7\3\2\2\2\649\5\n\6\2\65\66\7"+
		"\6\2\2\668\5\n\6\2\67\65\3\2\2\28;\3\2\2\29\67\3\2\2\29:\3\2\2\2:=\3\2"+
		"\2\2;9\3\2\2\2<>\7\6\2\2=<\3\2\2\2=>\3\2\2\2>A\3\2\2\2?A\3\2\2\2@\64\3"+
		"\2\2\2@?\3\2\2\2A\t\3\2\2\2BC\7\26\2\2CD\7\7\2\2DE\5\f\7\2E\13\3\2\2\2"+
		"FL\7\26\2\2GH\7\b\2\2HI\5\f\7\2IJ\7\t\2\2JL\3\2\2\2KF\3\2\2\2KG\3\2\2"+
		"\2L\r\3\2\2\2MN\7\n\2\2NO\7\26\2\2OP\7\13\2\2PQ\5\b\5\2QT\7\f\2\2RS\7"+
		"\r\2\2SU\5\f\7\2TR\3\2\2\2TU\3\2\2\2UV\3\2\2\2VW\7\4\2\2WX\5\20\t\2XY"+
		"\7\5\2\2Y\17\3\2\2\2Z_\5\22\n\2[\\\7\16\2\2\\^\5\22\n\2][\3\2\2\2^a\3"+
		"\2\2\2_]\3\2\2\2_`\3\2\2\2`c\3\2\2\2a_\3\2\2\2bd\7\16\2\2cb\3\2\2\2cd"+
		"\3\2\2\2dg\3\2\2\2eg\3\2\2\2fZ\3\2\2\2fe\3\2\2\2g\21\3\2\2\2hi\7\17\2"+
		"\2ij\7\26\2\2jk\7\20\2\2kn\5\26\f\2ln\5\26\f\2mh\3\2\2\2ml\3\2\2\2n\23"+
		"\3\2\2\2ot\5\26\f\2pq\7\6\2\2qs\5\26\f\2rp\3\2\2\2sv\3\2\2\2tr\3\2\2\2"+
		"tu\3\2\2\2ux\3\2\2\2vt\3\2\2\2wy\7\6\2\2xw\3\2\2\2xy\3\2\2\2y|\3\2\2\2"+
		"z|\3\2\2\2{o\3\2\2\2{z\3\2\2\2|\25\3\2\2\2}~\b\f\1\2~\177\5\30\r\2\177"+
		"\u0095\3\2\2\2\u0080\u0081\f\5\2\2\u0081\u0082\t\2\2\2\u0082\u0094\5\26"+
		"\f\6\u0083\u0084\f\4\2\2\u0084\u0085\t\3\2\2\u0085\u0094\5\26\f\5\u0086"+
		"\u0087\f\b\2\2\u0087\u0088\7\b\2\2\u0088\u0089\5\26\f\2\u0089\u008a\7"+
		"\t\2\2\u008a\u0094\3\2\2\2\u008b\u008c\f\7\2\2\u008c\u008d\7\13\2\2\u008d"+
		"\u008e\5\24\13\2\u008e\u008f\7\f\2\2\u008f\u0094\3\2\2\2\u0090\u0091\f"+
		"\6\2\2\u0091\u0092\7\21\2\2\u0092\u0094\7\26\2\2\u0093\u0080\3\2\2\2\u0093"+
		"\u0083\3\2\2\2\u0093\u0086\3\2\2\2\u0093\u008b\3\2\2\2\u0093\u0090\3\2"+
		"\2\2\u0094\u0097\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0096\3\2\2\2\u0096"+
		"\27\3\2\2\2\u0097\u0095\3\2\2\2\u0098\u009e\7\26\2\2\u0099\u009e\7\27"+
		"\2\2\u009a\u009e\7\30\2\2\u009b\u009e\5\32\16\2\u009c\u009e\5 \21\2\u009d"+
		"\u0098\3\2\2\2\u009d\u0099\3\2\2\2\u009d\u009a\3\2\2\2\u009d\u009b\3\2"+
		"\2\2\u009d\u009c\3\2\2\2\u009e\31\3\2\2\2\u009f\u00a0\7\26\2\2\u00a0\u00a1"+
		"\7\4\2\2\u00a1\u00a2\5\34\17\2\u00a2\u00a3\7\5\2\2\u00a3\33\3\2\2\2\u00a4"+
		"\u00a9\5\36\20\2\u00a5\u00a6\7\6\2\2\u00a6\u00a8\5\36\20\2\u00a7\u00a5"+
		"\3\2\2\2\u00a8\u00ab\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa"+
		"\u00ad\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ac\u00ae\7\6\2\2\u00ad\u00ac\3\2"+
		"\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00b1\3\2\2\2\u00af\u00b1\3\2\2\2\u00b0"+
		"\u00a4\3\2\2\2\u00b0\u00af\3\2\2\2\u00b1\35\3\2\2\2\u00b2\u00b3\7\26\2"+
		"\2\u00b3\u00b4\7\7\2\2\u00b4\u00b5\5\26\f\2\u00b5\37\3\2\2\2\u00b6\u00b7"+
		"\7\b\2\2\u00b7\u00b8\5\24\13\2\u00b8\u00b9\7\t\2\2\u00b9!\3\2\2\2\26%"+
		",9=@KT_cfmtx{\u0093\u0095\u009d\u00a9\u00ad\u00b0";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
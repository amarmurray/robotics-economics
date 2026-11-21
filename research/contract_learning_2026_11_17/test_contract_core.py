import unittest
from fractions import Fraction as F
from contract_core import source,path,choose

class TestQ3(unittest.TestCase):
 def test_hourly_cash_quantity(self):
  self.assertEqual([(source(s,'hourly')['q'],source(s,'hourly')['m']) for s in (2,4)],[(F(4),F(6)),(F(5),F(15,4))])
 def test_output_cash_quantity(self):
  self.assertEqual([(source(s,'output')['q'],source(s,'output')['m']) for s in (2,4)],[(F(4),F(6)),(F(4),F(7))])
 def test_hourly_source(self):
  win,cases=choose('hourly');self.assertEqual(win,2);self.assertEqual((cases[2]['choice'],cases[4]['choice']),('qualify_B','retain'))
 def test_output_source(self):
  win,cases=choose('output');self.assertEqual(win,4);self.assertEqual((cases[2]['added'],cases[4]['added']),(F(56,5),F(61,5)))
 def test_hour_experience(self):
  win,cases=choose('output',metric='hours',tau=F(2),cash=F(5));self.assertEqual(win,2);self.assertEqual((cases[2]['added'],cases[4]['added']),(F(56,5),F(51,5)))
 def test_no_rights(self):
  _,cases=choose('output',rights=False);self.assertEqual({v['choice'] for v in cases.values()},{'incumbent_A'})
 def test_weaker_target(self):
  _,cases=choose('output',target_a=F(16));self.assertEqual({v['choice'] for v in cases.values()},{'incumbent_A'})
 def test_large_cash(self):
  win,cases=choose('hourly',cash=F(100));self.assertEqual(win,2);self.assertEqual({v['choice'] for v in cases.values()},{'qualify_B'})
 def test_cash_and_option_dominance(self):
  for kind in ('hourly','output'):
   for s in (2,4):
    prev=None
    for n in range(24):
     v=path(s,kind,cash=F(n));self.assertEqual(v['terminal'],F(n)+v['added']);self.assertLessEqual(v['cost'],v['budget'])
     if prev is not None:self.assertGreaterEqual(v['added'],prev)
     prev=v['added']
 def test_customer_participation(self):
  for kind in ('hourly','output'):
   for s in (2,4):self.assertGreaterEqual(source(s,kind)['customer'],F(9,2))
 def test_invalid(self):
  with self.assertRaises(ValueError):source(0,'hourly')
  with self.assertRaises(ValueError):path(2,'output',metric='other')
 def test_optional_old_speed(self):
  for kind in ('hourly','output'):
   for c in (0,4,5,100):self.assertGreaterEqual(max(path(s,kind,cash=F(c))['added'] for s in (2,4)),path(2,kind,cash=F(c))['added'])

if __name__=='__main__':unittest.main()

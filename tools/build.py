#!/usr/bin/env python3
"""glasswallschildcare.com - Glass Walls Childcare, the childcare design-and-construction site of Estier.
Generates every page. Edit copy here, run python3 tools/build.py. Never edit the .html."""
import os, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://glasswallschildcare.com"
PHONE = "0411 250 058"; PHONE_TEL = "0411250058"
PHONE2 = "0450 084 175"; PHONE2_TEL = "0450084175"
EMAIL = "info@estier.com.au"
GA = '<script async src="https://www.googletagmanager.com/gtag/js?id=G-9XJ7DRJZG0"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag("js",new Date());gtag("config","G-9XJ7DRJZG0");</script>'
ICON = """<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 48 48'%3E%3Crect x='6' y='8' width='36' height='32' rx='3' fill='none' stroke='%231E2C4F' stroke-width='4'/%3E%3Cline x1='24' y1='8' x2='24' y2='40' stroke='%232E8B74' stroke-width='4'/%3E%3Cline x1='6' y1='24' x2='42' y2='24' stroke='%232E8B74' stroke-width='4'/%3E%3C/svg%3E">"""
LOGO = """<img src="/images/estier-logo.png" alt="Estier" width="118" height="75">"""

# ------------------------------------------------------------------ the eight concept renders (never captioned as built work)
RENDERS = [
 ("preschool-room.jpg", "Preschool room", "Glass between the room and the garden, and between this room and the next. An educator at the tables sees the verandah, the bathroom door and the room next door without moving."),
 ("toddler-room.jpg", "Toddler room", "Low sills so a two-year-old sees out, a glazed wall to the nappy-change and bathroom so the educator changing one child still has the room in view."),
 ("sleep-room.jpg", "Sleep room", "A glazed wall to the playroom with a blind that drops to half height: the cots are dark, the educator outside can still count every child."),
 ("dining-room.jpg", "Dining and shared space", "The central room every group walks through to the garden. Glass to the kitchen so the cook and the educators see each other."),
 ("art-room.jpg", "Art and messy play", "Wet area off the playroom, glazed on two sides. Washable walls, a floor waste, and a sink at child height."),
 ("outdoor-play.jpg", "Outdoor play", "Seven square metres per child, facing north, with shade over at least half of it. The verandah is the wet-weather room and the sightline across the whole yard."),
 ("entry-lobby.jpg", "Entry and reception", "One door in, one secure door through. Parents sign in with the rooms in view, which is the point of the glass: nothing in the centre is hidden."),
 ("parent-lounge.jpg", "Parent lounge", "A place to sit at drop-off and pick-up, glazed to the babies' room, so a parent can watch without walking in."),
]

PAGES = [  # (file, clean url, title, description)
    ("index.html", "/", "Glass Walls Childcare - childcare centre design and construction, Sydney | Estier",
     "Estier designs and builds childcare and early-learning centres across Sydney: new centres, conversions and fitouts, designed around the National Regulations and built to a fixed price. Check the cost of your centre in ten seconds."),
    ("childcare-centre-design-sydney.html", "/childcare-centre-design-sydney", "Childcare centre design, Sydney | Glass Walls Childcare by Estier", "How Estier designs a childcare centre: the rooms, the ratios, the sightlines, the outdoor area and the approvals, from the first site check to the licensing inspection."),
    ("childcare-centre-construction-sydney.html", "/childcare-centre-construction-sydney", "Childcare centre builders, Sydney | Glass Walls Childcare by Estier", "Estier builds new childcare centres, converts existing buildings and fits out shells in new developments, to a fixed price and the operator's licensing date."),
    ("examples.html", "/examples", "Childcare design examples | Glass Walls Childcare by Estier", "Eight design concepts for a glass-walled childcare centre: playrooms, sleep room, bathrooms, kitchen, outdoor play, entry and parent lounge."),
    ("childcare-centre-cost.html", "/childcare-centre-cost", "Childcare centre cost calculator, Sydney 2026 | Glass Walls Childcare by Estier", "What a childcare centre costs to build in Sydney: new build, conversion or fitout, by licensed places and finish. Space, parking and staffing minimums worked out for you."),
    ("childcare-centre-rules-nsw.html", "/childcare-centre-rules-nsw", "The rules a NSW childcare centre is designed to | Glass Walls Childcare by Estier", "The National Regulations, the NSW Child Care Planning Guideline, the SEPP, the National Construction Code and council controls that shape every childcare centre in NSW, in one page."),
    ("childcare-site-check.html", "/childcare-site-check", "Will your site work for a childcare centre? | Glass Walls Childcare by Estier", "Zoning, size, slope, roads, power lines, parking and outdoor space: the site tests a childcare centre has to pass in NSW, and a free site check from Estier."),
    ("about.html", "/about", "About Estier | Glass Walls Childcare", "Estier is a Sydney design and construction company. Glass Walls Childcare is its childcare centre practice: design, approval and construction under one contract."),
    ("contact.html", "/contact", "Contact | Glass Walls Childcare by Estier", "Talk to Estier about a new childcare centre, a conversion or a fitout in Sydney."),
]

def head(title, desc, url, img="preschool-room.jpg"):
    return f"""<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{DOMAIN}{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{DOMAIN}{url}">
<meta property="og:type" content="website">
<meta property="og:image" content="{DOMAIN}/images/{img}">
{ICON}
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Jost:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css">
<link rel="stylesheet" href="/gw.css">
{GA}
</head>
<body>
<div class="wrap">
  <header class="top">
    <a class="brand" href="/">{LOGO}<span class="bname"><b>Glass Walls</b><small>Childcare</small></span></a>
    <nav><a href="/childcare-centre-design-sydney">Design</a><a href="/childcare-centre-construction-sydney">Construction</a><a href="/examples">Examples</a><a href="/childcare-centre-rules-nsw">The rules</a><a href="/childcare-site-check">Site check</a><a href="/childcare-centre-cost">Cost calculator</a><a class="cta" href="/contact">Contact</a></nav>
  </header>
"""

FOOT = f"""
  <footer>
    <div class="fcols">
      <div><b>Glass Walls Childcare</b><br>Childcare and early-learning centres designed and built by Estier: new centres, conversions and fitouts across Sydney, under one contract and one fixed price.<br><span class="muted">Glass Walls Childcare is a practice of Estier Pty Ltd.</span></div>
      <div><b>Talk to us</b><br>6 Ossary Street, Mascot NSW 2020<br>Mon - Fri 9am - 5pm, weekends by appointment<br><a href="tel:{PHONE_TEL}">{PHONE}</a><br><a href="tel:{PHONE2_TEL}">{PHONE2}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></div>
      <div><b>Pages</b><br><a href="/childcare-centre-design-sydney">Design</a> · <a href="/childcare-centre-construction-sydney">Construction</a> · <a href="/examples">Examples</a><br><a href="/childcare-centre-rules-nsw">The rules</a> · <a href="/childcare-site-check">Site check</a><br><a href="/childcare-centre-cost">Cost calculator</a> · <a href="/about">About Estier</a><br><b style="display:block;margin-top:8px">Also by Estier</b><a href="https://cityfitouts.com.au">City Fitouts</a> - shops, offices, cafes, medical<br><a href="https://coastbuild.com.au">Coast Build</a> - homes</div>
    </div>
    <p class="fine">The pictures on this site are design concepts by Estier, not photographs of built centres. Cost ranges are a guide only; every centre is priced after a site visit and off the drawings. Nothing here is planning or legal advice: the National Regulations, the Child Care Planning Guideline and your council's controls govern.</p>
  </footer>
</div>
</body></html>
"""

def gallery(n=8, small=True):
    out = '<div class="gallery">'
    for f, t, d in RENDERS[:n]:
        src = "/images/" + (f.replace(".jpg", "-s.jpg") if small else f)
        out += f'<figure><a href="/examples#{f[:-4]}"><img src="{src}" alt="{t}: childcare design concept" loading="lazy" width="640" height="360"></a><figcaption><b>{t}</b> {d}</figcaption></figure>'
    return out + "</div>"

PROCESS = """
  <section class="band">
    <h2>How we work</h2>
    <div class="steps four">
      <div><span class="num">01</span><h3>Check the site</h3><p>Zoning, size, slope, the road, the neighbours, power lines and parking. We tell you how many places the site can carry before you spend anything on it.</p></div>
      <div><span class="num">02</span><h3>Check the cost</h3><p>The calculator gives a Sydney range for the places you want and the way you are building. If the numbers work, we draw the centre.</p></div>
      <div><span class="num">03</span><h3>Design and approve</h3><p>We design the centre to the National Regulations and the Child Care Planning Guideline, and take it through the development application with the planner, traffic, acoustic and access consultants it needs.</p></div>
      <div><span class="num">04</span><h3>Build and license</h3><p>One fixed price, one site manager, and the centre handed over to a program built backwards from the operator's service-approval inspection.</p></div>
    </div>
  </section>"""

CALC = """
  <div class="calc" id="calc">
    <div>
      <div class="q"><label class="h">1. What are you doing?</label>
        <div class="opts" id="type">
          <button class="opt on" data-v="new">New centre<small>a cleared site, built from the ground</small></button>
          <button class="opt" data-v="conv">Convert a building<small>a house, church hall, shop or office</small></button>
          <button class="opt" data-v="shell">Fit out a shell<small>ground floor of a new development</small></button>
        </div></div>
      <div class="q"><label class="h">2. Licensed places by age</label>
        <div class="three"><div><label for="p0">Under 2</label><input type="number" id="p0" value="16" min="0" max="80" step="1"></div><div><label for="p2">2 to 3</label><input type="number" id="p2" value="20" min="0" max="80" step="1"></div><div><label for="p3">3 to 5</label><input type="number" id="p3" value="54" min="0" max="150" step="1"></div></div>
        <p class="hint" id="placesHint"></p></div>
      <div class="q"><label class="h">3. Level of finish</label>
        <div class="opts" id="grade">
          <button class="opt on" data-v="std">Standard<small>operator spec: vinyl plank, laminate joinery, aluminium glazing</small></button>
          <button class="opt" data-v="prem">Premium<small>timber floors and joinery, full-height glass walls, bespoke outdoor play</small></button>
        </div></div>
      <div class="q"><label class="h">4. The site</label>
        <label class="chk nb"><input type="checkbox" id="demo"> Demolish an existing house or building</label>
        <label class="chk"><input type="checkbox" id="slope"> Sloping or difficult site</label>
        <label class="chk nb">Basement car spaces <input type="number" id="bays" value="0" min="0" max="60" style="width:84px;margin-left:8px"></label></div>
    </div>
    <aside class="result" id="result">
      <div class="cap">Estimated cost</div>
      <div class="big" id="cost">-</div>
      <div class="sub" id="perplace">-</div>
      <div class="row"><span>Construction, building</span><b id="cCon">-</b></div>
      <div class="row"><span>Outdoor play area and site works</span><b id="cOut">-</b></div>
      <div class="row"><span>Design (Estier)</span><b id="cDes">-</b></div>
      <div class="row"><span>Approvals and consultants</span><b id="cApp">-</b></div>
      <div class="mins" id="mins"></div>
      <div class="appr" id="appr"></div>
      <div class="fine">Sydney rates, 2026, excluding GST and land, from published childcare cost guides and current builder pricing. Indicative only, and subject to survey, ground conditions, the council's conditions and the operator's brief. It is the range you plan around until we price the drawings.</div>
      <p style="margin:16px 0 0"><a class="btn" href="/contact">Get a fixed price</a></p>
    </aside>
  </div>
"""

CALC_JS = """
<script>
// Sydney 2026 ranges per m2 of building, by scenario and finish. Building area allowed at 9.5 m2 per licensed place (playrooms at 3.25 m2 unencumbered, plus cot rooms, bathrooms, kitchen, laundry, staff, storage, circulation).
const T={new:{name:'New centre',gfa:9.5,r:{std:[4000,4800],prem:[4800,5800]},out:{std:[350,500],prem:[500,750]},site:[150000,250000],weeks:[36,52],
   ap:'A new centre is a development application to council under the Transport and Infrastructure SEPP, assessed against the Child Care Planning Guideline. Allow six to twelve months for the approval, then the service approval from the NSW Department of Education after the build.'},
 conv:{name:'Conversion',gfa:9.5,r:{std:[2600,3300],prem:[3300,4200]},out:{std:[350,500],prem:[500,750]},site:[60000,120000],weeks:[20,30],
   ap:'Converting a building to a centre is a change of use and a development application, with the same space, parking and outdoor rules as a new centre. Existing buildings rarely give 3.25 m2 a child without opening walls, so the structure is checked first.'},
 shell:{name:'Fitout of a shell',gfa:9.5,r:{std:[2000,2600],prem:[2600,3300]},out:{std:[500,800],prem:[800,1100]},site:[0,0],weeks:[14,22],
   ap:'If the development consent already names a centre-based child care facility on the ground floor, the fitout can go through a private certifier. If it does not, it is a development application. The outdoor area is usually a podium or rooftop with a fall-height fence and soft-fall over the slab.'}};
const DES={std:0.07,prem:0.09}, APP={std:0.03,prem:0.04}, ADDS={demo:[40000,80000],bay:[75000,110000],slope:[0.08,0.15]};
const S={type:'new',grade:'std'};
const $=id=>document.getElementById(id);
const money=n=>n>=1000000?'$'+(n/1000000).toFixed(n<10000000?2:1)+'m':'$'+Math.round(n/1000)+'k';
const n=id=>Math.max(0,Math.round(+$(id).value||0));
function calc(){
  const t=T[S.type], g=S.grade, p0=n('p0'), p2=n('p2'), p3=n('p3'), places=p0+p2+p3;
  $('qDemo')&&0; [...document.querySelectorAll('.nb')].forEach(x=>x.style.display=S.type==='shell'?'none':'');
  const ed=Math.ceil(p0/4)+Math.ceil(p2/5)+Math.ceil(p3/10), staff=ed+2;
  const indoor=Math.ceil(places*3.25), outdoor=places*7, gfa=Math.round(places*t.gfa);
  const park=Math.ceil(places/6)+Math.ceil(staff/2);
  $('placesHint').textContent=places?(places+' places. At the NSW ratios (1:4 under 2, 1:5 at 2 to 3, 1:10 at 3 to 5) that is '+ed+' educators on the floor, about '+staff+' staff with the director and cook.'):'Put in the places in each age group.';
  if(!places){ $('cost').textContent='-'; $('perplace').textContent='Put in the licensed places to see the range.'; $('mins').innerHTML=''; return; }
  let con=[gfa*t.r[g][0],gfa*t.r[g][1]];
  if($('slope').checked){con=[con[0]*(1+ADDS.slope[0]),con[1]*(1+ADDS.slope[1])];}
  let out=[outdoor*t.out[g][0]+t.site[0],outdoor*t.out[g][1]+t.site[1]];
  if(S.type!=='shell'){ if($('demo').checked){out[0]+=ADDS.demo[0];out[1]+=ADDS.demo[1];} const b=n('bays'); out[0]+=b*ADDS.bay[0]; out[1]+=b*ADDS.bay[1]; }
  const base=[con[0]+out[0],con[1]+out[1]];
  const des=[base[0]*DES[g],base[1]*DES[g]], app=[base[0]*APP[g],base[1]*APP[g]], tot=[base[0]+des[0]+app[0],base[1]+des[1]+app[1]];
  const rng=r=>money(r[0])+' - '+money(r[1]);
  $('cost').textContent=rng(tot);
  $('perplace').textContent=money(tot[0]/places)+' - '+money(tot[1]/places)+' per licensed place · '+places+' places · about '+gfa.toLocaleString('en-AU')+' m² of building';
  $('cCon').textContent=rng(con); $('cOut').textContent=rng(out); $('cDes').textContent=rng(des); $('cApp').textContent=rng(app);
  $('mins').innerHTML='<b>What the rules ask of this centre</b><div class="row"><span>Unencumbered indoor play space, 3.25 m² a child</span><b>'+indoor+' m²</b></div><div class="row"><span>Unencumbered outdoor play space, 7 m² a child</span><b>'+outdoor+' m²</b></div><div class="row"><span>Building, all rooms, about 9.5 m² a place</span><b>'+gfa.toLocaleString('en-AU')+' m²</b></div><div class="row"><span>Car spaces at the usual council rate (1 per 6 children, 1 per 2 staff)</span><b>'+park+'</b></div><div class="row"><span>Educators on the floor at ratio</span><b>'+ed+'</b></div><div class="row"><span>Build time after approval</span><b>'+t.weeks[0]+' - '+t.weeks[1]+' weeks</b></div>';
  $('appr').innerHTML='<b>Approval path</b><span>'+t.ap+'</span>';
  const line=t.name+' | '+places+' places ('+p0+'/'+p2+'/'+p3+') | '+g+' finish | demo:'+($('demo').checked?'y':'n')+' slope:'+($('slope').checked?'y':'n')+' bays:'+n('bays')+' | '+rng(tot)+' (building '+rng(con)+', outdoor and site '+rng(out)+', design '+rng(des)+', approvals '+rng(app)+')';
  try{sessionStorage.setItem('gw_calc',line)}catch(e){}
  const cf=$('calcField'); if(cf) cf.value=line;
}
$('type').addEventListener('click',e=>{const b=e.target.closest('.opt');if(!b)return;[...$('type').children].forEach(x=>x.classList.remove('on'));b.classList.add('on');S.type=b.dataset.v;calc();});
$('grade').addEventListener('click',e=>{const b=e.target.closest('.opt');if(!b)return;[...$('grade').children].forEach(x=>x.classList.remove('on'));b.classList.add('on');S.grade=b.dataset.v;calc();});
['p0','p2','p3','bays'].forEach(id=>$(id).addEventListener('input',calc));
['demo','slope'].forEach(id=>$(id).addEventListener('change',calc));
const pre=new URLSearchParams(location.search).get('type'); if(pre&&T[pre]){S.type=pre;[...$('type').children].forEach(x=>x.classList.toggle('on',x.dataset.v===pre));}
calc();
</script>"""

def calc_section(h2="What will your centre cost?", lede="Pick how you are building, the places in each age group and the finish. You get a Sydney range, and the space, parking and staffing the rules ask for, in ten seconds. No email needed to see the result."):
    return f"""
  <section class="band" id="checker">
    <h2>{h2}</h2>
    <p>{lede}</p>
    {CALC}
  </section>"""

def quote_form(page):
    return f"""
    <form class="form" name="childcare-enquiry" method="POST" enctype="multipart/form-data" data-netlify="true" action="/thanks.html">
      <input type="hidden" name="form-name" value="childcare-enquiry">
      <input type="hidden" name="page" value="{page}">
      <input type="hidden" name="calculator" id="calcField">
      <div class="two"><div><label for="name">Name</label><input id="name" name="name" required></div><div><label for="phone">Phone</label><input id="phone" name="phone" type="tel" required></div></div>
      <label for="email">Email</label><input id="email" name="email" type="email" required>
      <label for="address">Address of the site or building</label><input id="address" name="address" required>
      <div class="two"><div><label for="ptype">What are you doing?</label>
      <select id="ptype" name="project_type"><option>New centre on a site</option><option>Converting an existing building</option><option>Fitting out a shell in a new development</option><option>Not sure yet - checking a site</option></select></div>
      <div><label for="places">Licensed places (roughly)</label><input id="places" name="places" type="number" min="0" max="300"></div></div>
      <label for="notes">Anything we should know (optional)</label><textarea id="notes" name="notes" rows="4"></textarea>
      <label for="plan">Survey, plans or photos (optional, PDF or image)</label><input type="file" id="plan" name="plan" accept="image/*,.pdf">
      <p style="margin:16px 0 0"><button class="btn" type="submit">Send</button></p>
    </form>"""

def home():
    p = PAGES[0]
    return head(p[2], p[3], "/") + f"""
  <section class="hero">
    <div class="kick">Childcare centre design and construction, Sydney</div>
    <h1>A centre where every child is in sight.</h1>
    <p>Estier designs and builds childcare and early-learning centres: new centres on cleared sites, conversions of existing buildings, and fitouts of the ground floor in new developments. Designed around the National Regulations and the NSW Child Care Planning Guideline, built to a fixed price and the operator's licensing date.</p>
    <p>Glass walls is the idea the practice is named for. Rooms glazed to each other, to the bathrooms and sleep rooms, and to the garden: the educator never loses sight of a child, the parent at the door sees the whole centre, and the rooms fill with light. It is also the cheapest way to meet the supervision rule the regulator cares most about.</p>
    <p><a class="btn" href="/childcare-centre-cost">Check what your centre will cost</a> <a class="btn ghost" href="/childcare-site-check">Check your site</a></p>
  </section>
  <section class="band">
    <h2>The concept</h2>
    <p>Eight rooms of a glass-walled centre, drawn by Estier. <a class="textlink" href="/examples">See all eight with the thinking behind each.</a></p>
    {gallery(4)}
  </section>
  <section class="band">
    <h2>Three ways to get a centre</h2>
    <div class="cards three">
      <div class="card"><h3><a href="/childcare-centre-construction-sydney#new">A new centre</a></h3><p>A cleared site of 1,500 to 4,000 m², a single-storey or two-storey building of 60 to 120 places and the outdoor area to match. The longest road, through a development application, and the one that gives the operator exactly the centre it wants.</p></div>
      <div class="card"><h3><a href="/childcare-centre-construction-sydney#convert">A conversion</a></h3><p>A house on a large block, a church hall, a shop or an office floor turned into a centre. Faster and cheaper than a new build when the building and the block pass the tests; we check them before you commit.</p></div>
      <div class="card"><h3><a href="/childcare-centre-construction-sydney#shell">A fitout in a new development</a></h3><p>The ground floor of an apartment or mixed-use building, handed over as a shell. The consent usually already names the centre, so the fitout moves fast, and the outdoor area goes on the podium.</p></div>
    </div>
  </section>
  {PROCESS}
  {calc_section()}
  <section class="band">
    <h2>Why operators and developers come to us</h2>
    <div class="cards three">
      <div class="card"><h3>One contract</h3><p>Design, approval and construction under one agreement with one company, so the drawings are priced by the people who will build them and nothing falls between a designer and a builder.</p></div>
      <div class="card"><h3>Designed to the rules first</h3><p>Every room is sized to the unencumbered-space rule, every group has its own bathroom, every sightline is checked against the supervision regulation, and the parking, acoustic and traffic reports are briefed before the drawings go to council.</p></div>
      <div class="card"><h3>Priced before you buy the site</h3><p>Developers send us the address and the places they want. We tell them what the site can carry, what it will cost to build and how long it will take, before they exchange.</p></div>
    </div>
  </section>
  <section class="band two-col">
    <div>
      <h2>Talk to us about a centre</h2>
      <p>Send us the address and the places you have in mind. We will tell you whether the site works, what it will cost and how long the approval will take, within a few days.</p>
      <p>6 Ossary Street, Mascot NSW 2020<br>Mon - Fri 9am - 5pm, weekends by appointment<br><a href="tel:{PHONE_TEL}">{PHONE}</a> · <a href="tel:{PHONE2_TEL}">{PHONE2}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
    {quote_form("home")}
  </section>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"GeneralContractor","name":"Glass Walls Childcare by Estier","url":"{DOMAIN}/","telephone":"+61 {PHONE}","email":"{EMAIL}","image":"{DOMAIN}/images/preschool-room.jpg","areaServed":"Sydney, NSW","address":{{"@type":"PostalAddress","streetAddress":"6 Ossary Street","addressLocality":"Mascot","addressRegion":"NSW","postalCode":"2020","addressCountry":"AU"}},"description":"Childcare and early-learning centre design and construction in Sydney: new centres, conversions and fitouts, designed to the National Regulations and built to a fixed price."}}</script>
{CALC_JS}
""" + FOOT

def design_page():
    p = PAGES[1]
    return head(p[2], p[3], p[1], "toddler-room.jpg") + f"""
  <section class="hero"><div class="kick">Childcare centre design</div><h1>Designed from the regulations outward.</h1>
    <p>A childcare centre is the most rule-bound small building in Australia. The number of children sets the floor area, the age mix sets the rooms and the bathrooms, the staff ratios set the sightlines, and the council sets the parking, the setbacks and the noise. Estier designs the centre from those numbers outward, so the plan that goes to council is the plan that gets licensed.</p></section>
  <section class="band">
    <h2>What the plan has to do</h2>
    <div class="cards three">
      <div class="card"><h3>Space for every child</h3><p>3.25 m² of unencumbered indoor space and 7 m² of unencumbered outdoor space for each child, measured without furniture, fixed equipment, passageways, bathrooms, kitchens, offices or the staff room. The licensed capacity of the centre is the smaller of what the two tests allow.</p></div>
      <div class="card"><h3>Rooms that match the ratios</h3><p>In NSW one educator looks after four children under two, five children of two to three, and ten of three and over. So the rooms are sized to those multiples: a babies' room of 8 or 12, a toddlers' room of 10 or 15, preschool rooms of 20 or 30. Odd numbers waste a wage.</p></div>
      <div class="card"><h3>A bathroom for every group</h3><p>Child-height toilets and basins off each playroom, visible from it, and a nappy-change bench with a sink in every room for children under three. The National Construction Code sets the count; the regulations set where they go.</p></div>
      <div class="card"><h3>Supervision by design</h3><p>Regulation 115 asks for premises designed so educators can supervise children at all times. We take it literally: glass between rooms, into bathrooms and sleep rooms, low sills to the garden, no blind corners, and the verandah as the vantage point over the whole yard.</p></div>
      <div class="card"><h3>Light, air and quiet</h3><p>Natural light and ventilation to every playroom, a sleep room that can be darkened, acoustic separation between rooms and from the neighbours, and the outdoor area kept under 55 dB(A) from the road where a council asks for it.</p></div>
      <div class="card"><h3>The back of house</h3><p>Kitchen to food-safety standard, laundry, a cot room for the babies, staff room, office, parent reception, secure entry, storage for every room, and the bins, plant and deliveries kept away from the children's areas.</p></div>
    </div>
  </section>
  <section class="band">
    <h2>The glass-walls idea</h2>
    <div class="two-col">
      <div>
        <p>Most centres are built as a corridor with rooms off it, each room a box with one door. The educator in the room cannot see the bathroom, the sleep room or the room next door, so every centre runs on staff walking between boxes.</p>
        <p>Our centres are glazed. Playroom to playroom, playroom to bathroom, playroom to sleep room, kitchen to dining, reception to the rooms, every room to the garden. Full-height toughened glass, acoustic laminated where rooms meet, with blinds where a room needs to be dark or private. The result is a centre that an educator can supervise standing still, that a parent can read from the front door, and that is full of daylight from both sides.</p>
        <p>It costs about the same as plasterboard once the acoustic glass and the blinds are counted, and it photographs far better, which matters to the operator filling the places.</p>
      </div>
      <div><img src="/images/toddler-room-s.jpg" alt="Toddler room design concept with a glazed wall to the bathroom" width="640" height="360" loading="lazy"><p class="cap">Toddler room: glass to the bathroom and the nappy change, so one educator on the floor still has every child in view. Design concept.</p></div>
    </div>
  </section>
  <section class="band">
    <h2>How a centre gets designed</h2>
    <div class="steps four">
      <div><span class="num">01</span><h3>The brief</h3><p>Places, age mix, hours, the operator's model (long day care, preschool, occasional care) and the budget. Everything else follows from these.</p></div>
      <div><span class="num">02</span><h3>The site test</h3><p>Zoning, area, width, slope, the road, the neighbours, power lines, flooding, bushfire and trees. Then a capacity study: how many places the site carries once parking, setbacks and the outdoor area are drawn.</p></div>
      <div><span class="num">03</span><h3>Concept and cost</h3><p>A plan and a cost on the same page. If the places and the budget do not meet, we change the plan before anything is lodged.</p></div>
      <div><span class="num">04</span><h3>Development application</h3><p>Drawings, the planner's statement, the traffic, acoustic, access and landscape reports, and the National Quality Framework checklist, lodged on the Planning Portal and followed through council or the planning panel.</p></div>
    </div>
  </section>
  <section class="band"><h2>Who draws it</h2><p>Estier's design team draws the centre and documents it for the development application and construction. Where an operator has its own architect, we build to their drawings and bring the regulatory review, the cost control and the construction. Either way the people who price the centre are the people who build it.</p></section>
  {calc_section("What will the centre cost?", "Places by age, the way you are building and the finish. A Sydney range in ten seconds.")}
  <section class="band two-col">
    <div><h2>Start with the site</h2><p>Send us the address and the places you want. We come back with whether it works, what it carries and what it costs.</p></div>
    {quote_form("design")}
  </section>
{CALC_JS}
""" + FOOT

def construction_page():
    p = PAGES[2]
    return head(p[2], p[3], p[1], "outdoor-play.jpg") + f"""
  <section class="hero"><div class="kick">Childcare centre construction</div><h1>Built to a fixed price and the licensing date.</h1>
    <p>Estier builds childcare centres three ways: new centres on cleared sites, conversions of existing buildings, and fitouts of shells in new developments. The contract is a fixed price off the drawings, and the program is built backwards from the day the NSW Department of Education inspects the centre for its service approval.</p></section>
  <section class="band" id="new">
    <h2>A new centre</h2>
    <div class="two-col">
      <div>
        <p>Sixty to a hundred and twenty places on 1,500 to 4,000 m², usually single storey with the babies' rooms nearest the entry and the preschool rooms opening to the biggest part of the yard. Thirty-six to fifty-two weeks on site after the approval.</p>
        <ul class="ticks"><li>Demolition, excavation and the slab, with the floor wastes and the hydraulics set out for every bathroom and the kitchen</li><li>Frame, roof, glazing and the acoustic glass walls</li><li>Children's bathrooms, nappy change, kitchen, laundry, cot room, staff and office</li><li>Outdoor play: soft-fall, turf, sandpit, water play, shade sails over at least half the area, fencing a child cannot climb, and the covered verandah</li><li>Car park, drop-off, fencing, landscaping and the deep-soil planting the council asked for</li><li>Fire services, access control, CCTV, data and the AV the operator wants</li></ul>
      </div>
      <div><img src="/images/outdoor-play-s.jpg" alt="Outdoor play area design concept" width="640" height="360" loading="lazy"><p class="cap">Outdoor play, facing north, with shade over half the area and the verandah as the wet-weather room. Design concept.</p></div>
    </div>
  </section>
  <section class="band" id="convert">
    <h2>A conversion</h2>
    <p>A house on a 1,000 m² block, a church hall, a medical centre, a shop with a yard, an office floor with a terrace. Converting is a change of use, and a development application, with the same space, parking and outdoor rules as a new centre. What decides it is the structure: most houses only give 3.25 m² a child once two or three walls come out, and most shops need a yard or a podium for the outdoor area. We check the building before you commit, and the program runs twenty to thirty weeks.</p>
  </section>
  <section class="band" id="shell">
    <h2>A fitout in a new development</h2>
    <p>Developers are putting centres on the ground floor of apartment and mixed-use buildings, handed over as a shell with the services capped. If the development consent already names a centre-based child care facility, the fitout goes through a private certifier and runs fourteen to twenty-two weeks. The outdoor area is a podium or rooftop: fall-height fencing, soft-fall over the slab, drainage, shade and the acoustic treatment the apartments above will want. We build for the developer before the operator is signed, or for the operator under its lease.</p>
  </section>
  <section class="band">
    <h2>The program is the licensing date</h2>
    <div class="steps four">
      <div><span class="num">01</span><h3>Price</h3><p>A fixed price off the approved drawings and the operator's fitout brief, with the provisional sums listed, not hidden.</p></div>
      <div><span class="num">02</span><h3>Build</h3><p>One site manager, weekly photo reports, and the regulator's checklist walked at each stage so nothing is rebuilt after the inspection.</p></div>
      <div><span class="num">03</span><h3>Fit</h3><p>Joinery, play equipment, soft furnishings, kitchen and laundry equipment, data and security, coordinated with the operator's suppliers.</p></div>
      <div><span class="num">04</span><h3>Hand over</h3><p>Occupation certificate, the fire safety certificate, the as-built drawings and the file the operator needs for its service-approval inspection.</p></div>
    </div>
  </section>
  {calc_section()}
  <section class="band two-col">
    <div><h2>Get a fixed price</h2><p>Send us the drawings if you have them, or the address if you do not. We price what is there and tell you what is missing.</p></div>
    {quote_form("construction")}
  </section>
{CALC_JS}
""" + FOOT

def examples_page():
    p = PAGES[3]
    out = head(p[2], p[3], p[1], "entry-lobby.jpg") + """
  <section class="hero"><div class="kick">Design examples</div><h1>Eight rooms of a glass-walled centre.</h1>
    <p>These are design concepts drawn by Estier to show the idea: what each room is for, what it has to do under the regulations, and how glass does it. They are not photographs of built centres.</p></section>
  <section class="band"><div class="examples">"""
    for i, (f, t, d) in enumerate(RENDERS):
        out += f'<figure id="{f[:-4]}" class="{"flip" if i % 2 else ""}"><img src="/images/{f}" alt="{t}: childcare design concept" loading="lazy" width="1280" height="720"><figcaption><h2>{t}</h2><p>{d}</p><p class="tag">Design concept</p></figcaption></figure>'
    out += """</div></section>
  <section class="band"><h2>Want to see it drawn for your site?</h2><p>Send us the address and the places you have in mind. The first concept and the cost come together, before anything is lodged. <a class="btn" href="/contact">Talk to us</a></p></section>
"""
    return out + FOOT

def cost_page():
    p = PAGES[4]
    return head(p[2], p[3], p[1]) + f"""
  <section class="hero"><div class="kick">Childcare centre cost, Sydney 2026</div><h1>What does a childcare centre cost to build?</h1>
    <p>In Sydney in 2026 a new centre costs roughly $45,000 to $60,000 for each licensed place, all in, before the land: a 90-place centre lands between $4 million and $5.5 million. Converting a building runs about $30,000 to $42,000 a place, and fitting out a shell in a new development $22,000 to $32,000. The calculator below works it out for your centre, and shows the space, parking and staffing the rules ask for.</p></section>
  {calc_section("Your centre", "Pick how you are building, the places in each age group and the finish.")}
  <section class="band">
    <h2>Where the money goes</h2>
    <div class="cards three">
      <div class="card"><h3>The building</h3><p>About 9.5 m² of building for every licensed place once the playrooms (3.25 m² a child unencumbered), cot rooms, bathrooms, kitchen, laundry, staff, office, storage and circulation are added up. A 90-place centre is roughly 850 m² of building at $4,000 to $5,800 a square metre for a new build.</p></div>
      <div class="card"><h3>The outdoor area and the site</h3><p>Seven square metres a child outdoors, which for 90 places is 630 m² of soft-fall, turf, sandpit, shade and fencing at $350 to $750 a square metre, plus the car park, drop-off, driveway, landscaping and deep-soil planting, $150,000 to $250,000 on a typical site.</p></div>
      <div class="card"><h3>Design and approvals</h3><p>Design at 7 to 9 per cent of the works and the development application with its planner, traffic, acoustic, access, landscape and National Quality Framework consultants at 3 to 4 per cent. Council fees and the state levy on top.</p></div>
    </div>
  </section>
  <section class="band">
    <h2>What moves the number</h2>
    <ul class="ticks">
      <li><b>Places.</b> Cost per place falls as the centre grows: a 120-place centre is not much dearer to run than a 90, and the kitchen, laundry, office and car park are shared across more places.</li>
      <li><b>Age mix.</b> Babies' rooms are the most expensive space in the building: cot rooms, nappy change, a bathroom for every eight to twelve children and the one-to-four ratio. A centre weighted to three-to-fives is cheaper to build and to staff.</li>
      <li><b>Two storeys.</b> Children's rooms above the ground floor need a refuge area, a second stair and a lift, and the regulator's extra assessment. Single storey is cheaper if the site allows it.</li>
      <li><b>Basement parking.</b> $75,000 to $110,000 a space in Sydney. A site that fits its parking at grade saves a million dollars on a 90-place centre.</li>
      <li><b>The site.</b> Slope, rock, trees, a flood or bushfire overlay, a main road needing acoustic treatment, or a neighbour needing a bigger setback. Every one of these is a cost before the first brick, which is why we check the site before you buy it.</li>
      <li><b>The outdoor area on a podium.</b> In a new development the yard is on a slab: drainage, waterproofing, fall-height fencing and the acoustic treatment for the apartments above make it the dearest outdoor area of all.</li>
    </ul>
  </section>
  <section class="band">
    <h2>What a centre earns</h2>
    <p>Operators in Sydney charge about $150 to $200 a day for a place in 2026 and the federal Child Care Subsidy pays most of it for most families. A 90-place centre at 85 per cent occupancy turns over roughly $3 to $4 million a year. Investors pay for leased centres on yields of about 4.25 to 5.25 per cent in metropolitan Sydney, which is why a well-built centre on a 15 to 20 year lease is worth more than it cost. The federal $1 billion Building Early Education Fund, open since July 2025, and the three-day guarantee of subsidised care from January 2026 both push demand the same way: more places needed, and a shortage of sites that pass the tests.</p>
  </section>
  <section class="band two-col">
    <div><h2>Turn the range into a price</h2><p>Send us the address and the places. We come back with what the site carries and a cost you can take to the bank.</p></div>
    {quote_form("cost")}
  </section>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{{"@type":"Question","name":"How much does a childcare centre cost to build in Sydney?","acceptedAnswer":{{"@type":"Answer","text":"In 2026 a new centre costs roughly $45,000 to $60,000 per licensed place before land, so a 90-place centre is about $4 million to $5.5 million. Converting an existing building is about $30,000 to $42,000 a place and fitting out a shell in a new development $22,000 to $32,000."}}}},{{"@type":"Question","name":"How much space does a childcare centre need per child?","acceptedAnswer":{{"@type":"Answer","text":"The Education and Care Services National Regulations require 3.25 square metres of unencumbered indoor space and 7 square metres of unencumbered outdoor space for each child. Including bathrooms, cot rooms, kitchen, laundry, staff and office areas, a centre needs about 9.5 square metres of building per licensed place."}}}},{{"@type":"Question","name":"How long does a childcare centre take to build?","acceptedAnswer":{{"@type":"Answer","text":"A development application takes six to twelve months in Sydney. After approval a new centre takes 36 to 52 weeks to build, a conversion 20 to 30 weeks and a fitout of a shell 14 to 22 weeks, followed by the service-approval inspection by the NSW Department of Education."}}}}]}}</script>
{CALC_JS}
""" + FOOT

def rules_page():
    p = PAGES[5]
    return head(p[2], p[3], p[1], "sleep-room.jpg") + f"""
  <section class="hero"><div class="kick">The rules</div><h1>Everything a NSW childcare centre is designed to.</h1>
    <p>Five sets of rules shape a centre: the National Regulations that licence it, the state planning policy and guideline that approve it, the National Construction Code that builds it, and the council's controls that sit over the top. This page puts the numbers that drive the design in one place. It is a designer's summary, not advice: the instruments themselves govern.</p></section>
  <section class="band">
    <h2>1. The Education and Care Services National Regulations</h2>
    <p>The rules the NSW Department of Education licenses the centre against, through the National Quality Framework. The physical ones are in Part 4.3 (regulations 103 to 117).</p>
    <table class="rules">
      <tr><th>Regulation</th><th>What it asks</th><th>What we design</th></tr>
      <tr><td>107 Indoor space</td><td>3.25 m² of unencumbered indoor space for each child, excluding passageways, toilets, bathrooms, kitchens, offices, storage, staff rooms and anything the children do not use for play</td><td>Playrooms sized to the ratio multiples with the furniture drawn in, so the unencumbered figure is measured, not assumed</td></tr>
      <tr><td>108 Outdoor space</td><td>7 m² of unencumbered outdoor space for each child</td><td>North-facing where the site allows, with the verandah counted only where the regulator accepts it</td></tr>
      <tr><td>104 Fencing</td><td>A fence or barrier a preschool-age child cannot go through, over or under</td><td>Fences to the regulator's climb-resistant detail, gates self-closing and latched out of reach</td></tr>
      <tr><td>106 Laundry and hygiene</td><td>Laundry facilities or access to them, and hygienic disposal of soiled items</td><td>A laundry with its own entry from outside the children's areas</td></tr>
      <tr><td>109 Toilets and hand washing</td><td>Toilets and washing facilities developmentally and age appropriate</td><td>A bathroom off every playroom, child-height, visible from the room</td></tr>
      <tr><td>110 Ventilation and light</td><td>Adequate ventilation and natural light; comfortable temperature</td><td>Playrooms on an outside wall with openable glazing; a sleep room that can be darkened</td></tr>
      <tr><td>111 Administrative space</td><td>Adequate space for administration, consultation and private conversations</td><td>Office and a meeting room off reception</td></tr>
      <tr><td>112 Nappy change</td><td>Nappy-change facilities with hand washing, where children who wear nappies attend</td><td>A change bench and sink in every room for under-threes, screened from the yard, in sight of the room</td></tr>
      <tr><td>113 Natural environment</td><td>Outdoor space that lets children explore the natural environment</td><td>Trees, soil, sand, water and planting as part of the play area, not just soft-fall</td></tr>
      <tr><td>114 Shade</td><td>Adequate shade over the outdoor space</td><td>Fixed shade and sails over at least half the area, checked against the summer sun path</td></tr>
      <tr><td>115 Supervision</td><td>Premises designed to facilitate supervision of children at all times</td><td>The glass walls: between rooms, into bathrooms and sleep rooms, and across the yard</td></tr>
      <tr><td>116 Premises above ground</td><td>An assessment by the regulator for children's rooms above the ground floor</td><td>Single storey where the site allows; a refuge area of 0.25 m² a person, a second exit and a lift where it does not</td></tr>
      <tr><td>123 Educator ratios (NSW)</td><td>1 educator to 4 children under 24 months; 1 to 5 from 24 to 36 months; 1 to 10 from 36 months to preschool age</td><td>Rooms of 8 or 12 babies, 10 or 15 toddlers, 20 or 30 preschoolers, so no educator is paid for a fraction of a group</td></tr>
    </table>
  </section>
  <section class="band">
    <h2>2. The state planning rules</h2>
    <p>Centre-based child care is governed by the <b>State Environmental Planning Policy (Transport and Infrastructure) 2021, Chapter 3</b> (the old Education and Child Care SEPP) and the <b>Child Care Planning Guideline 2021</b> that the consent authority must consider.</p>
    <ul class="ticks">
      <li><b>Every new centre is a development application.</b> Only school-based, home-based, mobile and temporary care are exempt or complying. A conversion is a DA too. A fitout of a shell can go to a private certifier only where the consent for the building already approved the centre.</li>
      <li><b>The indoor and outdoor space standards are non-discretionary.</b> If the plan meets 3.25 m² and 7 m² a child, council cannot refuse on space. If it does not, the Department of Education has to concur, and usually does not.</li>
      <li><b>The Guideline overrides the council's DCP</b> on everything it covers except three things: building height, side and rear setbacks, and car parking rates. Those stay with the council.</li>
      <li><b>A council cannot</b> limit how close a new centre is to an existing one, control the age mix, or set rules beyond the National Regulations.</li>
      <li><b>Centre-based child care is permitted with consent in the R2 low-density zone</b>, so most of Sydney's house streets are candidates, subject to the site tests below. In industrial zones the test is the health and safety of the children.</li>
      <li><b>The Guideline's site tests:</b> away from petrol stations, high-voltage lines, mobile base stations, busy roads and contaminated land, or with the consultant's report that says the risk is managed. Many councils put numbers on these: a report within 500 m of a base station, within 70 m of a line over 33 kV, within 125 m of a major road.</li>
      <li><b>Ground floor first.</b> Children's rooms above the ground floor need the regulator's assessment and a refuge, so the Guideline and most councils push the rooms to the ground.</li>
    </ul>
  </section>
  <section class="band">
    <h2>3. The council's controls</h2>
    <p>Each council's development control plan keeps height, setbacks and parking, and adds its own site and amenity controls. Typical Sydney figures, which vary by council:</p>
    <table class="rules">
      <tr><th>Control</th><th>Typical figure</th></tr>
      <tr><td>Car parking</td><td>1 space per 6 children plus 1 per 2 staff (Ku-ring-gai); other councils 1 per 4 children. At least one accessible space; bicycle parking at 1 per 10 staff</td></tr>
      <tr><td>Site width</td><td>18 m minimum at the building line in a residential zone (Central Coast)</td></tr>
      <tr><td>Site coverage</td><td>40 per cent, excluding the playground and shade structures (Central Coast)</td></tr>
      <tr><td>Setbacks</td><td>3 m to side and rear in residential zones is common; the front setback follows the street; bigger setbacks where the outdoor area or the neighbours need it</td></tr>
      <tr><td>Slope</td><td>Sites steeper than 1 in 20 are not supported by some councils</td></tr>
      <tr><td>Noise</td><td>Outdoor play areas kept under 55 dB(A) average from the road during operating hours, and the centre's own noise managed at the neighbours' boundaries, usually with an acoustic report and operating hours as conditions</td></tr>
      <tr><td>Deep soil and trees</td><td>1 m of deep soil at side boundaries, 2 m at the rear, 3 m at the front against low-density housing; 1 to 7 medium or tall trees depending on lot size (Ku-ring-gai)</td></tr>
      <tr><td>Driveway</td><td>Maximum 3.7 m wide in low-density streets; vehicles enter and leave in a forward direction; stacked parking limited to two spaces; separate drop-off where the site allows</td></tr>
      <tr><td>Hours</td><td>Stated in the DA and conditioned; 7am to 6pm or 6.30pm is the usual approval</td></tr>
    </table>
  </section>
  <section class="band">
    <h2>4. The National Construction Code</h2>
    <p>A childcare centre is a Class 9b building. The Code sets the construction type, fire separation and exits, the accessible path of travel and accessible toilet, the sanitary fixtures (separate toilets for staff and children, with junior pans for the children, a kitchen, and laundry and nappy-change facilities where children under three attend), the energy-efficiency and condensation rules, and the glazing standard the glass walls are built to: Grade A safety glass to AS 1288, laminated where it has to perform acoustically.</p>
  </section>
  <section class="band">
    <h2>5. The National Quality Standard</h2>
    <p>Once the centre is built the Department of Education assesses the service under the National Quality Standard. Quality Area 3, physical environment, is the one the building answers: fit for purpose, inclusive, well maintained, with indoor and outdoor spaces that let every child play, explore and be supervised. A centre designed to the table above arrives at the inspection with that area already met.</p>
  </section>
  <section class="band two-col">
    <div><h2>Test your site against the rules</h2><p>Send us the address. We run the site tests, draw the capacity and tell you how many places it carries.</p></div>
    {quote_form("rules")}
  </section>
""" + FOOT

def site_page():
    p = PAGES[6]
    return head(p[2], p[3], p[1], "entry-lobby.jpg") + f"""
  <section class="hero"><div class="kick">Site check</div><h1>Will your site work for a childcare centre?</h1>
    <p>Most sites fail on one of ten tests, and the tests are cheap to run before you buy. Here they are, in the order we run them. Send us the address and we run them for you, free, within a few days.</p></section>
  <section class="band">
    <ol class="tests">
      <li><b>Zoning.</b> Centre-based child care is permitted with consent in R2, R3, R4, the business and mixed-use zones and most others. Rural and conservation zones usually not. We read the zone off the planning portal in a minute.</li>
      <li><b>Size and shape.</b> A 90-place centre wants about 850 m² of building, 630 m² of outdoor area, 25 to 30 car spaces and the setbacks: 1,800 to 2,500 m² on one level, less if the building goes to two storeys or the parking goes under. Frontage of 18 m or more.</li>
      <li><b>Slope.</b> Over 1 in 20 the outdoor area needs terracing and the drop-off gets hard; some councils will not support it.</li>
      <li><b>The road.</b> A main road brings traffic objections, a 55 dB(A) acoustic problem in the yard and, within 125 m of a major road, a safety report. A quiet street off a collector road is the sweet spot.</li>
      <li><b>Hazards.</b> Petrol stations, high-voltage lines (a report within 70 m of a line over 33 kV), mobile base stations (within 500 m), contaminated or former industrial land, flood and bushfire overlays.</li>
      <li><b>Neighbours.</b> A centre next to houses needs the 3 m setbacks, deep-soil planting, an acoustic fence and conditioned hours. Next to a school, a park, a church or shops it is an easier approval.</li>
      <li><b>Trees.</b> Protected trees fix the building footprint before you draw it. Councils want trees kept and more planted.</li>
      <li><b>Parking and drop-off.</b> The parking rate and a drop-off that lets cars leave in a forward direction. On a narrow site the car park eats the yard; on a corner it solves itself.</li>
      <li><b>Orientation.</b> The outdoor area wants the north. A site whose only yard faces south needs a cleverer plan and more shade engineering.</li>
      <li><b>The market.</b> Council cannot refuse a centre for being near another one, but the operator can. We look at the places within two kilometres and the suburbs' ages before we draw.</li>
    </ol>
  </section>
  <section class="band">
    <h2>What a capacity study gives you</h2>
    <p>A plan at 1:200 with the building, the outdoor area, the parking and the setbacks drawn to the rules; the places the site carries by age group; the approval path and the consultants it needs; and the cost from the calculator, refined to the site. Developers use it to decide whether to exchange. Operators use it to decide whether to sign the lease.</p>
  </section>
  <section class="band two-col">
    <div><h2>Send us the address</h2><p>We run the ten tests and come back with the places the site carries and what it will cost. No charge for the first look.</p></div>
    {quote_form("site")}
  </section>
""" + FOOT

def about_page():
    p = PAGES[7]
    return head(p[2], p[3], p[1], "parent-lounge.jpg") + f"""
  <section class="hero"><div class="kick">About</div><h1>Estier designs and builds.</h1>
    <p>Estier Pty Ltd is a Sydney design, development and construction company. Glass Walls Childcare is its childcare practice: centres designed to the regulations, approved through council and built to a fixed price, by the same people from the first site visit to the licensing inspection.</p></section>
  <section class="band">
    <div class="cards three">
      <div class="card"><h3>Design</h3><p>Estier's design team draws centres for operators and developers and documents them for approval and construction. Where a client brings its own architect, we build to their drawings.</p></div>
      <div class="card"><h3>Construction</h3><p>Licensed builders of commercial and residential work across Sydney. Our commercial fitouts trade as <a href="https://cityfitouts.com.au">City Fitouts</a>, our homes as <a href="https://coastbuild.com.au">Coast Build</a>.</p></div>
      <div class="card"><h3>Development</h3><p>Estier assesses and develops sites of its own, so it reads a childcare site the way a developer does: what it carries, what it costs and what it is worth with a lease on it.</p></div>
    </div>
  </section>
  <section class="band">
    <h2>Why glass walls</h2>
    <p>The practice is named for one idea: a centre where nothing is hidden. Rooms glazed to each other, to the bathrooms and sleep rooms, to reception and to the garden, so educators supervise without moving, parents see the whole centre from the door, and the building is full of light. It is the supervision rule in the National Regulations made visible, and it is what makes a centre photograph well enough to fill its places.</p>
  </section>
  <section class="band">
    <h2>Contact</h2>
    <p>6 Ossary Street, Mascot NSW 2020<br>Mon - Fri 9am - 5pm, weekends by appointment<br><a href="tel:{PHONE_TEL}">{PHONE}</a> · <a href="tel:{PHONE2_TEL}">{PHONE2}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
  </section>
""" + FOOT

def contact_page():
    p = PAGES[8]
    return head(p[2], p[3], p[1]) + f"""
  <section class="hero"><div class="kick">Contact</div><h1>Talk to us about a centre.</h1>
    <p>A new centre, a conversion, a fitout in a new development, or a site you are thinking of buying. Send the address and the places you have in mind and we come back within a few days with whether it works, what it carries and what it will cost.</p></section>
  <section class="band two-col">
    <div>
      <p><b>Estier</b><br>6 Ossary Street, Mascot NSW 2020<br>Mon - Fri 9am - 5pm, weekends by appointment<br><a href="tel:{PHONE_TEL}">{PHONE}</a><br><a href="tel:{PHONE2_TEL}">{PHONE2}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <p>Operators, developers, landowners and the architects who look after them are all welcome. We also price centres drawn by others.</p>
    </div>
    {quote_form("contact")}
  </section>
""" + FOOT

THANKS = f"""<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Thanks - Glass Walls Childcare</title><meta name="robots" content="noindex"><link href="https://fonts.googleapis.com/css2?family=Jost:wght@400;500;600&display=swap" rel="stylesheet"><style>body{{font-family:Jost,system-ui,sans-serif;color:#2B3A49;max-width:640px;margin:80px auto;padding:0 20px;line-height:1.5}}h1{{color:#1E2C4F;font-weight:600}}a{{color:#1E2C4F}}</style>{GA}
</head><body><h1>Thanks, we have it.</h1><p>We will call you within two working days. If it is urgent, ring <a href="tel:{PHONE_TEL}">{PHONE}</a>.</p><p><a href="/">Back to Glass Walls Childcare</a></p></body></html>
"""

CSS = """/* Glass Walls Childcare additions on top of style.css (shared with Sydney Fitouts / City Fitouts / Coast Build). Navy text, sage-green accent. */
:root{--amber:#2E8B74;--sea:#2E8B74;--sage:#2E8B74;--sand:#F6F3EC}
body{background:#fff}
.kick{color:var(--sage);margin-bottom:22px}
.textlink{color:var(--sage)}
nav a.cta{background:var(--navy)}
.appr{border-left-color:var(--sage)}
.btn.amber{background:var(--navy)}
.btn.ghost{background:#fff;color:var(--navy);border:2px solid var(--navy);margin-left:8px}
header.top .brand{display:flex;align-items:center;gap:14px;text-decoration:none}
header.top .brand img{width:88px;height:auto}
header.top .bname{display:flex;flex-direction:column;line-height:1.05;border-left:1px solid #cfd4de;padding-left:14px}
header.top .bname b{font-size:24px;color:var(--navy);white-space:nowrap}
header.top .bname small{font-size:13px;letter-spacing:.18em;text-transform:uppercase;color:var(--sage);font-weight:600;margin-top:4px}
.hero{padding:30px 0 10px}.hero h1{max-width:820px}.hero p{margin:0 0 14px;max-width:820px}.hero p:last-child{margin-top:26px}
.calc .hint{font-size:13px;color:#5b6477;margin:6px 0 0}.calc .two{display:grid;grid-template-columns:1fr 1fr;gap:12px}.calc .three{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px}.calc .two label,.calc .three label{display:block;font-size:14px;margin:0 0 4px}.calc input[type=number]{width:100%;max-width:220px;padding:10px;border:1px solid #cfd4de;border-radius:8px;font:inherit}.calc .chk{display:block;margin:6px 0}.calc .opts{flex-wrap:wrap}
.result .mins{margin:14px 0 6px;padding:10px 0 2px;border-top:1px solid #d9dde5}.result .mins b{display:block;margin-bottom:6px;color:var(--navy)}.result .mins .row span{font-size:13.5px}
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}.steps.four{grid-template-columns:repeat(4,1fr)}
@media(max-width:820px){.steps,.steps.four{grid-template-columns:1fr}.calc .three{grid-template-columns:1fr}header.top .brand img{width:64px}header.top .bname b{font-size:19px}}
.steps .num{font-size:13px;letter-spacing:.14em;color:var(--sage);font-weight:600}
.steps h3{margin:4px 0 6px;color:var(--navy);font-size:19px}.steps p{margin:0;font-size:15.5px}
.cards.three{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
@media(max-width:820px){.cards.three{grid-template-columns:1fr}}
.card{background:var(--sand);border-radius:12px;padding:20px 22px;border-left:5px solid var(--sage)}.card h3{margin:0 0 8px;font-size:19px;color:var(--navy)}.card h3 a{text-decoration:none;color:var(--navy)}.card p{margin:0;font-size:15.5px}
.gallery{display:grid;grid-template-columns:repeat(2,1fr);gap:22px}
@media(max-width:820px){.gallery{grid-template-columns:1fr}}
.gallery figure{margin:0}.gallery img{width:100%;height:auto;border-radius:12px;display:block}.gallery figcaption{font-size:14.5px;margin-top:8px;color:var(--body)}.gallery figcaption b{color:var(--navy);display:block;font-size:16px;margin-bottom:2px}
.examples figure{display:grid;grid-template-columns:3fr 2fr;gap:28px;align-items:center;margin:0 0 44px}
.examples figure.flip{grid-template-columns:2fr 3fr}.examples figure.flip img{order:2}
@media(max-width:820px){.examples figure,.examples figure.flip{grid-template-columns:1fr}.examples figure.flip img{order:0}}
.examples img{width:100%;height:auto;border-radius:12px;display:block}.examples h2{margin:0 0 8px;font-size:24px}.examples p{margin:0 0 8px;font-size:16px}.examples .tag{display:inline-block;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--sage);font-weight:600;margin-top:6px}
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:36px;align-items:start}
@media(max-width:820px){.two-col{grid-template-columns:1fr}}
.two-col img{width:100%;height:auto;border-radius:12px;display:block}.cap{font-size:13.5px;color:#5b6477;margin:8px 0 0}
.ticks{list-style:none;padding:0;margin:0}.ticks li{position:relative;padding-left:28px;margin:0 0 10px;font-size:16px}.ticks li:before{content:"";position:absolute;left:0;top:7px;width:12px;height:12px;border-radius:50%;background:var(--sage)}
.tests{padding-left:22px;margin:0}.tests li{margin:0 0 14px;font-size:16px}.tests li b{color:var(--navy)}
table.rules{width:100%;border-collapse:collapse;font-size:15px;margin:10px 0 0}table.rules th{text-align:left;background:#D9D9D9;color:#000;padding:10px 12px;font-weight:600}table.rules td{padding:10px 12px;border-bottom:1px solid #e3e6ec;vertical-align:top}table.rules td:first-child{white-space:nowrap;color:var(--navy);font-weight:600}
@media(max-width:820px){table.rules td:first-child{white-space:normal}}
.fcols{display:grid;grid-template-columns:1.3fr 1fr 1fr;gap:28px}@media(max-width:820px){.fcols{grid-template-columns:1fr}}
.muted{color:#5b6477;font-size:14px}
"""

def main():
    os.chdir(ROOT)
    open("gw.css", "w").write(CSS)
    pages = {"index.html": home(), "childcare-centre-design-sydney.html": design_page(), "childcare-centre-construction-sydney.html": construction_page(),
             "examples.html": examples_page(), "childcare-centre-cost.html": cost_page(), "childcare-centre-rules-nsw.html": rules_page(),
             "childcare-site-check.html": site_page(), "about.html": about_page(), "contact.html": contact_page()}
    for f, s in pages.items():
        open(f, "w").write(s)
    open("thanks.html", "w").write(THANKS)
    lines = ["# glasswallschildcare.com - generated by tools/build.py", "https://glasswallsdaycare.com/* https://glasswallschildcare.com/:splat 301!", "https://www.glasswallschildcare.com/* https://glasswallschildcare.com/:splat 301!"]
    for f, url, _, _ in PAGES:
        if url != "/": lines.append(f"{url} /{f} 200")
    lines.append("/thanks /thanks.html 200")
    open("_redirects", "w").write("\n".join(lines) + "\n")
    today = datetime.date.today().isoformat()
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for f, url, _, _ in PAGES: sm += f"  <url><loc>{DOMAIN}{url}</loc><lastmod>{today}</lastmod></url>\n"
    open("sitemap.xml", "w").write(sm + "</urlset>\n")
    open("robots.txt", "w").write(f"User-agent: *\nAllow: /\nDisallow: /thanks.html\nSitemap: {DOMAIN}/sitemap.xml\n")
    for f, s in pages.items():
        for w in ["Republic", "Trevor", "architect-designed by Estier", "our architects", "Estier's architects", "guaranteed"]:
            assert w not in s, (f, w)
    print("built", len(pages) + 1, "pages")

if __name__ == "__main__":
    main()

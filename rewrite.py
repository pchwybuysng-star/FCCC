import re

with open('/Users/panaoonchuayboonsong/Desktop/untitled folder/dammm.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS
css_replacements = {
    "width: 440px;": "width: 360px;\n            background: linear-gradient(180deg, rgba(15, 23, 42, 0.96) 0%, rgba(9, 13, 22, 0.98) 100%);",
    "background: var(--bg-panel);": "",
    "padding: 20px 22px;": "padding: 24px 20px;",
    ".header-title h1 {": ".header-title h1 {\n            font-size: 1.5rem;\n            color: var(--text-primary);",
    "border-bottom: 2px solid var(--accent-cyan);": "border-bottom: 1px solid rgba(56, 189, 248, 0.3);",
    "background: #1e293b;\n            padding: 4px;\n            border-radius: 10px;": "background: rgba(30, 41, 59, 0.5);\n            padding: 6px;\n            border-radius: 24px;",
    "border-radius: 6px;": "border-radius: 20px;",
    "font-size: 0.75rem;": "font-size: 1.1rem;",
    "text-transform: uppercase;": "",
    "background: var(--bg-card);\n            border: 1px solid var(--border-color);": "background: rgba(30, 41, 59, 0.4);\n            border: 1px solid rgba(51, 65, 85, 0.5);",
    "padding: 6px 12px;": "padding: 0;",
    "display: flex;\n            align-items: center;\n            gap: 5px;": "display: flex;\n            align-items: center;\n            justify-content: center;",
    ".view-btn {": ".view-btn {\n            width: 36px;\n            height: 36px;\n            border-radius: 50%;",
    "border: 1px solid #334155;": "border: 1px solid transparent;",
    "border-radius: 10px;": "border-radius: 12px;",
    ".info-value {": ".info-value {\n            font-size: 1.05rem;",
    ".close-btn {": ".close-btn {\n            width: 40px;\n            height: 40px;\n            font-size: 1.5rem;",
    ".explain-box {": ".explain-box {\n            background: rgba(15, 23, 42, 0.6);\n            border-left: 3px solid var(--accent-cyan);\n            padding: 12px 14px;",
    "font-size: 0.82rem;": "font-size: 0.85rem;"
}

for k, v in css_replacements.items():
    content = content.replace(k, v)

# Clean out specific classes or properties
content = re.sub(r'#mode-badge\s*{[^}]+}', '', content)

# 2. Update HTML
html_replacements = {
    '<p>แบบจำลอง 3D แลปโครงสร้างผลึก & เรียงลูกปิงปอง (AB / ABC / Holes)</p>': '',
    '<h1>🧪 Crystal Lab Simulator</h1>': '<h1>🧪 Crystal Lab</h1>',
    '<button class="tab-btn active" data-tab="pingpong">🏓 เรียงปิงปอง</button>': '<button class="tab-btn active" data-tab="pingpong" title="เรียงปิงปอง">🏓</button>',
    '<button class="tab-btn" data-tab="holes">🕳️ ชนิดช่องว่าง</button>': '<button class="tab-btn" data-tab="holes" title="ชนิดช่องว่าง">🕳️</button>',
    '<button class="tab-btn" data-tab="unitcells">🧊 ยูนิตเซลล์</button>': '<button class="tab-btn" data-tab="unitcells" title="ยูนิตเซลล์">🧊</button>',
    '<button class="tab-btn" data-tab="ionic">💎 สารไอออนิก</button>': '<button class="tab-btn" data-tab="ionic" title="สารไอออนิก">💎</button>',
    '<button class="view-btn" id="btnViewTop" title="มองจากด้านบนตรงเพื่อดูการเรียงตัวของชั้นตามแลปหน้า 16">🎯 Top View (2D)</button>': '<button class="view-btn" id="btnViewTop" title="Top View (2D)">🎯</button>',
    '<button class="view-btn" id="btnViewSide" title="มองจากด้านข้างเพื่อดูลำดับชั้น A-B-A หรือ A-B-C">📐 Side View</button>': '<button class="view-btn" id="btnViewSide" title="Side View">📐</button>',
    '<button class="view-btn active" id="btnView3D" title="มุมมอง 3 มิติ หมุนอิสระ">🔄 3D Perspective</button>': '<button class="view-btn active" id="btnView3D" title="3D Perspective">🔄</button>',
    '<button class="view-btn" id="btnAutoRotate" title="เปิด/ปิดการหมุนช้าๆ อัตโนมัติ">⏸ Auto-Rotate</button>': '<button class="view-btn" id="btnAutoRotate" title="Auto-Rotate">⏸</button>',
    '<button class="view-btn" id="btnResetView" title="รีเซ็ตตำแหน่งกล้อง">🔍 Reset</button>': '<button class="view-btn" id="btnResetView" title="Reset View">🔍</button>',
    'ลำดับการเรียงชั้น (Stacking Order)': 'ลำดับการเรียง',
    'เจาะลึกชนิดช่องว่าง (Isolated Void)': 'ชนิดช่องว่าง',
    'รูปแบบแพลูกปิงปอง': 'รูปแบบแพ',
    'ชั้นลูกปิงปอง (เปิด/ปิด ทีละชั้น)': 'ชั้นลูกปิงปอง',
    'ไฮไลต์ช่องว่างในแพ (Show Holes)': 'ไฮไลต์ช่องว่าง',
    'การจัดเรียงอนุภาค 1 ชั้น (ตอนที่ 1 ก.)': 'อนุภาค 1 ชั้น',
    'โลหะ (Metallic Unit Cells)': 'โลหะ',
    'สารประกอบไอออนิก (Ionic Compounds)': 'สารไอออนิก',
    'ระยะห่างแยกชั้น (Explode Layers):': 'ระยะห่างแยกชั้น:',
    'แยกลูกปิงปองออกจากศูนย์กลาง (Explode Void):': 'แยกลูกปิงปอง:',
    'ชุดทดลองตามแลป (รูปที่ 17: ฐาน 19 + หกเหลี่ยม 7 + สามเหลี่ยม 3)': 'ชุดทดลองตามแลป',
    'ผลึกหกเหลี่ยมเต็ม (Full Grid: 19 + 12 + 12 ลูก)': 'ผลึกหกเหลี่ยมเต็ม',
    'เปรียบเทียบชั้นเดียว (1 Layer: Closest vs Simple Cubic)': 'เปรียบเทียบชั้นเดียว',
    'ช่องเททระฮีดรัล (Tetrahedral Hole - 4 ลูก)': 'Tetrahedral (4 ลูก)',
    'ช่องออกตะฮีดรัล (Octahedral Hole - 6 ลูก)': 'Octahedral (6 ลูก)',
    'ช่องลูกบาศก์ (Cubic Hole - 8 ลูก)': 'Cubic (8 ลูก)',
    'Rock Salt (NaCl) - แทรกในช่อง Octahedral': 'Rock Salt (NaCl)',
    'Cesium Chloride (CsCl) - แทรกในช่อง Cubic': 'Cesium Chloride (CsCl)',
    'Zinc Blende (ZnS) - แทรกใน Tetrahedral สลับช่อง': 'Zinc Blende (ZnS)',
    'Fluorite (CaF₂) - แทรกใน Tetrahedral ครบ 8 ช่อง': 'Fluorite (CaF₂)',
    'โครงสร้าง/แบบจำลอง:': 'โมเดล:',
    'เลขโคออร์ดิเนชัน (CN):': 'CN:',
    'Packing Efficiency:': 'Packing:'
}

for k, v in html_replacements.items():
    content = content.replace(k, v)

# Remove badge pills
content = re.sub(r'<span class="badge-pill"[^>]*>.*?</span>', '', content)

# Remove mode badge HTML
content = re.sub(r'<div id="mode-badge">.*?</div>', '', content, flags=re.DOTALL)

# Remove info rows that aren't needed
content = re.sub(r'<div class="info-row"><span class="info-label">ลำดับชั้น / ชนิด:.*?</div>', '', content)
content = re.sub(r'<div class="info-row"><span class="info-label">ชนิดช่องว่างที่เกิด:.*?</div>', '', content)

# 3. Update JS in updateUIInfo
js_new_updateUIInfo = """function updateUIInfo() {
            const statName = document.getElementById('statName');
            const statCN = document.getElementById('statCN');
            const statPE = document.getElementById('statPE');
            const explainBox = document.getElementById('explainBox');
            const legendContainer = document.getElementById('legendContainer');
            legendContainer.innerHTML = '';

            function addLegend(color, name) {
                const item = document.createElement('div');
                item.className = 'legend-item';
                item.innerHTML = `<span class="color-dot" style="background:${color}; color:${color}"></span><span>${name}</span>`;
                legendContainer.appendChild(item);
            }

            if (state.currentTab === 'pingpong') {
                if (state.pingpongCluster === 'single') {
                    if (state.singleLayerType === 'closest') {
                        statName.textContent = '1 Layer: Closest';
                        statCN.textContent = '6';
                        statPE.textContent = '60.48%';
                        explainBox.innerHTML = `<b>Closest Packing:</b><br>เรียงสับหว่าง หนาแน่นสุดใน 2D เกิดช่องสามเหลี่ยม (หงาย/คว่ำ)<br>ปริมาตร 1 ลูก = 4/3&pi;<i>r</i><sup>3</sup>`;
                        addLegend('#38bdf8', 'ลูกปิงปอง (A)');
                        addLegend('#ef4444', 'กรอบหน่วยเซลล์');
                    } else {
                        statName.textContent = '1 Layer: Simple Cubic';
                        statCN.textContent = '4';
                        statPE.textContent = '52.38%';
                        explainBox.innerHTML = `<b>Simple Cubic:</b><br>เรียงตรงกัน เกิดช่องสี่เหลี่ยมระหว่าง 4 ลูก<br>จัดเรียงหลวมกว่าแบบ Closest Packing`;
                        addLegend('#f59e0b', 'ลูกปิงปอง');
                        addLegend('#ef4444', 'กรอบหน่วยเซลล์');
                    }
                } else {
                    const isHCP = (state.stacking === 'hcp');
                    statName.textContent = isHCP ? 'HCP (ABAB...)' : 'FCC (ABCABC...)';
                    statCN.textContent = '12';
                    statPE.textContent = '74.08%';

                    if (isHCP) {
                        explainBox.innerHTML = `<b>HCP (ABAB...):</b><br>ชั้น 3 วางทับชั้น 1 พอดี (Top View ซ้อนทับกัน)<br>มีช่อง <span class="highlight-t">Tetrahedral</span> และ <span class="highlight-o">Octahedral</span>`;
                    } else {
                        explainBox.innerHTML = `<b>FCC (ABCABC...):</b><br>ชั้น 3 ไม่ตรงกับชั้น 1 หรือ 2 (Top View สลับกัน)<br>ชั้น 4 ถึงจะตรงกับชั้น 1`;
                    }

                    addLegend('#38bdf8', 'ชั้นที่ 1 (A)');
                    addLegend('#f59e0b', 'ชั้นที่ 2 (B)');
                    addLegend(isHCP ? '#38bdf8' : '#10b981', isHCP ? 'ชั้นที่ 3 (A)' : 'ชั้นที่ 3 (C)');
                    addLegend('#d946ef', 'ช่อง T (4 ลูก)');
                    addLegend('#fb923c', 'ช่อง O (6 ลูก)');
                }
            } else if (state.currentTab === 'holes') {
                if (state.holeType === 'tetra') {
                    statName.textContent = 'Tetrahedral Hole';
                    statCN.textContent = '4';
                    statPE.textContent = 'r = 0.225 R';
                    explainBox.innerHTML = `<b>ช่องเททระฮีดรัล:</b> เกิดจากทรงกลม 4 ลูก<br>ขนาดช่องว่าง: <i>r</i><sub>void</sub> &approx; 0.225<i>R</i><br>ตัวอย่าง: Zn<sup>2+</sup> ใน ZnS`;
                    addLegend('#38bdf8', 'ฐาน 3 ลูก');
                    addLegend('#f59e0b', 'ปิดยอด 1 ลูก');
                    addLegend('#d946ef', 'ช่องว่างทรงสี่หน้า');
                } else if (state.holeType === 'octa') {
                    statName.textContent = 'Octahedral Hole';
                    statCN.textContent = '6';
                    statPE.textContent = 'r = 0.414 R';
                    explainBox.innerHTML = `<b>ช่องออกตะฮีดรัล:</b> เกิดจากทรงกลม 6 ลูก<br>ขนาดช่องว่าง: <i>r</i><sub>void</sub> &approx; 0.414<i>R</i> (ใหญ่กว่า T)<br>ตัวอย่าง: Na<sup>+</sup> ใน NaCl`;
                    addLegend('#38bdf8', 'ชั้นล่าง 3 ลูก');
                    addLegend('#f59e0b', 'ชั้นบน 3 ลูก');
                    addLegend('#fb923c', 'ช่องว่างทรงแปดหน้า');
                } else if (state.holeType === 'cubic') {
                    statName.textContent = 'Cubic Hole';
                    statCN.textContent = '8';
                    statPE.textContent = 'r = 0.732 R';
                    explainBox.innerHTML = `<b>ช่องลูกบาศก์:</b> เกิดจากทรงกลม 8 ลูกเรียงแบบ SC<br>ขนาดช่องว่าง: <i>r</i><sub>void</sub> &approx; 0.732<i>R</i><br>ตัวอย่าง: Cs<sup>+</sup> ใน CsCl`;
                    addLegend('#38bdf8', 'มุมล่าง 4 ลูก');
                    addLegend('#f59e0b', 'มุมบน 4 ลูก');
                    addLegend('#f43f5e', 'ช่องว่างลูกบาศก์');
                }
            } else if (state.currentTab === 'unitcells') {
                if (state.metallicType === 'sc') {
                    statName.textContent = 'Simple Cubic';
                    statCN.textContent = '6';
                    statPE.textContent = '52.38%';
                    explainBox.innerHTML = `<b>SC:</b> อะตอมอยู่ที่มุม 8 มุม (รวม 1 อะตอม)<br>ความสัมพันธ์: <i>a</i> = 2<i>r</i><br>จัดเรียงหลวม พบได้ยาก`;
                    addLegend('#38bdf8', 'อะตอมที่มุม');
                } else if (state.metallicType === 'bcc') {
                    statName.textContent = 'Body-Centred Cubic';
                    statCN.textContent = '8';
                    statPE.textContent = '68.04%';
                    explainBox.innerHTML = `<b>BCC:</b> มุม 8 จุด + กลางเซลล์ 1 (รวม 2 อะตอม)<br>ความสัมพันธ์: <i>a</i>&radic;3 = 4<i>r</i>`;
                    addLegend('#38bdf8', 'อะตอมที่มุม');
                    addLegend('#f59e0b', 'กลางยูนิตเซลล์');
                } else if (state.metallicType === 'fcc') {
                    statName.textContent = 'Face-Centred Cubic';
                    statCN.textContent = '12';
                    statPE.textContent = '74.08%';
                    explainBox.innerHTML = `<b>FCC:</b> มุม 8 จุด + กลางหน้า 6 (รวม 4 อะตอม)<br>ความสัมพันธ์: <i>a</i>&radic;2 = 4<i>r</i><br>แข็งแรงและเสถียรที่สุด`;
                    addLegend('#38bdf8', 'อะตอมที่มุม');
                    addLegend('#f59e0b', 'อะตอมผิวหน้า');
                }
            } else if (state.currentTab === 'ionic') {
                if (state.ionicType === 'nacl') {
                    statName.textContent = 'Rock Salt (NaCl)';
                    statCN.textContent = '6 : 6';
                    statPE.textContent = 'n = 4';
                    explainBox.innerHTML = `<b>NaCl:</b> Cl<sup>-</sup> เป็น FCC, Na<sup>+</sup> ในช่อง Octahedral ทั้งหมด<br>อัตราส่วนรัศมี <i>r</i><sub>+</sub>/<i>r</i><sub>-</sub> = 0.414 - 0.732`;
                    addLegend('#22c55e', 'Cl- (FCC)');
                    addLegend('#a855f7', 'Na+ (Octahedral)');
                } else if (state.ionicType === 'cscl') {
                    statName.textContent = 'Cesium Chloride';
                    statCN.textContent = '8 : 8';
                    statPE.textContent = 'n = 1';
                    explainBox.innerHTML = `<b>CsCl:</b> Cl<sup>-</sup> เป็น SC, Cs<sup>+</sup> อยู่กลางเซลล์ (Cubic)<br>อัตราส่วนรัศมี <i>r</i><sub>+</sub>/<i>r</i><sub>-</sub> > 0.732`;
                    addLegend('#22c55e', 'Cl- (SC)');
                    addLegend('#e11d48', 'Cs+ (Cubic)');
                } else if (state.ionicType === 'zns') {
                    statName.textContent = 'Zinc Blende';
                    statCN.textContent = '4 : 4';
                    statPE.textContent = 'n = 4';
                    explainBox.innerHTML = `<b>ZnS:</b> S<sup>2-</sup> เป็น FCC, Zn<sup>2+</sup> ในช่อง Tetrahedral ครึ่งเดียว<br>อัตราส่วนรัศมี <i>r</i><sub>+</sub>/<i>r</i><sub>-</sub> = 0.225 - 0.414`;
                    addLegend('#eab308', 'S2- (FCC)');
                    addLegend('#06b6d4', 'Zn2+ (Tetrahedral 50%)');
                } else if (state.ionicType === 'caf2') {
                    statName.textContent = 'Fluorite';
                    statCN.textContent = '8 : 4';
                    statPE.textContent = 'n = 4';
                    explainBox.innerHTML = `<b>CaF<sub>2</sub>:</b> Ca<sup>2+</sup> เป็น FCC, F<sup>-</sup> ในช่อง Tetrahedral ทั้งหมด<br>อัตราส่วน Ca<sup>2+</sup> : F<sup>-</sup> = 1 : 2`;
                    addLegend('#6366f1', 'Ca2+ (FCC)');
                    addLegend('#14b8a6', 'F- (Tetrahedral 100%)');
                }
            }
        }"""

# Replace the whole updateUIInfo function
content = re.sub(r'function updateUIInfo\(\) \{.*?(?=// ================= EVENT LISTENERS =================)', js_new_updateUIInfo + '\n\n        ', content, flags=re.DOTALL)

# Remove badgeText logic from tabs event listener
content = re.sub(r'const badgeText = document.getElementById\(\'badgeText\'\);.*?renderPingPongPacking\(\);', 'renderPingPongPacking();', content, flags=re.DOTALL)
content = re.sub(r'badgeText\.textContent = \'โหมด: เจาะลึกชนิดช่องว่าง \(Isolated Void Explorer\)\';', '', content)
content = re.sub(r'badgeText\.textContent = \'โหมด: ยูนิตเซลล์โลหะ \(Metallic Unit Cells\)\';', '', content)
content = re.sub(r'badgeText\.textContent = \'โหมด: สารประกอบไอออนิก \(Ionic Compounds\)\';', '', content)

with open('/Users/panaoonchuayboonsong/Desktop/untitled folder/dammm.html', 'w', encoding='utf-8') as f:
    f.write(content)


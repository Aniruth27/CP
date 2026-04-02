import os
import re

# Same replacements as before
desktop_megamenu = """                <div class="relative group py-4">
                    <a href="products.html"
                        class="text-slate-900 font-medium hover:text-primary transition-colors relative flex items-center gap-1 after:content-[''] after:absolute after:bottom-0 after:left-0 after:h-0.5 after:bg-primary after:transition-all after:duration-300 after:w-0 group-hover:after:w-full group-hover:text-primary">
                        Products
                        <i data-lucide="chevron-down" class="w-4 h-4 transition-transform group-hover:rotate-180"></i>
                    </a>
                    
                    <!-- Mega Menu -->
                    <div class="absolute top-full left-1/2 -translate-x-1/2 w-[900px] bg-white shadow-2xl rounded-xl border border-slate-100 p-8 invisible opacity-0 translate-y-4 group-hover:visible group-hover:opacity-100 group-hover:translate-y-0 transition-all duration-300 z-50">
                        <div class="grid grid-cols-4 gap-8">
                            <!-- Category: Polycarbonate -->
                            <div class="space-y-4">
                                <h4 class="text-primary font-bold text-sm uppercase tracking-wider flex items-center gap-2">
                                    <span class="w-2 h-2 bg-primary rounded-full"></span>
                                    Polycarbonate
                                </h4>
                                <ul class="space-y-2">
                                    <li><a href="polycarbonate-solid-sheet-and-roll.html" class="text-sm text-slate-600 hover:text-primary hover:translate-x-1 transition-all block">PC Solid Sheet & Roll</a></li>
                                    <li><a href="polycarbonate-multiwall-sheet.html" class="text-sm text-slate-600 hover:text-primary hover:translate-x-1 transition-all block">PC Multiwall Sheet</a></li>
                                    <li><a href="polycarbonate-profile-sheet.html" class="text-sm text-slate-600 hover:text-primary hover:translate-x-1 transition-all block">PC Profile Sheet</a></li>
                                </ul>
                                
                                <h4 class="text-primary font-bold text-sm uppercase tracking-wider pt-2 flex items-center gap-2">
                                    <span class="w-2 h-2 bg-primary rounded-full"></span>
                                    Acrylic (PMMA)
                                </h4>
                                <ul class="space-y-2">
                                    <li><a href="acrylic-pmma-sheets.html" class="text-sm text-slate-600 hover:text-primary hover:translate-x-1 transition-all block">Acrylic PMMA Sheets</a></li>
                                    <li><a href="acrylic-pmma-tubes.html" class="text-sm text-slate-600 hover:text-primary hover:translate-x-1 transition-all block">Acrylic PMMA Tubes</a></li>
                                    <li><a href="acrylic-pmma-rods.html" class="text-sm text-slate-600 hover:text-primary hover:translate-x-1 transition-all block">Acrylic PMMA Rods</a></li>
                                </ul>
                            </div>

                            <!-- Category: Polypropylene & HDPE -->
                            <div class="space-y-4">
                                <h4 class="text-primary font-bold text-sm uppercase tracking-wider flex items-center gap-2">
                                    <span class="w-2 h-2 bg-primary rounded-full"></span>
                                    Polypropylene
                                </h4>
                                <ul class="space-y-2">
                                    <li><a href="polypropylene-corrugated-sheets.html" class="text-sm text-slate-600 hover:text-primary hover:translate-x-1 transition-all block">PP Corrugated Sheets</a></li>
                                    <li><a href="pp-h–polypropylene.html" class="text-sm text-slate-600 hover:text-primary hover:translate-x-1 transition-all block">PP-H Polypropylene</a></li>
                                    <li><a href="polypropylene-sheets-and-rods.html" class="text-sm text-slate-600 hover:text-primary hover:translate-x-1 transition-all block">PP Polypropylene</a></li>
                                </ul>

                                <h4 class="text-primary font-bold text-sm uppercase tracking-wider pt-2 flex items-center gap-2">
                                    <span class="w-2 h-2 bg-primary rounded-full"></span>
                                    High Density PE
                                </h4>
                                <ul class="space-y-2">
                                    <li><a href="hdpe-polyethylene-sheets-rods.html" class="text-sm text-slate-600 hover:text-primary hover:translate-x-1 transition-all block">HDPE Sheets & Rods</a></li>
                                    <li><a href="uhmw-polyethylene-sheets-rods.html" class="text-sm text-slate-600 hover:text-primary hover:translate-x-1 transition-all block">UHMW-PE Sheets & Rods</a></li>
                                </ul>
                            </div>

                            <!-- Category: Engineering Plastics -->
                            <div class="space-y-4">
                                <h4 class="text-primary font-bold text-sm uppercase tracking-wider flex items-center gap-2">
                                    <span class="w-2 h-2 bg-primary rounded-full"></span>
                                    Eng. Plastics
                                </h4>
                                <ul class="space-y-2">
                                    <li><a href="pom-sheets-and-rods.html" class="text-sm text-slate-600 hover:text-primary hover:translate-x-1 transition-all block">Polyacetal (POM)</a></li>
                                    <li><a href="pa6-sheets-and-rods.html" class="text-sm text-slate-600 hover:text-primary hover:translate-x-1 transition-all block">PA6 – Polyamide</a></li>
                                    <li><a href="ptfe-sheets-and-rods.html" class="text-sm text-slate-600 hover:text-primary hover:translate-x-1 transition-all block">PTFE Sheets & Rods</a></li>
                                    <li><a href="peek-sheets-and-rods.html" class="text-sm text-slate-600 hover:text-primary hover:translate-x-1 transition-all block">PEEK Sheets & Rods</a></li>
                                    <li><a href="polyurethane-sheets-and-rods.html" class="text-sm text-slate-600 hover:text-primary hover:translate-x-1 transition-all block">Polyurethane (PU)</a></li>
                                    <li><a href="acrylonitrile-butadiene-styrene-sheets.html" class="text-sm text-slate-600 hover:text-primary hover:translate-x-1 transition-all block">ABS Sheets</a></li>
                                </ul>
                            </div>

                            <!-- Category: Industrial & Insulation -->
                            <div class="space-y-4">
                                <h4 class="text-primary font-bold text-sm uppercase tracking-wider flex items-center gap-2">
                                    <span class="w-2 h-2 bg-primary rounded-full"></span>
                                    Insulation & More
                                </h4>
                                <ul class="space-y-2">
                                    <li><a href="epoxy-glass-cloth-laminated-sheets.html" class="text-sm text-slate-600 hover:text-primary hover:translate-x-1 transition-all block">Epoxy Glass Sheets</a></li>
                                    <li><a href="phenolic-fabric-sheets-and-rods.html" class="text-sm text-slate-600 hover:text-primary hover:translate-x-1 transition-all block">Phenolic Fabric</a></li>
                                    <li><a href="phenolic-paper-sheets.html" class="text-sm text-slate-600 hover:text-primary hover:translate-x-1 transition-all block">Phenolic Paper</a></li>
                                    <li><a href="syndanio-sheets.html" class="text-sm text-slate-600 hover:text-primary hover:translate-x-1 transition-all block">Syndanio Sheets</a></li>
                                    <li><a href="bakelite-sheets.html" class="text-sm text-slate-600 hover:text-primary hover:translate-x-1 transition-all block">Bakelite Sheets</a></li>
                                    <li><a href="esd-products.html" class="text-sm text-slate-600 hover:text-primary hover:translate-x-1 transition-all block">ESD Products</a></li>
                                </ul>
                            </div>
                        </div>
                        
                        <!-- Bottom Link -->
                        <div class="mt-8 pt-6 border-t border-slate-100 flex justify-between items-center">
                            <p class="text-xs text-slate-400 font-medium">Over 25+ years of industrial expertise</p>
                            <a href="products.html" class="flex items-center gap-2 text-primary font-bold text-xs uppercase tracking-widest hover:gap-3 transition-all">
                                View All Products
                                <i data-lucide="arrow-right" class="w-4 h-4"></i>
                            </a>
                        </div>
                    </div>
                </div>"""

mobile_accordion = """                <div class="flex flex-col">
                    <button id="mobile-products-toggle"
                        class="text-3xl font-bold text-slate-900 hover:text-primary transition-colors flex items-center justify-between group py-2">
                        <span>Products</span>
                        <i data-lucide="chevron-down"
                            class="w-8 h-8 transition-transform duration-300"></i>
                    </button>
                    <div id="mobile-products-menu" class="hidden flex-col space-y-4 pl-4 pt-4 pb-2 border-l-2 border-primary/20 mt-2">
                        <div class="space-y-6">
                            <div>
                                <h4 class="text-primary font-bold text-sm uppercase tracking-wider mb-3">Polycarbonate</h4>
                                <ul class="space-y-3">
                                    <li><a href="polycarbonate-solid-sheet-and-roll.html" class="text-xl text-slate-600 hover:text-primary block italic">PC Solid Sheet & Roll</a></li>
                                    <li><a href="polycarbonate-multiwall-sheet.html" class="text-xl text-slate-600 hover:text-primary block italic">PC Multiwall Sheet</a></li>
                                    <li><a href="polycarbonate-profile-sheet.html" class="text-xl text-slate-600 hover:text-primary block italic">PC Profile Sheet</a></li>
                                </ul>
                            </div>
                            <div>
                                <h4 class="text-primary font-bold text-sm uppercase tracking-wider mb-3">Acrylic (PMMA)</h4>
                                <ul class="space-y-3">
                                    <li><a href="acrylic-pmma-sheets.html" class="text-xl text-slate-600 hover:text-primary block italic">Acrylic PMMA Sheets</a></li>
                                    <li><a href="acrylic-pmma-tubes.html" class="text-xl text-slate-600 hover:text-primary block italic">Acrylic PMMA Tubes</a></li>
                                    <li><a href="acrylic-pmma-rods.html" class="text-xl text-slate-600 hover:text-primary block italic">Acrylic PMMA Rods</a></li>
                                </ul>
                            </div>
                            <div>
                                <h4 class="text-primary font-bold text-sm uppercase tracking-wider mb-3">Polypropylene</h4>
                                <ul class="space-y-3">
                                    <li><a href="polypropylene-corrugated-sheets.html" class="text-xl text-slate-600 hover:text-primary block italic">PP Corrugated Sheets</a></li>
                                    <li><a href="pp-h–polypropylene.html" class="text-xl text-slate-600 hover:text-primary block italic">PP-H Polypropylene</a></li>
                                    <li><a href="polypropylene-sheets-and-rods.html" class="text-xl text-slate-600 hover:text-primary block italic">PP Polypropylene</a></li>
                                </ul>
                            </div>
                            <div>
                                <h4 class="text-primary font-bold text-sm uppercase tracking-wider mb-3">Engineering Plastics</h4>
                                <ul class="space-y-3">
                                    <li><a href="pom-sheets-and-rods.html" class="text-xl text-slate-600 hover:text-primary block italic">Polyacetal (POM)</a></li>
                                    <li><a href="pa6-sheets-and-rods.html" class="text-xl text-slate-600 hover:text-primary block italic">PA6 – Polyamide</a></li>
                                    <li><a href="ptfe-sheets-and-rods.html" class="text-xl text-slate-600 hover:text-primary block italic">PTFE Sheets & Rods</a></li>
                                    <li><a href="peek-sheets-and-rods.html" class="text-xl text-slate-600 hover:text-primary block italic">PEEK Sheets & Rods</a></li>
                                    <li><a href="polyurethane-sheets-and-rods.html" class="text-xl text-slate-600 hover:text-primary block italic">Polyurethane (PU)</a></li>
                                </ul>
                            </div>
                        </div>
                        <a href="products.html" class="text-primary font-bold text-lg uppercase tracking-widest pt-4 flex items-center gap-2">
                            View All Products <i data-lucide="arrow-right" class="w-5 h-5"></i>
                        </a>
                    </div>
                </div>"""

script_to_inject = """    <script>
        // Initialize Lucide Icons
        lucide.createIcons();

        // Mobile Menu Toggles
        const mobileMenuToggle = document.getElementById('mobile-menu-toggle');
        const mobileMenuClose = document.getElementById('mobile-menu-close');
        const mobileMenu = document.getElementById('mobile-menu');

        if (mobileMenuToggle && mobileMenuClose && mobileMenu) {
            mobileMenuToggle.addEventListener('click', () => {
                mobileMenu.classList.remove('translate-x-full');
            });

            mobileMenuClose.addEventListener('click', () => {
                mobileMenu.classList.add('translate-x-full');
            });
        }

        // Mobile Products Accordion
        const mobileProductsToggle = document.getElementById('mobile-products-toggle');
        const mobileProductsMenu = document.getElementById('mobile-products-menu');
        
        if (mobileProductsToggle && mobileProductsMenu) {
            const productsChevron = mobileProductsToggle.querySelector('[data-lucide="chevron-down"]');
            mobileProductsToggle.addEventListener('click', () => {
                const isHidden = mobileProductsMenu.classList.contains('hidden');
                if (isHidden) {
                    mobileProductsMenu.classList.remove('hidden');
                    mobileProductsMenu.classList.add('flex');
                    if (productsChevron) productsChevron.classList.add('rotate-180');
                } else {
                    mobileProductsMenu.classList.remove('flex');
                    mobileProductsMenu.classList.add('hidden');
                    if (productsChevron) productsChevron.classList.remove('rotate-180');
                }
            });
        }
    </script>"""

src_dir = r"c:\Users\aniru\OneDrive\Desktop\CP\CP\src"

for filename in os.listdir(src_dir):
    if filename.endswith(".html"):
        filepath = os.path.join(src_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update desktop nav
        desktop_pattern = r'                <div class="relative group py-4">.*?</div>\s*</div>'
        # Actually better to target the anchor if it hasn't been updated yet
        old_desktop = r'                <a href="products\.html"\s+class="[^"]*">Products</a>'
        if re.search(old_desktop, content):
            content = re.sub(old_desktop, desktop_megamenu, content)

        # Update mobile nav
        old_mobile = r'                <a href="products\.html"\s+class="text-3xl font-bold[^>]*>.*?<span>Products</span>.*?</a>'
        if re.search(old_mobile, content, re.DOTALL):
            content = re.sub(old_mobile, mobile_accordion, content, flags=re.DOTALL)

        # CLEANUP SCRIPTS: Remove all navigation scripts to start fresh
        content = re.sub(r'<script>\s*// Initialize Lucide icons.*?</script>', '', content, flags=re.DOTALL)
        content = re.sub(r'<script>\s*// Initialize Lucide Icons.*?</script>', '', content, flags=re.DOTALL)
        content = re.sub(r'<script>\s*// Mobile Menu Functionality.*?</script>', '', content, flags=re.DOTALL)
        
        # Inject the single clean script
        content = content.replace('</body>', script_to_inject + '\n</body>')

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Cleanup and Updates complete.")

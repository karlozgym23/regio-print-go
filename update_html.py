import re

filepath = '/Users/carlosmartinez/Desktop/regio-print-go/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. HERO HEADLINE
old_hero_headline = 'La imagen que tu <span class="text-brand-lime">negocio</span> merece'
new_hero_headline = 'Lonas, tarjetas y volantes en Monterrey — listos en 24 hrs'
html = html.replace(old_hero_headline, new_hero_headline)

old_hero_sub = 'Tarjetas, volantes, lonas y papelería profesional para negocios en Monterrey. Cotiza fácil y\n                        rápido por WhatsApp.'
new_hero_sub = 'Cotiza por WhatsApp en 1 minuto. Sin locales que visitar. Producción profesional con entrega a domicilio en toda el Área Metropolitana.'
html = html.replace(old_hero_sub, new_hero_sub)

html = html.replace(
    'Cotiza en 1 minuto por WhatsApp <i class="fab fa-whatsapp text-xl"></i>',
    'Quiero mi cotización ahora <i class="fab fa-whatsapp text-xl"></i>'
)

# 2. TRUST BAR & 3. LONAS SECTION
trust_and_lonas = """
        <!-- Trust Bar -->
        <section class="py-6 bg-white border-b border-gray-100 w-full animate-on-scroll">
            <div class="container mx-auto px-4 md:px-6">
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6 text-center font-bold text-brand-dark">
                    <div class="flex items-center justify-center gap-3">
                        <i class="fas fa-box text-brand-lime text-xl"></i>
                        <span>500+ pedidos entregados</span>
                    </div>
                    <div class="flex items-center justify-center gap-3">
                        <i class="fas fa-bolt text-brand-lime text-xl"></i>
                        <span>Entrega en 24-48 hrs</span>
                    </div>
                    <div class="flex items-center justify-center gap-3">
                        <i class="fas fa-map-location-dot text-brand-lime text-xl"></i>
                        <span>Área Metropolitana MTY</span>
                    </div>
                </div>
            </div>
        </section>

        <!-- Sección Lonas -->
        <section id="lonas" class="py-16 md:py-24 bg-brand-light w-full animate-on-scroll">
            <div class="container mx-auto px-4 md:px-6 max-w-4xl">
                <div class="bg-white rounded-2xl md:rounded-3xl p-8 md:p-12 shadow-sm border border-gray-100 text-center">
                    <h2 class="text-3xl md:text-4xl font-black text-brand-dark mb-4">Lonas Publicitarias en Monterrey</h2>
                    <p class="text-gray-500 mb-8 max-w-2xl mx-auto text-lg">Desde $180/m². Cualquier medida. Te ayudamos a calcularla en minutos por WhatsApp.</p>
                    
                    <div class="mb-8">
                        <p class="text-5xl font-black text-brand-lime mb-2">Desde $180/m²</p>
                        <p class="text-sm font-bold text-brand-dark">Incluye diseño básico</p>
                        <p class="text-xs text-gray-500 mt-1">Ejemplo: 3m × 1m = $540 aprox.</p>
                    </div>

                    <ul class="text-left text-sm space-y-3 mb-8 max-w-md mx-auto font-medium text-gray-600">
                        <li class="flex items-center gap-3"><i class="fas fa-check text-brand-lime text-lg"></i> Impresión de alta calidad</li>
                        <li class="flex items-center gap-3"><i class="fas fa-check text-brand-lime text-lg"></i> Material resistente para exterior</li>
                        <li class="flex items-center gap-3"><i class="fas fa-check text-brand-lime text-lg"></i> Incluye diseño básico</li>
                        <li class="flex items-center gap-3"><i class="fas fa-check text-brand-lime text-lg"></i> Entrega en Monterrey y Área Metropolitana</li>
                        <li class="flex items-center gap-3"><i class="fas fa-check text-brand-lime text-lg"></i> Respuesta en menos de 1 hora</li>
                    </ul>

                    <p class="text-brand-dark font-bold mb-6">¿La necesitas rápido? Escríbenos hoy y te confirmamos tiempo de entrega.</p>

                    <a href="https://wa.me/528120364198?text=Hola%2C%20quiero%20cotizar%20una%20lona.%20Mi%20medida%20aproximada%20es%20___%20x%20___%20metros." target="_blank" rel="noopener noreferrer" class="w-full md:w-auto inline-flex px-8 py-4 bg-brand-lime text-brand-dark font-black rounded-full hover:shadow-lg transition justify-center items-center gap-2 mb-3">
                        Calcular mi lona por WhatsApp <i class="fab fa-whatsapp text-xl"></i>
                    </a>
                    <p class="text-xs text-gray-400">Respuesta rápida en horario laboral · Lun-Vie 9am–6pm</p>
                </div>
            </div>
        </section>
"""
html = html.replace('</section>\n\n        <!-- 3. Ventajas -->', '</section>\n' + trust_and_lonas + '\n        <!-- 3. Ventajas -->')

# 4. NAVIGATION MENU
html = html.replace(
    '<a href="#ventajas" class="text-gray-600 hover:text-brand-lime transition">Ventajas</a>',
    '<a href="#lonas" class="text-gray-600 hover:text-brand-lime transition">Lonas</a>\n                <a href="#ventajas" class="text-gray-600 hover:text-brand-lime transition">Ventajas</a>'
)

html = html.replace(
    '<a href="#ventajas"\n            class="mobile-link text-2xl font-bold text-white hover:text-brand-lime transition">Ventajas</a>',
    '<a href="#lonas"\n            class="mobile-link text-2xl font-bold text-white hover:text-brand-lime transition">Lonas</a>\n        <a href="#ventajas"\n            class="mobile-link text-2xl font-bold text-white hover:text-brand-lime transition">Ventajas</a>'
)

# 5. MERGE SERVICE SECTIONS
extra_match = re.search(r'<!-- SECCIÓN: SERVICIOS DE IMPRESIÓN \(EXTRA\) -->\n        <section id="servicios-extra".*?<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">\n(.*?)\n                </div>\n            </div>\n        </section>', html, re.DOTALL)
if extra_match:
    extra_cards = extra_match.group(1)
    insert_target = '                    <!-- Added an extra space intentionally empty or skip -->'
    html = html.replace(insert_target, extra_cards + '\n' + insert_target)
    html = re.sub(r'<!-- SECCIÓN: SERVICIOS DE IMPRESIÓN \(EXTRA\) -->\n        <section id="servicios-extra".*?</section>', '', html, flags=re.DOTALL)

# 6. FAQ FIX
html = html.replace(
    'Nos enfocamos en\n                            impresión. Requerimos tu archivo listo.',
    'Sí incluimos diseño básico en todos nuestros paquetes. Para pedidos individuales contáctanos por WhatsApp y te indicamos las opciones disponibles.'
)

# 7. TESTIMONIALS
quote_p_pattern = r'<p class="text-gray-600 mb-6 relative z-10 italic">"Nos ayudaron'
html = html.replace(
    '<p class="text-gray-600 mb-6 relative z-10 italic">"Nos ayudaron',
    '<div class="text-brand-lime text-sm mb-4">★★★★★</div>\n                        <p class="text-gray-600 mb-6 relative z-10 italic">"Nos ayudaron'
)

quote_p2 = r'<p class="text-gray-600 mb-6 relative z-10 italic">"El proceso fue rápido'
html = html.replace(
    quote_p2,
    '<div class="text-brand-lime text-sm mb-4">★★★★★</div>\n                        ' + quote_p2
)

quote_p3 = r'<p class="text-gray-600 mb-6 relative z-10 italic">"Las tarjetas y materiales se ven'
html = html.replace(
    quote_p3,
    '<div class="text-brand-lime text-sm mb-4">★★★★★</div>\n                        ' + quote_p3
)

html = html.replace('Cliente – Consultorio Médico', 'Dr. García – Consultorio Médico')
html = html.replace('Cliente – Clínica Dental', 'Dr. Martínez – Clínica Dental')
html = html.replace('Cliente – Despacho de Arquitectura', 'Arq. Rodríguez – Despacho de Arquitectura')

# 8. CONTACT SECTION
old_contact_right = """<div class="bg-white/5 p-6 md:p-8 rounded-2xl border border-white/10">
                            <form class="space-y-4 flex flex-col">
                                <div>
                                    <label
                                        class="block text-xs font-bold text-brand-lime mb-2 uppercase tracking-wide">Nombre</label>
                                    <input type="text" id="nombre-contacto" placeholder="Tu nombre"
                                        class="w-full bg-brand-dark/50 border border-white/20 rounded-lg px-4 py-3 outline-none focus:border-brand-lime text-white transition">
                                </div>
                                <div>
                                    <label
                                        class="block text-xs font-bold text-brand-lime mb-2 uppercase tracking-wide">Tu WhatsApp (para cotizarte directo)</label>
                                    <input type="tel" id="telefono-contacto" inputmode="numeric" placeholder="Ej: 8112345678"
                                        class="w-full bg-brand-dark/50 border border-white/20 rounded-lg px-4 py-3 outline-none focus:border-brand-lime text-white transition">
                                </div>
                                <a href="https://wa.me/528120364198" target="_blank" rel="noopener noreferrer" id="whatsapp-submit"
                                    class="w-full py-4 bg-brand-lime text-brand-dark font-black rounded-xl mt-4 hover:opacity-90 flex justify-center items-center gap-2 shadow-lg">Cotizar
                                    por WhatsApp <i class="fab fa-whatsapp text-lg"></i></a>
                            </form>
                        </div>"""

new_contact_right = """<div class="bg-white/5 p-6 md:p-8 rounded-2xl border border-white/10 text-center flex flex-col justify-center">
                            <div class="hidden">
                                <span id="whatsapp-submit"></span>
                                <input type="hidden" id="nombre-contacto">
                                <input type="hidden" id="telefono-contacto">
                            </div>
                            <h3 class="text-2xl font-black text-white mb-2">¿Listo para cotizar?</h3>
                            <p class="text-sm text-gray-400 mb-6">Escríbenos ahora y recibe respuesta en menos de 1 hora.</p>
                            <a href="https://wa.me/528120364198?text=Hola%2C%20quiero%20cotizar%20impresi%C3%B3n%20para%20mi%20negocio%20en%20Monterrey." target="_blank" rel="noopener noreferrer" class="w-full py-4 bg-brand-lime text-brand-dark font-black rounded-xl hover:opacity-90 flex justify-center items-center gap-2 shadow-lg mb-4">
                                Iniciar cotización por WhatsApp <i class="fab fa-whatsapp text-lg"></i>
                            </a>
                            <p class="text-xs text-gray-500">Lun-Vie 9am–6pm · +52 81 2036 4198</p>
                        </div>"""
html = html.replace(old_contact_right, new_contact_right)

# 9. URGENCY BANNER IN #PAQUETES
banner = """
                <div class="bg-brand-lime/20 border border-brand-lime/30 text-brand-lime font-bold text-sm rounded-xl px-6 py-3 text-center mb-8 mx-auto max-w-2xl">
                    ⚡ Producción disponible esta semana — confirma tu pedido hoy
                </div>
"""
html = html.replace(
    'marcas que quieren vender más en Monterrey.</p>\n                </div>\n                <div class="grid grid-cols-1 md:grid-cols-3 gap-6 relative z-10">',
    'marcas que quieren vender más en Monterrey.</p>\n                </div>' + banner + '                <div class="grid grid-cols-1 md:grid-cols-3 gap-6 relative z-10">'
)

# 10. FOOTER
footer_addition = """<p class="text-sm text-gray-500">Impresión Premium en Monterrey.</p>
                <p class="text-sm text-gray-500">Lun-Vie 9:00am – 6:00pm</p>
                <p class="text-sm text-gray-500">+52 81 2036 4198</p>
                <p class="text-sm text-gray-500">contacto@regioprintgo.com</p>"""
html = html.replace('<p class="text-sm text-gray-500">Impresión Premium en Monterrey.</p>', footer_addition)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
print("SUCCESS")

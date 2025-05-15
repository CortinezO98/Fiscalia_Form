categorias = [
    # Categorías para la tipificación 1
    {
        "id": 1,
        "nombre":"Sicecon",
        "nivel":1,
        "tipificacion_id":1,
        "categoria_padre_id":None,
    },
    {
        "id": 2,
        "nombre":"Denuncia fácil",
        "nivel":1,
        "tipificacion_id":1,
        "categoria_padre_id":None,
    },
    
    # Categorías para la tipificación 2
    {
        "id": 3,
        "nombre":"Se corrige el relato y se clasifica",
        "nivel":1,
        "tipificacion_id":2,
        "categoria_padre_id":None,
    },
    {
        "id": 4,
        "nombre":"Solo se clasifica la denuncia",
        "nivel":1,
        "tipificacion_id":2,
        "categoria_padre_id":None,
    },
    
    # Categorías para la tipificación 3
    {
        "id": 5,
        "nombre": "Orientación para interponer denuncia",
        "nivel": 1,
        "tipificacion_id": 3,
        "categoria_padre_id": None
    },
    {
        "id": 6,
        "nombre": "Orientación para interponer PQRS",
        "nivel": 1,
        "tipificacion_id": 3,
        "categoria_padre_id": None
    },
    {
        "id": 7,
        "nombre": "Información denuncia y despacho asignado",
        "nivel": 1,
        "tipificacion_id": 3,
        "categoria_padre_id": None
    },
    {
        "id": 8,
        "nombre": "Orientación e información general",
        "nivel": 1,
        "tipificacion_id": 3,
        "categoria_padre_id": None
    },
    {
        "id": 9,
        "nombre": "Orientación para perdida de documentos",
        "nivel": 1,
        "tipificacion_id": 3,
        "categoria_padre_id": None
    },
    
    # Subcategorías de ID 5 ("Orientación para interponer denuncia")
    
    {
        "id": 10,
        "nombre": "Link Suip- autogestión denuncia.",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 5
    },
    {
        "id": 11,
        "nombre": "Formulario denuncia fácil",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 5
    },
    {
        "id": 12,
        "nombre": "Comisaria, inspección u otros",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 5
    },

    # Subcategorías de ID 6 ("Orientación para interponer PQRS")
    {
        "id": 13,
        "nombre": "Orientación SUSI - Página Web",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 6
    },
    {
        "id": 14,
        "nombre": "Orientación Correo",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 6
    },
    
    
    
    
    
    
    
    
    # Categorías para la tipificación 4 (PQRS)
    {
        "id": 15,
        "nombre": "Petición",
        "nivel": 1,
        "tipificacion_id": 4,
        "categoria_padre_id": None
    },
    {
        "id": 16,
        "nombre": "Queja",
        "nivel": 1,
        "tipificacion_id": 4,
        "categoria_padre_id": None
    },
    {
        "id": 17,
        "nombre": "Reclamo",
        "nivel": 1,
        "tipificacion_id": 4,
        "categoria_padre_id": None
    },
    {
        "id": 18,
        "nombre": "Sugerencia",
        "nivel": 1,
        "tipificacion_id": 4,
        "categoria_padre_id": None
    },
    {
        "id": 19,
        "nombre": "Felicitación",
        "nivel": 1,
        "tipificacion_id": 4,
        "categoria_padre_id": None
    },
    {
        "id": 20,
        "nombre": "Solicitud copia de la denuncia",
        "nivel": 1,
        "tipificacion_id": 4,
        "categoria_padre_id": None
    },
    {
        "id": 21,
        "nombre": "Reclamo por falta de rta a PQRS",
        "nivel": 1,
        "tipificacion_id": 4,
        "categoria_padre_id": None
    },
    
    
    
    
    
    
    
    
    # Categorías para la tipificación 5 (Transferencias)
    {
        "id": 22,
        "nombre": "Transferencia a Nivel 1",
        "nivel": 1,
        "tipificacion_id": 5,
        "categoria_padre_id": None
    },
    {
        "id": 23,
        "nombre": "Transferencia a Nivel 2",
        "nivel": 1,
        "tipificacion_id": 5,
        "categoria_padre_id": None
    },
    {
        "id": 24,
        "nombre": "Transferencia Creadores de denuncia",
        "nivel": 1,
        "tipificacion_id": 5,
        "categoria_padre_id": None
    },
    {
        "id": 25,
        "nombre": "Transferencia a Abogados",
        "nivel": 1,
        "tipificacion_id": 5,
        "categoria_padre_id": None
    },
    {
        "id": 26,
        "nombre": "Transferencia a Psicologia",
        "nivel": 1,
        "tipificacion_id": 5,
        "categoria_padre_id": None
    },
    {
        "id": 27,
        "nombre": "Transferencia a Justicia Transicional",
        "nivel": 1,
        "tipificacion_id": 5,
        "categoria_padre_id": None
    },
    {
        "id": 28,
        "nombre": "Transferencia Agente Bilingüe",
        "nivel": 1,
        "tipificacion_id": 5,
        "categoria_padre_id": None
    },
    
    
    
    
    
    # Categorías para la tipificación 6 (Agendamiento Sala Presencial)
    {
        "id": 29,
        "nombre": "Cancelar Cita",
        "nivel": 1,
        "tipificacion_id": 6,
        "categoria_padre_id": None
    },
    {
        "id": 30,
        "nombre": "Agendar Cita",
        "nivel": 1,
        "tipificacion_id": 6,
        "categoria_padre_id": None
    },
    
    
    
    
    
    
    # Categorías para la tipificación 7 (Requiere presencia Inmediata de la Policía)
    
    {
        "id": 31,
        "nombre": "Solicita Presencia Inmediata de Policia",
        "nivel": 1,
        "tipificacion_id": 7,
        "categoria_padre_id": None
    },
    {
        "id": 32,
        "nombre": "Solicita presencia de Policía pero (No está en riesgo la vida o la integridad)",
        "nivel": 1,
        "tipificacion_id": 7,
        "categoria_padre_id": None
    },
    # Subcategorías de ID 31 ("Solicita Presencia Inmediata de Policia")
    {
        "id": 33,
        "nombre": "Presencia exitosa",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 31
    },
    {
        "id": 34,
        "nombre": "Transfiere a 123 u otra entidad",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 31
    },
    {
        "id": 35,
        "nombre": "Solicita presencia de Policía pero (No está en riesgo la vida o la integridad de la víctima o no es penal)",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 32
    },
    
    
    
    
    # Categorías para la tipificación 8 (Llamadas ociosas)
    {
        "id": 36,
        "nombre": "Llamada Equivocada",
        "nivel": 1,
        "tipificacion_id": 8,
        "categoria_padre_id": None
    },
    {
        "id": 37,
        "nombre": "Llamada Colgada",
        "nivel": 1,
        "tipificacion_id": 8,
        "categoria_padre_id": None
    },
    {
        "id": 38,
        "nombre": "Llamada Muda",
        "nivel": 1,
        "tipificacion_id": 8,
        "categoria_padre_id": None
    },
    {
        "id": 39,
        "nombre": "Llamada de Broma",
        "nivel": 1,
        "tipificacion_id": 8,
        "categoria_padre_id": None
    },
    {
        "id": 40,
        "nombre": "Llamada Caida",
        "nivel": 1,
        "tipificacion_id": 8,
        "categoria_padre_id": None
    },
    {
        "id": 41,
        "nombre": "Llamada de Prueba",
        "nivel": 1,
        "tipificacion_id": 8,
        "categoria_padre_id": None
    },
    
    
    
    
    # Categorías para la tipificación 9 (Solicitud copia de denuncia)
    {
        "id": 42,
        "nombre": "Presencial",
        "nivel": 1,
        "tipificacion_id": 9,
        "categoria_padre_id": None
    },
    {
        "id": 43,
        "nombre": "Denuncia fácil",
        "nivel": 1,
        "tipificacion_id": 9,
        "categoria_padre_id": None
    },
    {
        "id": 44,
        "nombre": "Telefónico",
        "nivel": 1,
        "tipificacion_id": 9,
        "categoria_padre_id": None
    },
    {
        "id": 45,
        "nombre": "Link Suip",
        "nivel": 1,
        "tipificacion_id": 9,
        "categoria_padre_id": None
    },
    {
        "id": 46,
        "nombre": "ADenunciar",
        "nivel": 1,
        "tipificacion_id": 9,
        "categoria_padre_id": None
    },
    
    
    
    
    
    # Categorías para la tipificación 10 (OUTBOUND)
    {
        "id": 47,
        "nombre": "Outbound Denuncia",
        "nivel": 1,
        "tipificacion_id": 10,
        "categoria_padre_id": None
    },
    {
        "id": 48,
        "nombre": "Outbound PQRS",
        "nivel": 1,
        "tipificacion_id": 10,
        "categoria_padre_id": None
    },
    {
        "id": 49,
        "nombre": "Outbound Orientacion, Informacion  y Consulta de Casos",
        "nivel": 1,
        "tipificacion_id": 10,
        "categoria_padre_id": None
    },
    {
        "id": 50,
        "nombre": "Outbound Proceso clasificación denuncia",
        "nivel": 1,
        "tipificacion_id": 10,
        "categoria_padre_id": None
    },
    {
        "id": 51,
        "nombre": "Outbound Presencia inmediata de policia",
        "nivel": 1,
        "tipificacion_id": 10,
        "categoria_padre_id": None
    },
    {
        "id": 52,
        "nombre": "Outbound Desaparecidos",
        "nivel": 1,
        "tipificacion_id": 10,
        "categoria_padre_id": None
    },
    {
        "id": 53,
        "nombre": "Outbound No Efectivo",
        "nivel": 1,
        "tipificacion_id": 10,
        "categoria_padre_id": None
    },
    {
        "id": 54,
        "nombre": "Outbound agendamiento presencial",
        "nivel": 1,
        "tipificacion_id": 10,
        "categoria_padre_id": None
    },
    
    
    
    
    
    # Categorías para la tipificación 11 (Denuncia)
    {
        "id": 55,
        "nombre": "Sicecon",
        "nivel": 1,
        "tipificacion_id": 11,
        "categoria_padre_id": None
    },
    {
        "id": 56,
        "nombre": "Denuncia fácil",
        "nivel": 1,
        "tipificacion_id": 11,
        "categoria_padre_id": None
    },


    
    
    # Categorías para la tipificación 12 (Clasificación de denuncia)
    {
        "id": 57,
        "nombre": "Se corrige el relato y se clasifica",
        "nivel": 1,
        "tipificacion_id": 12,
        "categoria_padre_id": None
    },
    {
        "id": 58,
        "nombre": "Solo se clasifica la denuncia",
        "nivel": 1,
        "tipificacion_id": 12,
        "categoria_padre_id": None
    },
    
    
    
    # Categorías de nivel 1 para tipificacion_id = 13 (Orientacion, informacion y consulta de casos)
    {
        "id": 59,
        "nombre": "Orientación para interponer denuncia",
        "nivel": 1,
        "tipificacion_id": 13,
        "categoria_padre_id": None
    },
    {
        "id": 60,
        "nombre": "Orientación para interponer PQRS",
        "nivel": 1,
        "tipificacion_id": 13,
        "categoria_padre_id": None
    },
    {
        "id": 61,
        "nombre": "Información denuncia y despacho asignado",
        "nivel": 1,
        "tipificacion_id": 13,
        "categoria_padre_id": None
    },
    {
        "id": 62,
        "nombre": "Orientación e información general",
        "nivel": 1,
        "tipificacion_id": 13,
        "categoria_padre_id": None
    },
    {
        "id": 63,
        "nombre": "Orientación para perdida de documentos",
        "nivel": 1,
        "tipificacion_id": 13,
        "categoria_padre_id": None
    },
    
    # Subcategorías de ID 59 ("Orientación para interponer denuncia")
    {
        "id": 64,
        "nombre": "Link Suip- autogestión denuncia.",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 59
    },
    {
        "id": 65,
        "nombre": "Formulario denuncia fácil",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 59
    },
    {
        "id": 66,
        "nombre": "Comisaria, inspección u otros",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 59
    },

    # Subcategorías de ID 60 ("Orientación para interponer PQRS")
    {
        "id": 67,
        "nombre": "Orientación SUSI - Página Web",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 60
    },
    {
        "id": 68,
        "nombre": "Orientación Correo",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 60
    },
    
    
    
    
    # Categorías de nivel 1 para la tipificación PQRS (tipificacion_id = 14)
    
    {
        "id": 69,
        "nombre": "Petición",
        "nivel": 1,
        "tipificacion_id": 14,
        "categoria_padre_id": None
    },
    {
        "id": 70,
        "nombre": "Queja",
        "nivel": 1,
        "tipificacion_id": 14,
        "categoria_padre_id": None
    },
    {
        "id": 71,
        "nombre": "Reclamo",
        "nivel": 1,
        "tipificacion_id": 14,
        "categoria_padre_id": None
    },
    {
        "id": 72,
        "nombre": "Sugerencia",
        "nivel": 1,
        "tipificacion_id": 14,
        "categoria_padre_id": None
    },
    {
        "id": 73,
        "nombre": "Felicitación",
        "nivel": 1,
        "tipificacion_id": 14,
        "categoria_padre_id": None
    },
    {
        "id": 74,
        "nombre": "Solicitud copia de la denuncia",
        "nivel": 1,
        "tipificacion_id": 14,
        "categoria_padre_id": None
    },
    {
        "id": 75,
        "nombre": "Reclamo por falta de rta a PQRS",
        "nivel": 1,
        "tipificacion_id": 14,
        "categoria_padre_id": None
    },
    
    
    
    # Categorías de nivel 1 para la tipificación Transferencias (tipificacion_id = 15)
    
    {
        "id": 76,
        "nombre": "Transferencia a Nivel 1",
        "nivel": 1,
        "tipificacion_id": 15,
        "categoria_padre_id": None
    },
    {
        "id": 77,
        "nombre": "Transferencia a Nivel 2",
        "nivel": 1,
        "tipificacion_id": 15,
        "categoria_padre_id": None
    },
    {
        "id": 78,
        "nombre": "Transferencia Creadores de denuncia",
        "nivel": 1,
        "tipificacion_id": 15,
        "categoria_padre_id": None
    },
    {
        "id": 79,
        "nombre": "Transferencia a Abogados",
        "nivel": 1,
        "tipificacion_id": 15,
        "categoria_padre_id": None
    },
    {
        "id": 80,
        "nombre": "Transferencia a Psicologia",
        "nivel": 1,
        "tipificacion_id": 15,
        "categoria_padre_id": None
    },
    {
        "id": 81,
        "nombre": "Transferencia a Justicia Transicional",
        "nivel": 1,
        "tipificacion_id": 15,
        "categoria_padre_id": None
    },
    {
        "id": 82,
        "nombre": "Transferencia Agente Bilingüe",
        "nivel": 1,
        "tipificacion_id": 15,
        "categoria_padre_id": None
    },
    
    
    
    # categorías de nivel 1 para la tipificación Agendamiento Sala Presencial (tipificacion_id = 16)
    
    {
        "id": 83,
        "nombre": "Cancelar Cita",
        "nivel": 1,
        "tipificacion_id": 16,
        "categoria_padre_id": None
    },
    {
        "id": 84,
        "nombre": "Agendar Cita",
        "nivel": 1,
        "tipificacion_id": 16,
        "categoria_padre_id": None
    },

    
    
    
    # Categorías de nivel 1 para la tipificación Requiere presencia Inmediata de la Policía (tipificacion_id = 17)
    {
        "id": 85,
        "nombre": "Solicita Presencia Inmediata de Policia",
        "nivel": 1,
        "tipificacion_id": 17,
        "categoria_padre_id": None
    },
    {
        "id": 86,
        "nombre": "Solicita presencia de Policía pero (No está en riesgo la vida o la integridad)",
        "nivel": 1,
        "tipificacion_id": 17,
        "categoria_padre_id": None
    },
    
    # Subcategorías de ID 85
    
    {
        "id": 87,
        "nombre": "Presencia exitosa",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 85
    },
    {
        "id": 88,
        "nombre": "Transfiere a 123 u otra entidad",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 85
    },

    # Subcategoría de ID 86
    {
        "id": 89,
        "nombre": "Solicita presencia de Policía pero (No está en riesgo la vida o la integridad de la víctima o no es penal)",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 86
    },
    
    
    
    
    # Categorías de nivel 1 para la tipificación Llamadas ociosas (tipificacion_id = 18)
    
    {
        "id": 90,
        "nombre": "Llamada Equivocada",
        "nivel": 1,
        "tipificacion_id": 18,
        "categoria_padre_id": None
    },
    {
        "id": 91,
        "nombre": "Llamada Colgada",
        "nivel": 1,
        "tipificacion_id": 18,
        "categoria_padre_id": None
    },
    {
        "id": 92,
        "nombre": "Llamada Muda",
        "nivel": 1,
        "tipificacion_id": 18,
        "categoria_padre_id": None
    },
    {
        "id": 93,
        "nombre": "Llamada de Broma",
        "nivel": 1,
        "tipificacion_id": 18,
        "categoria_padre_id": None
    },
    {
        "id": 94,
        "nombre": "Llamada Caida",
        "nivel": 1,
        "tipificacion_id": 18,
        "categoria_padre_id": None
    },
    {
        "id": 95,
        "nombre": "Llamada de Prueba",
        "nivel": 1,
        "tipificacion_id": 18,
        "categoria_padre_id": None
    },
    
    
    
    
    # Categorías de nivel 1 para la tipificación Solicitud copia de denuncia (tipificacion_id = 19)

    {
        "id": 96,
        "nombre": "Presencial",
        "nivel": 1,
        "tipificacion_id": 19,
        "categoria_padre_id": None
    },
    {
        "id": 97,
        "nombre": "Denuncia fácil",
        "nivel": 1,
        "tipificacion_id": 19,
        "categoria_padre_id": None
    },
    {
        "id": 98,
        "nombre": "Telefónico",
        "nivel": 1,
        "tipificacion_id": 19,
        "categoria_padre_id": None
    },
    {
        "id": 99,
        "nombre": "Link Suip",
        "nivel": 1,
        "tipificacion_id": 19,
        "categoria_padre_id": None
    },
    {
        "id": 100,
        "nombre": "ADenunciar",
        "nivel": 1,
        "tipificacion_id": 19,
        "categoria_padre_id": None
    },
    
    
    
    # Categorías de nivel 1 para la tipificación OUTBOUND (tipificacion_id = 20)
    
    {
        "id": 101,
        "nombre": "Outbound Denuncia",
        "nivel": 1,
        "tipificacion_id": 20,
        "categoria_padre_id": None
    },
    {
        "id": 102,
        "nombre": "Outbound PQRS",
        "nivel": 1,
        "tipificacion_id": 20,
        "categoria_padre_id": None
    },
    {
        "id": 103,
        "nombre": "Outbound Orientacion, Informacion  y Consulta de Casos",
        "nivel": 1,
        "tipificacion_id": 20,
        "categoria_padre_id": None
    },
    {
        "id": 104,
        "nombre": "Outbound Proceso clasificación denuncia",
        "nivel": 1,
        "tipificacion_id": 20,
        "categoria_padre_id": None
    },
    {
        "id": 105,
        "nombre": "Outbound Presencia inmediata de policia",
        "nivel": 1,
        "tipificacion_id": 20,
        "categoria_padre_id": None
    },
    {
        "id": 106,
        "nombre": "Outbound Desaparecidos",
        "nivel": 1,
        "tipificacion_id": 20,
        "categoria_padre_id": None
    },
    {
        "id": 107,
        "nombre": "Outbound No Efectivo",
        "nivel": 1,
        "tipificacion_id": 20,
        "categoria_padre_id": None
    },
    {
        "id": 108,
        "nombre": "Outbound agendamiento presencial",
        "nivel": 1,
        "tipificacion_id": 20,
        "categoria_padre_id": None
    },
    
    
    # Categorías de nivel 1 para la tipificación Denuncia (tipificacion_id = 21)
    {
        "id": 109,
        "nombre": "Reporte denuncias de genero",
        "nivel": 1,
        "tipificacion_id": 21,
        "categoria_padre_id": None
    },
    {
        "id": 110,
        "nombre": "Trata de personas",
        "nivel": 1,
        "tipificacion_id": 21,
        "categoria_padre_id": None
    },
    {
        "id": 111,
        "nombre": "Denuncias anónimas",
        "nivel": 1,
        "tipificacion_id": 21,
        "categoria_padre_id": None
    },
    {
        "id": 112,
        "nombre": "Hechos de corrupción",
        "nivel": 1,
        "tipificacion_id": 21,
        "categoria_padre_id": None
    },
    {
        "id": 113,
        "nombre": "Crimen organizado",
        "nivel": 1,
        "tipificacion_id": 21,
        "categoria_padre_id": None
    },
    {
        "id": 114,
        "nombre": "Líderes sociales",
        "nivel": 1,
        "tipificacion_id": 21,
        "categoria_padre_id": None
    },
    {
        "id": 115,
        "nombre": "Conflicto armado",
        "nivel": 1,
        "tipificacion_id": 21,
        "categoria_padre_id": None
    },
    
    
    
    # Subcategorías de ID 109 ("Reporte denuncias de genero")
    {
        "id": 116,
        "nombre": "Violencia intrafamiliar",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 109
    },
    {
        "id": 117,
        "nombre": "Violencia sexual",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 109
    },
    {
        "id": 118,
        "nombre": "Violencia de pareja",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 109
    },
    
    
    
    
    # Categorías de nivel 1 para la tipificación Clasificación de denuncia (tipificacion_id = 22)
    {
        "id": 119,
        "nombre": "MBU",
        "nivel": 1,
        "tipificacion_id": 22,
        "categoria_padre_id": None
    },
    {
        "id": 120,
        "nombre": "Reporte de desaparecidos",
        "nivel": 1,
        "tipificacion_id": 22,
        "categoria_padre_id": None
    },
    
    
    
    # Categorías de nivel 1 para la tipificación Orientacion, informacion y consulta de casos (tipificacion_id = 23)
    {
        "id": 121,
        "nombre": "Se corrige el relato y se clasifica",
        "nivel": 1,
        "tipificacion_id": 23,
        "categoria_padre_id": None
    },
    {
        "id": 122,
        "nombre": "Solo se clasifica la denuncia",
        "nivel": 1,
        "tipificacion_id": 23,
        "categoria_padre_id": None
    },
    
    
    
    # Categorías de nivel 1 para la tipificación Transferencias (tipificacion_id = 24)
    {
        "id": 123,
        "nombre": "Orientación para interponer denuncia",
        "nivel": 1,
        "tipificacion_id": 24,
        "categoria_padre_id": None
    },
    {
        "id": 124,
        "nombre": "Orientación para interponer PQRS",
        "nivel": 1,
        "tipificacion_id": 24,
        "categoria_padre_id": None
    },
    {
        "id": 125,
        "nombre": "Información denuncia y despacho asignado",
        "nivel": 1,
        "tipificacion_id": 24,
        "categoria_padre_id": None
    },
    {
        "id": 126,
        "nombre": "Orientación e información general",
        "nivel": 1,
        "tipificacion_id": 24,
        "categoria_padre_id": None
    },
    {
        "id": 127,
        "nombre": "Orientación para perdida de documentos",
        "nivel": 1,
        "tipificacion_id": 24,
        "categoria_padre_id": None
    },
    
    # Subcategorías de ID 123 ("Orientación para interponer denuncia")
    {
        "id": 128,
        "nombre": "Link Suip- autogestión denuncia.",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 123
    },
    {
        "id": 129,
        "nombre": "Formulario denuncia fácil",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 123
    },
    {
        "id": 130,
        "nombre": "Comisaria, inspección u otros",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 123
    },
    # Subcategorías de ID 124 ("Orientación para interponer PQRS")
    {
        "id": 131,
        "nombre": "Orientación SUSI - Página Web",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 124
    },
    {
        "id": 132,
        "nombre": "Orientación Correo",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 124
    },
    
    # Categorías de nivel 1 para la tipificación Transferencias (tipificacion_id = 25)
    {
        "id": 133,
        "nombre": "Petición",
        "nivel": 1,
        "tipificacion_id": 25,
        "categoria_padre_id": None
    },
    {
        "id": 134,
        "nombre": "Queja",
        "nivel": 1,
        "tipificacion_id": 25,
        "categoria_padre_id": None
    },
    {
        "id": 135,
        "nombre": "Reclamo",
        "nivel": 1,
        "tipificacion_id": 25,
        "categoria_padre_id": None
    },
    {
        "id": 136,
        "nombre": "Sugerencia",
        "nivel": 1,
        "tipificacion_id": 25,
        "categoria_padre_id": None
    },
    {
        "id": 137,
        "nombre": "Felicitación",
        "nivel": 1,
        "tipificacion_id": 25,
        "categoria_padre_id": None
    },
    {
        "id": 138,
        "nombre": "Solicitud copia de la denuncia",
        "nivel": 1,
        "tipificacion_id": 25,
        "categoria_padre_id": None
    },
    {
        "id": 139,
        "nombre": "Reclamo por falta de rta a PQRS",
        "nivel": 1,
        "tipificacion_id": 25,
        "categoria_padre_id": None
    },
    
    # Categorías de nivel 1 para la tipificación Transferencias (tipificacion_id = 26)
    {
        "id": 140,
        "nombre": "Transferencia a Nivel 1",
        "nivel": 1,
        "tipificacion_id": 26,
        "categoria_padre_id": None
    },
    {
        "id": 141,
        "nombre": "Transferencia a Nivel 2",
        "nivel": 1,
        "tipificacion_id": 26,
        "categoria_padre_id": None
    },
    {
        "id": 142,
        "nombre": "Transferencia Creadores de denuncia",
        "nivel": 1,
        "tipificacion_id": 26,
        "categoria_padre_id": None
    },
    {
        "id": 143,
        "nombre": "Transferencia a Abogados",
        "nivel": 1,
        "tipificacion_id": 26,
        "categoria_padre_id": None
    },
    {
        "id": 144,
        "nombre": "Transferencia a Psicologia",
        "nivel": 1,
        "tipificacion_id": 26,
        "categoria_padre_id": None
    },
    {
        "id": 145,
        "nombre": "Transferencia a Justicia Transicional",
        "nivel": 1,
        "tipificacion_id": 26,
        "categoria_padre_id": None
    },
    {
        "id": 146,
        "nombre": "Transferencia Agente Bilingüe",
        "nivel": 1,
        "tipificacion_id": 26,
        "categoria_padre_id": None
    },
    
    # Categorías de nivel 1 para la tipificación Agendamiento Sala Presencial (tipificacion_id = 27)
    {
        "id": 147,
        "nombre": "Cancelar Cita",
        "nivel": 1,
        "tipificacion_id": 27,
        "categoria_padre_id": None
    },
    {
        "id": 148,
        "nombre": "Agendar Cita",
        "nivel": 1,
        "tipificacion_id": 27,
        "categoria_padre_id": None
    },
    
    # Categorías de nivel 1 para la tipificación Requiere presencia Inmediata de la Policía (tipificacion_id = 28)
    {
        "id": 149,
        "nombre": "Solicita Presencia Inmediata de Policia",
        "nivel": 1,
        "tipificacion_id": 28,
        "categoria_padre_id": None
    },
    {
        "id": 150,
        "nombre": "Solicita presencia de Policía pero (No está en riesgo la vida o la integridad)",
        "nivel": 1,
        "tipificacion_id": 28,
        "categoria_padre_id": None
    },
    # Subcategorías de ID 149 ("Solicita Presencia Inmediata de Policia")
    {
        "id": 151,
        "nombre": "Presencia exitosa",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 149
    },
    {
        "id": 152,
        "nombre": "Transfiere a 123 u otra entidad",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 149
    },
    {
        "id": 153,
        "nombre": "Solicita presencia de Policía pero (No está en riesgo la vida o la integridad de la víctima o no es penal)",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 150
    },
    
    # Categorías de nivel 1 para la tipificación Llamadas ociosas (tipificacion_id = 29)
    {
        "id": 154,
        "nombre": "Llamada Equivocada",
        "nivel": 1,
        "tipificacion_id": 29,
        "categoria_padre_id": None
    },
    {
        "id": 155,
        "nombre": "Llamada Colgada",
        "nivel": 1,
        "tipificacion_id": 29,
        "categoria_padre_id": None
    },
    {
        "id": 156,
        "nombre": "Llamada Muda",
        "nivel": 1,
        "tipificacion_id": 29,
        "categoria_padre_id": None
    },
    {
        "id": 157,
        "nombre": "Llamada de Broma",
        "nivel": 1,
        "tipificacion_id": 29,
        "categoria_padre_id": None
    },
    {
        "id": 158,
        "nombre": "Llamada Caida",
        "nivel": 1,
        "tipificacion_id": 29,
        "categoria_padre_id": None
    },
    {
        "id": 159,
        "nombre": "Llamada de Prueba",
        "nivel": 1,
        "tipificacion_id": 29,
        "categoria_padre_id": None
    },
    
    # Categorías de nivel 1 para la tipificación Solicitud copia de denuncia (tipificacion_id = 30)
    {
        "id": 160,
        "nombre": "Presencial",
        "nivel": 1,
        "tipificacion_id": 30,
        "categoria_padre_id": None
    },
    {
        "id": 161,
        "nombre": "Denuncia fácil",
        "nivel": 1,
        "tipificacion_id": 30,
        "categoria_padre_id": None
    },
    {
        "id": 162,
        "nombre": "Telefónico",
        "nivel": 1,
        "tipificacion_id": 30,
        "categoria_padre_id": None
    },
    {
        "id": 163,
        "nombre": "Link Suip",
        "nivel": 1,
        "tipificacion_id": 30,
        "categoria_padre_id": None
    },
    {
        "id": 164,
        "nombre": "ADenunciar",
        "nivel": 1,
        "tipificacion_id": 30,
        "categoria_padre_id": None
    },
    
    
    # Categorías de nivel 1 para la tipificación OUTBOUND (tipificacion_id = 31)
    {
        "id": 165,
        "nombre": "Outbound Denuncia N1",
        "nivel": 1,
        "tipificacion_id": 31,
        "categoria_padre_id": None
    },
    {
        "id": 166,
        "nombre": "Outbound Denuncias Nivel 2",
        "nivel": 1,
        "tipificacion_id": 31,
        "categoria_padre_id": None
    },
    {
        "id": 167,
        "nombre": "Outbound PQRS",
        "nivel": 1,
        "tipificacion_id": 31,
        "categoria_padre_id": None
    },
    {
        "id": 168,
        "nombre": "Outbound Orientacion, Informacion  y Consulta de Casos",
        "nivel": 1,
        "tipificacion_id": 31,
        "categoria_padre_id": None
    },
    {
        "id": 169,
        "nombre": "Outbound Proceso clasificación denuncia",
        "nivel": 1,
        "tipificacion_id": 31,
        "categoria_padre_id": None
    },
    {
        "id": 170,
        "nombre": "Outbound Presencia inmediata de policia ",
        "nivel": 1,
        "tipificacion_id": 31,
        "categoria_padre_id": None
    },
    {
        "id": 171,
        "nombre": "Outbound Desaparecidos",
        "nivel": 1,
        "tipificacion_id": 31,
        "categoria_padre_id": None
    },
    {
        "id": 172,
        "nombre": "Outbound No Efectivo",
        "nivel": 1,
        "tipificacion_id": 31,
        "categoria_padre_id": None
    },
    {
        "id": 173,
        "nombre": "Outbound agendamiento presencial",
        "nivel": 1,
        "tipificacion_id": 31,
        "categoria_padre_id": None
    },
    
    
    # Categorías de nivel 1 para la tipificación Denuncia (tipificacion_id = 32)
    {
        "id": 174,
        "nombre": "Sicecon",
        "nivel": 1,
        "tipificacion_id": 32,
        "categoria_padre_id": None
    },
    {
        "id": 175,
        "nombre": "Denuncia fácil",
        "nivel": 1,
        "tipificacion_id": 32,
        "categoria_padre_id": None
    },
    
    # Categorías de nivel 1 para la tipificación Clasificación de denuncia (tipificacion_id = 33)
    {
        "id": 176,
        "nombre": "Reporte denuncias de genero",
        "nivel": 1,
        "tipificacion_id": 33,
        "categoria_padre_id": None
    },
    {
        "id": 177,
        "nombre": "Trata de personas",
        "nivel": 1,
        "tipificacion_id": 33,
        "categoria_padre_id": None
    },
    {
        "id": 178,
        "nombre": "Denuncias anónimas",
        "nivel": 1,
        "tipificacion_id": 33,
        "categoria_padre_id": None
    },
    {
        "id": 179,
        "nombre": "Hechos de corrupción",
        "nivel": 1,
        "tipificacion_id": 33,
        "categoria_padre_id": None
    },
    {
        "id": 180,
        "nombre": "Crimen organizado",
        "nivel": 1,
        "tipificacion_id": 33,
        "categoria_padre_id": None
    },
    {
        "id": 181,
        "nombre": "Líderes sociales",
        "nivel": 1,
        "tipificacion_id": 33,
        "categoria_padre_id": None
    },
    {
        "id": 182,
        "nombre": "Conflicto armado",
        "nivel": 1,
        "tipificacion_id": 33,
        "categoria_padre_id": None
    },
    
    # Subcategorías de ID 176 ("Reporte denuncias de genero")
    {
        "id": 183,
        "nombre": "Violencia Sexual",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 176
    },
    {
        "id": 184,
        "nombre": "Violencia Intrafamiliar",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 176
    },
    {
        "id": 185,
        "nombre": "Violencia de Genero",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 176
    },
    
    # Categorías de nivel 1 para la tipificación Transferencias (tipificacion_id = 34)

    {
        "id": 186,
        "nombre": "MBU",
        "nivel": 1,
        "tipificacion_id": 34,
        "categoria_padre_id": None
    },
    {
        "id": 187,
        "nombre": "Reporte de desaparecidos",
        "nivel": 1,
        "tipificacion_id": 34,
        "categoria_padre_id": None
    },
    
    # Categorías de c2c para la tipificación Orientacion, informacion y consulta de casos (tipificacion_id = 35)
    {
        "id": 188,
        "nombre": "Se corrige el relato y se clasifica",
        "nivel": 1,
        "tipificacion_id": 35,
        "categoria_padre_id": None
    },
    {
        "id": 189,
        "nombre": "Solo se clasifica la denuncia",
        "nivel": 1,
        "tipificacion_id": 35,
        "categoria_padre_id": None
    },
    
    # Categorías de c2c para la tipificación Transferencias (tipificacion_id = 36)
    {
        "id": 190,
        "nombre": "Orientación para interponer denuncia",
        "nivel": 1,
        "tipificacion_id": 36,
        "categoria_padre_id": None
    },
    {
        "id": 191,
        "nombre": "Orientación para interponer PQRS",
        "nivel": 1,
        "tipificacion_id": 36,
        "categoria_padre_id": None
    },
    {
        "id": 192,
        "nombre": "Información denuncia y despacho asignado",
        "nivel": 1,
        "tipificacion_id": 36,
        "categoria_padre_id": None
    },
    {
        "id": 193,
        "nombre": "Orientación e información general",
        "nivel": 1,
        "tipificacion_id": 36,
        "categoria_padre_id": None
    },
    {
        "id": 194,
        "nombre": "Orientación para perdida de documentos",
        "nivel": 1,
        "tipificacion_id": 36,
        "categoria_padre_id": None
    },
    # Subcategorías de ID 190 ("Orientación para interponer denuncia")
    {
        "id": 195,
        "nombre": "Link Suip- autogestión denuncia.",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 190
    },
    {
        "id": 196,
        "nombre": "Formulario denuncia fácil",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 190
    },
    {
        "id": 197,
        "nombre": "Comisaria, inspección u otros",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 190
    },
    # Subcategorías de ID 191 ("Orientación para interponer PQRS")
    {
        "id": 198,
        "nombre": "Orientación SUSI - Página Web",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 191
    },
    {
        "id": 199,
        "nombre": "Orientación Correo",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 191
    },
    
    # C ategorías de c2c para la tipificación Transferencias (tipificacion_id = 37)
    {
        "id": 200,
        "nombre": "Petición",
        "nivel": 1,
        "tipificacion_id": 37,
        "categoria_padre_id": None
    },
    {
        "id": 201,
        "nombre": "Queja",
        "nivel": 1,
        "tipificacion_id": 37,
        "categoria_padre_id": None
    },
    {
        "id": 202,
        "nombre": "Reclamo",
        "nivel": 1,
        "tipificacion_id": 37,
        "categoria_padre_id": None
    },
    {
        "id": 203,
        "nombre": "Sugerencia",
        "nivel": 1,
        "tipificacion_id": 37,
        "categoria_padre_id": None
    },
    {
        "id": 204,
        "nombre": "Felicitación",
        "nivel": 1,
        "tipificacion_id": 37,
        "categoria_padre_id": None
    },
    {
        "id": 205,
        "nombre": "Solicitud copia de la denuncia",
        "nivel": 1,
        "tipificacion_id": 37,
        "categoria_padre_id": None
    },
    {
        "id": 206,
        "nombre": "Reclamo por falta de rta a PQRS",
        "nivel": 1,
        "tipificacion_id": 37,
        "categoria_padre_id": None
    },
    
    
    # Categorías de c2c para la tipificación Transferencias (tipificacion_id = 38)
    {
        "id": 207,
        "nombre": "Transferencia a Nivel 1",
        "nivel": 1,
        "tipificacion_id": 38,
        "categoria_padre_id": None
    },
    {
        "id": 208,
        "nombre": "Transferencia a Nivel 2",
        "nivel": 1,
        "tipificacion_id": 38,
        "categoria_padre_id": None
    },
    {
        "id": 209,
        "nombre": "Transferencia Creadores de denuncia",
        "nivel": 1,
        "tipificacion_id": 38,
        "categoria_padre_id": None
    },
    {
        "id": 210,
        "nombre": "Transferencia a Abogados",
        "nivel": 1,
        "tipificacion_id": 38,
        "categoria_padre_id": None
    },
    {
        "id": 211,
        "nombre": "Transferencia a Psicologia",
        "nivel": 1,
        "tipificacion_id": 38,
        "categoria_padre_id": None
    },
    {
        "id": 212,
        "nombre": "Transferencia a Justicia Transicional",
        "nivel": 1,
        "tipificacion_id": 38,
        "categoria_padre_id": None
    },
    {
        "id": 213,
        "nombre": "Transferencia Agente Bilingüe",
        "nivel": 1,
        "tipificacion_id": 38,
        "categoria_padre_id": None
    },
    
    # Categorías de c2c para la tipificación Agendamiento Sala Presencial (tipificacion_id = 39)
    {
        "id": 214,
        "nombre": "Cancelar Cita",
        "nivel": 1,
        "tipificacion_id": 39,
        "categoria_padre_id": None
    },
    {
        "id": 215,
        "nombre": "Agendar Cita",
        "nivel": 1,
        "tipificacion_id": 39,
        "categoria_padre_id": None
    },
    
    
    # Categorías de c2c para la tipificación Requiere presencia Inmediata de la Policía (tipificacion_id = 40)
    {
        "id": 216,
        "nombre": "Solicita Presencia Inmediata de Policia",
        "nivel": 1,
        "tipificacion_id": 40,
        "categoria_padre_id": None
    },
    {
        "id": 217,
        "nombre": "Solicita presencia de Policía pero (No está en riesgo la vida o la integridad)",
        "nivel": 1,
        "tipificacion_id": 40,
        "categoria_padre_id": None
    },
    # Subcategorías de ID 216 ("Solicita Presencia Inmediata de Policia")
    {
        "id": 218,
        "nombre": "Presencia exitosa",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 216
    },
    {
        "id": 219,
        "nombre": "Transfiere a 123 u otra entidad",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 216
    },
    {
        "id": 220,
        "nombre": "Solicita presencia de Policía pero (No está en riesgo la vida o la integridad de la víctima o no es penal)",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 217
    },
    
    # Categorías de c2c para la tipificación Llamadas ociosas (tipificacion_id = 41)
    {
        "id": 221,
        "nombre": "Llamada Equivocada",
        "nivel": 1,
        "tipificacion_id": 41,
        "categoria_padre_id": None
    },
    {
        "id": 222,
        "nombre": "Llamada Colgada",
        "nivel": 1,
        "tipificacion_id": 41,
        "categoria_padre_id": None
    },
    {
        "id": 223,
        "nombre": "Llamada Muda",
        "nivel": 1,
        "tipificacion_id": 41,
        "categoria_padre_id": None
    },
    {
        "id": 224,
        "nombre": "Llamada de Broma",
        "nivel": 1,
        "tipificacion_id": 41,
        "categoria_padre_id": None
    },
    {
        "id": 225,
        "nombre": "Llamada Caida",
        "nivel": 1,
        "tipificacion_id": 41,
        "categoria_padre_id": None
    },
    {
        "id": 226,
        "nombre": "Llamada de Prueba",
        "nivel": 1,
        "tipificacion_id": 41,
        "categoria_padre_id": None
    },  
    
    # Categorías de c2c para la tipificación Solicitud copia de denuncia (tipificacion_id = 42)
    {
        "id": 227,
        "nombre": "Presencial",
        "nivel": 1,
        "tipificacion_id": 42,
        "categoria_padre_id": None
    },
    {
        "id": 228,
        "nombre": "Denuncia fácil",
        "nivel": 1,
        "tipificacion_id": 42,
        "categoria_padre_id": None
    },
    {
        "id": 229,
        "nombre": "Telefónico",
        "nivel": 1,
        "tipificacion_id": 42,
        "categoria_padre_id": None
    },
    {
        "id": 230,
        "nombre": "Link Suip",
        "nivel": 1,
        "tipificacion_id": 42,
        "categoria_padre_id": None
    },
    {
        "id": 231,
        "nombre": "ADenunciar",
        "nivel": 1,
        "tipificacion_id": 42,
        "categoria_padre_id": None
    },
    
    
    # Categorías de c2c para la tipificación OUTBOUND (tipificacion_id = 43)
    {
        "id": 232,
        "nombre": "Outbound Denuncia N1",
        "nivel": 1,
        "tipificacion_id": 43,
        "categoria_padre_id": None
    },
    {
        "id": 233,
        "nombre": "Outbound Denuncias Nivel 2",
        "nivel": 1,
        "tipificacion_id": 43,
        "categoria_padre_id": None
    },
    {
        "id": 234,
        "nombre": "Outbound PQRS",
        "nivel": 1,
        "tipificacion_id": 43,
        "categoria_padre_id": None
    },
    {
        "id": 235,
        "nombre": "Outbound Orientacion, Informacion  y Consulta de Casos",
        "nivel": 1,
        "tipificacion_id": 43,
        "categoria_padre_id": None
    },
    {
        "id": 236,
        "nombre": "Outbound Proceso clasificación denuncia",
        "nivel": 1,
        "tipificacion_id": 43,
        "categoria_padre_id": None
    },
    {
        "id": 237,
        "nombre": "Outbound Presencia inmediata de policia ",
        "nivel": 1,
        "tipificacion_id": 43,
        "categoria_padre_id": None
    },
    {
        "id": 238,
        "nombre": "Outbound Desaparecidos",
        "nivel": 1,
        "tipificacion_id": 43,
        "categoria_padre_id": None
    },
    {
        "id": 239,
        "nombre": "Outbound No Efectivo",
        "nivel": 1,
        "tipificacion_id": 43,
        "categoria_padre_id": None
    },
    {
        "id": 240,
        "nombre": "Outbound agendamiento presencial",
        "nivel": 1,
        "tipificacion_id": 43,
        "categoria_padre_id": None
    },
    
    
    # Categorías de c2c para la tipificación Denuncia (tipificacion_id = 44)
    {
        "id": 241,
        "nombre": "Sicecon",
        "nivel": 1,
        "tipificacion_id": 44,
        "categoria_padre_id": None
    },
    {
        "id": 242,
        "nombre": "Denuncia fácil",
        "nivel": 1,
        "tipificacion_id": 44,
        "categoria_padre_id": None
    },
    
    # Categorías de c2c para la tipificación Clasificación de denuncia (tipificacion_id = 45)
    {
        "id": 243,
        "nombre": "Reporte denuncias de genero",
        "nivel": 1,
        "tipificacion_id": 45,
        "categoria_padre_id": None
    },
    {
        "id": 244,
        "nombre": "Trata de personas",
        "nivel": 1,
        "tipificacion_id": 45,
        "categoria_padre_id": None
    },
    {
        "id": 245,
        "nombre": "Denuncias anónimas",
        "nivel": 1,
        "tipificacion_id": 45,
        "categoria_padre_id": None
    },
    {
        "id": 246,
        "nombre": "Hechos de corrupción",
        "nivel": 1,
        "tipificacion_id": 45,
        "categoria_padre_id": None
    },
    {
        "id": 247,
        "nombre": "Crimen organizado",
        "nivel": 1,
        "tipificacion_id": 45,
        "categoria_padre_id": None
    },
    {
        "id": 248,
        "nombre": "Líderes sociales",
        "nivel": 1,
        "tipificacion_id": 45,
        "categoria_padre_id": None
    },
    {
        "id": 249,
        "nombre": "Conflicto armado",
        "nivel": 1,
        "tipificacion_id": 45,
        "categoria_padre_id": None
    },
    # Subcategorías de ID 243 ("Reporte denuncias de genero")
    {
        "id": 250,
        "nombre": "Violencia Sexual",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 243
    },
    {
        "id": 251,
        "nombre": "Violencia Intrafamiliar",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 243
    },
    {
        "id": 252,
        "nombre": "Violencia de Genero",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 243
    },
    
    # Categorías de c2c para la tipificación Clasificación de denuncia  (tipificacion_id = 46)
    {
        "id": 253,
        "nombre": "Se corrige el relato y se clasifica",
        "nivel": 1,
        "tipificacion_id": 46,
        "categoria_padre_id": None
    },
    {
        "id": 254,
        "nombre": "Solo se clasifica la denuncia",
        "nivel": 1,
        "tipificacion_id": 46,
        "categoria_padre_id": None
    },
    
    
    # Categorías de c2c para la tipificación Transferencias (tipificacion_id = 47)
    {
        "id": 255,
        "nombre": "Orientación para interponer denuncia",
        "nivel": 1,
        "tipificacion_id": 47,
        "categoria_padre_id": None
    },
    {
        "id": 256,
        "nombre": "Orientación para interponer PQRS",
        "nivel": 1,
        "tipificacion_id": 47,
        "categoria_padre_id": None
    },
    {
        "id": 257,
        "nombre": "Información denuncia y despacho asignado",
        "nivel": 1,
        "tipificacion_id": 47,
        "categoria_padre_id": None
    },
    {
        "id": 258,
        "nombre": "Orientación e información general",
        "nivel": 1,
        "tipificacion_id": 47,
        "categoria_padre_id": None
    },
    {
        "id": 259,
        "nombre": "Orientación para perdida de documentos",
        "nivel": 1,
        "tipificacion_id": 47,
        "categoria_padre_id": None
    },
    
    # Subcategorías de ID 255 ("Orientación para interponer denuncia")
    {
        "id": 260,
        "nombre": "Link Suip- autogestión denuncia.",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 255
    },
    {
        "id": 261,
        "nombre": "Formulario denuncia fácil",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 255
    },
    {
        "id": 262,
        "nombre": "Comisaria, inspección u otros",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 255
    },
    # Subcategorías de ID 256 ("Orientación para interponer PQRS")
    {
        "id": 263,
        "nombre": "Orientación SUSI - Página Web",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 256
    },
    {
        "id": 264,
        "nombre": "Orientación Correo",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 256
    },
    
    
    # Categorías de c2c para la tipificación Transferencias (tipificacion_id = 48)
    {
        "id": 265,
        "nombre": "Petición",
        "nivel": 1,
        "tipificacion_id": 48,
        "categoria_padre_id": None
    },
    {
        "id": 266,
        "nombre": "Queja",
        "nivel": 1,
        "tipificacion_id": 48,
        "categoria_padre_id": None
    },
    {
        "id": 267,
        "nombre": "Reclamo",
        "nivel": 1,
        "tipificacion_id": 48,
        "categoria_padre_id": None
    },
    {
        "id": 268,
        "nombre": "Sugerencia",
        "nivel": 1,
        "tipificacion_id": 48,
        "categoria_padre_id": None
    },
    {
        "id": 269,
        "nombre": "Felicitación",
        "nivel": 1,
        "tipificacion_id": 48,
        "categoria_padre_id": None
    },
    {
        "id": 270,
        "nombre": "Solicitud copia de la denuncia",
        "nivel": 1,
        "tipificacion_id": 48,
        "categoria_padre_id": None
    },
    {
        "id": 271,
        "nombre": "Reclamo por falta de rta a PQRS",
        "nivel": 1,
        "tipificacion_id": 48,
        "categoria_padre_id": None
    },
    
    
    # Categorías de c2c para la tipificación Transferencias (tipificacion_id = 49)
    {
        "id": 272,
        "nombre": "Cancelar Cita",
        "nivel": 1,
        "tipificacion_id": 49,
        "categoria_padre_id": None
    },
    {
        "id": 273,
        "nombre": "Agendar Cita",
        "nivel": 1,
        "tipificacion_id": 49,
        "categoria_padre_id": None
    },
    
    
    # Categorías de c2c para la tipificación Requiere presencia Inmediata de la Policía (tipificacion_id = 50)
    {
        "id": 274,
        "nombre": "Solicita Presencia Inmediata de Policia",
        "nivel": 1,
        "tipificacion_id": 50,
        "categoria_padre_id": None
    },
    {
        "id": 275,
        "nombre": "Solicita presencia de Policía pero (No está en riesgo la vida o la integridad)",
        "nivel": 1,
        "tipificacion_id": 50,
        "categoria_padre_id": None
    },
    # Subcategorías de ID 274 ("Solicita Presencia Inmediata de Policia")
    {
        "id": 276,
        "nombre": "Presencia exitosa",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 274
    },
    {
        "id": 277,
        "nombre": "Transfiere a 123 u otra entidad",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 274
    },
    {
        "id": 278,
        "nombre": "Solicita presencia de Policía pero (No está en riesgo la vida o la integridad de la víctima o no es penal)",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 275
    },
    
    # Categorías de c2c para la tipificación Llamadas ociosas (tipificacion_id = 51)
    {
        "id": 279,
        "nombre": "Presencial",
        "nivel": 1,
        "tipificacion_id": 51,
        "categoria_padre_id": None
    },
    {
        "id": 280,
        "nombre": "Denuncia fácil",
        "nivel": 1,
        "tipificacion_id": 51,
        "categoria_padre_id": None
    },
    {
        "id": 281,
        "nombre": "Telefónico",
        "nivel": 1,
        "tipificacion_id": 51,
        "categoria_padre_id": None
    },
    {
        "id": 282,
        "nombre": "Link Suip",
        "nivel": 1,
        "tipificacion_id": 51,
        "categoria_padre_id": None
    },
    {
        "id": 283,
        "nombre": "ADenunciar",
        "nivel": 1,
        "tipificacion_id": 51,
        "categoria_padre_id": None
    },
    
    
    # Categorías de c2c para la tipificación OUTBOUND (tipificacion_id = 52)
    {
        "id": 284,
        "nombre": "Llamada Equivocada",
        "nivel": 1,
        "tipificacion_id": 52,
        "categoria_padre_id": None
    },
    {
        "id": 285,
        "nombre": "Llamada Colgada",
        "nivel": 1,
        "tipificacion_id": 52,
        "categoria_padre_id": None
    },
    {
        "id": 286,
        "nombre": "Llamada Muda",
        "nivel": 1,
        "tipificacion_id": 52,
        "categoria_padre_id": None
    },
    {
        "id": 287,
        "nombre": "Llamada de Broma",
        "nivel": 1,
        "tipificacion_id": 52,
        "categoria_padre_id": None
    },
    {
        "id": 288,
        "nombre": "Llamada Caida",
        "nivel": 1,
        "tipificacion_id": 52,
        "categoria_padre_id": None
    },
    {
        "id": 289,
        "nombre": "Llamada de Prueba",
        "nivel": 1,
        "tipificacion_id": 52,
        "categoria_padre_id": None
    },
    
    # Categorías de c2c para la tipificación Solicitud copia de denuncia (tipificacion_id = 53)
    {
        "id": 290,
        "nombre": "Sicecon",
        "nivel": 1,
        "tipificacion_id": 53,
        "categoria_padre_id": None
    },
    {
        "id": 291,
        "nombre": "Denuncia fácil",
        "nivel": 1,
        "tipificacion_id": 53,
        "categoria_padre_id": None
    },
    
    # Categorías de c2c para la tipificación Clasificación de denuncia (tipificacion_id = 54)
    {
        "id": 292,
        "nombre": "Reporte denuncias de genero",
        "nivel": 1,
        "tipificacion_id": 54,
        "categoria_padre_id": None
    },
    {
        "id": 293,
        "nombre": "Trata de personas",
        "nivel": 1,
        "tipificacion_id": 54,
        "categoria_padre_id": None
    },
    {
        "id": 294,
        "nombre": "Denuncias anónimas",
        "nivel": 1,
        "tipificacion_id": 54,
        "categoria_padre_id": None
    },
    {
        "id": 295,
        "nombre": "Hechos de corrupción",
        "nivel": 1,
        "tipificacion_id": 54,
        "categoria_padre_id": None
    },
    {
        "id": 296,
        "nombre": "Crimen organizado",
        "nivel": 1,
        "tipificacion_id": 54,
        "categoria_padre_id": None
    },
    {
        "id": 297,
        "nombre": "Líderes sociales",
        "nivel": 1,
        "tipificacion_id": 54,
        "categoria_padre_id": None
    },
    {
        "id": 298,
        "nombre": "Conflicto armado",
        "nivel": 1,
        "tipificacion_id": 54,
        "categoria_padre_id": None
    },
    
    # Subcategorías de ID 292 ("Reporte denuncias de genero")
    {
        "id": 299,
        "nombre": "Violencia Sexual",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 292
    },
    {
        "id": 300,
        "nombre": "Violencia Intrafamiliar",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 292
    },
    {
        "id": 301,
        "nombre": "Violencia de Genero",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 292
    },
    
    # Categorías de c2c para la tipificación Transferencias (tipificacion_id = 55)
    {
        "id": 302,
        "nombre": "Se corrige el relato y se clasifica",
        "nivel": 1,
        "tipificacion_id": 55,
        "categoria_padre_id": None
    },
    {
        "id": 303,
        "nombre": "Solo se clasifica la denuncia",
        "nivel": 1,
        "tipificacion_id": 55,
        "categoria_padre_id": None
    },
    
    # Categorías de c2c para la tipificación Transferencias (tipificacion_id = 56)
        {
        "id": 304,
        "nombre": "Orientación para interponer denuncia",
        "nivel": 1,
        "tipificacion_id": 56,
        "categoria_padre_id": None
    },
    {
        "id": 305,
        "nombre": "Orientación para interponer PQRS",
        "nivel": 1,
        "tipificacion_id": 56,
        "categoria_padre_id": None
    },
    {
        "id": 306,
        "nombre": "Información denuncia y despacho asignado",
        "nivel": 1,
        "tipificacion_id": 56,
        "categoria_padre_id": None
    },
    {
        "id": 307,
        "nombre": "Orientación e información general",
        "nivel": 1,
        "tipificacion_id": 56,
        "categoria_padre_id": None
    },
    {
        "id": 308,
        "nombre": "Orientación para perdida de documentos",
        "nivel": 1,
        "tipificacion_id": 56,
        "categoria_padre_id": None
    },

    # Subcategorías de "Orientación para interponer denuncia"
    {
        "id": 309,
        "nombre": "Link Suip- autogestión denuncia.",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 304
    },
    {
        "id": 310,
        "nombre": "Formulario denuncia fácil",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 304
    },
    {
        "id": 311,
        "nombre": "Comisaria, inspección u otros",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 304
    },

    # Subcategorías de "Orientación para interponer PQRS"
    {
        "id": 312,
        "nombre": "Orientación SUSI - Página Web",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 305
    },
    {
        "id": 313,
        "nombre": "Orientación Correo",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 305
    },
    
    # Categorías de c2c para la tipificación Transferencias (tipificacion_id = 57)
    {
        "id": 314,
        "nombre": "Petición",
        "nivel": 1,
        "tipificacion_id": 57,
        "categoria_padre_id": None
    },
    {
        "id": 315,
        "nombre": "Queja",
        "nivel": 1,
        "tipificacion_id": 57,
        "categoria_padre_id": None
    },
    {
        "id": 316,
        "nombre": "Reclamo",
        "nivel": 1,
        "tipificacion_id": 57,
        "categoria_padre_id": None
    },
    {
        "id": 317,
        "nombre": "Sugerencia",
        "nivel": 1,
        "tipificacion_id": 57,
        "categoria_padre_id": None
    },
    {
        "id": 318,
        "nombre": "Felicitación",
        "nivel": 1,
        "tipificacion_id": 57,
        "categoria_padre_id": None
    },
    {
        "id": 319,
        "nombre": "Solicitud copia de la denuncia",
        "nivel": 1,
        "tipificacion_id": 57,
        "categoria_padre_id": None
    },
    {
        "id": 320,
        "nombre": "Reclamo por falta de rta a PQRS",
        "nivel": 1,
        "tipificacion_id": 57,
        "categoria_padre_id": None
    },
    
    # Categorías de c2c para la tipificación Transferencias (tipificacion_id = 58)
    {
        "id": 321,
        "nombre": "Cancelar Cita",
        "nivel": 1,
        "tipificacion_id": 58,
        "categoria_padre_id": None
    },
    {
        "id": 322,
        "nombre": "Agendar Cita",
        "nivel": 1,
        "tipificacion_id": 58,
        "categoria_padre_id": None
    },
    
    # Categorías de  para la tipificación Requiere presencia Inmediata de la Policía (tipificacion_id = 59)
    {
        "id": 323,
        "nombre": "Solicita Presencia Inmediata de Policia",
        "nivel": 1,
        "tipificacion_id": 59,
        "categoria_padre_id": None
    },
    {
        "id": 324,
        "nombre": "Solicita presencia de Policía pero (No está en riesgo la vida o la integridad)",
        "nivel": 1,
        "tipificacion_id": 59,
        "categoria_padre_id": None
    },
    # Subcategorías de ID 323 ("Solicita Presencia Inmediata de Policia")
    {
        "id": 325,
        "nombre": "Presencia exitosa",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 323
    },
    {
        "id": 326,
        "nombre": "Transfiere a 123 u otra entidad",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 323
    },
    {
        "id": 327,
        "nombre": "Solicita presencia de Policía pero (No está en riesgo la vida o la integridad de la víctima o no es penal)",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 324
    },
    
    
    
    
    # Categorías de c2c para la tipificación Llamadas ociosas (tipificacion_id = 60)
    {
        "id": 328,
        "nombre": "Presencial",
        "nivel": 1,
        "tipificacion_id": 60,
        "categoria_padre_id": None
    },
    {
        "id": 329,
        "nombre": "Denuncia fácil",
        "nivel": 1,
        "tipificacion_id": 60,
        "categoria_padre_id": None
    },
    {
        "id": 330,
        "nombre": "Telefónico",
        "nivel": 1,
        "tipificacion_id": 60,
        "categoria_padre_id": None
    },
    {
        "id": 331,
        "nombre": "Link Suip",
        "nivel": 1,
        "tipificacion_id": 60,
        "categoria_padre_id": None
    },
    {
        "id": 332,
        "nombre": "ADenunciar",
        "nivel": 1,
        "tipificacion_id": 60,
        "categoria_padre_id": None
    },
    
    # Categorías de c2c para la tipificación OUTBOUND (tipificacion_id = 61)
    
    {
        "id": 333,
        "nombre": "Llamada Equivocada",
        "nivel": 1,
        "tipificacion_id": 61,
        "categoria_padre_id": None
    },
    {
        "id": 334,
        "nombre": "Llamada Colgada",
        "nivel": 1,
        "tipificacion_id": 61,
        "categoria_padre_id": None
    },
    {
        "id": 335,
        "nombre": "Llamada Muda",
        "nivel": 1,
        "tipificacion_id": 61,
        "categoria_padre_id": None
    },
    {
        "id": 336,
        "nombre": "Llamada de Broma",
        "nivel": 1,
        "tipificacion_id": 61,
        "categoria_padre_id": None
    },
    {
        "id": 337,
        "nombre": "Llamada Caida",
        "nivel": 1,
        "tipificacion_id": 61,
        "categoria_padre_id": None
    },
    {
        "id": 338,
        "nombre": "Llamada de Prueba",
        "nivel": 1,
        "tipificacion_id": 61,
        "categoria_padre_id": None
    },

    
    # Categorías de psicologo para la tipificación Solicitud copia de denuncia (tipificacion_id = 62)
    {
    "id": 339,
    "nombre": "NNA",
    "nivel": 1,
    "tipificacion_id": 62,
    "categoria_padre_id": None
    },
    {
        "id": 340,
        "nombre": "Sicecon",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 339
    },
    {
        "id": 341,
        "nombre": "Denuncia fácil",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 339
    },
    {
        "id": 342,
        "nombre": "Usuario en crisis",
        "nivel": 1,
        "tipificacion_id": 62,
        "categoria_padre_id": None
    },
    {
        "id": 343,
        "nombre": "Sicecon",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 342
    },
    {
        "id": 344,
        "nombre": "Denuncia fácil",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 342
    },
    
    # Categorías de c2c para la tipificación Clasificación de denuncia (tipificacion_id = 63)
    {
        "id": 345,
        "nombre": "NNA",
        "nivel": 1,
        "tipificacion_id": 63,
        "categoria_padre_id": None
    },
    {
        "id": 346,
        "nombre": "Usuario en crisis",
        "nivel": 1,
        "tipificacion_id": 63,
        "categoria_padre_id": None
    },
    {
        "id": 347,
        "nombre": "Reporte denuncias de genero",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 345
    },
    {
        "id": 348,
        "nombre": "Trata de personas",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 345
    },
    {
        "id": 349,
        "nombre": "Denuncias anónimas",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 345
    },
    {
        "id": 350,
        "nombre": "Hechos de corrupción",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 346
    },
    {
        "id": 351,
        "nombre": "Crimen organizado",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 346
    },
    {
        "id": 352,
        "nombre": "Líderes sociales",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 346
    },
    {
        "id": 353,
        "nombre": "Conflicto armado",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 346
    },
    {
        "id": 354,
        "nombre": "Violencia Sexual",
        "nivel": 3,
        "tipificacion_id": None,
        "categoria_padre_id": 347
    },
    {
        "id": 355,
        "nombre": "Violencia Intrafamiliar",
        "nivel": 3,
        "tipificacion_id": None,
        "categoria_padre_id": 347
    },
    {
        "id": 356,
        "nombre": "Violencia de Genero",
        "nivel": 3,
        "tipificacion_id": None,
        "categoria_padre_id": 347
    },

    # Categorías de c2c para la tipificación Transferencias (tipificacion_id = 64)
    {
        "id": 357,
        "nombre": "MBU",
        "nivel": 1,
        "tipificacion_id": 64,
        "categoria_padre_id": None
    },
    {
        "id": 358,
        "nombre": "Reporte de desaparecidos",
        "nivel": 1,
        "tipificacion_id": 64,
        "categoria_padre_id": None
    },
    {
        "id": 359,
        "nombre": "Se corrige el relato y se clasifica",
        "nivel": 1,
        "tipificacion_id": 65,
        "categoria_padre_id": None
    },
    {
        "id": 360,
        "nombre": "Solo se clasifica la denuncia",
        "nivel": 1,
        "tipificacion_id": 65,
        "categoria_padre_id": None
    },
    {
        "id": 361,
        "nombre": "Asesoria Psicológica",
        "nivel": 1,
        "tipificacion_id": 66,
        "categoria_padre_id": None
    },
    {
        "id": 362,
        "nombre": "Orientación para interponer denuncia",
        "nivel": 1,
        "tipificacion_id": 66,
        "categoria_padre_id": None
    },
    {
        "id": 363,
        "nombre": "Orientación para interponer PQRS",
        "nivel": 1,
        "tipificacion_id": 66,
        "categoria_padre_id": None
    },
    {
        "id": 364,
        "nombre": "Información denuncia y despacho asignado",
        "nivel": 1,
        "tipificacion_id": 66,
        "categoria_padre_id": None
    },
    {
        "id": 365,
        "nombre": "Orientación copia de la denuncia",
        "nivel": 1,
        "tipificacion_id": 66,
        "categoria_padre_id": None
    },
    {
        "id": 366,
        "nombre": "Orientación e información general",
        "nivel": 1,
        "tipificacion_id": 66,
        "categoria_padre_id": None
    },

    # // Subcategorías de Asesoría Psicológica
    {
        "id": 367,
        "nombre": "Atencion en Crisis",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 361
    },
    {
        "id": 368,
        "nombre": "Orientacion Psicológica",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 361
    },
    {
        "id": 369,
        "nombre": "Presunto Paciente Psiquiátrico",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 361
    },

    # // Subcategorías de ID 362
    {
        "id": 370,
        "nombre": "Comisaria, inspección u otros",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 362
    },

    # // Subcategorías de ID 363
    {
        "id": 371,
        "nombre": "Orientación SUSI - Página Web",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 363
    },
    {
        "id": 372,
        "nombre": "Orientación Correo",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 363
    },

    # // Tipificación PQRS - tipificacion_id: 67
    {
        "id": 373,
        "nombre": "Petición",
        "nivel": 1,
        "tipificacion_id": 67,
        "categoria_padre_id": None
    },
    {
        "id": 374,
        "nombre": "Queja",
        "nivel": 1,
        "tipificacion_id": 67,
        "categoria_padre_id": None
    },
    {
        "id": 375,
        "nombre": "Reclamo",
        "nivel": 1,
        "tipificacion_id": 67,
        "categoria_padre_id": None
    },
    {
        "id": 376,
        "nombre": "Sugerencia",
        "nivel": 1,
        "tipificacion_id": 67,
        "categoria_padre_id": None
    },
    {
        "id": 377,
        "nombre": "Felicitación",
        "nivel": 1,
        "tipificacion_id": 67,
        "categoria_padre_id": None
    },
    {
        "id": 378,
        "nombre": "Solicitud copia de la denuncia",
        "nivel": 1,
        "tipificacion_id": 67,
        "categoria_padre_id": None
    },
    {
        "id": 379,
        "nombre": "Reclamo por falta de rta a PQRS",
        "nivel": 1,
        "tipificacion_id": 67,
        "categoria_padre_id": None
    },
    
    {
        "id": 380,
        "nombre": "Transferencia a Nivel 1",
        "nivel": 1,
        "tipificacion_id": 68,
        "categoria_padre_id": None
    },
    {
        "id": 381,
        "nombre": "Transferencia a Nivel 2",
        "nivel": 1,
        "tipificacion_id": 68,
        "categoria_padre_id": None
    },
    {
        "id": 382,
        "nombre": "Transferencia Creadores de denuncia",
        "nivel": 1,
        "tipificacion_id": 68,
        "categoria_padre_id": None
    },
    {
        "id": 383,
        "nombre": "Transferencia a Abogados",
        "nivel": 1,
        "tipificacion_id": 68,
        "categoria_padre_id": None
    },
    {
        "id": 384,
        "nombre": "Transferencia a Psicologia",
        "nivel": 1,
        "tipificacion_id": 68,
        "categoria_padre_id": None
    },
    {
        "id": 385,
        "nombre": "Transferencia a Justicia Transicional",
        "nivel": 1,
        "tipificacion_id": 68,
        "categoria_padre_id": None
    },
    {
        "id": 386,
        "nombre": "Transferencia Agente Bilingüe",
        "nivel": 1,
        "tipificacion_id": 68,
        "categoria_padre_id": None
    },

    {
        "id": 387,
        "nombre": "Cancelar Cita",
        "nivel": 1,
        "tipificacion_id": 69,
        "categoria_padre_id": None
    },
    {
        "id": 388,
        "nombre": "Agendar Cita",
        "nivel": 1,
        "tipificacion_id": 69,
        "categoria_padre_id": None
    },

    {
        "id": 389,
        "nombre": "Solicita Presencia Inmediata de Policia",
        "nivel": 1,
        "tipificacion_id": 70,
        "categoria_padre_id": None
    },
    {
        "id": 390,
        "nombre": "Solicita presencia de Policía pero (No está en riesgo la vida o la integridad)",
        "nivel": 1,
        "tipificacion_id": 70,
        "categoria_padre_id": None
    },

    {
        "id": 391,
        "nombre": "Presencia exitosa",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 389
    },
    {
        "id": 392,
        "nombre": "Transfiere a 123 u otra entidad",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 389
    },
    {
        "id": 393,
        "nombre": "Solicita presencia de Policía pero (No está en riesgo la vida o la integridad de la víctima o no es penal)",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 390
    },

    {
        "id": 394,
        "nombre": "Llamada Equivocada",
        "nivel": 1,
        "tipificacion_id": 71,
        "categoria_padre_id": None
    },
    {
        "id": 395,
        "nombre": "Llamada Colgada",
        "nivel": 1,
        "tipificacion_id": 71,
        "categoria_padre_id": None
    },
    {
        "id": 396,
        "nombre": "Llamada Muda",
        "nivel": 1,
        "tipificacion_id": 71,
        "categoria_padre_id": None
    },
    {
        "id": 397,
        "nombre": "Llamada de Broma",
        "nivel": 1,
        "tipificacion_id": 71,
        "categoria_padre_id": None
    },
    {
        "id": 398,
        "nombre": "Llamada Caida",
        "nivel": 1,
        "tipificacion_id": 71,
        "categoria_padre_id": None
    },
    {
        "id": 399,
        "nombre": "Llamada de Prueba",
        "nivel": 1,
        "tipificacion_id": 71,
        "categoria_padre_id": None
    },

    {
        "id": 400,
        "nombre": "Presencial",
        "nivel": 1,
        "tipificacion_id": 72,
        "categoria_padre_id": None
    },
    {
        "id": 401,
        "nombre": "Denuncia fácil",
        "nivel": 1,
        "tipificacion_id": 72,
        "categoria_padre_id": None
    },
    {
        "id": 402,
        "nombre": "Telefónico",
        "nivel": 1,
        "tipificacion_id": 72,
        "categoria_padre_id": None
    },
    {
        "id": 403,
        "nombre": "Link Suip",
        "nivel": 1,
        "tipificacion_id": 72,
        "categoria_padre_id": None
    },
    {
        "id": 404,
        "nombre": "ADenunciar",
        "nivel": 1,
        "tipificacion_id": 72,
        "categoria_padre_id": None
    },

    {
        "id": 405,
        "nombre": "Outbound Denuncia N1",
        "nivel": 1,
        "tipificacion_id": 73,
        "categoria_padre_id": None
    },
    {
        "id": 406,
        "nombre": "Outbound Denuncias Nivel 2",
        "nivel": 1,
        "tipificacion_id": 73,
        "categoria_padre_id": None
    },
    {
        "id": 407,
        "nombre": "Outbound PQRS",
        "nivel": 1,
        "tipificacion_id": 73,
        "categoria_padre_id": None
    },
    {
        "id": 408,
        "nombre": "Outbound Orientacion, Informacion  y Consulta de Casos",
        "nivel": 1,
        "tipificacion_id": 73,
        "categoria_padre_id": None
    },
    {
        "id": 409,
        "nombre": "Outbound Proceso clasificación denuncia",
        "nivel": 1,
        "tipificacion_id": 73,
        "categoria_padre_id": None
    },
    {
        "id": 410,
        "nombre": "Outbound Presencia inmediata de policia",
        "nivel": 1,
        "tipificacion_id": 73,
        "categoria_padre_id": None
    },
    {
        "id": 411,
        "nombre": "Outbound Desaparecidos",
        "nivel": 1,
        "tipificacion_id": 73,
        "categoria_padre_id": None
    },
    {
        "id": 412,
        "nombre": "Outbound No Efectivo",
        "nivel": 1,
        "tipificacion_id": 73,
        "categoria_padre_id": None
    },
    {
        "id": 413,
        "nombre": "Outbound agendamiento presencial",
        "nivel": 1,
        "tipificacion_id": 73,
        "categoria_padre_id": None
    },


    {
        "id": 414,
        "nombre": "Sicecon",
        "nivel": 1,
        "tipificacion_id": 74,
        "categoria_padre_id": None
    },
    {
        "id": 415,
        "nombre": "Denuncia fácil",
        "nivel": 1,
        "tipificacion_id": 74,
        "categoria_padre_id": None
    },

    {
        "id": 416,
        "nombre": "Reporte denuncias de genero",
        "nivel": 1,
        "tipificacion_id": 75,
        "categoria_padre_id": None
    },
    {
        "id": 417,
        "nombre": "Violencia Sexual",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 416
    },
    {
        "id": 418,
        "nombre": "Violencia Intrafamiliar",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 416
    },
    {
        "id": 419,
        "nombre": "Violencia de Genero",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 416
    },
    {
        "id": 420,
        "nombre": "Trata de personas",
        "nivel": 1,
        "tipificacion_id": 75,
        "categoria_padre_id": None
    },
    {
        "id": 421,
        "nombre": "Denuncias anónimas",
        "nivel": 1,
        "tipificacion_id": 75,
        "categoria_padre_id": None
    },
    {
        "id": 422,
        "nombre": "Hechos de corrupción",
        "nivel": 1,
        "tipificacion_id": 75,
        "categoria_padre_id": None
    },
    {
        "id": 423,
        "nombre": "Crimen organizado",
        "nivel": 1,
        "tipificacion_id": 75,
        "categoria_padre_id": None
    },
    {
        "id": 424,
        "nombre": "Líderes sociales",
        "nivel": 1,
        "tipificacion_id": 75,
        "categoria_padre_id": None
    },
    {
        "id": 425,
        "nombre": "Conflicto armado",
        "nivel": 1,
        "tipificacion_id": 75,
        "categoria_padre_id": None
    },
    {
        "id": 426,
        "nombre": "MBU",
        "nivel": 1,
        "tipificacion_id": 76,
        "categoria_padre_id": None
    },
    {
        "id": 427,
        "nombre": "Reporte de desaparecidos",
        "nivel": 1,
        "tipificacion_id": 76,
        "categoria_padre_id": None
    },
    {
        "id": 428,
        "nombre": "Se corrige el relato y se clasifica",
        "nivel": 1,
        "tipificacion_id": 77,
        "categoria_padre_id": None
    },
    {
        "id": 429,
        "nombre": "Solo se clasifica la denuncia",
        "nivel": 1,
        "tipificacion_id": 77,
        "categoria_padre_id": None
    },
    
    {
        "id": 430,
        "nombre": "Orientación para interponer denuncia",
        "nivel": 1,
        "tipificacion_id": 78,
        "categoria_padre_id": None
    },
    {
        "id": 431,
        "nombre": "Orientación para interponer PQRS",
        "nivel": 1,
        "tipificacion_id": 78,
        "categoria_padre_id": None
    },
    {
        "id": 432,
        "nombre": "Información denuncia y despacho asignado",
        "nivel": 1,
        "tipificacion_id": 78,
        "categoria_padre_id": None
    },
    {
        "id": 433,
        "nombre": "Orientación e información general",
        "nivel": 1,
        "tipificacion_id": 78,
        "categoria_padre_id": None
    },
    {
        "id": 434,
        "nombre": "Orientación para perdida de documentos",
        "nivel": 1,
        "tipificacion_id": 78,
        "categoria_padre_id": None
    },
    {
        "id": 435,
        "nombre": "Link Suip- autogestión denuncia.",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 430
    },
    {
        "id": 436,
        "nombre": "Formulario denuncia fácil",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 430
    },
    {
        "id": 437,
        "nombre": "Comisaria, inspección u otros",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 430
    },
    {
        "id": 438,
        "nombre": "Orientación SUSI - Página Web",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 431
    },
    {
        "id": 439,
        "nombre": "Orientación Correo",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 431
    },
    
    
    {
        "id": 440,
        "nombre": "Petición",
        "nivel": 1,
        "tipificacion_id": 79,
        "categoria_padre_id": None
    },
    {
        "id": 441,
        "nombre": "Queja",
        "nivel": 1,
        "tipificacion_id": 79,
        "categoria_padre_id": None
    },
    {
        "id": 442,
        "nombre": "Reclamo",
        "nivel": 1,
        "tipificacion_id": 79,
        "categoria_padre_id": None
    },
    {
        "id": 443,
        "nombre": "Sugerencia",
        "nivel": 1,
        "tipificacion_id": 79,
        "categoria_padre_id": None
    },
    {
        "id": 444,
        "nombre": "Felicitación",
        "nivel": 1,
        "tipificacion_id": 79,
        "categoria_padre_id": None
    },
    {
        "id": 445,
        "nombre": "Solicitud copia de la denuncia",
        "nivel": 1,
        "tipificacion_id": 79,
        "categoria_padre_id": None
    },
    {
        "id": 446,
        "nombre": "Reclamo por falta de rta a PQRS",
        "nivel": 1,
        "tipificacion_id": 79,
        "categoria_padre_id": None
    },
    
    {
        "id": 447,
        "nombre": "Transferencia a Nivel 1",
        "nivel": 1,
        "tipificacion_id": 80,
        "categoria_padre_id": None
    },
    {
        "id": 448,
        "nombre": "Transferencia a Nivel 2",
        "nivel": 1,
        "tipificacion_id": 80,
        "categoria_padre_id": None
    },
    {
        "id": 449,
        "nombre": "Transferencia Creadores de denuncia",
        "nivel": 1,
        "tipificacion_id": 80,
        "categoria_padre_id": None
    },
    {
        "id": 450,
        "nombre": "Transferencia a Abogados",
        "nivel": 1,
        "tipificacion_id": 80,
        "categoria_padre_id": None
    },
    {
        "id": 451,
        "nombre": "Transferencia a Psicologia",
        "nivel": 1,
        "tipificacion_id": 80,
        "categoria_padre_id": None
    },
    {
        "id": 452,
        "nombre": "Transferencia a Justicia Transicional",
        "nivel": 1,
        "tipificacion_id": 80,
        "categoria_padre_id": None
    },
    {
        "id": 453,
        "nombre": "Transferencia Agente Bilingüe",
        "nivel": 1,
        "tipificacion_id": 80,
        "categoria_padre_id": None
    },
    
    {
        "id": 454,
        "nombre": "Cancelar Cita",
        "nivel": 1,
        "tipificacion_id": 81,
        "categoria_padre_id": None
    },
    {
        "id": 455,
        "nombre": "Agendar Cita",
        "nivel": 1,
        "tipificacion_id": 81,
        "categoria_padre_id": None
    },
    
    {
        "id": 456,
        "nombre": "Solicita Presencia Inmediata de Policia",
        "nivel": 1,
        "tipificacion_id": 82,
        "categoria_padre_id": None
    },
    {
        "id": 457,
        "nombre": "Solicita presencia de Policía pero (No está en riesgo la vida o la integridad)",
        "nivel": 1,
        "tipificacion_id": 82,
        "categoria_padre_id": None
    },
    {
        "id": 458,
        "nombre": "Presencia exitosa",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 456
    },
    {
        "id": 459,
        "nombre": "Transfiere a 123 u otra entidad",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 456
    },
    {
        "id": 460,
        "nombre": "Solicita presencia de Policía pero (No está en riesgo la vida o la integridad de la víctima o no es penal)",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 457
    },
    
    
    
    {
        "id": 461,
        "nombre": "Llamada Equivocada",
        "nivel": 1,
        "tipificacion_id": 83,
        "categoria_padre_id": None
    },
    {
        "id": 462,
        "nombre": "Llamada Muda",
        "nivel": 1,
        "tipificacion_id": 83,
        "categoria_padre_id": None
    },
    {
        "id": 463,
        "nombre": "Llamada de Broma",
        "nivel": 1,
        "tipificacion_id": 83,
        "categoria_padre_id": None
    },
    {
        "id": 464,
        "nombre": "Llamada Caida",
        "nivel": 1,
        "tipificacion_id": 83,
        "categoria_padre_id": None
    },
    {
        "id": 465,
        "nombre": "Llamada de Prueba",
        "nivel": 1,
        "tipificacion_id": 83,
        "categoria_padre_id": None
    },
    
    
    {
        "id": 466,
        "nombre": "Presencial",
        "nivel": 1,
        "tipificacion_id": 84,
        "categoria_padre_id": None
    },
    {
        "id": 467,
        "nombre": "Denuncia fácil",
        "nivel": 1,
        "tipificacion_id": 84,
        "categoria_padre_id": None
    },
    {
        "id": 468,
        "nombre": "Telefónico",
        "nivel": 1,
        "tipificacion_id": 84,
        "categoria_padre_id": None
    },
    {
        "id": 469,
        "nombre": "Link Suip",
        "nivel": 1,
        "tipificacion_id": 84,
        "categoria_padre_id": None
    },
    {
        "id": 470,
        "nombre": "ADenunciar",
        "nivel": 1,
        "tipificacion_id": 84,
        "categoria_padre_id": None
    },
    
    
    
    {
        "id": 471,
        "nombre": "Consulta de sedes y despachos de FGN / PQRS",
        "nivel": 1,
        "tipificacion_id": 86,
        "categoria_padre_id": None
    },
    {
        "id": 472,
        "nombre": "Consulta de casos NUNC / Estado denuncia",
        "nivel": 1,
        "tipificacion_id": 86,
        "categoria_padre_id": None
    },
    {
        "id": 473,
        "nombre": "Saber si ha sido denunciado",
        "nivel": 1,
        "tipificacion_id": 86,
        "categoria_padre_id": None
    },
    {
        "id": 474,
        "nombre": "Orientación General",
        "nivel": 1,
        "tipificacion_id": 86,
        "categoria_padre_id": None
    },
    {
        "id": 475,
        "nombre": "Orientación radicar denuncia",
        "nivel": 1,
        "tipificacion_id": 86,
        "categoria_padre_id": None
    },
    {
        "id": 476,
        "nombre": "Orientación para perdida de documentos",
        "nivel": 1,
        "tipificacion_id": 86,
        "categoria_padre_id": None
    },
    {
        "id": 477,
        "nombre": "Orientación Comisaria, inspección u otros",
        "nivel": 1,
        "tipificacion_id": 86,
        "categoria_padre_id": None
    },
    {
        "id": 478,
        "nombre": "Interacción Equivocada",
        "nivel": 1,
        "tipificacion_id": 87,
        "categoria_padre_id": None
    },
    {
        "id": 479,
        "nombre": "Interacción Muda",
        "nivel": 1,
        "tipificacion_id": 87,
        "categoria_padre_id": None
    },
    {
        "id": 480,
        "nombre": "Interacción de Broma",
        "nivel": 1,
        "tipificacion_id": 87,
        "categoria_padre_id": None
    },
    {
        "id": 481,
        "nombre": "Interacción Caida",
        "nivel": 1,
        "tipificacion_id": 87,
        "categoria_padre_id": None
    },
    {
        "id": 482,
        "nombre": "Interacción de Prueba",
        "nivel": 1,
        "tipificacion_id": 87,
        "categoria_padre_id": None
    },
    {
        "id": 483,
        "nombre": "Presencial",
        "nivel": 1,
        "tipificacion_id": 88,
        "categoria_padre_id": None
    },
    {
        "id": 484,
        "nombre": "Denuncia fácil",
        "nivel": 1,
        "tipificacion_id": 88,
        "categoria_padre_id": None
    },
    {
        "id": 485,
        "nombre": "Telefónico",
        "nivel": 1,
        "tipificacion_id": 88,
        "categoria_padre_id": None
    },
    {
        "id": 486,
        "nombre": "Link Suip",
        "nivel": 1,
        "tipificacion_id": 88,
        "categoria_padre_id": None
    },
    {
        "id": 487,
        "nombre": "ADenunciar",
        "nivel": 1,
        "tipificacion_id": 88,
        "categoria_padre_id": None
    },
    
    
    
    {
        "id": 488,
        "nombre": "Consulta de sedes y despachos de FGN / PQRS",
        "nivel": 1,
        "tipificacion_id": 89,
        "categoria_padre_id": None
    },
    {
        "id": 489,
        "nombre": "Consulta de casos NUNC / Estado denuncia",
        "nivel": 1,
        "tipificacion_id": 89,
        "categoria_padre_id": None
    },
    {
        "id": 490,
        "nombre": "Saber si ha sido denunciado",
        "nivel": 1,
        "tipificacion_id": 89,
        "categoria_padre_id": None
    },
    {
        "id": 491,
        "nombre": "Orientación General",
        "nivel": 1,
        "tipificacion_id": 89,
        "categoria_padre_id": None
    },
    {
        "id": 492,
        "nombre": "Orientación radicar denuncia",
        "nivel": 1,
        "tipificacion_id": 89,
        "categoria_padre_id": None
    },
    {
        "id": 493,
        "nombre": "Orientación para perdida de documentos",
        "nivel": 1,
        "tipificacion_id": 89,
        "categoria_padre_id": None
    },
    {
        "id": 494,
        "nombre": "Orientación Comisaria, inspección u otros",
        "nivel": 1,
        "tipificacion_id": 89,
        "categoria_padre_id": None
    },
    {
        "id": 495,
        "nombre": "Interacción Equivocada",
        "nivel": 1,
        "tipificacion_id": 90,
        "categoria_padre_id": None
    },
    {
        "id": 496,
        "nombre": "Interacción Muda",
        "nivel": 1,
        "tipificacion_id": 90,
        "categoria_padre_id": None
    },
    {
        "id": 497,
        "nombre": "Interacción de Broma",
        "nivel": 1,
        "tipificacion_id": 90,
        "categoria_padre_id": None
    },
    {
        "id": 498,
        "nombre": "Interacción Caida",
        "nivel": 1,
        "tipificacion_id": 90,
        "categoria_padre_id": None
    },
    {
        "id": 499,
        "nombre": "Interacción de Prueba",
        "nivel": 1,
        "tipificacion_id": 90,
        "categoria_padre_id": None
    },
    {
        "id": 500,
        "nombre": "Presencial",
        "nivel": 1,
        "tipificacion_id": 91,
        "categoria_padre_id": None
    },
    {
        "id": 501,
        "nombre": "Denuncia fácil",
        "nivel": 1,
        "tipificacion_id": 91,
        "categoria_padre_id": None
    },
    {
        "id": 502,
        "nombre": "Telefónico",
        "nivel": 1,
        "tipificacion_id": 91,
        "categoria_padre_id": None
    },
    {
        "id": 503,
        "nombre": "Link Suip",
        "nivel": 1,
        "tipificacion_id": 91,
        "categoria_padre_id": None
    },
    {
        "id": 504,
        "nombre": "ADenunciar",
        "nivel": 1,
        "tipificacion_id": 91,
        "categoria_padre_id": None
    },
    
    
    
    {
        "id": 505,
        "nombre": "Sicecon",
        "nivel": 1,
        "tipificacion_id": 92,
        "categoria_padre_id": None
    },
    {
        "id": 506,
        "nombre": "Denuncia fácil",
        "nivel": 1,
        "tipificacion_id": 92,
        "categoria_padre_id": None
    },
    {
        "id": 507,
        "nombre": "Reporte denuncias de genero",
        "nivel": 1,
        "tipificacion_id": 93,
        "categoria_padre_id": None
    },
    {
        "id": 508,
        "nombre": "Violencia Sexual",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 507
    },
    {
        "id": 509,
        "nombre": "Violencia Intrafamiliar",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 507
    },
    {
        "id": 510,
        "nombre": "Violencia de Genero",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 507
    },
    {
        "id": 511,
        "nombre": "Trata de personas",
        "nivel": 1,
        "tipificacion_id": 93,
        "categoria_padre_id": None
    },
    {
        "id": 512,
        "nombre": "Denuncias anónimas",
        "nivel": 1,
        "tipificacion_id": 93,
        "categoria_padre_id": None
    },
    {
        "id": 513,
        "nombre": "Hechos de corrupción",
        "nivel": 1,
        "tipificacion_id": 93,
        "categoria_padre_id": None
    },
    {
        "id": 514,
        "nombre": "Crimen organizado",
        "nivel": 1,
        "tipificacion_id": 93,
        "categoria_padre_id": None
    },
    {
        "id": 515,
        "nombre": "Líderes sociales",
        "nivel": 1,
        "tipificacion_id": 93,
        "categoria_padre_id": None
    },
    {
        "id": 516,
        "nombre": "Conflicto armado",
        "nivel": 1,
        "tipificacion_id": 93,
        "categoria_padre_id": None
    },
    {
        "id": 517,
        "nombre": "MBU",
        "nivel": 1,
        "tipificacion_id": 94,
        "categoria_padre_id": None
    },
    {
        "id": 518,
        "nombre": "Reporte de desaparecidos",
        "nivel": 1,
        "tipificacion_id": 94,
        "categoria_padre_id": None
    },
    
    
    
    
    {
        "id": 519,
        "nombre": "Se corrige el relato y se clasifica",
        "nivel": 1,
        "tipificacion_id": 95,
        "categoria_padre_id": None
    },
    {
        "id": 520,
        "nombre": "Solo se clasifica la denuncia",
        "nivel": 1,
        "tipificacion_id": 95,
        "categoria_padre_id": None
    },
    {
        "id": 521,
        "nombre": "Orientación para interponer denuncia",
        "nivel": 1,
        "tipificacion_id": 96,
        "categoria_padre_id": None
    },
    {
        "id": 522,
        "nombre": "Link Suip- autogestión denuncia.",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 521
    },
    {
        "id": 523,
        "nombre": "Formulario denuncia fácil",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 521
    },
    {
        "id": 524,
        "nombre": "Comisaria, inspección u otros",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 521
    },
    {
        "id": 525,
        "nombre": "Orientación para interponer PQRS",
        "nivel": 1,
        "tipificacion_id": 96,
        "categoria_padre_id": None
    },
    {
        "id": 526,
        "nombre": "Orientación SUSI - Página Web",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 525
    },
    {
        "id": 527,
        "nombre": "Orientación Correo",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 525
    },
    {
        "id": 528,
        "nombre": "Información denuncia y despacho asignado",
        "nivel": 1,
        "tipificacion_id": 96,
        "categoria_padre_id": None
    },
    {
        "id": 529,
        "nombre": "Orientación e información general",
        "nivel": 1,
        "tipificacion_id": 96,
        "categoria_padre_id": None
    },
    {
        "id": 530,
        "nombre": "Orientación para perdida de documentos",
        "nivel": 1,
        "tipificacion_id": 96,
        "categoria_padre_id": None
    },
    {
        "id": 531,
        "nombre": "Petición",
        "nivel": 1,
        "tipificacion_id": 97,
        "categoria_padre_id": None
    },
    {
        "id": 532,
        "nombre": "Queja",
        "nivel": 1,
        "tipificacion_id": 97,
        "categoria_padre_id": None
    },
    {
        "id": 533,
        "nombre": "Reclamo",
        "nivel": 1,
        "tipificacion_id": 97,
        "categoria_padre_id": None
    },
    {
        "id": 534,
        "nombre": "Sugerencia",
        "nivel": 1,
        "tipificacion_id": 97,
        "categoria_padre_id": None
    },
    {
        "id": 535,
        "nombre": "Felicitación",
        "nivel": 1,
        "tipificacion_id": 97,
        "categoria_padre_id": None
    },
    {
        "id": 536,
        "nombre": "Solicitud copia de la denuncia",
        "nivel": 1,
        "tipificacion_id": 97,
        "categoria_padre_id": None
    },
    {
        "id": 537,
        "nombre": "Reclamo por falta de rta a PQRS",
        "nivel": 1,
        "tipificacion_id": 97,
        "categoria_padre_id": None
    },

    {
        "id": 538,
        "nombre": "Transferencia a Nivel 1",
        "nivel": 1,
        "tipificacion_id": 98,
        "categoria_padre_id": None
    },
    {
        "id": 539,
        "nombre": "Transferencia a Nivel 2",
        "nivel": 1,
        "tipificacion_id": 98,
        "categoria_padre_id": None
    },
    {
        "id": 540,
        "nombre": "Transferencia Creadores de denuncia",
        "nivel": 1,
        "tipificacion_id": 98,
        "categoria_padre_id": None
    },
    {
        "id": 541,
        "nombre": "Transferencia a Abogados",
        "nivel": 1,
        "tipificacion_id": 98,
        "categoria_padre_id": None
    },
    {
        "id": 542,
        "nombre": "Transferencia a Psicologia",
        "nivel": 1,
        "tipificacion_id": 98,
        "categoria_padre_id": None
    },
    {
        "id": 543,
        "nombre": "Transferencia a Justicia Transicional",
        "nivel": 1,
        "tipificacion_id": 98,
        "categoria_padre_id": None
    },
    {
        "id": 544,
        "nombre": "Transferencia Agente Bilingüe",
        "nivel": 1,
        "tipificacion_id": 97,
        "categoria_padre_id": None
    },
    
    {
        "id": 545,
        "nombre": "Cancelar Cita",
        "nivel": 1,
        "tipificacion_id": 99,
        "categoria_padre_id": None
    },
    {
        "id": 546,
        "nombre": "Agendar Cita",
        "nivel": 1,
        "tipificacion_id": 99,
        "categoria_padre_id": None
    },
    
    {
        "id": 547,
        "nombre": "Solicita Presencia Inmediata de Policia",
        "nivel": 1,
        "tipificacion_id": 100,
        "categoria_padre_id": None
    },
    {
        "id": 548,
        "nombre": "Presencia exitosa",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 547
    },
    {
        "id": 549,
        "nombre": "Transfiere a 123 u otra entidad",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 547
    },
    {
        "id": 550,
        "nombre": "Solicita presencia de Policía pero (No está en riesgo la vida o la integridad)",
        "nivel": 1,
        "tipificacion_id": 100,
        "categoria_padre_id": None
    },
    {
        "id": 551,
        "nombre": "Solicita presencia de Policía pero (No está en riesgo la vida o la integridad de la víctima o no es penal)",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 550
    },
    
    {
        "id": 552,
        "nombre": "Llamada Equivocada",
        "nivel": 1,
        "tipificacion_id": 101,
        "categoria_padre_id": None
    },
    {
        "id": 553,
        "nombre": "Llamada Colgada",
        "nivel": 1,
        "tipificacion_id": 101,
        "categoria_padre_id": None
    },
    {
        "id": 554,
        "nombre": "Llamada Muda",
        "nivel": 1,
        "tipificacion_id": 101,
        "categoria_padre_id": None
    },
    {
        "id": 555,
        "nombre": "Llamada de Broma",
        "nivel": 1,
        "tipificacion_id": 101,
        "categoria_padre_id": None
    },
    {
        "id": 556,
        "nombre": "Llamada Caida",
        "nivel": 1,
        "tipificacion_id": 101,
        "categoria_padre_id": None
    },
    {
        "id": 557,
        "nombre": "Llamada de Prueba",
        "nivel": 1,
        "tipificacion_id": 101,
        "categoria_padre_id": None
    },
    
    
    {
        "id": 558,
        "nombre": "Presencial",
        "nivel": 1,
        "tipificacion_id": 102,
        "categoria_padre_id": None
    },
    {
        "id": 559,
        "nombre": "Denuncia fácil",
        "nivel": 1,
        "tipificacion_id": 102,
        "categoria_padre_id": None
    },
    {
        "id": 560,
        "nombre": "Telefónico",
        "nivel": 1,
        "tipificacion_id": 102,
        "categoria_padre_id": None
    },
    {
        "id": 561,
        "nombre": "Link Suip",
        "nivel": 1,
        "tipificacion_id": 102,
        "categoria_padre_id": None
    },
    {
        "id": 562,
        "nombre": "ADenunciar",
        "nivel": 1,
        "tipificacion_id": 102,
        "categoria_padre_id": None
    },
    {
        "id": 563,
        "nombre": "Outbound Denuncia",
        "nivel": 1,
        "tipificacion_id": 103,
        "categoria_padre_id": None
    },
    {
        "id": 564,
        "nombre": "Outbound PQRS",
        "nivel": 1,
        "tipificacion_id": 103,
        "categoria_padre_id": None
    },
    {
        "id": 565,
        "nombre": "Outbound Orientacion, Informacion  y Consulta de Casos",
        "nivel": 1,
        "tipificacion_id": 103,
        "categoria_padre_id": None
    },
    {
        "id": 566,
        "nombre": "Outbound Proceso clasificación denuncia",
        "nivel": 1,
        "tipificacion_id": 103,
        "categoria_padre_id": None
    },
    {
        "id": 567,
        "nombre": "Outbound Presencia inmediata de policia",
        "nivel": 1,
        "tipificacion_id": 103,
        "categoria_padre_id": None
    },
    {
        "id": 568,
        "nombre": "Outbound Desaparecidos",
        "nivel": 1,
        "tipificacion_id": 103,
        "categoria_padre_id": None
    },
    {
        "id": 569,
        "nombre": "Outbound No Efectivo",
        "nivel": 1,
        "tipificacion_id": 103,
        "categoria_padre_id": None
    },
    {
        "id": 570,
        "nombre": "Outbound agendamiento presencial",
        "nivel": 1,
        "tipificacion_id": 103,
        "categoria_padre_id": None
    },
    
    
    
    
    {
        "id": 571,
        "nombre": "Sicecon",
        "nivel": 1,
        "tipificacion_id": 104,
        "categoria_padre_id": None
    },
    {
        "id": 572,
        "nombre": "Denuncia fácil",
        "nivel": 1,
        "tipificacion_id": 104,
        "categoria_padre_id": None
    },
    {
        "id": 573,
        "nombre": "Reporte denuncias de genero",
        "nivel": 1,
        "tipificacion_id": 105,
        "categoria_padre_id": None
    },
    {
        "id": 574,
        "nombre": "Violencia Sexual",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 573
    },
    {
        "id": 575,
        "nombre": "Violencia Intrafamiliar",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 573
    },
    {
        "id": 576,
        "nombre": "Violencia de Genero",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 573
    },
    {
        "id": 577,
        "nombre": "Trata de personas",
        "nivel": 1,
        "tipificacion_id": 105,
        "categoria_padre_id": None
    },
    {
        "id": 578,
        "nombre": "Denuncias anónimas",
        "nivel": 1,
        "tipificacion_id": 105,
        "categoria_padre_id": None
    },
    {
        "id": 579,
        "nombre": "Hechos de corrupción",
        "nivel": 1,
        "tipificacion_id": 105,
        "categoria_padre_id": None
    },
    {
        "id": 580,
        "nombre": "Crimen organizado",
        "nivel": 1,
        "tipificacion_id": 105,
        "categoria_padre_id": None
    },
    {
        "id": 581,
        "nombre": "Líderes sociales",
        "nivel": 1,
        "tipificacion_id": 105,
        "categoria_padre_id": None
    },
    {
        "id": 582,
        "nombre": "Conflicto armado",
        "nivel": 1,
        "tipificacion_id": 105,
        "categoria_padre_id": None
    },
    {
        "id": 583,
        "nombre": "MBU",
        "nivel": 1,
        "tipificacion_id": 106,
        "categoria_padre_id": None
    },
    {
        "id": 584,
        "nombre": "Reporte de desaparecidos",
        "nivel": 1,
        "tipificacion_id": 106,
        "categoria_padre_id": None
    },
    {
        "id": 585,
        "nombre": "Se corrige el relato y se clasifica",
        "nivel": 1,
        "tipificacion_id": 107,
        "categoria_padre_id": None
    },
    {
        "id": 586,
        "nombre": "Solo se clasifica la denuncia",
        "nivel": 1,
        "tipificacion_id": 107,
        "categoria_padre_id": None
    },
    
    {
        "id": 587,
        "nombre": "Orientación para interponer denuncia",
        "nivel": 1,
        "tipificacion_id": 108,
        "categoria_padre_id": None
    },
    {
        "id": 588,
        "nombre": "Link Suip- autogestión denuncia.",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 587
    },
    {
        "id": 589,
        "nombre": "Formulario denuncia fácil",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 587
    },
    {
        "id": 590,
        "nombre": "Comisaria, inspección u otros",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 587
    },
    {
        "id": 591,
        "nombre": "Orientación para interponer PQRS",
        "nivel": 1,
        "tipificacion_id": 108,
        "categoria_padre_id": None
    },
    {
        "id": 592,
        "nombre": "Orientación SUSI - Página Web",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 591
    },
    {
        "id": 593,
        "nombre": "Orientación Correo",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 591
    },
    {
        "id": 594,
        "nombre": "Información denuncia y despacho asignado",
        "nivel": 1,
        "tipificacion_id": 108,
        "categoria_padre_id": None
    },
    {
        "id": 595,
        "nombre": "Orientación e información general",
        "nivel": 1,
        "tipificacion_id": 108,
        "categoria_padre_id": None
    },
    {
        "id": 596,
        "nombre": "Orientación para perdida de documentos",
        "nivel": 1,
        "tipificacion_id": 108,
        "categoria_padre_id": None
    },
    {
        "id": 597,
        "nombre": "Petición",
        "nivel": 1,
        "tipificacion_id": 109,
        "categoria_padre_id": None
    },
    {
        "id": 598,
        "nombre": "Queja",
        "nivel": 1,
        "tipificacion_id": 109,
        "categoria_padre_id": None
    },
    {
        "id": 599,
        "nombre": "Reclamo",
        "nivel": 1,
        "tipificacion_id": 109,
        "categoria_padre_id": None
    },
    {
        "id": 600,
        "nombre": "Sugerencia",
        "nivel": 1,
        "tipificacion_id": 109,
        "categoria_padre_id": None
    },
    {
        "id": 601,
        "nombre": "Felicitación",
        "nivel": 1,
        "tipificacion_id": 109,
        "categoria_padre_id": None
    },
    {
        "id": 602,
        "nombre": "Solicitud copia de la denuncia",
        "nivel": 1,
        "tipificacion_id": 109,
        "categoria_padre_id": None
    },
    {
        "id": 603,
        "nombre": "Reclamo por falta de rta a PQRS",
        "nivel": 1,
        "tipificacion_id": 109,
        "categoria_padre_id": None
    },
    {
        "id": 604,
        "nombre": "Transferencia a Nivel 1",
        "nivel": 1,
        "tipificacion_id": 110,
        "categoria_padre_id": None
    },
    {
        "id": 605,
        "nombre": "Transferencia a Nivel 2",
        "nivel": 1,
        "tipificacion_id": 110,
        "categoria_padre_id": None
    },
    {
        "id": 606,
        "nombre": "Transferencia Creadores de denuncia",
        "nivel": 1,
        "tipificacion_id": 110,
        "categoria_padre_id": None
    },
    {
        "id": 607,
        "nombre": "Transferencia a Abogados",
        "nivel": 1,
        "tipificacion_id": 110,
        "categoria_padre_id": None
    },
    {
        "id": 608,
        "nombre": "Transferencia a Psicologia",
        "nivel": 1,
        "tipificacion_id": 110,
        "categoria_padre_id": None
    },
    {
        "id": 609,
        "nombre": "Transferencia a Justicia Transicional",
        "nivel": 1,
        "tipificacion_id": 110,
        "categoria_padre_id": None
    },
    {
        "id": 610,
        "nombre": "Transferencia Agente Bilingüe",
        "nivel": 1,
        "tipificacion_id": 110,
        "categoria_padre_id": None
    },
    
    {
        "id": 611,
        "nombre": "Cancelar Cita",
        "nivel": 1,
        "tipificacion_id": 111,
        "categoria_padre_id": None
    },
    {
        "id": 612,
        "nombre": "Agendar Cita",
        "nivel": 1,
        "tipificacion_id": 111,
        "categoria_padre_id": None
    },
    {
        "id": 613,
        "nombre": "Solicita Presencia Inmediata de Policia",
        "nivel": 1,
        "tipificacion_id": 112,
        "categoria_padre_id": None
    },
    {
        "id": 614,
        "nombre": "Presencia exitosa",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 613
    },
    {
        "id": 615,
        "nombre": "Transfiere a 123 u otra entidad",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 613
    },
    {
        "id": 616,
        "nombre": "Solicita presencia de Policía pero (No está en riesgo la vida o la integridad)",
        "nivel": 1,
        "tipificacion_id": 112,
        "categoria_padre_id": None
    },
    {
        "id": 617,
        "nombre": "Solicita presencia de Policía pero (No está en riesgo la vida o la integridad de la víctima o no es penal)",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 616
    },
    {
        "id": 618,
        "nombre": "Llamada Equivocada",
        "nivel": 1,
        "tipificacion_id": 113,
        "categoria_padre_id": None
    },
    {
        "id": 619,
        "nombre": "Llamada Colgada",
        "nivel": 1,
        "tipificacion_id": 113,
        "categoria_padre_id": None
    },
    {
        "id": 620,
        "nombre": "Llamada Muda",
        "nivel": 1,
        "tipificacion_id": 113,
        "categoria_padre_id": None
    },
    {
        "id": 621,
        "nombre": "Llamada de Broma",
        "nivel": 1,
        "tipificacion_id": 113,
        "categoria_padre_id": None
    },
    {
        "id": 622,
        "nombre": "Llamada Caida",
        "nivel": 1,
        "tipificacion_id": 113,
        "categoria_padre_id": None
    },
    {
        "id": 623,
        "nombre": "Llamada de Prueba",
        "nivel": 1,
        "tipificacion_id": 113,
        "categoria_padre_id": None
    },
    {
        "id": 624,
        "nombre": "Presencial",
        "nivel": 1,
        "tipificacion_id": 114,
        "categoria_padre_id": None
    },
    {
        "id": 625,
        "nombre": "Denuncia fácil",
        "nivel": 1,
        "tipificacion_id": 114,
        "categoria_padre_id": None
    },
    {
        "id": 626,
        "nombre": "Telefónico",
        "nivel": 1,
        "tipificacion_id": 114,
        "categoria_padre_id": None
    },
    {
        "id": 627,
        "nombre": "Link Suip",
        "nivel": 1,
        "tipificacion_id": 114,
        "categoria_padre_id": None
    },
    {
        "id": 628,
        "nombre": "ADenunciar",
        "nivel": 1,
        "tipificacion_id": 114,
        "categoria_padre_id": None
    },
    {
        "id": 629,
        "nombre": "Outbound Denuncia",
        "nivel": 1,
        "tipificacion_id": 115,
        "categoria_padre_id": None
    },
    {
        "id": 630,
        "nombre": "Outbound PQRS",
        "nivel": 1,
        "tipificacion_id": 115,
        "categoria_padre_id": None
    },
    {
        "id": 631,
        "nombre": "Outbound Orientacion, Informacion  y Consulta de Casos",
        "nivel": 1,
        "tipificacion_id": 115,
        "categoria_padre_id": None
    },
    {
        "id": 632,
        "nombre": "Outbound Proceso clasificación denuncia",
        "nivel": 1,
        "tipificacion_id": 115,
        "categoria_padre_id": None
    },
    {
        "id": 633,
        "nombre": "Outbound Presencia inmediata de policia",
        "nivel": 1,
        "tipificacion_id": 115,
        "categoria_padre_id": None
    },
    {
        "id": 634,
        "nombre": "Outbound Desaparecidos",
        "nivel": 1,
        "tipificacion_id": 115,
        "categoria_padre_id": None
    },
    {
        "id": 635,
        "nombre": "Outbound No Efectivo",
        "nivel": 1,
        "tipificacion_id": 115,
        "categoria_padre_id": None
    },
    {
        "id": 636,
        "nombre": "Outbound agendamiento presencial",
        "nivel": 1,
        "tipificacion_id": 115,
        "categoria_padre_id": None
    },
    
    
    {
        "id": 637,
        "nombre": "Sicecon",
        "nivel": 1,
        "tipificacion_id": 116,
        "categoria_padre_id": None
    },
    {
        "id": 638,
        "nombre": "Denuncia fácil",
        "nivel": 1,
        "tipificacion_id": 116,
        "categoria_padre_id": None
    },

    {
        "id": 639,
        "nombre": "Reporte denuncias de genero",
        "nivel": 1,
        "tipificacion_id": 117,
        "categoria_padre_id": None
    },
    {
        "id": 640,
        "nombre": "Violencia Sexual",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 639
    },
    {
        "id": 641,
        "nombre": "Violencia Intrafamiliar",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 639
    },
    {
        "id": 642,
        "nombre": "Violencia de Genero",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 639
    },
    {
        "id": 643,
        "nombre": "Trata de personas",
        "nivel": 1,
        "tipificacion_id": 117,
        "categoria_padre_id": None
    },
    {
        "id": 644,
        "nombre": "Denuncias anónimas",
        "nivel": 1,
        "tipificacion_id": 117,
        "categoria_padre_id": None
    },
    {
        "id": 645,
        "nombre": "Hechos de corrupción",
        "nivel": 1,
        "tipificacion_id": 117,
        "categoria_padre_id": None
    },
    {
        "id": 646,
        "nombre": "Crimen organizado",
        "nivel": 1,
        "tipificacion_id": 117,
        "categoria_padre_id": None
    },
    {
        "id": 647,
        "nombre": "Líderes sociales",
        "nivel": 1,
        "tipificacion_id": 117,
        "categoria_padre_id": None
    },
    {
        "id": 648,
        "nombre": "Conflicto armado",
        "nivel": 1,
        "tipificacion_id": 117,
        "categoria_padre_id": None
    },

    {
        "id": 649,
        "nombre": "MBU",
        "nivel": 1,
        "tipificacion_id": 118,
        "categoria_padre_id": None
    },
    {
        "id": 650,
        "nombre": "Reporte de desaparecidos",
        "nivel": 1,
        "tipificacion_id": 118,
        "categoria_padre_id": None
    },


    {
        "id": 651,
        "nombre": "Se corrige el relato y se clasifica",
        "nivel": 1,
        "tipificacion_id": 119,
        "categoria_padre_id": None
    },
    {
        "id": 652,
        "nombre": "Solo se clasifica la denuncia",
        "nivel": 1,
        "tipificacion_id": 119,
        "categoria_padre_id": None
    },

    {
        "id": 653,
        "nombre": "Orientación para interponer denuncia",
        "nivel": 1,
        "tipificacion_id": 120,
        "categoria_padre_id": None
    },
    {
        "id": 654,
        "nombre": "Link Suip- autogestión denuncia.",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 653
    },
    {
        "id": 655,
        "nombre": "Formulario denuncia fácil",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 653
    },
    {
        "id": 656,
        "nombre": "Comisaria, inspección u otros",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 653
    },
    {
        "id": 657,
        "nombre": "Orientación para interponer PQRS",
        "nivel": 1,
        "tipificacion_id": 120,
        "categoria_padre_id": None
    },
    {
        "id": 658,
        "nombre": "Orientación SUSI - Página Web",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 657
    },
    {
        "id": 659,
        "nombre": "Orientación Correo",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 657
    },
    {
        "id": 660,
        "nombre": "Información denuncia y despacho asignado",
        "nivel": 1,
        "tipificacion_id": 120,
        "categoria_padre_id": None
    },
    {
        "id": 661,
        "nombre": "Orientación e información general",
        "nivel": 1,
        "tipificacion_id": 120,
        "categoria_padre_id": None
    },
    {
        "id": 662,
        "nombre": "Orientación para perdida de documentos",
        "nivel": 1,
        "tipificacion_id": 120,
        "categoria_padre_id": None
    },

    {
        "id": 663,
        "nombre": "Petición",
        "nivel": 1,
        "tipificacion_id": 121,
        "categoria_padre_id": None
    },
    {
        "id": 664,
        "nombre": "Queja",
        "nivel": 1,
        "tipificacion_id": 121,
        "categoria_padre_id": None
    },
    {
        "id": 665,
        "nombre": "Reclamo",
        "nivel": 1,
        "tipificacion_id": 121,
        "categoria_padre_id": None
    },
    {
        "id": 666,
        "nombre": "Sugerencia",
        "nivel": 1,
        "tipificacion_id": 121,
        "categoria_padre_id": None
    },
    {
        "id": 667,
        "nombre": "Felicitación",
        "nivel": 1,
        "tipificacion_id": 121,
        "categoria_padre_id": None
    },
    {
        "id": 668,
        "nombre": "Solicitud copia de la denuncia",
        "nivel": 1,
        "tipificacion_id": 121,
        "categoria_padre_id": None
    },
    {
        "id": 669,
        "nombre": "Reclamo por falta de rta a PQRS",
        "nivel": 1,
        "tipificacion_id": 121,
        "categoria_padre_id": None
    },
    
    {
        "id": 670,
        "nombre": "Transferencia a Nivel 1",
        "nivel": 1,
        "tipificacion_id": 122,
        "categoria_padre_id": None
    },
    {
        "id": 671,
        "nombre": "Transferencia a Nivel 2",
        "nivel": 1,
        "tipificacion_id": 122,
        "categoria_padre_id": None
    },
    {
        "id": 672,
        "nombre": "Transferencia Creadores de denuncia",
        "nivel": 1,
        "tipificacion_id": 122,
        "categoria_padre_id": None
    },
    {
        "id": 673,
        "nombre": "Transferencia a Abogados",
        "nivel": 1,
        "tipificacion_id": 122,
        "categoria_padre_id": None
    },
    {
        "id": 674,
        "nombre": "Transferencia a Psicologia",
        "nivel": 1,
        "tipificacion_id": 122,
        "categoria_padre_id": None
    },
    {
        "id": 675,
        "nombre": "Transferencia a Justicia Transicional",
        "nivel": 1,
        "tipificacion_id": 122,
        "categoria_padre_id": None
    },
    {
        "id": 676,
        "nombre": "Transferencia Agente Bilingüe",
        "nivel": 1,
        "tipificacion_id": 122,
        "categoria_padre_id": None
    },
    {
        "id": 677,
        "nombre": "Cancelar Cita",
        "nivel": 1,
        "tipificacion_id": 123,
        "categoria_padre_id": None
    },
    {
        "id": 678,
        "nombre": "Agendar Cita",
        "nivel": 1,
        "tipificacion_id": 123,
        "categoria_padre_id": None
    },
    {
        "id": 679,
        "nombre": "Solicita Presencia Inmediata de Policia",
        "nivel": 1,
        "tipificacion_id": 124,
        "categoria_padre_id": None
    },
    {
        "id": 680,
        "nombre": "Presencia exitosa",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 679
    },
    {
        "id": 681,
        "nombre": "Transfiere a 123 u otra entidad",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 679
    },
    {
        "id": 682,
        "nombre": "Solicita presencia de Policía pero (No está en riesgo la vida o la integridad)",
        "nivel": 1,
        "tipificacion_id": 124,
        "categoria_padre_id": None
    },
    {
        "id": 683,
        "nombre": "Solicita presencia de Policía pero (No está en riesgo la vida o la integridad de la víctima o no es penal)",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 682
    },
    {
        "id": 684,
        "nombre": "Llamada Equivocada",
        "nivel": 1,
        "tipificacion_id": 125,
        "categoria_padre_id": None
    },
    {
        "id": 685,
        "nombre": "Llamada Colgada",
        "nivel": 1,
        "tipificacion_id": 125,
        "categoria_padre_id": None
    },
    {
        "id": 686,
        "nombre": "Llamada Muda",
        "nivel": 1,
        "tipificacion_id": 125,
        "categoria_padre_id": None
    },
    {
        "id": 687,
        "nombre": "Llamada de Broma",
        "nivel": 1,
        "tipificacion_id": 125,
        "categoria_padre_id": None
    },
    {
        "id": 688,
        "nombre": "Llamada Caida",
        "nivel": 1,
        "tipificacion_id": 125,
        "categoria_padre_id": None
    },
    {
        "id": 689,
        "nombre": "Llamada de Prueba",
        "nivel": 1,
        "tipificacion_id": 125,
        "categoria_padre_id": None
    },
    {
        "id": 690,
        "nombre": "Presencial",
        "nivel": 1,
        "tipificacion_id": 126,
        "categoria_padre_id": None
    },
    {
        "id": 691,
        "nombre": "Denuncia fácil",
        "nivel": 1,
        "tipificacion_id": 126,
        "categoria_padre_id": None
    },
    {
        "id": 692,
        "nombre": "Telefónico",
        "nivel": 1,
        "tipificacion_id": 126,
        "categoria_padre_id": None
    },
    {
        "id": 693,
        "nombre": "Link Suip",
        "nivel": 1,
        "tipificacion_id": 126,
        "categoria_padre_id": None
    },
    {
        "id": 694,
        "nombre": "ADenunciar",
        "nivel": 1,
        "tipificacion_id": 126,
        "categoria_padre_id": None
    },
    {
        "id": 695,
        "nombre": "Outbound Denuncia Nivel 1",
        "nivel": 1,
        "tipificacion_id": 127,
        "categoria_padre_id": None
    },
    
    {
        "id": 696,
        "nombre": "Outbound Denuncias Nivel 2",
        "nivel": 1,
        "tipificacion_id": 127,
        "categoria_padre_id": None
    },
    {
        "id": 697,
        "nombre": "Outbound PQRS",
        "nivel": 1,
        "tipificacion_id": 127,
        "categoria_padre_id": None
    },
    {
        "id": 698,
        "nombre": "Outbound Orientacion, Informacion  y Consulta de Casos",
        "nivel": 1,
        "tipificacion_id": 127,
        "categoria_padre_id": None
    },
    {
        "id": 699,
        "nombre": "Outbound Proceso clasificación denuncia",
        "nivel": 1,
        "tipificacion_id": 127,
        "categoria_padre_id": None
    },
    {
        "id": 700,
        "nombre": "Outbound Presencia inmediata de policia",
        "nivel": 1,
        "tipificacion_id": 127,
        "categoria_padre_id": None
    },
    {
        "id": 701,
        "nombre": "Outbound Desaparecidos",
        "nivel": 1,
        "tipificacion_id": 127,
        "categoria_padre_id": None
    },
    {
        "id": 702,
        "nombre": "Outbound No Efectivo",
        "nivel": 1,
        "tipificacion_id": 127,
        "categoria_padre_id": None
    },
    {
        "id": 703,
        "nombre": "Outbound agendamiento presencial",
        "nivel": 1,
        "tipificacion_id": 127,
        "categoria_padre_id": None
    },
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    {
        "id": 704,
        "nombre": "Sicecon",
        "nivel": 1,
        "tipificacion_id": 128,
        "categoria_padre_id": None
    },
    {
        "id": 705,
        "nombre": "Denuncia fácil",
        "nivel": 1,
        "tipificacion_id": 128,
        "categoria_padre_id": None
    },
    {
        "id": 706,
        "nombre": "Reporte denuncias de genero",
        "nivel": 1,
        "tipificacion_id": 129,
        "categoria_padre_id": None
    },
    {
        "id": 707,
        "nombre": "Violencia Sexual",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 706
    },
    {
        "id": 708,
        "nombre": "Violencia Intrafamiliar",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 706
    },
    {
        "id": 709,
        "nombre": "Violencia de Genero",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 706
    },
    {
        "id": 710,
        "nombre": "Trata de personas",
        "nivel": 1,
        "tipificacion_id": 129,
        "categoria_padre_id": None
    },
    {
        "id": 711,
        "nombre": "Denuncias anónimas",
        "nivel": 1,
        "tipificacion_id": 129,
        "categoria_padre_id": None
    },
    {
        "id": 712,
        "nombre": "Hechos de corrupción",
        "nivel": 1,
        "tipificacion_id": 129,
        "categoria_padre_id": None
    },
    {
        "id": 713,
        "nombre": "Crimen organizado",
        "nivel": 1,
        "tipificacion_id": 129,
        "categoria_padre_id": None
    },
    {
        "id": 714,
        "nombre": "Líderes sociales",
        "nivel": 1,
        "tipificacion_id": 129,
        "categoria_padre_id": None
    },
    {
        "id": 715,
        "nombre": "Conflicto armado",
        "nivel": 1,
        "tipificacion_id": 129,
        "categoria_padre_id": None
    },
    {
        "id": 716,
        "nombre": "MBU",
        "nivel": 1,
        "tipificacion_id": 130,
        "categoria_padre_id": None
    },
    {
        "id": 717,
        "nombre": "Reporte de desaparecidos",
        "nivel": 1,
        "tipificacion_id": 130,
        "categoria_padre_id": None
    },
    {
        "id": 718,
        "nombre": "Se corrige el relato y se clasifica",
        "nivel": 1,
        "tipificacion_id": 119,
        "categoria_padre_id": None
    },
    {
        "id": 719,
        "nombre": "Solo se clasifica la denuncia",
        "nivel": 1,
        "tipificacion_id": 119,
        "categoria_padre_id": None
    },
    {
        "id": 720,
        "nombre": "Orientación para interponer denuncia",
        "nivel": 1,
        "tipificacion_id": 120,
        "categoria_padre_id": None
    },
    {
        "id": 721,
        "nombre": "Link Suip- autogestión denuncia.",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 720
    },
    {
        "id": 722,
        "nombre": "Formulario denuncia fácil",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 720
    },
    {
        "id": 723,
        "nombre": "Comisaria, inspección u otros",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 720
    },
    {
        "id": 724,
        "nombre": "Orientación para interponer PQRS",
        "nivel": 1,
        "tipificacion_id": 120,
        "categoria_padre_id": None
    },
    {
        "id": 725,
        "nombre": "Orientación SUSI - Página Web",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 724
    },
    {
        "id": 726,
        "nombre": "Orientación Correo",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 724
    },
    {
        "id": 727,
        "nombre": "Información denuncia y despacho asignado",
        "nivel": 1,
        "tipificacion_id": 120,
        "categoria_padre_id": None
    },
    {
        "id": 728,
        "nombre": "Orientación e información general",
        "nivel": 1,
        "tipificacion_id": 120,
        "categoria_padre_id": None
    },
    {
        "id": 729,
        "nombre": "Orientación para perdida de documentos",
        "nivel": 1,
        "tipificacion_id": 120,
        "categoria_padre_id": None
    },
    {
        "id": 730,
        "nombre": "Petición",
        "nivel": 1,
        "tipificacion_id": 121,
        "categoria_padre_id": None
    },
    {
        "id": 731,
        "nombre": "Queja",
        "nivel": 1,
        "tipificacion_id": 121,
        "categoria_padre_id": None
    },
    {
        "id": 732,
        "nombre": "Reclamo",
        "nivel": 1,
        "tipificacion_id": 121,
        "categoria_padre_id": None
    },
    {
        "id": 733,
        "nombre": "Sugerencia",
        "nivel": 1,
        "tipificacion_id": 121,
        "categoria_padre_id": None
    },
    {
        "id": 734,
        "nombre": "Felicitación",
        "nivel": 1,
        "tipificacion_id": 121,
        "categoria_padre_id": None
    },
    {
        "id": 735,
        "nombre": "Solicitud copia de la denuncia",
        "nivel": 1,
        "tipificacion_id": 121,
        "categoria_padre_id": None
    },
    {
        "id": 736,
        "nombre": "Reclamo por falta de rta a PQRS",
        "nivel": 1,
        "tipificacion_id": 121,
        "categoria_padre_id": None
    },
    {
        "id": 737,
        "nombre": "Transferencia a Nivel 1",
        "nivel": 1,
        "tipificacion_id": 122,
        "categoria_padre_id": None
    },
    {
        "id": 738,
        "nombre": "Transferencia a Nivel 2",
        "nivel": 1,
        "tipificacion_id": 122,
        "categoria_padre_id": None
    },
    {
        "id": 739,
        "nombre": "Transferencia Creadores de denuncia",
        "nivel": 1,
        "tipificacion_id": 122,
        "categoria_padre_id": None
    },
    {
        "id": 740,
        "nombre": "Transferencia a Abogados",
        "nivel": 1,
        "tipificacion_id": 122,
        "categoria_padre_id": None
    },
    {
        "id": 741,
        "nombre": "Transferencia a Psicologia",
        "nivel": 1,
        "tipificacion_id": 122,
        "categoria_padre_id": None
    },
    {
        "id": 742,
        "nombre": "Transferencia a Justicia Transicional",
        "nivel": 1,
        "tipificacion_id": 122,
        "categoria_padre_id": None
    },
    {
        "id": 743,
        "nombre": "Transferencia Agente Bilingüe",
        "nivel": 1,
        "tipificacion_id": 122,
        "categoria_padre_id": None
    },
    {
        "id": 744,
        "nombre": "Cancelar Cita",
        "nivel": 1,
        "tipificacion_id": 123,
        "categoria_padre_id": None
    },
    {
        "id": 745,
        "nombre": "Agendar Cita",
        "nivel": 1,
        "tipificacion_id": 123,
        "categoria_padre_id": None
    },
    {
        "id": 746,
        "nombre": "Solicita Presencia Inmediata de Policia",
        "nivel": 1,
        "tipificacion_id": 124,
        "categoria_padre_id": None
    },
    {
        "id": 747,
        "nombre": "Presencia exitosa",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 746
    },
    {
        "id": 748,
        "nombre": "Transfiere a 123 u otra entidad",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 746
    },
    {
        "id": 749,
        "nombre": "Solicita presencia de Policía pero (No está en riesgo la vida o la integridad)",
        "nivel": 1,
        "tipificacion_id": 124,
        "categoria_padre_id": None
    },
    {
        "id": 750,
        "nombre": "Solicita presencia de Policía pero (No está en riesgo la vida o la integridad de la víctima o no es penal)",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 749
    },
    {
        "id": 751,
        "nombre": "Llamada Equivocada",
        "nivel": 1,
        "tipificacion_id": 125,
        "categoria_padre_id": None
    },
    {
        "id": 752,
        "nombre": "Llamada Colgada",
        "nivel": 1,
        "tipificacion_id": 125,
        "categoria_padre_id": None
    },
    {
        "id": 753,
        "nombre": "Llamada Muda",
        "nivel": 1,
        "tipificacion_id": 125,
        "categoria_padre_id": None
    },
    {
        "id": 754,
        "nombre": "Llamada de Broma",
        "nivel": 1,
        "tipificacion_id": 125,
        "categoria_padre_id": None
    },
    {
        "id": 755,
        "nombre": "Llamada Caida",
        "nivel": 1,
        "tipificacion_id": 125,
        "categoria_padre_id": None
    },
    {
        "id": 756,
        "nombre": "Llamada de Prueba",
        "nivel": 1,
        "tipificacion_id": 125,
        "categoria_padre_id": None
    },
    {
        "id": 757,
        "nombre": "Presencial",
        "nivel": 1,
        "tipificacion_id": 126,
        "categoria_padre_id": None
    },
    {
        "id": 758,
        "nombre": "Denuncia fácil",
        "nivel": 1,
        "tipificacion_id": 126,
        "categoria_padre_id": None
    },
    {
        "id": 759,
        "nombre": "Telefónico",
        "nivel": 1,
        "tipificacion_id": 126,
        "categoria_padre_id": None
    },
    {
        "id": 760,
        "nombre": "Link Suip",
        "nivel": 1,
        "tipificacion_id": 126,
        "categoria_padre_id": None
    },
    {
        "id": 761,
        "nombre": "ADenunciar",
        "nivel": 1,
        "tipificacion_id": 126,
        "categoria_padre_id": None
    },
    {
        "id": 762,
        "nombre": "Outbound Denuncia Nivel 1",
        "nivel": 1,
        "tipificacion_id": 127,
        "categoria_padre_id": None
    },
    {
        "id": 763,
        "nombre": "Outbound Denuncias Nivel 2",
        "nivel": 1,
        "tipificacion_id": 127,
        "categoria_padre_id": None
    },
    {
        "id": 764,
        "nombre": "Outbound PQRS",
        "nivel": 1,
        "tipificacion_id": 127,
        "categoria_padre_id": None
    },
    {
        "id": 765,
        "nombre": "Outbound Orientacion, Informacion  y Consulta de Casos",
        "nivel": 1,
        "tipificacion_id": 127,
        "categoria_padre_id": None
    },
    {
        "id": 766,
        "nombre": "Outbound Proceso clasificación denuncia",
        "nivel": 1,
        "tipificacion_id": 127,
        "categoria_padre_id": None
    },
    {
        "id": 767,
        "nombre": "Outbound Presencia inmediata de policia",
        "nivel": 1,
        "tipificacion_id": 127,
        "categoria_padre_id": None
    },
    {
        "id": 768,
        "nombre": "Outbound Desaparecidos",
        "nivel": 1,
        "tipificacion_id": 127,
        "categoria_padre_id": None
    },
    {
        "id": 769,
        "nombre": "Outbound No Efectivo",
        "nivel": 1,
        "tipificacion_id": 127,
        "categoria_padre_id": None
    },
    {
        "id": 770,
        "nombre": "Outbound agendamiento presencial",
        "nivel": 1,
        "tipificacion_id": 127,
        "categoria_padre_id": None
    },
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        {
        "id": 771,
        "nombre": "Sicecon",
        "nivel": 1,
        "tipificacion_id": 128,
        "categoria_padre_id": None
    },
    {
        "id": 772,
        "nombre": "Denuncia fácil",
        "nivel": 1,
        "tipificacion_id": 128,
        "categoria_padre_id": None
    },
    {
        "id": 773,
        "nombre": "Reporte denuncias de genero",
        "nivel": 1,
        "tipificacion_id": 129,
        "categoria_padre_id": None
    },
    {
        "id": 774,
        "nombre": "Violencia Sexual",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 773
    },
    {
        "id": 775,
        "nombre": "Violencia Intrafamiliar",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 773
    },
    {
        "id": 776,
        "nombre": "Violencia de Genero",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 773
    },
    {
        "id": 777,
        "nombre": "Trata de personas",
        "nivel": 1,
        "tipificacion_id": 129,
        "categoria_padre_id": None
    },
    {
        "id": 778,
        "nombre": "Denuncias anónimas",
        "nivel": 1,
        "tipificacion_id": 129,
        "categoria_padre_id": None
    },
    {
        "id": 779,
        "nombre": "Hechos de corrupción",
        "nivel": 1,
        "tipificacion_id": 129,
        "categoria_padre_id": None
    },
    {
        "id": 780,
        "nombre": "Crimen organizado",
        "nivel": 1,
        "tipificacion_id": 129,
        "categoria_padre_id": None
    },
    {
        "id": 781,
        "nombre": "Líderes sociales",
        "nivel": 1,
        "tipificacion_id": 129,
        "categoria_padre_id": None
    },
    {
        "id": 782,
        "nombre": "Conflicto armado",
        "nivel": 1,
        "tipificacion_id": 129,
        "categoria_padre_id": None
    },
    {
        "id": 783,
        "nombre": "MBU",
        "nivel": 1,
        "tipificacion_id": 130,
        "categoria_padre_id": None
    },
    {
        "id": 784,
        "nombre": "Reporte de desaparecidos",
        "nivel": 1,
        "tipificacion_id": 130,
        "categoria_padre_id": None
    },
    {
        "id": 785,
        "nombre": "Se corrige el relato y se clasifica",
        "nivel": 1,
        "tipificacion_id": 131,
        "categoria_padre_id": None
    },
    {
        "id": 786,
        "nombre": "Solo se clasifica la denuncia",
        "nivel": 1,
        "tipificacion_id": 131,
        "categoria_padre_id": None
    },
    {
        "id": 787,
        "nombre": "Orientación para interponer denuncia",
        "nivel": 1,
        "tipificacion_id": 132,
        "categoria_padre_id": None
    },
    {
        "id": 788,
        "nombre": "Link Suip- autogestión denuncia.",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 787
    },
    {
        "id": 789,
        "nombre": "Formulario denuncia fácil",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 787
    },
    {
        "id": 790,
        "nombre": "Comisaria, inspección u otros",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 787
    },
    {
        "id": 791,
        "nombre": "Orientación para interponer PQRS",
        "nivel": 1,
        "tipificacion_id": 132,
        "categoria_padre_id": None
    },
    {
        "id": 792,
        "nombre": "Orientación SUSI - Página Web",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 791
    },
    {
        "id": 793,
        "nombre": "Orientación Correo",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 791
    },
    {
        "id": 794,
        "nombre": "Información denuncia y despacho asignado",
        "nivel": 1,
        "tipificacion_id": 132,
        "categoria_padre_id": None
    },
    {
        "id": 795,
        "nombre": "Orientación e información general",
        "nivel": 1,
        "tipificacion_id": 132,
        "categoria_padre_id": None
    },
    {
        "id": 796,
        "nombre": "Orientación para perdida de documentos",
        "nivel": 1,
        "tipificacion_id": 132,
        "categoria_padre_id": None
    },
    {
        "id": 797,
        "nombre": "Petición",
        "nivel": 1,
        "tipificacion_id": 133,
        "categoria_padre_id": None
    },
    {
        "id": 798,
        "nombre": "Queja",
        "nivel": 1,
        "tipificacion_id": 133,
        "categoria_padre_id": None
    },
    {
        "id": 799,
        "nombre": "Reclamo",
        "nivel": 1,
        "tipificacion_id": 133,
        "categoria_padre_id": None
    },
    {
        "id": 800,
        "nombre": "Sugerencia",
        "nivel": 1,
        "tipificacion_id": 133,
        "categoria_padre_id": None
    },
    {
        "id": 801,
        "nombre": "Felicitación",
        "nivel": 1,
        "tipificacion_id": 133,
        "categoria_padre_id": None
    },
    {
        "id": 802,
        "nombre": "Solicitud copia de la denuncia",
        "nivel": 1,
        "tipificacion_id": 133,
        "categoria_padre_id": None
    },
    {
        "id": 803,
        "nombre": "Reclamo por falta de rta a PQRS",
        "nivel": 1,
        "tipificacion_id": 133,
        "categoria_padre_id": None
    },
    {
        "id": 804,
        "nombre": "Transferencia a Nivel 1",
        "nivel": 1,
        "tipificacion_id": 134,
        "categoria_padre_id": None
    },
    {
        "id": 805,
        "nombre": "Transferencia a Nivel 2",
        "nivel": 1,
        "tipificacion_id": 134,
        "categoria_padre_id": None
    },
    {
        "id": 806,
        "nombre": "Transferencia Creadores de denuncia",
        "nivel": 1,
        "tipificacion_id": 134,
        "categoria_padre_id": None
    },
    {
        "id": 807,
        "nombre": "Transferencia a Abogados",
        "nivel": 1,
        "tipificacion_id": 134,
        "categoria_padre_id": None
    },
    {
        "id": 808,
        "nombre": "Transferencia a Psicologia",
        "nivel": 1,
        "tipificacion_id": 134,
        "categoria_padre_id": None
    },
    {
        "id": 809,
        "nombre": "Transferencia a Justicia Transicional",
        "nivel": 1,
        "tipificacion_id": 134,
        "categoria_padre_id": None
    },
    {
        "id": 810,
        "nombre": "Transferencia Agente Bilingüe",
        "nivel": 1,
        "tipificacion_id": 134,
        "categoria_padre_id": None
    },
    {
        "id": 811,
        "nombre": "Cancelar Cita",
        "nivel": 1,
        "tipificacion_id": 135,
        "categoria_padre_id": None
    },
    {
        "id": 812,
        "nombre": "Agendar Cita",
        "nivel": 1,
        "tipificacion_id": 135,
        "categoria_padre_id": None
    },
    {
        "id": 813,
        "nombre": "Solicita Presencia Inmediata de Policia",
        "nivel": 1,
        "tipificacion_id": 136,
        "categoria_padre_id": None
    },
    {
        "id": 814,
        "nombre": "Presencia exitosa",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 813
    },
    {
        "id": 815,
        "nombre": "Transfiere a 123 u otra entidad",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 813
    },
    {
        "id": 816,
        "nombre": "Solicita presencia de Policía pero (No está en riesgo la vida o la integridad)",
        "nivel": 1,
        "tipificacion_id": 136,
        "categoria_padre_id": None
    },
    {
        "id": 817,
        "nombre": "Solicita presencia de Policía pero (No está en riesgo la vida o la integridad de la víctima o no es penal)",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 816
    },
    {
        "id": 818,
        "nombre": "Llamada Equivocada",
        "nivel": 1,
        "tipificacion_id": 137,
        "categoria_padre_id": None
    },
    {
        "id": 819,
        "nombre": "Llamada Colgada",
        "nivel": 1,
        "tipificacion_id": 137,
        "categoria_padre_id": None
    },
    {
        "id": 820,
        "nombre": "Llamada Muda",
        "nivel": 1,
        "tipificacion_id": 137,
        "categoria_padre_id": None
    },
    {
        "id": 821,
        "nombre": "Llamada de Broma",
        "nivel": 1,
        "tipificacion_id": 137,
        "categoria_padre_id": None
    },
    {
        "id": 822,
        "nombre": "Llamada Caida",
        "nivel": 1,
        "tipificacion_id": 137,
        "categoria_padre_id": None
    },
    {
        "id": 823,
        "nombre": "Llamada de Prueba",
        "nivel": 1,
        "tipificacion_id": 137,
        "categoria_padre_id": None
    },
    
    
    
    
    
    
    
    
    {
        "id": 824,
        "nombre": "Presencial",
        "nivel": 1,
        "tipificacion_id": 138,
        "categoria_padre_id": None
    },
    {
        "id": 825,
        "nombre": "Denuncia fácil",
        "nivel": 1,
        "tipificacion_id": 138,
        "categoria_padre_id": None
    },
    {
        "id": 826,
        "nombre": "Telefónico",
        "nivel": 1,
        "tipificacion_id": 138,
        "categoria_padre_id": None
    },
    {
        "id": 827,
        "nombre": "Link Suip",
        "nivel": 1,
        "tipificacion_id": 138,
        "categoria_padre_id": None
    },
    {
        "id": 828,
        "nombre": "ADenunciar",
        "nivel": 1,
        "tipificacion_id": 138,
        "categoria_padre_id": None
    },
    {
        "id": 829,
        "nombre": "Outbound Denuncia Nivel 1",
        "nivel": 1,
        "tipificacion_id": 139,
        "categoria_padre_id": None
    },
    {
        "id": 830,
        "nombre": "Outbound Denuncias Nivel 2",
        "nivel": 1,
        "tipificacion_id": 139,
        "categoria_padre_id": None
    },
    {
        "id": 831,
        "nombre": "Outbound PQRS",
        "nivel": 1,
        "tipificacion_id": 139,
        "categoria_padre_id": None
    },
    {
        "id": 832,
        "nombre": "Outbound Orientacion, Informacion  y Consulta de Casos",
        "nivel": 1,
        "tipificacion_id": 139,
        "categoria_padre_id": None
    },
    {
        "id": 833,
        "nombre": "Outbound Proceso clasificación denuncia",
        "nivel": 1,
        "tipificacion_id": 139,
        "categoria_padre_id": None
    },
    {
        "id": 834,
        "nombre": "Outbound Presencia inmediata de policia",
        "nivel": 1,
        "tipificacion_id": 139,
        "categoria_padre_id": None
    },
    {
        "id": 835,
        "nombre": "Outbound Desaparecidos",
        "nivel": 1,
        "tipificacion_id": 139,
        "categoria_padre_id": None
    },
    {
        "id": 836,
        "nombre": "Outbound No Efectivo",
        "nivel": 1,
        "tipificacion_id": 139,
        "categoria_padre_id": None
    },
    {
        "id": 837,
        "nombre": "Outbound agendamiento presencial",
        "nivel": 1,
        "tipificacion_id": 139,
        "categoria_padre_id": None
    },
    
    {
        "id": 838,
        "nombre": "Sicecon",
        "nivel": 1,
        "tipificacion_id": 140,
        "categoria_padre_id": None
    },
    {
        "id": 839,
        "nombre": "Denuncia fácil",
        "nivel": 1,
        "tipificacion_id": 140,
        "categoria_padre_id": None
    },
    {
        "id": 840,
        "nombre": "Reporte denuncias de genero",
        "nivel": 1,
        "tipificacion_id": 141,
        "categoria_padre_id": None
    },
    {
        "id": 841,
        "nombre": "Violencia Sexual",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 840
    },
    {
        "id": 842,
        "nombre": "Violencia Intrafamiliar",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 840
    },
    {
        "id": 843,
        "nombre": "Violencia de Genero",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 840
    },
    {
        "id": 844,
        "nombre": "Trata de personas",
        "nivel": 1,
        "tipificacion_id": 141,
        "categoria_padre_id": None
    },
    {
        "id": 845,
        "nombre": "Denuncias anónimas",
        "nivel": 1,
        "tipificacion_id": 141,
        "categoria_padre_id": None
    },
    {
        "id": 846,
        "nombre": "Hechos de corrupción",
        "nivel": 1,
        "tipificacion_id": 141,
        "categoria_padre_id": None
    },
    {
        "id": 847,
        "nombre": "Crimen organizado",
        "nivel": 1,
        "tipificacion_id": 141,
        "categoria_padre_id": None
    },
    {
        "id": 848,
        "nombre": "Líderes sociales",
        "nivel": 1,
        "tipificacion_id": 141,
        "categoria_padre_id": None
    },
    {
        "id": 849,
        "nombre": "Conflicto armado",
        "nivel": 1,
        "tipificacion_id": 141,
        "categoria_padre_id": None
    },
    {
        "id": 850,
        "nombre": "MBU",
        "nivel": 1,
        "tipificacion_id": 142,
        "categoria_padre_id": None
    },
    {
        "id": 851,
        "nombre": "Reporte de desaparecidos",
        "nivel": 1,
        "tipificacion_id": 142,
        "categoria_padre_id": None
    },
    {
        "id": 852,
        "nombre": "Se corrige el relato y se clasifica",
        "nivel": 1,
        "tipificacion_id": 143,
        "categoria_padre_id": None
    },
    {
        "id": 853,
        "nombre": "Solo se clasifica la denuncia",
        "nivel": 1,
        "tipificacion_id": 143,
        "categoria_padre_id": None
    },
    {
        "id": 854,
        "nombre": "Orientación para interponer denuncia",
        "nivel": 1,
        "tipificacion_id": 144,
        "categoria_padre_id": None
    },
    {
        "id": 855,
        "nombre": "Link Suip- autogestión denuncia.",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 854
    },
    {
        "id": 856,
        "nombre": "Formulario denuncia fácil",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 854
    },
    {
        "id": 857,
        "nombre": "Comisaria, inspección u otros",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 854
    },
    {
        "id": 858,
        "nombre": "Orientación para interponer PQRS",
        "nivel": 1,
        "tipificacion_id": 144,
        "categoria_padre_id": None
    },
    {
        "id": 859,
        "nombre": "Orientación SUSI - Página Web",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 858
    },
    {
        "id": 860,
        "nombre": "Orientación Correo",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 858
    },
    {
        "id": 861,
        "nombre": "Información denuncia y despacho asignado",
        "nivel": 1,
        "tipificacion_id": 144,
        "categoria_padre_id": None
    },
    {
        "id": 862,
        "nombre": "Orientación e información general",
        "nivel": 1,
        "tipificacion_id": 144,
        "categoria_padre_id": None
    },
    {
        "id": 863,
        "nombre": "Orientación para perdida de documentos",
        "nivel": 1,
        "tipificacion_id": 144,
        "categoria_padre_id": None
    },
    {
        "id": 864,
        "nombre": "Petición",
        "nivel": 1,
        "tipificacion_id": 145,
        "categoria_padre_id": None
    },
    {
        "id": 865,
        "nombre": "Queja",
        "nivel": 1,
        "tipificacion_id": 145,
        "categoria_padre_id": None
    },
    {
        "id": 866,
        "nombre": "Reclamo",
        "nivel": 1,
        "tipificacion_id": 145,
        "categoria_padre_id": None
    },
    {
        "id": 867,
        "nombre": "Sugerencia",
        "nivel": 1,
        "tipificacion_id": 145,
        "categoria_padre_id": None
    },
    {
        "id": 868,
        "nombre": "Felicitación",
        "nivel": 1,
        "tipificacion_id": 145,
        "categoria_padre_id": None
    },
    {
        "id": 869,
        "nombre": "Solicitud copia de la denuncia",
        "nivel": 1,
        "tipificacion_id": 145,
        "categoria_padre_id": None
    },
    {
        "id": 870,
        "nombre": "Reclamo por falta de rta a PQRS",
        "nivel": 1,
        "tipificacion_id": 145,
        "categoria_padre_id": None
    },
    {
        "id": 871,
        "nombre": "Transferencia a Nivel 1",
        "nivel": 1,
        "tipificacion_id": 146,
        "categoria_padre_id": None
    },
    {
        "id": 872,
        "nombre": "Transferencia a Nivel 2",
        "nivel": 1,
        "tipificacion_id": 146,
        "categoria_padre_id": None
    },
    {
        "id": 873,
        "nombre": "Transferencia Creadores de denuncia",
        "nivel": 1,
        "tipificacion_id": 146,
        "categoria_padre_id": None
    },
    {
        "id": 874,
        "nombre": "Transferencia a Abogados",
        "nivel": 1,
        "tipificacion_id": 146,
        "categoria_padre_id": None
    },
    {
        "id": 875,
        "nombre": "Transferencia a Psicologia",
        "nivel": 1,
        "tipificacion_id": 146,
        "categoria_padre_id": None
    },
    {
        "id": 876,
        "nombre": "Transferencia a Justicia Transicional",
        "nivel": 1,
        "tipificacion_id": 146,
        "categoria_padre_id": None
    },
    {
        "id": 877,
        "nombre": "Transferencia Agente Bilingüe",
        "nivel": 1,
        "tipificacion_id": 146,
        "categoria_padre_id": None
    },
    {
        "id": 878,
        "nombre": "Cancelar Cita",
        "nivel": 1,
        "tipificacion_id": 147,
        "categoria_padre_id": None
    },
    {
        "id": 879,
        "nombre": "Agendar Cita",
        "nivel": 1,
        "tipificacion_id": 147,
        "categoria_padre_id": None
    },
    {
        "id": 880,
        "nombre": "Solicita Presencia Inmediata de Policia",
        "nivel": 1,
        "tipificacion_id": 148,
        "categoria_padre_id": None
    },
    {
        "id": 881,
        "nombre": "Presencia exitosa",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 880
    },
    {
        "id": 882,
        "nombre": "Transfiere a 123 u otra entidad",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 880
    },
    {
        "id": 883,
        "nombre": "Solicita presencia de Policía pero (No está en riesgo la vida o la integridad)",
        "nivel": 1,
        "tipificacion_id": 148,
        "categoria_padre_id": None
    },
    {
        "id": 884,
        "nombre": "Solicita presencia de Policía pero (No está en riesgo la vida o la integridad de la víctima o no es penal)",
        "nivel": 2,
        "tipificacion_id": None,
        "categoria_padre_id": 883
    },
    {
        "id": 885,
        "nombre": "Llamada Equivocada",
        "nivel": 1,
        "tipificacion_id": 149,
        "categoria_padre_id": None
    },
    {
        "id": 886,
        "nombre": "Llamada Colgada",
        "nivel": 1,
        "tipificacion_id": 149,
        "categoria_padre_id": None
    },
    {
        "id": 887,
        "nombre": "Llamada Muda",
        "nivel": 1,
        "tipificacion_id": 149,
        "categoria_padre_id": None
    },
    {
        "id": 888,
        "nombre": "Llamada de Broma",
        "nivel": 1,
        "tipificacion_id": 149,
        "categoria_padre_id": None
    },
    {
        "id": 889,
        "nombre": "Llamada Caida",
        "nivel": 1,
        "tipificacion_id": 149,
        "categoria_padre_id": None
    },
    {
        "id": 890,
        "nombre": "Llamada de Prueba",
        "nivel": 1,
        "tipificacion_id": 149,
        "categoria_padre_id": None
    },
    {
        "id": 891,
        "nombre": "Presencial",
        "nivel": 1,
        "tipificacion_id": 150,
        "categoria_padre_id": None
    },
    {
        "id": 892,
        "nombre": "Denuncia fácil",
        "nivel": 1,
        "tipificacion_id": 150,
        "categoria_padre_id": None
    },
    {
        "id": 893,
        "nombre": "Telefónico",
        "nivel": 1,
        "tipificacion_id": 150,
        "categoria_padre_id": None
    },
    {
        "id": 894,
        "nombre": "Link Suip",
        "nivel": 1,
        "tipificacion_id": 150,
        "categoria_padre_id": None
    },
    {
        "id": 895,
        "nombre": "ADenunciar",
        "nivel": 1,
        "tipificacion_id": 150,
        "categoria_padre_id": None
    },
    {
        "id": 896,
        "nombre": "Outbound Denuncia Nivel 1",
        "nivel": 1,
        "tipificacion_id": 151,
        "categoria_padre_id": None
    },
    {
        "id": 897,
        "nombre": "Outbound Denuncias Nivel 2",
        "nivel": 1,
        "tipificacion_id": 151,
        "categoria_padre_id": None
    },
    {
        "id": 898,
        "nombre": "Outbound PQRS",
        "nivel": 1,
        "tipificacion_id": 151,
        "categoria_padre_id": None
    },
    {
        "id": 899,
        "nombre": "Outbound Orientacion, Informacion  y Consulta de Casos",
        "nivel": 1,
        "tipificacion_id": 151,
        "categoria_padre_id": None
    },
    {
        "id": 900,
        "nombre": "Outbound Proceso clasificación denuncia",
        "nivel": 1,
        "tipificacion_id": 151,
        "categoria_padre_id": None
    },
    {
        "id": 901,
        "nombre": "Outbound Presencia inmediata de policia",
        "nivel": 1,
        "tipificacion_id": 151,
        "categoria_padre_id": None
    },
    {
        "id": 902,
        "nombre": "Outbound Desaparecidos",
        "nivel": 1,
        "tipificacion_id": 151,
        "categoria_padre_id": None
    },
    {
        "id": 903,
        "nombre": "Outbound No Efectivo",
        "nivel": 1,
        "tipificacion_id": 151,
        "categoria_padre_id": None
    },
    {
        "id": 904,
        "nombre": "Outbound agendamiento presencial",
        "nivel": 1,
        "tipificacion_id": 151,
        "categoria_padre_id": None
    },
    
]
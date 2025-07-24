segmentos = [
    # CHAT
    {
        "id": 1,
        "nombre": "Chat",
        "tipo_canal_id": 1,  # CHAT
        "tiene_segmento_ii": False
    },
    
    # SMS
    {
        "id": 2,
        "nombre": "SMS",
        "tipo_canal_id": 2,  # SMS
        "tiene_segmento_ii": False
    },
    
    # INBOUND
    {
        "id": 3,
        "nombre": "NIVEL I",
        "tipo_canal_id": 3,  # INBOUND
        "tiene_segmento_ii": False
    },
    {
        "id": 4,
        "nombre": "NIVEL II",
        "tipo_canal_id": 3,  # INBOUND
        "tiene_segmento_ii": False
    },
    {
        "id": 5,
        "nombre": "BILINGÜE",
        "tipo_canal_id": 3,  # INBOUND
        "tiene_segmento_ii": True  # Necesita Segmento II
    },
    {
        "id": 6,
        "nombre": "PSICOLOGIA",
        "tipo_canal_id": 3,  # INBOUND
        "tiene_segmento_ii": True  # Necesita Segmento II
    },
    
    # OUTBOUND
    {
        "id": 7,
        "nombre": "NIVEL I",
        "tipo_canal_id": 4,  # OUTBOUND
        "tiene_segmento_ii": False
    },
    {
        "id": 8,
        "nombre": "NIVEL II",
        "tipo_canal_id": 4,  # OUTBOUND
        "tiene_segmento_ii": False
    },
    {
        "id": 9,
        "nombre": "BILINGÜE",
        "tipo_canal_id": 4,  # OUTBOUND
        "tiene_segmento_ii": True
    },
    {
        "id": 10,
        "nombre": "PSICOLOGIA",
        "tipo_canal_id": 4,  # OUTBOUND
        "tiene_segmento_ii": True
    },
    
    # VIRTUAL HOLD
    {
        "id": 11,
        "nombre": "NIVEL I",
        "tipo_canal_id": 5,  # VIRTUAL HOLD
        "tiene_segmento_ii": False
    },
    {
        "id": 12,
        "nombre": "NIVEL II",
        "tipo_canal_id": 5,  # VIRTUAL HOLD
        "tiene_segmento_ii": False
    },
    {
        "id": 13,
        "nombre": "BILINGÜE",
        "tipo_canal_id": 5,  # VIRTUAL HOLD
        "tiene_segmento_ii": True
    },
    {
        "id": 14,
        "nombre": "PSICOLOGIA",
        "tipo_canal_id": 5,  # VIRTUAL HOLD
        "tiene_segmento_ii": True
    },
    
    # VIDEO LLAMADA
    {
        "id": 15,
        "nombre": "PERSONA OYENTE",
        "tipo_canal_id": 6,  # VIDEO LLAMADA
        "tiene_segmento_ii": False
    },
    {
        "id": 16,
        "nombre": "PERSONA NO OYENTE",
        "tipo_canal_id": 6,  # VIDEO LLAMADA
        "tiene_segmento_ii": False
    }
]
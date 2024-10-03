from app import create_app

# Inicializa a aplicação Flask
app = create_app()

if __name__ == "__main__":
    # Executa a aplicação Flask no modo de desenvolvimento
    app.run(debug=True, host="0.0.0.0", port=5000)

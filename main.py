from AudioSynthesisModule import AudioSynthesisModule
from DecisionEngine import DecisionEngine
from LauguageModel import LanguageModelInterface
from SensorIntegrationModule import SensorIntegrationModule





def main():
    # Step 1: Get the sensor data
    sim = SensorIntegrationModule()
    fused_data = sim.get_sensor_data()

    # Step 2: Process the data using the Decision Engine
    decision_engine = DecisionEngine()
    decisions = decision_engine.process_data(fused_data)

    # Ensure you have an API Key from OpenAI (this should be stored securely)
    API_KEY = "YOUR_OPENAI_API_KEY_HERE"
    lm_interface = LanguageModelInterface(API_KEY)
    audio_module = AudioSynthesisModule()

    for decision in decisions:
        # Step 3: Generate textual response
        response = lm_interface.get_response(decision)

        # Step 4: Convert the textual response to audio
        output_file = audio_module.text_to_audio(response)

        # Step 5: Play the audio
        audio_module.play_audio(output_file)

if __name__ == "__main__":
    main()

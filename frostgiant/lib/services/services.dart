import 'dart:convert';
import 'package:http/http.dart' as http;
import 'utils.dart';

class ApiService {
  static Future<String?> sendPrompt(String prompt) async {
    try {
      final response = await http.post(
        Uri.parse(API_URL),
        headers: {"Content-Type": "application/json"},
        body: jsonEncode({"prompt": prompt}),
      );

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        return data["response"]; // Assuming backend returns {"response": "Generated text..."}
      } else {
        return null;
      }
    } catch (e) {
      print("Error: $e");
      return null;
    }
  }
}

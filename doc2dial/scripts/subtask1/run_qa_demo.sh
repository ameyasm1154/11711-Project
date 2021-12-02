python run_qa_demo.py \
 --dataset_name '../data/v1.0.1/doc2dial_original.py' \
 --dataset_config_name doc2dial_rc \
 --model_name_or_path mrm8488/bert-tiny-5-finetuned-squadv2 \
 --do_train \
 --do_eval \
 --version_2_with_negative \
 --logging_steps 2000 \
 --save_steps 2000 \
 --learning_rate 3e-5  \
 --num_train_epochs 5 \
 --max_seq_length 512  \
 --max_answer_length 50 \
 --doc_stride 128  \
 --cache_dir demo \
 --output_dir demo \
 --overwrite_output_dir  \
 --per_device_train_batch_size 15 \
 --per_device_train_batch_size 15 \
 --gradient_accumulation_steps 2  \
 --warmup_steps 1000 \
 --weight_decay 0.01  \
 --fp16 